#!/usr/bin/env python3
"""
Compile a LaTeX resume to PDF, copy to outputs, and print paths for presentation.

Usage:
    python3 scripts/compile_resume.py <tex_file> [--name <output_name>] [--out <dir>]

Examples:
    python3 scripts/compile_resume.py ./resume.tex
    python3 scripts/compile_resume.py ./resume.tex --name Microsoft_MLE_Resume
    python3 scripts/compile_resume.py ./resume.tex --out ~/Documents/applications

Output directory resolution (first that works):
    1. --out <dir>
    2. $RESUME_TAILOR_OUT
    3. /mnt/user-data/outputs   (claude.ai sandbox)
    4. the .tex file's own directory
"""

import argparse
import os
import subprocess
import shutil
import sys
from pathlib import Path


def resolve_output_dir(tex_path: Path, explicit: str = None) -> Path:
    """Pick the first writable output directory from the resolution order."""
    candidates = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    if os.environ.get("RESUME_TAILOR_OUT"):
        candidates.append(Path(os.environ["RESUME_TAILOR_OUT"]).expanduser())
    # claude.ai sandbox: only when that tree actually exists, so a normal
    # machine doesn't get a stray /mnt/... directory created on it
    sandbox = Path("/mnt/user-data/outputs")
    if sandbox.parent.is_dir():
        candidates.append(sandbox)
    candidates.append(tex_path.parent)
    for c in candidates:
        try:
            c.mkdir(parents=True, exist_ok=True)
            probe = c / ".rt_write_test"
            probe.touch()
            probe.unlink()
            return c
        except Exception:
            continue
    return tex_path.parent

def compile_latex(tex_path: Path, output_name: str = None, out_dir: str = None) -> tuple[Path, Path]:
    """Compile LaTeX file to PDF and copy to outputs directory."""

    if not tex_path.exists():
        print(f"Error: {tex_path} not found", file=sys.stderr)
        sys.exit(1)
    
    # Determine output name
    if output_name:
        base_name = output_name
    else:
        base_name = tex_path.stem
    
    work_dir = tex_path.parent
    
    # Compile LaTeX (run twice for references)
    for i in range(2):
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-output-directory", str(work_dir), str(tex_path)],
            capture_output=True,
            text=True,
            cwd=work_dir
        )
        if result.returncode != 0 and i == 1:
            print(f"LaTeX compilation failed:\n{result.stdout[-2000:]}", file=sys.stderr)
            sys.exit(1)
    
    # Source PDF path
    pdf_source = work_dir / f"{tex_path.stem}.pdf"
    
    if not pdf_source.exists():
        print(f"Error: PDF not generated at {pdf_source}", file=sys.stderr)
        sys.exit(1)
    
    # Check page count
    try:
        result = subprocess.run(
            ["pdfinfo", str(pdf_source)],
            capture_output=True,
            text=True
        )
        for line in result.stdout.split('\n'):
            if line.startswith('Pages:'):
                pages = int(line.split(':')[1].strip())
                if pages > 1:
                    print(f"WARNING: Resume is {pages} pages (should be 1 page)", file=sys.stderr)
                else:
                    print(f"[OK] Resume is 1 page")
                break
    except:
        pass  # pdfinfo may not be available
    
    # Copy to outputs with desired name
    output_dir = resolve_output_dir(tex_path, out_dir)

    pdf_dest = output_dir / f"{base_name}.pdf"
    tex_dest = output_dir / f"{base_name}.tex"
    
    shutil.copy(pdf_source, pdf_dest)
    shutil.copy(tex_path, tex_dest)
    
    print(f"[OK] Compiled and copied to {output_dir}:")
    print(f"  PDF: {pdf_dest}")
    print(f"  TEX: {tex_dest}")

    # Machine-readable line for callers that want to pick up the paths
    print(f"\nPRESENT_FILES:{pdf_dest},{tex_dest}")

    return pdf_dest, tex_dest

def main():
    parser = argparse.ArgumentParser(description="Compile LaTeX resume and copy to an outputs directory")
    parser.add_argument("tex_file", help="Path to the .tex file")
    parser.add_argument("--name", help="Output filename (without extension)", default=None)
    parser.add_argument("--out", help="Output directory (default: sandbox outputs dir, else the .tex file's directory)", default=None)

    args = parser.parse_args()
    compile_latex(Path(args.tex_file), args.name, args.out)

if __name__ == "__main__":
    main()
