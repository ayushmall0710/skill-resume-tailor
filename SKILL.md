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

Use the compile script:

```bash
python3 scripts/compile_resume.py /home/claude/Resume.tex --name Company_Role_Resume
```

Or manually:
```bash
cd /home/claude && pdflatex -interaction=nonstopmode Resume.tex
cp Resume.tex Resume.pdf /mnt/user-data/outputs/
```

Then use `present_files` tool with both PDF and TEX paths.

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

- **H-1B Required**: Always include sponsorship analysis
- **Graduation**: March 2026
- **Experience**: 4+ years (3 yrs Shell + Corvic internship + Aegis co-founding)
- **Domain interest**: Climate/sustainability when relevant
- **Corvic ingestion bullet**: Always use 50M+ files version

## References

- `references/master-bullets.md`: All available bullets organized by experience
- `references/template-nlp-ds.tex`: NLP/Data Science focused resume template
- `references/template-de-sa.tex`: Data Engineering/Solution Architect focused resume template
- `references/template-cover-letter.tex`: Cover letter template

When creating a resume, copy the appropriate template to `/home/claude/` and modify from there.

## Cover Letters

Only create when explicitly requested. Use existing cover letter template structure. No em dashes. Exactly 1 page.
