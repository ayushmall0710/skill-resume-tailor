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

**Before handing anything to the user, run the identity check.** This skill ships with a
worked example (Ayush Mall's real resume). If your installed copy was not fully
personalized during setup, the example's identity can survive into a generated resume.
Grep the output for the example's values:

```bash
grep -riE 'ayush|corvic|awaken|aegis|amity|feedforward|sunnyvale|206\) 403|9\.26' <path/to/Resume.tex>
```

This must return **nothing**. If it returns anything, the skill is not set up for this
person: stop, do not deliver the resume, and complete the setup in the README first.
(If you are genuinely tailoring a resume for Ayush Mall, this check will fire on every
run - skip it deliberately rather than by accident.)

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

## Person-Specific Conventions

**Read the `## Conventions` block at the top of `references/master-bullets.md` and apply it.**

That block carries everything specific to the person this skill is set up for: their
background and framing, which projects are mandatory, which bullet variants to prefer,
exact phrasings for particular metrics. It is authoritative. If it contradicts an
assumption you would otherwise make, it wins.

All person-specific content lives in `references/master-bullets.md` and the `.tex`
templates. This file (SKILL.md) is person-agnostic and should never need editing to
set the skill up for someone new. If you find yourself wanting to edit SKILL.md with
someone's personal details, put them in `master-bullets.md` instead.

## Universal Conventions (Apply Without Asking)

These hold regardless of whose resume this is.

- **No em dashes** anywhere in resumes or outreach. Use commas, "to", or restructure.
- **Accuracy over polish**: never invent metrics, overstate tool familiarity, or use phrasing the user can't defend in an interview. Prefer deliberate and defensible.
- **Keep bullets outcome-focused**: specific orchestration/infra framework names belong in the Skills section (Languages/Frameworks and Platforms), not spelled out inside a bullet.
- **Page margins**: the shipped resume templates use `left=0.4in,right=0.4in,top=0.4in,bottom=0.4in`. The cover letter keeps its own 0.5in margins. Do not adjust either.
- **Project links**: every project with a `Link:` in master-bullets.md must render its subsection heading with `\href{<link>}{~\faExternalLink*}` (fontawesome5's external-link glyph, starred/solid form) before the `\hfill` date. Projects with no link get no icon.

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
