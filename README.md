# Resume Tailor Skill

A Claude AI skill for tailoring LaTeX resumes to job applications. Selects and arranges existing content from a master bullet list rather than rewriting — following the **"Pick, Don't Edit"** principle.

## Structure

```
resume-tailor/
├── SKILL.md                          # Skill instructions for Claude
├── references/
│   ├── master-bullets.md             # Worked example: one filled-in bullet history
│   ├── master-bullets.template.md    # Blank version to fill with your own history
│   ├── template-all-rounder.tex      # All-rounder resume template (default base)
│   ├── template-nlp-ds.tex           # NLP/Data Science focused resume template
│   ├── template-de-sa.tex            # Data Engineering/Solution Architect template
│   └── template-cover-letter.tex     # Cover letter template
└── scripts/
    └── compile_resume.py             # LaTeX compilation script
```

`master-bullets.md` and the `.tex` templates ship filled in with one person's real
history so you can see a complete working example. Replace them with your own:
start from `master-bullets.template.md` (see Quick Setup below) and edit the
contact block, education, and bullets in whichever `.tex` template you use.

## Prerequisites

The skill compiles LaTeX to PDF and checks the page count, so you need `pdflatex`
and `pdfinfo` on PATH, plus Python 3 (stdlib only, no `pip install` needed) to run
`scripts/compile_resume.py`.

### macOS

```bash
# LaTeX (pdflatex) - BasicTeX is a ~100MB minimal install; use mactex-no-gui for the full distribution
brew install --cask basictex
# pdfinfo (poppler)
brew install poppler
```

Open a new terminal after the BasicTeX install so PATH picks up `/Library/TeX/texbin`.
BasicTeX is a minimal subset and doesn't ship every package the templates use
(`fontawesome5`, `titlesec`, `enumitem`, `parskip`, `multicol`); if `pdflatex`
errors with "File `<package>.sty' not found", install it directly:

```bash
sudo tlmgr update --self
sudo tlmgr install fontawesome5 titlesec enumitem parskip multicol
```

(Use `brew install --cask mactex-no-gui` instead of BasicTeX if you'd rather have the full distribution up front and skip this step - it's a ~4GB download.)

### Windows

```bash
# LaTeX (pdflatex) via MiKTeX
winget install -e --id MiKTeX.MiKTeX
# pdfinfo via poppler (winget's build), or use choco/scoop if you prefer
winget install -e --id oschwartz10612.Poppler
```

Open a new terminal after installing so PATH picks up both tools. MiKTeX prompts
to install missing packages on first compile ("Install on-the-fly") - accept that
the first time you run the skill. If `winget` isn't available, install
[MiKTeX](https://miktex.org/download) and [poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)
directly and add both `bin` folders to PATH.

### Linux (Debian/Ubuntu)

```bash
sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended poppler-utils
```

`texlive-latex-extra` covers the packages the templates use (`fontawesome5`, `titlesec`, `enumitem`, `parskip`).

### Verify

```bash
pdflatex --version
pdfinfo -v
```

Both should print a version instead of "command not found".

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
