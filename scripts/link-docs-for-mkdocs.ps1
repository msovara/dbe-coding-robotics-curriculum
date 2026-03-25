# Link curriculum into docs/ for MkDocs (Windows). Run from repo root:
#   powershell -ExecutionPolicy Bypass -File scripts/link-docs-for-mkdocs.ps1
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root
$Docs = Join-Path $Root "docs"
New-Item -ItemType Directory -Force -Path $Docs | Out-Null

$dirs = @(
    "day-01-scratch", "day-02-scratch", "day-03-arduino",
    "day-04-microbit", "day-05-microbit-codeclub",
    "resources", "supporting-materials"
)
foreach ($name in $dirs) {
    $target = Join-Path $Root $name
    $link = Join-Path $Docs $name
    if (Test-Path $link) { Remove-Item $link -Force -Recurse -ErrorAction SilentlyContinue }
    if (Test-Path $target) {
        New-Item -ItemType Junction -Path $link -Target $target | Out-Null
    }
}

$files = @(
    "WORKSHOP_TIMETABLE_ONE_PAGE.md", "WORKSHOP_TIMETABLE.md",
    "CURRICULUM-SUMMARY.md", "CHPC_INTEGRATION.md", "MEETING_AGENDA.md",
    "EMAIL_TEMPLATE.md", "EMAIL_WORKSHOP_SUMMARY.md",
    "GITHUB_SETUP.md", "GITHUB_PAGES.md", "CHPC_DSI_CODING_SCHOOL_PR.md"
)
foreach ($f in $files) {
    $target = Join-Path $Root $f
    $link = Join-Path $Docs $f
    if (Test-Path $link) { Remove-Item $link -Force -ErrorAction SilentlyContinue }
    if (Test-Path $target) {
        New-Item -ItemType HardLink -Path $link -Target $target | Out-Null
    }
}

Write-Host "Linked curriculum into docs/. Run: python -m mkdocs serve"
