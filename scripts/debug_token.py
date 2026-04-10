"""
OGARCOM — Debug: lista contas de anúncio acessíveis pelo token
"""
import requests
import os

TOKEN = os.environ["META_ACCESS_TOKEN"]

print("\n  Verificando token...")
r = requests.get(f"https://graph.facebook.com/v19.0/me?access_token={TOKEN}&fields=id,name")
print(f"  Usuário: {r.json()}")

print("\n  Buscando contas de anúncio acessíveis...")
r = requests.get(
    f"https://graph.facebook.com/v19.0/me/adaccounts",
    params={
        "access_token": TOKEN,
        "fields": "id,name,account_status",
        "limit": 20,
    }
)
data = r.json()
if "data" in data:
    for acc in data["data"]:
        print(f"  Conta: {acc.get('name')} | ID: {acc.get('id')} | Status: {acc.get('account_status')}")
    if not data["data"]:
        print("  Nenhuma conta encontrada para este token.")
else:
    print(f"  Erro: {data}")
