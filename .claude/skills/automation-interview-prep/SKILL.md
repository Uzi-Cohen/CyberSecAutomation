---
name: automation-interview-prep
description: Analyze QA/Automation/SDET job postings (image, text, URL, PDF — English or Hebrew), generate tailored interview prep, and scaffold a matching automation project. Use when the user shares a job posting and asks for analysis, interview practice, mock questions, gap analysis against a resume, or to bootstrap a project (Selenium/Playwright/Cypress, API tests with REST Assured/Pytest/Postman, CI/CD) that matches the posting's tech stack.
---

# Automation Interview Prep

End-to-end helper for QA/Automation/SDET job applications:

1. **Analyze** a job posting (image / text / URL / PDF, English or Hebrew)
2. **Prep** the candidate (questions, mock interview, gap analysis vs. resume)
3. **Scaffold** an automation project matching the posting's tech stack

## When to invoke

Trigger this skill when the user:
- Pastes or attaches a job posting and asks for analysis, requirements breakdown, or translation
- Wants mock interview questions or to run a mock interview for an Automation/QA/SDET role
- Wants a gap analysis between a job posting and their CV/resume
- Wants to bootstrap a sample automation project that matches a posting's stack (so they can demo it)

If the user has only shared a job posting without saying what they want, ask which of the three workflows to run (analyze / prep / scaffold).

---

## Workflow 1 — Analyze the job posting

### Step 1: Extract raw text

- **Image** (most common): read it directly with the Read tool — Claude is multimodal. Hebrew RTL is fine; quote text as-is. Don't OCR via shell.
- **PDF**: use Read with the `pages` parameter.
- **URL**: use WebFetch.
- **Pasted text**: use as-is.

### Step 2: Normalize into the structured template

Use `templates/job-analysis.md` as the output shape. Fill in every section. If a field isn't in the posting, write `—` (don't invent).

Key fields to extract:
- Role title, company (if known), location, employment type
- Years of experience required
- **Must-have** skills (חובה / required / must)
- **Nice-to-have** skills (יתרון / advantage / plus / preferred)
- Tech stack (languages, frameworks, tools, CI, cloud)
- Testing types (Web UI, API, E2E, Client-Server, Mobile, Performance, Security)
- Methodologies (Agile/Scrum/Kanban, BDD, TDD)
- Soft skills / language requirements
- Red/yellow flags worth asking about in interview

### Step 3: Hebrew handling

Hebrew job postings use specific markers:
- `חובה` = **Required / Must-have**
- `יתרון` = **Advantage / Nice-to-have**
- `ניסיון` = experience
- `שנות ניסיון` = years of experience
- `ידע ב-` = knowledge of
- `יכולת` = ability to

When the posting is Hebrew, produce the analysis in **English by default** (most candidates want it in English for sharing/CV alignment) but keep original Hebrew terms in parentheses for accuracy. Ask if the user prefers Hebrew output.

### Step 4: Output

Render the filled template inline in the chat. Do NOT write it to disk unless the user asks — interview prep is conversational. If the user wants it saved, default path: `analyses/<company-or-role>-<YYYY-MM-DD>.md`.

---

## Workflow 2 — Interview prep

Run after Workflow 1, or directly if the user already has an analysis.

### Modes

1. **Question bank** — Generate a tailored list of likely interview questions, grouped by category (technical, scenario, behavioral, take-home).
2. **Mock interview** — Conversational: ask one question at a time, wait for answer, give feedback before next question. Adapt difficulty based on answers.
3. **Gap analysis** — Compare posting requirements to a resume/CV the user shares. Output a table: requirement → candidate evidence → gap level (none/minor/major) → suggested action (study topic, build a demo, reframe existing experience).

### Question generation rules

- Always tie questions to **specific requirements from the posting**, not generic QA trivia. If the posting requires API testing with Python, ask about `requests`, `pytest`, fixture design, contract testing — not Java RestAssured.
- Mix difficulty: ~40% fundamental, ~40% scenario/applied, ~20% deep/edge-case.
- Include at least 2 questions per "must-have" skill.
- For "nice-to-have" skills, include 1 question each — useful for the candidate to flag honestly.
- Pull from `references/interview-questions.md` for canonical question banks per topic (Selenium, API testing, CI/CD, Agile, scripting languages). Augment with role-specific framing.

### Mock interview rhythm

Per question:
1. Ask the question (one at a time — do not dump a list).
2. Wait for the candidate's answer.
3. Give feedback: what was strong, what was missing, a model answer outline, and a follow-up probe if the answer was shallow.
4. Track score across the session (out of 5 per question) and summarize at the end.

End the session whenever the user says "stop", "enough", or after ~10 questions, with an overall summary and study recommendations.

---

## Workflow 3 — Scaffold an automation project

Build a working demo project the candidate can put on GitHub and reference in the interview. The stack must match the posting.

### Step 1: Confirm scope with the user

Ask:
- Which stack from the posting to target (if multiple — e.g., posting lists "Python OR JavaScript")
- What to demo: Web UI tests, API tests, E2E, or all three
- Where to scaffold: in this repo under `examples/<name>/`, or in a new directory the user specifies
- CI: GitHub Actions yes/no

### Step 2: Generate the project

Use `references/scaffolding-recipes.md` for canonical project layouts per stack. Each recipe includes:
- Folder structure
- Dependency manifest (`requirements.txt`, `package.json`, `pom.xml`, etc.)
- One working example test per testing type
- A README explaining how to run locally and what each layer does
- Optional GitHub Actions workflow

### Step 3: Verify it runs

After scaffolding:
- Run the install command (`pip install -r requirements.txt`, `npm install`, etc.)
- Run the example test against a public sandbox (e.g., https://the-internet.herokuapp.com for Web, https://reqres.in or https://jsonplaceholder.typicode.com for API)
- Report results to the user

Do not claim "done" until at least one test executes successfully. If sandbox access fails, say so explicitly.

---

## Conventions

- **Default output language**: English. Switch to Hebrew if user writes in Hebrew or asks.
- **Don't fabricate**: if a requirement is ambiguous, say so rather than guessing.
- **Keep prep tied to the posting**: every question and every scaffolded test should map to a stated requirement.
- **Files vs. chat**: analyses and questions go in the chat. Scaffolded projects go to disk.

## Reference files

- `references/interview-questions.md` — canonical question bank per topic
- `references/scaffolding-recipes.md` — per-stack project layouts and starter code
- `references/hebrew-glossary.md` — Hebrew QA/tech terms → English
- `templates/job-analysis.md` — output template for Workflow 1
- `templates/gap-analysis.md` — output template for Workflow 2 gap mode
