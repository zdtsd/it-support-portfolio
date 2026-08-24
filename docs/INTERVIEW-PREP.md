# Interview Preparation Guide

Use the portfolio as a memory and evidence system. Select the closest honest example and rebuild the reasoning before an interview. A word-for-word recital will sound less natural and may hide the decisions that mattered.

## Build a concise answer

1. **Find the closest matching example.** Use the [Interview Evidence Index](../INTERVIEW-INDEX.md), then read the full entry.
2. **Describe the context honestly.** Say whether it was a supervised support activity, lab, simulation, exercise, or personal project.
3. **State your responsibility.** Identify the part you owned and credit teammates for their parts.
4. **Choose the important actions.** Explain why each major check was selected and how its result affected the next step.
5. **State the verified result.** Describe the functional test, comparison, observed state, or user confirmation.
6. **Mention collaboration accurately.** Explain what you escalated, what evidence you handed off, and what you did after receiving guidance.
7. **End with the lesson.** State what the experience changed about your future troubleshooting.

Aim for approximately 20-30 seconds initially. Let the interviewer ask for deeper technical details.

## A practical answer structure

- **Situation:** What function was failing or what needed to be built?
- **Responsibility:** What were you personally responsible for?
- **Actions and reasoning:** Which two or three decisions mattered most?
- **Result:** How did you verify the outcome?
- **Lesson:** What will you repeat or improve next time?

## Example: network printer troubleshooting

> In a supervised support exercise, one Windows workstation intermittently showed a shared printer as offline while other workstations could print. I was responsible for isolating the workstation-specific cause. I compared its printer properties and communication port with a known-good system, found that it was using a mismatched port configuration, and corrected the print object's communication path. I verified the printer showed ready status and produced a successful test page. The main lesson was to compare the failing configuration with known-good evidence before treating an intermittent symptom as a general network outage.

This answer is useful because it gives context, personal responsibility, comparison-based reasoning, correction, verification, and a lesson without exposing private details.

## Explain why, not every command

Avoid a long command-by-command recital. Compare these approaches:

**Weak:** “I ran `ipconfig`, then ping, then nslookup, then checked Settings.”

**Stronger:** “I confirmed the adapter had a valid configuration and could reach a known endpoint, which moved the investigation away from the physical link. Name-resolution testing then separated DNS behavior from general network access.”

The stronger version explains what the evidence meant.

## Discuss an incorrect initial theory

An incorrect first theory can be a strong example when you show disciplined correction:

1. State the first theory and why it seemed plausible.
2. Identify the result that didn't support it.
3. Explain the new theory or layer you tested.
4. State the final established cause.
5. Describe what you would check sooner next time.

Don't pretend you knew the cause from the beginning.

## Discuss collaboration and escalation

Good escalation isn't failure. A strong answer identifies:

- the permission, scope, safety, or expertise boundary;
- evidence already collected;
- the specific help requested;
- the handoff or feedback received; and
- your continuing contribution.

Avoid taking credit for a teammate's or instructor's work.

## Avoid unsupported claims

- Don't claim production employment for supervised training.
- Don't say “resolved” when only a configuration change was made without testing.
- Don't call a theory the root cause unless evidence established it.
- Don't claim tools or technologies you can't explain.
- Don't imply individual ownership of a team result.
- Don't reveal private details to make an answer sound more authentic.

## Practice prompts

For each featured entry, practice answering:

- What was the first useful observation?
- Which theory did you reject, and why?
- Which result changed your direction?
- What did you personally do?
- What was the safety or permission boundary?
- How did you verify the original function?
- What would you check sooner next time?
- Which part would you explain differently to a user and to a technician?

Record a short practice answer, compare it with the full entry, and remove details that don't contribute to context, reasoning, result, or lesson.
