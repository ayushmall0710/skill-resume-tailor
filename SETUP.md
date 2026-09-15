# Setup

**If you are an agent and someone handed you this repo's URL: this file is your
instruction set. Work through steps 1 to 6 in order. Do not start tailoring resumes
until step 6 passes.**

Setup does not edit this repo. You copy the skill into your agent runtime's own skill
location and personalize *that copy*. The repo stays intact as a worked example.

Steps 4 and 5 produce content that goes on someone's real resume. **Both require the
user's explicit approval before you move on.** Do not self-approve and do not batch the
two approvals into one.

---

## Step 1 - Clone as a read-only reference

```bash
git clone https://github.com/ayushmall0710/skill-resume-tailor.git
```

Treat the clone as reference material. Do not edit it and do not commit to it. The
worked example inside it stays intact so you can consult it as a model of a correctly
filled-in skill.

## Step 2 - Install the toolchain

The skill compiles LaTeX and checks page counts, so `pdflatex` and `pdfinfo` must be on
PATH, plus Python 3 (stdlib only, no `pip install` needed) for `scripts/compile_resume.py`.

### macOS

```bash
# LaTeX (pdflatex) - BasicTeX is a ~100MB minimal install; use mactex-no-gui for the full distribution
brew install --cask basictex
# pdfinfo (poppler)
brew install poppler
```

Open a new terminal after the BasicTeX install so PATH picks up `/Library/TeX/texbin`.
BasicTeX is a minimal subset and doesn't ship every package the resume files use
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

`texlive-latex-extra` covers the packages the resume files use (`fontawesome5`, `titlesec`, `enumitem`, `parskip`).

### Verify

```bash
pdflatex --version
pdfinfo -v
```

Both must print a version. If either says "command not found", stop and resolve it now.

## Step 3 - Copy the skill into your runtime's skill location

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

## Step 4 - Fill in `master-bullets.md` for this person

`<install>/references/master-bullets.md` currently holds the worked example. Replace it
with the target person's history, using `references/master-bullets.template.md` as the
shape.

Source material: their existing resume, LinkedIn, or whatever they give you. If you
have their resume text directly, fill the template yourself. If you are delegating to
another LLM, use the [copy-paste prompt](#appendix-filling-master-bulletsmd-with-another-llm) below.

Fill every section, including:

- The `## Conventions` block at the top. This is where all person-specific rules live
  (background and framing, mandatory projects, preferred bullet variants, exact metric
  phrasings). SKILL.md reads it and defers to it.
- The `## Education` section, which must match what you put in the `.tex` in step 5.

### Approval gate

Before moving to step 5, show the user what you produced and get explicit sign-off:

- Every bullet, grouped by company, and which ones you marked `PREFERRED`.
- The `## Conventions` block, especially anything you inferred rather than were told.
- Any metric, date, title, or claim you were not fully certain about. Flag these
  individually and ask the user to confirm each rather than burying them in the dump.

Do not invent bullets to fill the shape. If you do not have the material for a section,
leave it empty and ask. Then check the result against the
[4-point review checklist](#4-point-review-checklist).

**Wait for the user to approve before continuing.**

## Step 5 - Rebuild the resume as this person's baseline

First ask the user **which versions they want**. The repo ships three framings:

| File | Framing |
|---|---|
| `resume-all-rounder.tex` | Broad coverage, the default base |
| `resume-nlp-ds.tex` | NLP / Data Science slant |
| `resume-de-sa.tex` | Data Engineering / Solution Architect slant |

Most people want one. Some want two or three for different role types. Ask before
building, and ask whether they also want `cover-letter.tex` personalized.

For each version they chose, the shipped file is the worked example's own resume end to
end, so all of it needs replacing, not just the top:

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

Keep the preamble, section order, margins, and spacing exactly as they are.

### Approval gate

Compile each version and show the user the actual PDF, not just the source:

- Confirm the contact block is correct: name, city, phone, email, and every link.
- Confirm education, degree names, dates, and GPAs.
- Walk through which bullets and which projects you selected for each version, and why.
- Confirm each version is 1 page and reads the way they want.

**Wait for the user to approve each version before continuing.** Fix and re-show rather
than deferring corrections to the first real application.

Then delete the resume files they did not ask for from `<install>/references/`. Those
still hold the worked example's identity, and leaving them in place means a later
tailoring run can pick one up by mistake. They remain available in the clone:

```bash
# example: keeping only the all-rounder base and the cover letter
rm <install>/references/resume-nlp-ds.tex <install>/references/resume-de-sa.tex
```

## Step 6 - Verify setup, then stop

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
there; it assumes everything above is already done and does not re-check it.

---

## Appendix: Filling `master-bullets.md` with another LLM

For step 4, if you want to delegate the bullet extraction.

1. Upload `references/master-bullets.template.md` to any LLM.
2. Paste the prompt below along with the resume content.
3. Save the generated markdown over `<install>/references/master-bullets.md`, then take
   it through step 4's approval gate.

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
