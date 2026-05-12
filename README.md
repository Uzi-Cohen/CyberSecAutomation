# CyberSecAutomation

Personal toolkit for QA / Automation / SDET job applications and demo projects.

## Claude skills

### `automation-interview-prep`

Located at `.claude/skills/automation-interview-prep/`. Activates when you share a job posting (image, text, URL, PDF — English or Hebrew) and ask for analysis, interview prep, or to scaffold a matching automation project.

Three workflows:

1. **Analyze** — extract requirements, must-haves vs. nice-to-haves, tech stack, and flag open questions. Handles Hebrew postings (חובה / יתרון).
2. **Prep** — generate a tailored question bank, run a mock interview one question at a time, or gap-analyze a posting against your resume.
3. **Scaffold** — bootstrap a runnable demo project (Selenium/Playwright/Cypress, pytest API tests, Postman/Newman, REST Assured, Pester) that matches the posting's stack, with CI workflow.

How to invoke: just share a job posting screenshot and say what you want ("analyze this", "give me mock questions", "scaffold a Python+Selenium demo").

## Demo projects

Scaffolded projects land in `examples/<name>/`.
