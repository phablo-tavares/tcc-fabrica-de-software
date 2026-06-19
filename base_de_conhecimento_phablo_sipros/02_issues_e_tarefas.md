# Issues e Tarefas

Abaixo estão listadas as principais issues onde **Phablo Tavares** constou como atribuído (`assignee`) ou teve forte envolvimento no planejamento e execução dentro do projeto SIPROS.

## 1. Issue #214: Remoção do mock de autenticação e limpeza de credenciais
- **Status:** Concluída (Fechada em 17/04/2026)
- **Tipo:** Task
- **Descrição:** Phablo foi o responsável por limpar todo o código do SIPROS que continha dois serviços de autenticação paralelos e credenciais hardcoded. O serviço mock (`AuthService`) foi completamente removido, além da eliminação do arquivo `mock-users.json`. O `CLIENT_ID` do Keycloak foi externalizado para variáveis de ambiente.
- **Impacto:** Aumentou expressivamente a segurança do projeto e diminuiu o débito técnico/complexidade de manutenção ao organizar o fluxo de login em um único serviço (`AutenticacaoService`).

## 2. Issue #253: Autenticação via Google
- **Status:** Concluída (Fechada em 05/05/2026)
- **Tipo:** Feature
- **Descrição:** Essa issue visava fazer com que o botão "Entrar com Google" no front-end funcionasse. Phablo trabalhou na integração direta para registrar o SIPROS como aplicativo, configurar o Keycloak e redirecionar os fluxos de sucesso/cancelamento de login para a plataforma adequadamente.
- **Impacto:** Adicionou Login Social ao sistema, melhorando significativamente a acessibilidade para os candidatos.

## 3. Issue #179: Autenticação Keycloak e Tratamento de Sessão
- **Status:** Concluída (Fechada em 28/04/2026)
- **Descrição:** Trabalho feito em conjunto com outros membros da Equipe Dourada (Thiago Vicente de Aquino, Felipe Duarte da Rocha Paço, Hugo Moreno Veiga Jardim, Lucas Gabriel Nunes Alves, etc.) para eliminar lógicas paralelas, tratar o redirecionamento após o login que caía numa rota vazia `/dashboard` e verificar regras da senha (RN03).
- **Atuação:** O usuário atuou ativamente nesta task implementando restrições de session no Angular e a exibição do Hero Logado, bem como participando das PRs relacionadas (ex: `feature-179-autenticacao-keycloak-e-tratamento-de-sessao`).

## 4. Issue #176: Integração OAuth Google e Recuperação de Senha
- **Status:** Concluída (Fechada em 11/06/2026)
- **Descrição:** Issue pai ampla que englobou os fluxos de acesso pelo Google, Gov.br e a redefinição de senhas. A ausência dessas lógicas bloqueava testes em ambiente de homologação e produção.
- **Atuação:** Atuou junto à equipe em componentes front-end, redirecionamento pelo router (`/esqueci-minha-senha`), além de adequar o Keycloak IdP.

## 5. Issue #139: VV - Protótipos × Casos de Uso [1/2]
- **Status:** Concluída (Fechada em 05/04/2026)
- **Descrição:** Verificação e Validação (V&V) comparando protótipos de alta fidelidade no Figma com os casos de uso definidos em documentação Markdown.
- **Atuação:** Phablo identificou aderência, inconsistências e documentou os débitos técnicos nas telas Inscrição, Home, Processos, Detalhes do processo, Cadastro, etc.

## 6. Issue #309: Testes de Integração
- **Status:** Concluída (Fechada em 17/05/2026)
- **Descrição:** Testes robustos englobando o fluxo Keycloak, Autenticação, Banco de Dados, etc.
- **Atuação:** Como assignee junto a Hugo Moreno Veiga Jardim (membro da Equipe Dourada), auxiliou no fluxo que contemplava o OAuth Keycloak (que ele próprio havia implementado anteriormente).
