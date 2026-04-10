# ══════════════════════════════════════════════════════════
# OGARCOM — Sincronizador de Vault para GitHub
# Rode SINCRONIZAR.bat para atualizar a dashboard
# ══════════════════════════════════════════════════════════

$VAULT    = "G:\meu drive\ogarcom"
$REPO     = "G:\meu drive\ogarcom-dashboard"
$PROJETOS = @("GESSEIRO-MASTER", "PINTOR-PRO", "SINDICO-PRO")

Write-Host ""
Write-Host "  OGARCOM - Sincronizando vault..." -ForegroundColor Cyan
Write-Host ""

$erros = 0

# ── Copiar CLAUDE.md ────────────────────────────────────
$dataDir = "$REPO\data"
if (-not (Test-Path $dataDir)) { New-Item -ItemType Directory -Path $dataDir | Out-Null }
if (Test-Path "$VAULT\CLAUDE.md") {
    Copy-Item -Path "$VAULT\CLAUDE.md" -Destination "$dataDir\CLAUDE.md" -Force
    Write-Host "  [OK] CLAUDE.md" -ForegroundColor Green
}

# ── Copiar arquivos dos projetos ────────────────────────
foreach ($proj in $PROJETOS) {
    $origem  = "$VAULT\Conhecimento\MVT\Projetos\$proj"
    $destino = "$REPO\data\$proj"

    if (-not (Test-Path $destino)) { New-Item -ItemType Directory -Path $destino | Out-Null }

    $arquivos = @(
        @("$origem\INDEX.md",                   "$destino\INDEX.md"),
        @("$origem\Campanhas\CAMPANHAS.md",      "$destino\CAMPANHAS.md"),
        @("$origem\Copy\COPY.md",                "$destino\COPY.md"),
        @("$origem\Criativos\CRIATIVOS.md",      "$destino\CRIATIVOS.md"),
        @("$origem\Pagina\ESTRUTURA-PAGINA.md",  "$destino\ESTRUTURA-PAGINA.md"),
        @("$origem\Analises\ANALISES.md",        "$destino\ANALISES.md")
    )

    foreach ($arq in $arquivos) {
        $de   = $arq[0]
        $para = $arq[1]
        $nome = [System.IO.Path]::GetFileName($para)
        if (Test-Path $de) {
            Copy-Item -Path $de -Destination $para -Force
            Write-Host "  [OK] $proj\$nome" -ForegroundColor Green
        } else {
            Write-Host "  [--] $proj\$nome (nao encontrado)" -ForegroundColor DarkGray
        }
    }
}

# ── Copiar session logs ─────────────────────────────────
$logsDestino = "$REPO\data\session-logs"
if (-not (Test-Path $logsDestino)) { New-Item -ItemType Directory -Path $logsDestino | Out-Null }

$logs = Get-ChildItem "$VAULT\Session-Logs\*.md" -ErrorAction SilentlyContinue
foreach ($log in $logs) {
    Copy-Item -Path $log.FullName -Destination "$logsDestino\$($log.Name)" -Force
    Write-Host "  [OK] session-logs\$($log.Name)" -ForegroundColor Green
}

# ── Buscar dados da UTMify ──────────────────────────────
Write-Host ""
Write-Host "  Atualizando Meta Ads via UTMify..." -ForegroundColor Cyan
$nodeResult = node "$REPO\scripts\fetch_utmify.js" 2>&1
Write-Host $nodeResult
if ($LASTEXITCODE -ne 0) {
    Write-Host "  [AVISO] UTMify falhou, mantendo dados anteriores." -ForegroundColor Yellow
} else {
    Write-Host "  [OK] meta-ads.json atualizado" -ForegroundColor Green
}

Write-Host ""
Write-Host "  Enviando para o GitHub..." -ForegroundColor Cyan
Write-Host ""

# ── Git: pull + commit + push ───────────────────────────
Set-Location $REPO

git pull origin main 2>&1 | Out-Null

$data = Get-Date -Format "yyyy-MM-dd HH:mm"

git add data/ 2>&1 | Out-Null

$status = git status --porcelain 2>&1
if ($status) {
    git commit -m "sync: vault atualizado em $data" 2>&1 | Out-Null
    $push = git push origin main 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  Dashboard atualizada com sucesso!" -ForegroundColor Green
        Write-Host "  URL: https://BoubbleG.github.io/ogarcom-dashboard" -ForegroundColor Cyan
    } else {
        Write-Host "  Erro ao enviar para o GitHub:" -ForegroundColor Red
        Write-Host $push -ForegroundColor Red
        $erros++
    }
} else {
    Write-Host "  Nenhuma alteracao detectada. Dashboard ja esta atualizada." -ForegroundColor Yellow
}

Write-Host ""
if ($erros -eq 0) {
    Write-Host "  Concluido sem erros." -ForegroundColor Green
} else {
    Write-Host "  Concluido com $erros erro(s). Verifique acima." -ForegroundColor Red
}
Write-Host ""
