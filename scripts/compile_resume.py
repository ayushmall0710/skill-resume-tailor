#!/usr/bin/env python3
"""
Compile a LaTeX resume to PDF, copy to outputs, and print paths for presentation.

Usage:
    python3 scripts/compile_resume.py <tex_file> [--name <output_name>]

Examples:
    python3 scripts/compile_resume.py /home/claude/resume.tex
    python3 scripts/compile_resume.py /home/claude/resume.tex --name Microsoft_MLE_Resume
"""

import argparse
import subprocess
import shutil
import sys
from pathlib import Path

OUTPUT_DIR = Path("/mnt/user-data/outputs")

def compile_latex(tex_path: Path, output_name: str = None) -> tuple[Path, Path]:
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
                    print(f"⚠️  WARNING: Resume is {pages} pages (should be 1 page)", file=sys.stderr)
                else:
                    print(f"✓ Resume is 1 page")
                break
    except:
        pass  # pdfinfo may not be available
    
    # Copy to outputs with desired name
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    pdf_dest = OUTPUT_DIR / f"{base_name}.pdf"
    tex_dest = OUTPUT_DIR / f"{base_name}.tex"
    
    shutil.copy(pdf_source, pdf_dest)
    shutil.copy(tex_path, tex_dest)
    
    print(f"✓ Compiled and copied to outputs:")
    print(f"  PDF: {pdf_dest}")
    print(f"  TEX: {tex_dest}")
    
    # Output paths for present_files tool (JSON format for easy parsing)
    print(f"\nPRESENT_FILES:{pdf_dest},{tex_dest}")
    
    return pdf_dest, tex_dest

def main():
    parser = argparse.ArgumentParser(description="Compile LaTeX resume and copy to outputs")
    parser.add_argument("tex_file", help="Path to the .tex file")
    parser.add_argument("--name", help="Output filename (without extension)", default=None)
    
    args = parser.parse_args()
    compile_latex(Path(args.tex_file), args.name)

if __name__ == "__main__":
    main()
