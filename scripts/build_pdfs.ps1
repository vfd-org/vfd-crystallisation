# Build all LaTeX papers to PDF (Windows PowerShell)
# Usage: .\scripts\build_pdfs.ps1
# Requirements: pdflatex, bibtex (TeX Live or MiKTeX)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$PapersDir = Join-Path $RepoRoot "papers"

function Build-Paper {
    param([string]$Dir)

    $texFile = Get-ChildItem -Path $Dir -Filter "*.tex" | Select-Object -First 1
    if (-not $texFile) {
        Write-Host "  SKIP: no .tex file in $Dir"
        return
    }

    $basename = $texFile.BaseName
    Write-Host "  Building: $basename"

    Push-Location $Dir
    try {
        & pdflatex -interaction=nonstopmode "$basename.tex" 2>&1 | Out-Null
        & bibtex $basename 2>&1 | Out-Null
        & pdflatex -interaction=nonstopmode "$basename.tex" 2>&1 | Out-Null
        & pdflatex -interaction=nonstopmode "$basename.tex" 2>&1 | Out-Null

        if (Test-Path "$basename.pdf") {
            Write-Host "    OK: $basename.pdf"
        } else {
            Write-Host "    FAILED: $basename.pdf not generated"
            exit 1
        }

        # Clean auxiliary files
        Remove-Item -ErrorAction SilentlyContinue "$basename.aux", "$basename.bbl", `
            "$basename.blg", "$basename.log", "$basename.out", "$basename.toc"
    } finally {
        Pop-Location
    }
}

Write-Host "=== VFD Crystallisation - PDF Build ==="
Write-Host ""

Write-Host "Building main preprint (flagship)..."
Build-Paper (Join-Path $PapersDir "main-preprint")

Write-Host "Building formalism companion (A)..."
Build-Paper (Join-Path $PapersDir "formalism")

Write-Host "Building experimental companion (B)..."
Build-Paper (Join-Path $PapersDir "experimental")

Write-Host "Building supplementary..."
Build-Paper (Join-Path $PapersDir "supplementary")

Write-Host ""
Write-Host "=== All PDFs built successfully ==="
Get-ChildItem -Path $PapersDir -Recurse -Filter "*.pdf" | ForEach-Object {
    Write-Host "  $($_.FullName)"
}
