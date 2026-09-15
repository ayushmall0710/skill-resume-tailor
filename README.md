# Resume Tailor Skill

A Claude AI skill for tailoring LaTeX resumes to job applications. Selects and arranges
existing content from a master bullet list rather than rewriting — following the
**"Pick, Don't Edit"** principle.

The repo ships a complete **worked example** (one person's real resume history) so you
can see what a filled-in skill looks like.

## Setup

**→ [SETUP.md](SETUP.md)**

Hand that file (or this repo's URL) to an agent and it can install the skill and
configure it for a new person end to end. It covers prerequisites, install locations for
different runtimes, and the two approval gates where the user signs off on their bullets
and their resume versions.

Setup does not edit this repo. The agent copies the skill into its runtime's skill
location and personalizes that copy.

## Structure

```
resume-tailor/
├── SKILL.md                            # Skill instructions for Claude (person-agnostic)
├── references/
│   ├── master-bullets.template.md      # BLANK - fill in with your own history
│   ├── personal-header.template.tex    # BLANK - name/contact + education blocks
│   ├── master-bullets.md               # Bullet history (ships with the example's)
│   ├── resume-all-rounder.tex          # Resume, broad framing - the default base
│   ├── resume-nlp-ds.tex               # Resume, NLP/Data Science slant
│   ├── resume-de-sa.tex                # Resume, Data Engineering/Solution Architect slant
│   └── cover-letter.tex                # Cover letter
└── scripts/
    └── compile_resume.py               # LaTeX compilation script
```

**Naming rule:** a file with `.template.` in its name is **blank** and you fill it in.
Every other file is **operative** - the skill reads and produces it at runtime - and
ships carrying the worked example's data, which setup replaces in place.

Person-specific content lives entirely in `master-bullets.md` and the `.tex` files.
`SKILL.md` is person-agnostic and never needs editing to set the skill up for someone new.

## How It Works

Once setup is complete:

1. **Share a job description** → Claude provides structured analysis (fit score, gaps, H-1B sponsorship, optimization plan)
2. **Approve the plan** → Claude selects bullets from `master-bullets.md` and builds a tailored resume
3. **Compile output** → the resume is compiled to PDF and both TEX/PDF are returned

## Key Principles

- **Pick, Don't Edit**: default behavior is to SELECT bullets, not modify them
- **1 Page Always**: the resume must always be exactly 1 page
- **Format is Sacred**: never change LaTeX structure, margins, spacing, or section order
- **Person-agnostic skill**: all personal content lives in `master-bullets.md` and the `.tex` files
- **H-1B Analysis Required**: every JD analysis includes a sponsorship assessment
