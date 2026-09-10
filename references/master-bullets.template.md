# Master Bullet List - <Your Name>

All available bullets from your resume history. When tailoring a resume, SELECT from this list rather than editing bullets. Only modify a bullet if explicitly approved.

**Conventions:** <your standing conventions, e.g. "No em dashes anywhere. <Flagship project> is mandatory in every resume. Keep specific framework names out of bullet text; list them only in the Skills section.">

---

## <Most Recent Company> (<Start Mon YYYY> – <End Mon YYYY / Present>)

**Title:** <Your Title>
**Company Description:** <One-line company/domain summary>
**Hyperlink:** <company-domain.com, if you link the company name>

### Available Bullets:

1. **<Impact Label>** ⭐ STRONGEST
   > <Action + scope + measurable impact>

2. **<Preferred Label>** ⭐ PREFERRED
   > <Action + technology + measurable impact>

3. **<General Label>**
   > <Action + scope + outcome>

4. **<Niche Label>** (rarely used)
   > <Valid but narrower bullet>

---

## <Previous Company> (<Start Mon YYYY> – <End Mon YYYY>)

**Title:** <Your Title>
**Company Description:** <One-line company/domain summary>

### Available Bullets:

1. **<Impact Label (with headline metric)>** ⭐ PREFERRED
   > <Action + technology + measurable impact>

   *Note: if this bullet folds in a metric also covered elsewhere, don't use both in the same resume (avoids double-counting).*

2. **<Same bullet, metric removed>** (use only if pairing with a different savings/impact bullet)
   > <Action + technology, no overlapping metric>

3. **<General Label>**
   > <Action + scope + outcome>

4. **<Niche Label>** (rarely used)
   > <Valid but narrower bullet>

---

## <Earliest Relevant Company> (<Start Mon YYYY> – <End Mon YYYY>)

**Title:** <Your Title>
**Company Description:** <One-line company/domain summary>

### Available Bullets:

1. **<Impact Label>**
   > <Action + scope + outcome>

2. **<General Label>**
   > <Action + scope + outcome>

---

## Education

Fixed on every resume version, all templates. Do not vary GPA or dates.

1. **<Degree>** | <Institution, City> | <Start Mon YYYY> -- <End Mon YYYY>
   > <One-line coursework focus> | GPA: <X.X/Y.Y>

2. **<Degree>** | <Institution, City> | <Start Mon YYYY> -- <End Mon YYYY>
   > Major: <Major> | Minor: <Minor> | GPA: <X.XX/Y.Y>

### LaTeX Formatted (Copy-Paste Ready)

```latex
\subsection{<Degree> | <Institution, City> \hfill
\textit{<Start Mon YYYY> -- <End Mon YYYY>}}
<One-line coursework focus>\ $|$\ GPA: <X.X/Y.Y>

\subsection{<Degree> | <Institution, City> \hfill
\textit{<Start Mon YYYY> -- <End Mon YYYY>}}
Major: <Major>\ $|$\ Minor: <Minor>\ $|$\ GPA: <X.XX/Y.Y>
```

---

## Projects

Select 3 most relevant projects per resume. **<Flagship project, if any> is MANDATORY in every resume version.**

### Available Projects:

1. **<Flagship Project Name>** ⭐ MANDATORY (<context, e.g. Capstone>, <Date Range>)
   - **Shows:** <skills/technologies demonstrated>
   - **Link:** <URL if available>
   > <1-2 line project summary with outcome>

2. **<Project Name>** (<Date Range>)
   - **Shows:** <skills/technologies demonstrated>
   - **Link:** <URL if available>
   > <1-2 line project summary with outcome>

3. **<Project Name>** (<Date Range>)
   - **Shows:** <skills/technologies demonstrated. Note the role types this fits.>
   - **Link:** <URL if available>
   > <1-2 line project summary with outcome>

4. **<Project Name>** (<Date Range>)
   - **Shows:** <skills/technologies demonstrated>
   - **No link** (<reason, e.g. internal engagement, no public repo>)
   > <1-2 line project summary with outcome>

---

## Skills Sections

One block per resume framing. Rearrange within a block to match the JD; do not rename the three labels.

### <Primary Framing> Base (current active base)
```
Core Competencies: <comma-separated, highest-signal first>
Languages and Frameworks: <comma-separated>
Platforms & Tools: <comma-separated>
```

### <Secondary Framing, e.g. NLP/Data Science> Focus
```
Core Competencies: <comma-separated>
Languages and Frameworks: <comma-separated>
Platforms & Tools: <comma-separated>
```

### <Tertiary Framing, e.g. DE/Solution Architect> Focus
```
Core Competencies: <comma-separated>
Languages and Frameworks: <comma-separated>
Platforms & Tools: <comma-separated>
```

*Retired skills (no longer used, do not list): <comma-separated>.*

---

## Summary Statement Variants

1. **<Primary Framing> (current base):**
   > <1-2 lines>

2. **<Secondary Framing>:**
   > <1-2 lines>

3. **<Tertiary Framing>:**
   > <1-2 lines>

4. **<Niche Framing, e.g. Consulting/Governance>:**
   > <1-2 lines>

*Note: keep the summary consistent with your current status (e.g. degree complete vs in progress).*

---

## Quick Reference: Metrics

| Source | Metric | Context |
|--------|--------|---------|
| <Company/Project> | <Number> | <What it means> |
| <Company/Project> | <Number> | <What it means> |

---

## LaTeX Formatted Bullets (Copy-Paste Ready)

Keep these byte-identical to the plain bullets above. `\item` for work bullets, `\subsection{...}` for projects. Projects with a link render `\href{<link>}{~\faExternalLink*}` before the `\hfill` date; projects with no link get no icon.

### <Most Recent Company> Bullets

```latex
% 1. <Impact Label> (STRONGEST)
\item \textbf{<lead phrase>} <rest of bullet>.
```

### <Previous Company> Bullets

```latex
% 1. <Impact Label> - PREFERRED
\item \textbf{<lead phrase>} <rest of bullet>.
```

### Projects (LaTeX Formatted)

```latex
% MANDATORY: <Flagship Project>
\subsection{<Project Title>%
\href{<link>}{~\faExternalLink*} \hfill \textit{<Date Range>}}
<1-2 line project summary>.

% <Project Name> (no link)
\subsection{<Project Title> \hfill \textit{<Date Range>}}
<1-2 line project summary>.
```
