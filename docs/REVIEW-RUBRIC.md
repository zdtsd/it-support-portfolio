# Portfolio Entry Review Rubric

Use this rubric for instructor, peer, and self-review. Review the entry and every evidence file. Score quality only after completing the automatic publication blockers below.

## Automatic publication blockers

An entry is **not publishable** until corrected when it contains any of the following:

- a credential, token, key, certificate, password-reset value, or environment secret;
- personal, requester, participant, or production customer information;
- an internal address, hostname, path, ticket link, asset identifier, or raw ticket export;
- unreviewed screenshots or logs;
- instructor-only staging/reset instructions or internal remote-support implementation details;
- unsafe technical instructions without required permission or safety boundaries; or
- a false or materially misleading claim about experience, personal contribution, supervision, or verification.

Escalate live secret exposure according to policy. A later deletion alone doesn't make the history safe.

## Scored areas

Score each area from 0 to 2.

| Area | 2 - Ready | 1 - Needs revision | 0 - Not ready |
|---|---|---|---|
| Technical accuracy | Explanations and terminology are accurate; uncertainty is labeled | Mostly accurate but imprecise or missing an important qualification | Incorrect, unsafe, contradictory, or unsupported |
| Troubleshooting reasoning | Tests have reasons; results clearly drive next decisions; rejected theories are visible | Steps are present but reasoning or decision changes are incomplete | Action list with no diagnostic logic, or conclusion doesn't follow evidence |
| Evidence and verification | Evidence supports the claim; original and related functions were tested; limitations are explicit | Some verification exists but is vague, partial, or weakly linked | No credible verification or fabricated/irrelevant evidence |
| Personal contribution | First-person contribution is specific and separated from team/instructor work | General contribution is stated but ownership remains ambiguous | Claims team/instructor work as personal or omits role |
| Customer-facing communication | Clear, respectful, concise, useful, and free of internal-only detail | Understandable but wordy, vague, blaming, or missing next steps | Unprofessional, misleading, or exposes protected information |
| Reflection and learning | Identifies first theory, changed evidence, future improvement, lesson, and wording improvement | Reflection exists but is generic or misses important prompts | No meaningful reflection or refuses evident correction |
| Interview usefulness | A 20-45 second answer communicates context, responsibility, actions, result, and significance | Relevant but too long, too command-focused, or missing a key element | Can't support the claimed interview question |
| Sanitization and privacy | Manual review complete; examples and evidence are safe; context remains technically useful | No exposed data found, but confirmation or evidence review is incomplete | Any automatic blocker is present |
| Markdown organization and links | Headings are consistent; tables are readable; links resolve; navigation is clear | Minor organization or link issues make review slower | Broken structure, inaccessible evidence, or major broken links |

Maximum score: **18**.

## Overall assessment

### Ready

- No automatic publication blocker is present.
- Every area scores at least 1.
- Total score is 15-18.
- The entry can be understood without a verbal explanation.
- Any remaining suggestion is optional polish.

### Needs revision

- No automatic publication blocker is present, but one or more important areas need correction.
- Total score is commonly 8-14, or an area scores 0.
- The reviewer gives specific, testable revision requests.

Examples: identify the personally performed steps, add a functional verification result, explain why DNS was tested, shorten the closing note, or repair a relative link.

### Not publishable

- Any privacy, credential, safety, raw-export, confidential-process, or material honesty blocker is present; or
- the entry is too technically unreliable to correct through ordinary editing.

“Not publishable” is a temporary content state. It carries no judgment about the participant. State the required containment and correction steps clearly.

## Reviewer response format

Use this short structure:

1. **Assessment:** Ready, Needs revision, or Not publishable
2. **Strong evidence:** One or two specific strengths
3. **Required changes:** Numbered, testable corrections
4. **Privacy action:** None, ordinary sanitization, or immediate escalation
5. **Recheck:** What must be rerun or demonstrated

Ask the participant to make corrections in a follow-up commit so the review and learning remain visible.
