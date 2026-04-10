# ══════════════════════════════════════════════════════════
# OGARCOM — Sincronizador de Vault para GitHub
# Rode SINCRONIZAR.bat para atualizar a dashboard
# ══════════════════════════════════════════════════════════

$VAULT   = "G:\meu drive\ogarcom"
$REPO    = "C:\Users\Fabricio\Downloads\ogarcom-dashboard"
$PROJETOS = @("GESSEIRO-MASTER", "PINTOR-PRO", "SINDICO-PRO")

Write-Host ""
Write-Host "  OGARCOM — Sincronizando vault..." -ForegroundColor Cyan
Write-Host ""

$erros = 0

# ── Copiar arquivos dos projetos ────────────────────────
foreach ($proj in $PROJETOS) {
    $origem = "$VAULT\Conhecimento\MVT\Projetos\$proj"
    $destino = "$REPO\data\$proj"

    if (-not (Test-Path $destino)) { New-Item -ItemType Directory -Path $destino | Out-Null }

    $arquivos = @(
        @{ de = "$origem\INDEX.md";                    para = "$destino\INDEX.md"           },
        @{ de = "$origem\Campanhas\CAMPANHAS.md";      para = "$destino\CAMPANHAS.md"        },
        @{ de = "$origem\Copy\COPY.md";                para = "$destino\COPY.md"             },
        @{ de = "$origem\Criativos\CRIATIVOS.md";      para = "$destino\CRIATIVOS.md"        },
        @{ de = "$origem\Pagina\ESTRUTURA-PAGINA.md";  para = "$destino\ESTRUTURA-PAGINA.md" },
        @{ de = "$origem\Analises\ANALISES.md";        para = "$destino\ANALISES.md"         }
    )

    foreach ($arq in $arquivos) {
        if (Test-Path $arq.de) {
            Copy-Item -Path $arq.de -Destination $arq.para -Force
            Write-Host "  [OK] $proj\$(Split-Path $arq.para -Leaf)" -ForegroundColor Green
        } else {
            Write-Host "  [--] $proj\$(Split-Path $arq.para -Leaf) (nao encontrado)" -ForegroundColor DarkGray
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

Write-Host ""
Write-Host "  Enviando para o GitHub..." -ForegroundColor Cyan
Write-Host ""

# ── Git: commit e push ──────────────────────────────────
Set-Location $REPO

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
