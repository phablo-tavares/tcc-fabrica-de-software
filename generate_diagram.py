import base64
import zlib
import urllib.request
import os

mermaid_code = """
sequenceDiagram
    autonumber
    actor U as Usuário
    participant F as Frontend (Angular)
    participant K as Keycloak (Auth Server)
    participant G as Google (Identity Provider)
    participant B as Backend (Spring Boot)

    U->>F: Clica em "Login com Google"
    F->>F: Gera PKCE (Code Verifier e Challenge)
    F->>K: Redireciona com Auth Request<br/>(client_id, code_challenge, S256)
    K->>G: Delega Autenticação para o Google
    G-->>U: Solicita Credenciais Google
    U->>G: Insere Credenciais
    G-->>K: Retorna Auth Code do Google
    K-->>F: Redireciona com Authorization Code
    F->>K: POST /token<br/>(code, client_id, code_verifier)
    K->>K: Valida Code e Verifier
    K-->>F: Retorna Access Token (JWT)
    F->>B: Requisição API (Bearer Token)
    B->>K: Valida Assinatura (JWKS)
    K-->>B: Confirma Validade
    B-->>F: Retorna Dados Protegidos
    F-->>U: Renderiza Tela Principal
"""

os.makedirs('assets_tcc', exist_ok=True)

encoded = base64.urlsafe_b64encode(zlib.compress(mermaid_code.encode('utf-8'), 9)).decode('ascii')
url = f"https://kroki.io/mermaid/png/{encoded}"

print(f"Downloading from: {url}")

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open('assets_tcc/diagrama_oauth_pkce.png', 'wb') as out_file:
        out_file.write(response.read())
    print("Sucesso! Imagem salva em assets_tcc/diagrama_oauth_pkce.png via Kroki")
except Exception as e:
    print(f"Erro: {e}")
