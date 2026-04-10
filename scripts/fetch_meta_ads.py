"""
OGARCOM — Fetch Meta Ads Data
Busca métricas de todas as contas de anúncio e salva em data/meta-ads.json
"""

import requests
import json
import os
from datetime import datetime

TOKEN = os.environ["META_ACCESS_TOKEN"]

ACCOUNTS = {
    "GESSEIRO-MASTER": "1398408144771165",
    "PINTOR-PRO":      "1331372135233963",
    "SINDICO-PRO":     "2302574626902808"
}

FIELDS = ",".join([
    "spend",
    "impressions",
    "clicks",
    "ctr",
    "cpm",
    "cpc",
    "actions",
    "action_values",
    "purchase_roas",
    "cost_per_action_type",
])

API_VERSION = "v19.0"
DATE_PRESET = "last_30d"


def get_action(actions, action_type):
    if not actions:
        return 0
    for a in actions:
        if a.get("action_type") == action_type:
            return float(a.get("value", 0))
    return 0


def get_cost_per_action(cost_per_action_type, action_type):
    if not cost_per_action_type:
        return None
    for a in cost_per_action_type:
        if a.get("action_type") == action_type:
            return float(a.get("value", 0))
    return None


def fetch_account(account_id):
    url = f"https://graph.facebook.com/{API_VERSION}/act_{account_id}/insights"
    params = {
        "access_token": TOKEN,
        "fields": FIELDS,
        "date_preset": DATE_PRESET,
        "level": "account",
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json().get("data", [])
    return data[0] if data else {}


def safe_float(val, decimals=2):
    try:
        return round(float(val), decimals)
    except (TypeError, ValueError):
        return 0.0


def process(raw):
    spend   = safe_float(raw.get("spend", 0))
    actions = raw.get("actions", [])
    action_values    = raw.get("action_values", [])
    cost_per_action  = raw.get("cost_per_action_type", [])
    purchase_roas    = raw.get("purchase_roas", [])

    purchases          = get_action(actions, "purchase")
    initiate_checkout  = get_action(actions, "initiate_checkout")
    landing_page_views = get_action(actions, "landing_page_view")
    revenue            = get_action(action_values, "purchase")

    roas = 0.0
    if purchase_roas:
        roas = safe_float(purchase_roas[0].get("value", 0))

    lucro = safe_float(revenue - spend)
    roi   = safe_float((lucro / spend * 100) if spend > 0 else 0)
    cpv   = safe_float(spend / landing_page_views if landing_page_views > 0 else 0)
    icr   = safe_float((purchases / initiate_checkout * 100) if initiate_checkout > 0 else 0)
    cpa   = get_cost_per_action(cost_per_action, "purchase") or 0.0
    cpi   = get_cost_per_action(cost_per_action, "initiate_checkout") or 0.0

    return {
        "gasto":             spend,
        "impressoes":        int(raw.get("impressions", 0)),
        "cliques":           int(raw.get("clicks", 0)),
        "ctr":               safe_float(raw.get("ctr", 0)),
        "cpm":               safe_float(raw.get("cpm", 0)),
        "cpc":               safe_float(raw.get("cpc", 0)),
        "vendas":            int(purchases),
        "receita":           safe_float(revenue),
        "lucro":             lucro,
        "roas":              roas,
        "roi":               roi,
        "cpa":               safe_float(cpa),
        "initiate_checkout": int(initiate_checkout),
        "cpi":               safe_float(cpi),
        "visitas_pagina":    int(landing_page_views),
        "cpv":               cpv,
        "icr":               icr,
    }


def main():
    result = {
        "atualizado": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "periodo":    DATE_PRESET,
        "contas":     {}
    }

    for name, account_id in ACCOUNTS.items():
        print(f"  Buscando {name}...")
        try:
            raw = fetch_account(account_id)
            result["contas"][name] = process(raw)
            print(f"  [OK] {name}")
        except Exception as e:
            print(f"  [ERRO] {name}: {e}")
            result["contas"][name] = {"erro": str(e)}

    os.makedirs("data", exist_ok=True)
    with open("data/meta-ads.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n  Salvo em data/meta-ads.json")
    print(f"  Atualizado: {result['atualizado']}")


if __name__ == "__main__":
    main()
