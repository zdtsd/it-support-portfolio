#!/usr/bin/env python3
"""Validate the structural, privacy, and link basics of an ITC3 portfolio.

This standard-library utility is intentionally conservative and readable. It
does not inspect image pixels, understand organizational context, or replace a
manual technical and privacy review.
"""

from __future__ import annotations

import argparse
import ipaddress
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


CORE_FILES = (
    "README.md",
    "START-HERE.md",
    "WORKLOG.md",
    "INTERVIEW-INDEX.md",
    "SKILLS-MATRIX.md",
    "cases/README.md",
    "labs/README.md",
    "projects/README.md",
    "knowledge-base/README.md",
    "scripts/README.md",
    "templates/TICKET-CASE-STUDY.md",
    "templates/LAB-REPORT.md",
    "templates/XP-CYBER-POST-MORTEM.md",
    "templates/PROJECT-SUMMARY.md",
    "templates/KNOWLEDGE-BASE-ARTICLE.md",
    "templates/SCRIPT-README.md",
    "examples/network-printer-port/README.md",
    "examples/network-printer-port/evidence/README.md",
    "examples/browser-connectivity/README.md",
    "examples/browser-connectivity/evidence/README.md",
    "examples/switch-mac-learning/README.md",
    "examples/switch-mac-learning/evidence/README.md",
    "cases/system-startup-diagnosis/README.md",
    "cases/system-startup-diagnosis/evidence/README.md",
    "labs/command-line-troubleshooting/README.md",
    "labs/command-line-troubleshooting/evidence/README.md",
    "labs/dhcp-dora-analysis/README.md",
    "labs/dhcp-dora-analysis/evidence/README.md",
    "labs/xp-cyber-digital-duplicates-postmortem/README.md",
    "labs/xp-cyber-digital-duplicates-postmortem/evidence/README.md",
    "projects/windows-security-review/README.md",
    "projects/windows-security-review/evidence/README.md",
    "knowledge-base/printer-troubleshooting-guide/README.md",
    "knowledge-base/printer-troubleshooting-guide/evidence/README.md",
    "docs/STUDENT-GUIDE.md",
    "docs/INSTRUCTOR-GUIDE.md",
    "docs/GITHUB-WORKFLOW.md",
    "docs/SANITIZATION-GUIDE.md",
    "docs/REVIEW-RUBRIC.md",
    "docs/INTERVIEW-PREP.md",
    "docs/DEMO-CONTENT-NOTES.md",
    "tools/validate_portfolio.py",
    ".github/pull_request_template.md",
    ".github/workflows/validate-portfolio.yml",
    ".gitignore",
)

PRACTICAL_ENTRY_REQUIRED_HEADINGS = (
    "context",
    "problem or goal",
    "decision record",
    "result and verification",
    "my contribution",
    "what i learned",
    "interview answer",
    "evidence",
    "sanitization note",
)

KNOWLEDGE_BASE_REQUIRED_HEADINGS = (
    "intended audience and use case",
    "safety and prerequisites",
    "procedure",
    "verification",
    "recovery and escalation",
    "source and testing note",
    "sanitization note",
)

SCRIPT_REQUIRED_HEADINGS = (
    "purpose and authorship",
    "safety and prerequisites",
    "inputs and outputs",
    "usage",
    "example",
    "testing and verification",
    "rollback and limitations",
    "security and sanitization note",
)

TEXT_SUFFIXES = {".md", ".txt", ".rst", ".csv"}
SKIP_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "raw-evidence",
    "unreviewed-evidence",
    "local-project-inbox",
}

RFC1918_NETWORKS = (
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
)

IPV4_CANDIDATE = re.compile(
    r"(?<![\w.])(?P<address>(?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![\w.])"
)
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@(?P<domain>[A-Z0-9.-]+\.[A-Z]{2,})\b", re.I)
URL = re.compile(r"https?://[^\s<>()\]}`]+", re.I)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\((?P<target>[^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*#*\s*$")
SECRET_ASSIGNMENT = re.compile(
    r"\b(?:password|passwd|api[_ -]?key|access[_ -]?token|client[_ -]?secret)"
    r"\s*[:=]\s*[\"']?(?P<value>[A-Za-z0-9+/_.=-]{8,})",
    re.I,
)
PRIVATE_MATERIAL = re.compile(
    r"-----BEGIN (?:[A-Z0-9 ]+ )?(?:PRIVATE KEY|CERTIFICATE)-----"
)
FORBIDDEN_DASH = re.compile(r"[\N{EM DASH}\N{EN DASH}]")
FORBIDDEN_AUDIENCE_TERM = re.compile(r"\bhu(?:man)\b", re.I)
FORBIDDEN_CONTRAST = re.compile(r"\bnot\b[^.!?\n]{0,120}\bbut\b", re.I)

ALLOWED_EMAIL_DOMAINS = {
    "example.com",
    "example.org",
    "example.net",
    "users.noreply.github.com",
    "noreply.github.com",
}

SECRET_SUFFIXES = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
    ".jks",
    ".keystore",
    ".crt",
    ".cer",
    ".der",
}
ARCHIVE_SUFFIXES = {".zip", ".7z", ".rar", ".tar", ".tgz", ".gz", ".bz2", ".xz"}
DATA_EXPORT_SUFFIXES = {".csv", ".json", ".xml", ".sql", ".sqlite", ".db"}
PRIVATE_KEY_FILENAMES = {
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
}
PLACEHOLDER_SECRET_VALUES = {
    "placeholder",
    "examplevalue",
    "redacted",
    "removed",
    "changeme",
}


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    code: str
    message: str
    severity: str = "ERROR"

    def render(self) -> str:
        location = f"{self.path}:{self.line}" if self.line else self.path
        return f"{self.severity} {location} [{self.code}] {self.message}"


def parse_args(argv: list[str]) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description=(
            "Check expected portfolio files, common privacy patterns, unsafe file "
            "types, relative Markdown links, and required full-entry headings."
        ),
        epilog=(
            "Automated validation cannot inspect image pixels or recognize every "
            "name, identifier, confidential fact, or technically inaccurate claim. "
            "Manual privacy and technical review is still required."
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help=f"repository root to validate (default: {default_root})",
    )
    return parser.parse_args(argv)


def relative_name(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def should_skip(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return any(part in SKIP_DIRECTORIES for part in relative.parts)


def repository_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and not should_skip(path, root)
    )


def check_core_files(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for expected in CORE_FILES:
        if not (root / expected).is_file():
            findings.append(
                Finding(
                    expected,
                    0,
                    "STRUCTURE_MISSING",
                    "Expected core portfolio file is missing.",
                )
            )
    return findings


def check_filename(path: Path, root: Path) -> list[Finding]:
    name = path.name.lower()
    suffix = path.suffix.lower()
    relative = relative_name(path, root)
    findings: list[Finding] = []

    is_env_file = name == ".env" or (name.startswith(".env.") and name != ".env.example")
    is_named_secret = any(word in name for word in ("credential", "password", "secret", "token"))
    is_private_key_name = name in PRIVATE_KEY_FILENAMES or any(
        name.startswith(f"{key}.") for key in PRIVATE_KEY_FILENAMES
    )
    is_raw_export = (
        any(marker in name for marker in ("raw-ticket", "ticket-export", "osticket-export"))
        and suffix in DATA_EXPORT_SUFFIXES
    )

    if is_env_file:
        findings.append(
            Finding(relative, 0, "SECRET_FILE", "Environment or secret file type is not publishable.")
        )
    if suffix in SECRET_SUFFIXES or is_private_key_name:
        findings.append(
            Finding(relative, 0, "PRIVATE_MATERIAL_FILE", "Key or certificate file type is not publishable.")
        )
    if is_named_secret:
        findings.append(
            Finding(relative, 0, "SENSITIVE_FILENAME", "Filename suggests credential or secret material.")
        )
    if suffix in ARCHIVE_SUFFIXES:
        findings.append(
            Finding(relative, 0, "ARCHIVE_FILE", "Archive files require removal and manual content review.")
        )
    if is_raw_export:
        findings.append(
            Finding(relative, 0, "RAW_EXPORT_FILE", "Likely raw ticket export is not allowed.")
        )
    return findings


def is_rfc1918(address: str) -> bool:
    try:
        parsed = ipaddress.ip_address(address)
    except ValueError:
        return False
    return any(parsed in network for network in RFC1918_NETWORKS)


def safe_example_email(domain: str) -> bool:
    return domain.lower().rstrip(".") in ALLOWED_EMAIL_DOMAINS


def likely_internal_url(raw_url: str) -> bool:
    cleaned = raw_url.rstrip(".,;:'\"")
    try:
        parsed = urlsplit(cleaned)
    except ValueError:
        return False

    host = (parsed.hostname or "").lower().rstrip(".")
    if not host:
        return False
    if host in {"localhost", "127.0.0.1", "::1"}:
        return False
    if parsed.scheme.lower() == "http":
        return True
    if "." not in host or host.endswith((".local", ".lan", ".internal", ".corp", ".home")):
        return True
    return is_rfc1918(host)


def secret_value_is_placeholder(value: str) -> bool:
    normalized = value.lower().strip("'\"[]<>{}")
    return normalized in PLACEHOLDER_SECRET_VALUES or normalized.startswith(("example", "placeholder"))


def scan_text_file(path: Path, root: Path) -> list[Finding]:
    relative = relative_name(path, root)
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [
            Finding(relative, 0, "TEXT_ENCODING", "Text-like file is not valid UTF-8 and needs review.")
        ]

    seen: set[tuple[int, str]] = set()
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in IPV4_CANDIDATE.finditer(line):
            if is_rfc1918(match.group("address")) and (line_number, "PRIVATE_IPV4") not in seen:
                findings.append(
                    Finding(
                        relative,
                        line_number,
                        "PRIVATE_IPV4",
                        "Likely RFC1918 address found; replace it with a documentation range.",
                    )
                )
                seen.add((line_number, "PRIVATE_IPV4"))

        for match in EMAIL.finditer(line):
            if not safe_example_email(match.group("domain")) and (line_number, "EMAIL") not in seen:
                findings.append(
                    Finding(
                        relative,
                        line_number,
                        "EMAIL",
                        "Likely non-example email address found; remove or replace it.",
                    )
                )
                seen.add((line_number, "EMAIL"))

        if any(likely_internal_url(match.group(0)) for match in URL.finditer(line)):
            if (line_number, "INTERNAL_URL") not in seen:
                findings.append(
                    Finding(
                        relative,
                        line_number,
                        "INTERNAL_URL",
                        "Likely internal or insecure HTTP URL found; remove or replace it.",
                    )
                )
                seen.add((line_number, "INTERNAL_URL"))

        if PRIVATE_MATERIAL.search(line) and (line_number, "PRIVATE_MATERIAL") not in seen:
            findings.append(
                Finding(
                    relative,
                    line_number,
                    "PRIVATE_MATERIAL",
                    "Private-key or certificate material marker found.",
                )
            )
            seen.add((line_number, "PRIVATE_MATERIAL"))

        if FORBIDDEN_DASH.search(line) and (line_number, "STYLE_DASH") not in seen:
            findings.append(
                Finding(
                    relative,
                    line_number,
                    "STYLE_DASH",
                    "Use a plain hyphen, comma, colon, or sentence break here.",
                )
            )
            seen.add((line_number, "STYLE_DASH"))

        if FORBIDDEN_AUDIENCE_TERM.search(line) and (line_number, "STYLE_TERM") not in seen:
            findings.append(
                Finding(
                    relative,
                    line_number,
                    "STYLE_TERM",
                    "Restricted audience wording found; rewrite with a specific role or manual review.",
                )
            )
            seen.add((line_number, "STYLE_TERM"))

        if FORBIDDEN_CONTRAST.search(line) and (line_number, "STYLE_CONTRAST") not in seen:
            findings.append(
                Finding(
                    relative,
                    line_number,
                    "STYLE_CONTRAST",
                    "Rewrite the contrast as direct sentences.",
                )
            )
            seen.add((line_number, "STYLE_CONTRAST"))

        for match in SECRET_ASSIGNMENT.finditer(line):
            if not secret_value_is_placeholder(match.group("value")):
                findings.append(
                    Finding(
                        relative,
                        line_number,
                        "SECRET_ASSIGNMENT",
                        "Likely credential or secret assignment found; matched value is intentionally hidden.",
                    )
                )
                break

    return findings


def markdown_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    elif " " in target:
        target = target.split(" ", 1)[0]
    return unquote(target)


def check_markdown_links(path: Path, root: Path) -> list[Finding]:
    relative = relative_name(path, root)
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")

    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in MARKDOWN_LINK.finditer(line):
            target = markdown_target(match.group("target"))
            if not target or target.startswith("#"):
                continue
            if target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (path.parent / path_part).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                findings.append(
                    Finding(
                        relative,
                        line_number,
                        "LINK_OUTSIDE_ROOT",
                        "Relative Markdown link resolves outside the repository.",
                    )
                )
                continue
            if not resolved.exists():
                findings.append(
                    Finding(
                        relative,
                        line_number,
                        "BROKEN_LINK",
                        "Relative Markdown link target does not exist.",
                    )
                )
    return findings


def normalized_heading(title: str) -> str:
    without_code = title.replace("`", "")
    return re.sub(r"\s+", " ", without_code).strip().casefold()


def entry_heading_rule(
    path: Path, root: Path
) -> tuple[tuple[str, ...], str, str] | None:
    relative_path = path.relative_to(root)
    relative = relative_path.as_posix()

    practical_paths = {
        "templates/TICKET-CASE-STUDY.md",
        "templates/LAB-REPORT.md",
        "templates/XP-CYBER-POST-MORTEM.md",
        "templates/PROJECT-SUMMARY.md",
        "examples/network-printer-port/README.md",
        "examples/browser-connectivity/README.md",
        "examples/switch-mac-learning/README.md",
    }
    if relative in practical_paths:
        return PRACTICAL_ENTRY_REQUIRED_HEADINGS, "PRACTICAL_HEADINGS", "practical entry"

    if (
        len(relative_path.parts) == 3
        and relative_path.parts[0] in {"cases", "labs", "projects"}
        and relative_path.parts[2] == "README.md"
    ):
        return PRACTICAL_ENTRY_REQUIRED_HEADINGS, "PRACTICAL_HEADINGS", "practical entry"

    if relative == "templates/KNOWLEDGE-BASE-ARTICLE.md" or (
        len(relative_path.parts) == 3
        and relative_path.parts[0] == "knowledge-base"
        and relative_path.parts[2] == "README.md"
    ):
        return KNOWLEDGE_BASE_REQUIRED_HEADINGS, "KB_HEADINGS", "knowledge-base article"

    if relative == "templates/SCRIPT-README.md" or (
        len(relative_path.parts) == 3
        and relative_path.parts[0] == "scripts"
        and relative_path.parts[2] == "README.md"
    ):
        return SCRIPT_REQUIRED_HEADINGS, "SCRIPT_HEADINGS", "script documentation"

    return None


def check_required_headings(path: Path, root: Path) -> list[Finding]:
    rule = entry_heading_rule(path, root)
    if not rule:
        return []
    required, code, entry_label = rule
    text = path.read_text(encoding="utf-8")
    headings = {
        normalized_heading(match.group("title"))
        for line in text.splitlines()
        if (match := HEADING.match(line))
    }
    missing = [heading for heading in required if heading not in headings]
    if not missing:
        return []
    return [
        Finding(
            relative_name(path, root),
            1,
            code,
            f"Full {entry_label} is missing required heading(s): " + ", ".join(missing) + ".",
        )
    ]


def validate(root: Path) -> list[Finding]:
    findings = check_core_files(root)
    for path in repository_files(root):
        findings.extend(check_filename(path, root))
        if path.suffix.lower() in TEXT_SUFFIXES:
            findings.extend(scan_text_file(path, root))
        if path.suffix.lower() == ".md":
            findings.extend(check_markdown_links(path, root))
            findings.extend(check_required_headings(path, root))
    return sorted(set(findings))


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR {root} [ROOT] Validation root is not a directory.")
        return 2

    findings = validate(root)
    for finding in findings:
        print(finding.render())

    if findings:
        print(f"\nPortfolio validation failed with {len(findings)} finding(s).")
        print("Matched private values are intentionally not printed. Review the file and line locally.")
        return 1

    print("Portfolio validation passed: structure, privacy and style patterns, links, and entry headings checked.")
    print("Manual review is still required for images, context, technical accuracy, and subtle identifiers.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
