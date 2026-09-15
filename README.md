# Resume Tailor Skill

A Claude AI skill for tailoring LaTeX resumes to job applications. Selects and arranges existing content from a master bullet list rather than rewriting — following the **"Pick, Don't Edit"** principle.

The repo ships a complete **worked example** (one person's real resume history) so you can see what a filled-in skill looks like. Setup does not edit this repo: you copy the skill into your agent runtime's own skill location and personalize *that copy*.

---

## Setup (agent runbook)

**If you are an agent and someone handed you this repo's URL: this section is your
instruction set. Work through steps 1 to 6 in order. Do not start tailoring resumes
until step 6 passes.**

### Step 1 - Clone as a read-only reference

```bash
git clone https://github.com/ayushmall0710/skill-resume-tailor.git
```

Treat the clone as reference material. Do not edit it and do not commit to it. The
worked example inside it stays intact so you can consult it as a model of a correctly
filled-in skill.

### Step 2 - Install the toolchain

The skill compiles LaTeX and checks page counts, so `pdflatex` and `pdfinfo` must be on
PATH. Follow [Prerequisites](#prerequisites) below for your OS, then confirm:

```bash
pdflatex --version
pdfinfo -v
```

Both must print a version. If either says "command not found", stop and resolve it now.

### Step 3 - Copy the skill into your runtime's skill location

Create a `resume-tailor/` folder at the destination for your runtime and copy
`SKILL.md`, `references/`, and `scripts/` into it.

| Runtime | Destination |
|---|---|
| Claude Code, available in all projects | `~/.claude/skills/resume-tailor/` |
| Claude Code, scoped to one repo | `<repo>/.claude/skills/resume-tailor/` |
| Claude.ai | Bundle as a `.skill` archive (see below), then Settings -> Capabilities -> Skills -> + Add |
| Any runtime with no skills directory | Leave the clone somewhere stable and reference `SKILL.md` and `references/` by absolute path |

```bash
# Example: Claude Code user skill
mkdir -p ~/.claude/skills/resume-tailor
cp -r SKILL.md references scripts ~/.claude/skills/resume-tailor/
```

For a Claude.ai `.skill` bundle, the archive must contain a single top-level
`resume-tailor/` directory:

```bash
zip -r resume-tailor.skill resume-tailor/
```

From here on, **`<install>` means the copy you just created**, not the clone. Every
remaining step edits files under `<install>`.

### Step 4 - Fill in `master-bullets.md` for this person

`<install>/references/master-bullets.md` currently holds the worked example. Replace it
with the target person's history, using `references/master-bullets.template.md` as the
shape.

Source material: their existing resume, LinkedIn, or whatever they give you. If you
have their resume text directly, fill the template yourself. If you are delegating to
another LLM, use the [copy-paste prompt](#copy-paste-prompt) below.

Fill every section, including:

- The `## Conventions` block at the top. This is where all person-specific rules live
  (background and framing, mandatory projects, preferred bullet variants, exact metric
  phrasings). SKILL.md reads it and defers to it.
- The `## Education` section, which must match what you put in the `.tex` in step 5.

Then check it against the [4-point review checklist](#4-point-review-checklist).

### Step 5 - Rebuild the resume as this person's baseline

Pick the base you will work from (`resume-all-rounder.tex` is the default;
`resume-nlp-ds.tex` and `resume-de-sa.tex` are role-slanted variants).

The shipped file is the worked example's own resume end to end, so all of it needs
replacing, not just the top:

1. **Name/contact block and education block.** `references/personal-header.template.tex`
   holds both with `<placeholders>` and notes on exactly where they sit in the file.
2. **Summary line.** Pick one of the Summary Statement Variants from the new
   `master-bullets.md`.
3. **Skills & Tech-stack.** Use one of the Skills Sections blocks from `master-bullets.md`.
4. **Professional Experience.** Replace each `\subsection{...}` company heading and its
   `\item` bullets with the new person's companies and their LaTeX-formatted bullets
   from `master-bullets.md`.
5. **Research & Projects.** Same, using their projects. Keep the
   `\href{<link>}{~\faExternalLink*}` icon on projects that have a link.

The result should be a valid one-page resume for this person, which then serves as the
base that per-application tailoring starts from. Keep the preamble, section order,
margins, and spacing exactly as they are.

If you will also write cover letters, replace the contact block and the body of
`cover-letter.tex` too (its company/role fields are already `{[placeholders]}`).

**Then delete the resume files you did not personalize** from `<install>/references/`.
They still hold the worked example's identity, and leaving them in place means a later
tailoring run can pick one up by mistake. They remain available in the clone if you
want another framing later:

```bash
# example: keeping only the all-rounder base and the cover letter
rm <install>/references/resume-nlp-ds.tex <install>/references/resume-de-sa.tex
```

### Step 6 - Verify setup, then stop

Confirm nothing from the worked example survived into your installed copy:

```bash
grep -riE 'ayush|corvic|awaken|aegis|amity|feedforward|sunnyvale|206\) 403|9\.26' \
  <install>/references/
```

**This must return nothing.** Anything it returns is example data you have not replaced
yet: go back and finish step 4 or 5. (If you are genuinely setting this up for Ayush
Mall, this check fires by design - skip it deliberately.)

Then confirm the toolchain produces a valid resume:

```bash
cd <install>/references
pdflatex -interaction=nonstopmode resume-all-rounder.tex
pdflatex -interaction=nonstopmode resume-all-rounder.tex
pdfinfo resume-all-rounder.pdf | grep Pages    # must say 1
```

Once both checks pass, setup is complete. Read `SKILL.md` and follow its workflow from
there; it assumes everything above is already done.

---

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
ships carrying the worked example's data, which setup replaces in place. So
`master-bullets.template.md` is a blank you copy from; `master-bullets.md` is the real
file the skill reads.

Person-specific content lives entirely in `master-bullets.md` and the `.tex` files.
`SKILL.md` is person-agnostic and never needs editing to set the skill up for someone
new.

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

## How It Works

Once setup is complete:

1. **Share a job description** → Claude provides structured analysis (fit score, gaps, H-1B sponsorship, optimization plan)
2. **Approve the plan** → Claude selects bullets from `master-bullets.md` and builds a tailored resume
3. **Compile output** → LaTeX resume is compiled to PDF, the identity check runs, and both TEX/PDF are returned

## Key Principles

- **Pick, Don't Edit**: Default behavior is to SELECT bullets, not modify them
- **1 Page Always**: Resume must always be exactly 1 page
- **Format is Sacred**: Never change LaTeX structure, margins, spacing, or section order
- **Person-agnostic skill**: all personal content lives in `master-bullets.md` and the `.tex` files
- **H-1B Analysis Required**: Every JD analysis includes sponsorship assessment

## Filling `master-bullets.md` with another LLM

Step 4 of the runbook, if you want to delegate the bullet extraction.

1. Upload `references/master-bullets.template.md` to any LLM.
2. Paste the prompt below along with the resume content.
3. Save the generated markdown over `<install>/references/master-bullets.md` and review with the checklist.

### Copy-Paste Prompt

```text
Fill the attached template `master-bullets.template.md` using my resume content.

Rules:
- Keep the exact headings and order from the template, including the ## Conventions section.
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
- [ ] Conventions, projects, skills sections, summaries, and metrics table are all filled.

### If Output Is Off

- Wrong structure: `Regenerate using the exact template headings and order only.`
- Too repetitive: `Merge similar bullets and keep the strongest variant.`
