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

## How It Works

1. **User shares a job description** → Claude provides structured analysis (fit score, gaps, H-1B sponsorship, optimization plan)
2. **User approves plan** → Claude selects bullets from `master-bullets.md` and builds a tailored resume
3. **Compilation** → LaTeX resume compiled to PDF, both files presented to user

## Key Principles

- **Pick, Don't Edit**: Default behavior is to SELECT bullets, not modify them
- **1 Page Always**: Resume must always be exactly 1 page
- **Format is Sacred**: Never change LaTeX structure, margins, spacing, or section order
- **H-1B Analysis Required**: Every JD analysis includes sponsorship assessment
