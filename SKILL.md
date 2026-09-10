---
name: resume-tailor
description: Tailors LaTeX resumes for job applications. Use when user shares a job description and needs a customized resume. Handles JD analysis, bullet selection from master list, skills reordering, LaTeX compilation, and iterative edits. Requires H-1B sponsorship analysis for all applications.
compatibility: Requires pdflatex and pdfinfo system packages for LaTeX compilation.
allowed-tools: Bash
---

# Resume Tailor Skill

Tailors LaTeX resumes for job applications by selecting and arranging existing content, not rewriting it.

## Core Principle: Pick, Don't Edit

**Default behavior is to SELECT bullets from `references/master-bullets.md`, not modify them.**

Only alter a bullet if:
1. Explicitly mentioned in optimization plan
2. Rationale provided
3. User approves

## Workflow

### 1. JD Analysis (Always Provide First)

When user shares a JD, respond with structured analysis:

```
## Role Match Assessment
- Overall fit score (e.g., "Strong 80%")
- Must-have requirements coverage
- Nice-to-have requirements coverage

## Gaps & Mitigation
- Flag under-qualifications honestly
- Suggest reframing strategies

## H-1B Sponsorship Analysis (REQUIRED)
- Check if JD mentions sponsorship
- Research company H-1B history if not stated
- Recommendation: "Confirmed" / "Likely" / "Verify first"

## Company Research (1 paragraph)
- Mission, stage, recent news

## Optimization Plan
- Base template selection
- Bullet selections by section (reference master-bullets.md)
- Skills reordering priorities
- Project selection (pick 3)
- Summary statement adjustments
- Any proposed modifications (with rationale)
```

### 2. Get Approval

Wait for user to approve plan before creating resume. Ask clarifying questions if needed.

### 3. Create Resume

After approval:
1. Use exact LaTeX template structure (never change formatting)
2. Pull selected bullets from master list
3. Reorder skills as planned
4. Ensure exactly 1 page

### 4. Compile & Present

Copy the chosen template out of the skill to a working directory, edit it there, then compile with the script:

```bash
python3 scripts/compile_resume.py <path/to/Resume.tex> --name Company_Role_Resume
```

Or manually (run twice so links/refs resolve, then check the page count):

```bash
pdflatex -interaction=nonstopmode Resume.tex
pdflatex -interaction=nonstopmode Resume.tex
pdfinfo Resume.pdf | grep Pages   # must say 1
```

Then hand the user both the PDF and the TEX (the script also copies them to an outputs directory when one is available).

### 5. Document Changes

List all changes in bullet format:
- Major changes: Include rationale
- Minor changes: Brief note

## Format Rules (NEVER CHANGE)

- LaTeX structure: Identical to templates
- Margins/spacing: Do not adjust
- Section order: Do not reorder
- Length: Always exactly 1 page

## Content Rules (CAN CHANGE)

- **Skills section**: Rearrange within subsections, don't rename subsections
- **Work bullets**: Select from master list based on relevance
- **Projects**: Pick 3 most relevant
- **Summary**: Can adjust to match role/company

## Key Context

`references/master-bullets.md` is a filled-in **worked example** (one user's real history). The context and conventions below match that example. Replace `master-bullets.md` with your own history and swap these notes for your own before using the skill for real.

- **H-1B Required**: Always include sponsorship analysis (drop this step if work authorization is not a factor for you)
- **Current role**: Machine Learning Engineer at Corvic AI (full-time since April 2026)
- **Education**: MS in Data Science, University of Washington (graduated April 2026). No longer a student.
- **Experience**: 4+ years total (3 yrs Shell Data Engineer + Corvic + Aegis co-founding)
- **Domain interest**: Climate/sustainability when relevant, but search is broad
- **Primary title**: ML Engineer. Building the platform at Corvic; was a tools consumer at Shell. Frame this transition through word choice, never explicit contrast, and never characterize Shell negatively.

## Locked Conventions (Apply Without Asking)

These belong to the worked example. Keep the transferable ones (no em dashes, 1 page, accuracy over polish) and rewrite the rest for your own history.

- **No em dashes** anywhere in resumes or outreach. Use commas, "to", or restructure.
- **Awaken AI project is mandatory** in every resume version, without exception (EEG clinical prognostics pipeline, UW MSDS Capstone). Current description: "Built the first open-source, multi-paradigm EEG pipeline running oddball (P300/ERPs), language-tracking (ITPC/Morlet wavelets), and command-following (ERD + SVM classifier) on standard 19-channel ICU EEG, processing 9+ brain injury patients from raw EDF to automated HTML clinical report via a single CLI suite."
- **Corvic ingestion bullet**: always use the 50M+ files version.
- **Corvic conversational-platform bullet**: tightened wording is "...through natural language, with vector search and multi-tool LLM agent orchestration."
- **Corvic evaluation framework**: custom-built, described by four pillars: functionality, quality, security, performance.
- **Don't name-drop specific frameworks in bullets**: orchestration/infra framework names belong in the Skills section (Languages/Frameworks and Platforms), never spelled out inside a bullet. Keep bullets outcome-focused.
- **Corvic AI** hyperlinks to corvic.ai.
- **FeedForward** dataset covers 150+ countries (not "serving").
- **Page margins**: `left=0.4in,right=0.4in,top=0.4in,bottom=0.4in` on all resume templates. Cover letter keeps its own 0.5in margins.
- **Education section** (fixed, every resume): MSDS UW Seattle, Sept 2024 -- Mar 2026, GPA 3.9/4.0; B.Tech Amity University Mumbai, Mar 2017 -- Jun 2021, CS&E major, Photography minor, GPA 9.26/10.0. See `references/master-bullets.md` Education section.
- **Project links**: every project with a `Link:` in master-bullets.md must render its subsection heading with `\href{<link>}{~\faExternalLink*}` (fontawesome5's external-link glyph, starred/solid form) before the `\hfill` date. Projects with no link get no icon.
- **Accuracy over polish**: never invent metrics, overstate tool familiarity, or use phrasing the user can't defend in an interview. Prefer deliberate and defensible.

## Files

- `references/master-bullets.md`: worked example, all bullets organized by experience, plus the fixed Education section
- `references/master-bullets.template.md`: the blank version to fill in with your own history (see the README's Quick Setup)
- `references/template-all-rounder.tex`: all-rounder template (ML Engineer / FDE framing, broad role coverage) - the default base
- `references/template-nlp-ds.tex`: NLP/Data Science focused template
- `references/template-de-sa.tex`: Data Engineering/Solution Architect focused template
- `references/template-cover-letter.tex`: cover letter template

When creating a resume, copy the appropriate template to a working directory and modify from there.

## Cover Letters

Only create when explicitly requested. Use the existing cover letter template structure. No em dashes. Exactly 1 page. Slightly warm/enthusiastic tone preferred.

`references/template-cover-letter.tex` is a generic template, not a filled-in example. Fill in `{[Company Name]}`, `{[City, State]}`, `{[Role Title]}`, and the three `{[tailored ...]}` phrases per application; the contact block, name, and body structure otherwise stay fixed. Keep the braces around any placeholder that sits right after a `\\` line break (LaTeX otherwise reads `\\[...]` as an optional length argument). Contact info must match the resume templates.
