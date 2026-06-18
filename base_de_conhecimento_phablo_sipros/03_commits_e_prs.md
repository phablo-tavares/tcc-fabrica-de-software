# Commits e Pull Requests (PRs)

Este arquivo documenta as contribuições diretas de código realizadas por **Phablo Tavares** no repositório do SIPROS, englobando seus Pull Requests abertos e seus commits ao longo do projeto.

## Pull Requests Abertos por Phablo

Durante sua atuação, Phablo abriu e fundiu (merged) múltiplos PRs importantes para o andamento técnico da plataforma:

1. **PR #359: #342 - criado regras de interface tela meus procesos**
   - **Data de criação:** 31/05/2026
   - **Status:** Merged (01/06/2026)
   - **Contexto:** Adição de lógicas e feedback visual na tela do candidato focando em "Meus Processos".

2. **PR #318: Feature 304 testes de unidade oficial**
   - **Data de criação:** 18/05/2026
   - **Status:** Merged (19/05/2026)
   - **Contexto:** Criação e estruturação da suíte de testes de unidade com relatórios oficiais para garantir a qualidade do sistema.

3. **PR #282: Feature 253 autenticacao via google pr** (E PR #277 relacionado)
   - **Data de criação:** 04/05/2026
   - **Status:** Merged (05/05/2026)
   - **Contexto:** Entrega da feature de login com o Google, configurando OAuth via Keycloak, capturando callbacks e gerenciando erros (ex: cancelamento).

4. **PR #230: Feature 214 remocao do mock de autenticacao e limpeza de credenciais** (E PR #220 relacionado)
   - **Data de criação:** 17/04/2026
   - **Status:** Merged (17/04/2026)
   - **Contexto:** Exclusão completa de credenciais hardcoded e do serviço `AuthService` do front-end. O código passou a consultar inteiramente o Keycloak configurado por meio de `.env`.

5. **PR #172: #139 - relatorio vv prototipos vs casos de uso** (E PR #144 relacionado)
   - **Data de criação:** 05/04/2026
   - **Status:** Merged (05/04/2026)
   - **Contexto:** Entrega do relatório de inconsistências UI x Documentação, fundamental para criar as "sub-issues" e corrigir o backlog de front-end.

6. **PR #153: #89 - Delete Ambientacao-ESTER.md** (E PR #110 relacionado)
   - **Data de criação:** 01/04/2026
   - **Status:** Merged (01/04/2026)
   - **Contexto:** Ajustes e remoção de documentos defasados sobre ambientação da equipe.

## Histórico de Commits (Destaques)

No total, dezenas de commits foram realizados com autoria de `@phablo-tavares`. Alguns exemplos que demonstram rastreabilidade técnica:

- **01/06/2026**: `implementada mudanças solicitadas em code review` (Ligado à issue #342)
- **19/05/2026**: `#176 - Corrige validacao de state no fluxo OAuth/OIDC com PKCE para evitar troca de code injetado.`
- **18/05/2026**: Múltiplos commits da `Feature #304` implementando e documentando Testes Unitários.
- **04/05/2026**: `#253 - adicionado PKCE no login com google e nao deslogar em http 404` (Refinamentos de segurança vitais).
- **30/04/2026**: `#253 - Habilita o fluxo Authorization Code no client e conecta o botao "Continuar com o Google" ao Identity Provider. Adiciona o processamento do callback no Angular para obter o token e tratar erros.`
- **29/04/2026**: `#253 - automatiza criacao do Google IDP no setup do Keycloak. Adiciona carregamento do .env no script PowerShell...`
- **13/04/2026**: `#214 - limpeza completa do AuthService, mock-users e exclusao de credenciais hardcoded`
- **05/04/2026**: `#139 - relatorio vv prototipos vs casos de uso`
