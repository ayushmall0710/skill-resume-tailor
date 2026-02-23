# Resume Tailor Skill

A Claude AI skill for tailoring LaTeX resumes to job applications. Selects and arranges existing content from a master bullet list rather than rewriting — following the **"Pick, Don't Edit"** principle.

## Structure

```
resume-tailor/
├── SKILL.md                          # Skill instructions for Claude
├── references/
│   ├── master-bullets.md             # All available bullets organized by experience
│   ├── template-nlp-ds.tex           # NLP/Data Science focused resume template
│   ├── template-de-sa.tex            # Data Engineering/Solution Architect template
│   └── template-cover-letter.tex     # Cover letter template
└── scripts/
    └── compile_resume.py             # LaTeX compilation script
```

## Install in Claude (Skill Types)

Claude supports two common skill locations:

- **Skills in Claude AI**: Settings -> Capabilities -> Skills -> + Add
- **User skill** (available in all projects): `~/.claude/skills/resume-tailor/`
- **Project skill** (available only in one repo): `<repo>/.claude/skills/resume-tailor/`

Install steps:

1. Create the folder (`resume-tailor`) in one of the locations above.
2. Copy this repo's files into that folder (`SKILL.md`, `references/`, `scripts/`).
3. Restart Claude (or start a new chat) so the skill is loaded.

## How It Works

1. **Install the skill** → add `resume-tailor` as a user skill or project skill (see section above)
2. **Set up `master-bullets.md`** → generate it quickly using the "Quick Setup (Any LLM)" section below
3. **Share a job description** → Claude provides structured analysis (fit score, gaps, H-1B sponsorship, optimization plan)
4. **Approve the plan** → Claude selects bullets from `master-bullets.md` and builds a tailored resume
5. **Compile output** → LaTeX resume is compiled to PDF, and both TEX/PDF are returned

## Key Principles

- **Pick, Don't Edit**: Default behavior is to SELECT bullets, not modify them
- **1 Page Always**: Resume must always be exactly 1 page
- **Format is Sacred**: Never change LaTeX structure, margins, spacing, or section order
- **H-1B Analysis Required**: Every JD analysis includes sponsorship assessment

## Quick Setup (Any LLM)

Use this to bootstrap `references/master-bullets.md` in minutes.

1. Upload `references/master-bullets.template.md` to any other LLM.
2. Paste the prompt below into any LLM with your resume content.
3. Save the generated markdown into `references/master-bullets.md` and review with the checklist.

### Copy-Paste Prompt

```text
Fill the attached template `master-bullets.template.md` using my resume content.

Rules:
- Keep the exact headings and order from the template.
- Do not invent tools, metrics, dates, or titles.
- Ask user if they need rewrites for bullets, only if they approve rewrite for clarity and impact, but keep facts true.
- Mark only top 1-2 bullets per company as *PREFERRED*.
- Use (rarely used) only for valid but niche bullets.
- Return markdown only.

Resume content:
<PASTE_YOUR_RESUME_HERE>
```

### 4-Point Review Checklist

- [ ] Dates and company names match your resume exactly.
- [ ] No fabricated numbers, tools, or claims.
- [ ] Preferred bullets are clearly strongest and measurable.
- [ ] Projects, skills sections, summaries, and metrics table are all filled.

### If Output Is Off

- Wrong structure: `Regenerate using the exact template headings and order only.`
- Too repetitive: `Merge similar bullets and keep the strongest variant.`
