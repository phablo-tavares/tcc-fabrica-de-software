# Base de Conhecimento - Apresentação Equipe Dourada (Sipros)

Este documento foi gerado com base na análise de issues, commits e documentação do repositório Sipros para auxiliar no preenchimento dos slides faltantes da apresentação.

## Slide 3: O Sistema Sipros e o Desafio

- **Breve descrição do Sipros:** O Sistema Integrado de Processos Seletivos (SIPROS) é a plataforma oficial da Fábrica de Software INF para a criação e gestão de processos seletivos. Ele permite a administração de todo o ciclo de vida das inscrições e a interação dos candidatos.
- **Há quanto tempo está em produção / nível de criticidade:** É um sistema de alta criticidade pois lida com a admissão de novos integrantes, gestão de candidatos e pagamentos de GRU (Guia de Recolhimento da União).
- **Principal dor relatada pelos usuários antes da nossa entrada:** Candidatos não conseguiam usar login social (Google, Gov.BR) e o fluxo de "Esqueci minha senha" não existia (estava inerte na interface), deixando-os bloqueados de acessar suas contas. Além disso, a equipe administrativa não possuía ferramentas funcionais no backend (os endpoints retornavam 501 Not Implemented) para transitar o status das inscrições ou gerar relatórios de forma autônoma.
- **Manter o sistema evoluindo:** O desafio consistiu em remover mocks e lógicas falsas antigas em paralelo à implementação do modelo real no Keycloak.
- **Reduzir débitos técnicos:** A equipe fez um levantamento massivo onde identificaram cerca de 62 débitos técnicos para priorização.

## Slide 4: Nossa Atuação

- **Novas funcionalidades e ajustes entregues:**
  - Integração oficial com OAuth (Google e Gov.BR) e fluxo de recuperação de senha (#176).
  - Implementação completa do dashboard autenticado "Meus Processos" para o candidato (#192).
  - Refinamento público da listagem de processos seletivos, ativando paginação, filtros e ordenação que antes não funcionavam (#196).
  - Gestão Administrativa de Inscrições e Geração de Relatórios reais (Backend #195).
- **Testes, revisões de código e critérios de aceite aplicados:** Realizou-se um planejamento estruturado e execução formal dos testes para os fluxos críticos de autenticação Google e redefinição de senha, validando os requisitos (Issue #295).
- **Pontos de risco mapeados e tratados:** Identificou-se que o código misturava autenticação mockada com requisições reais. Além disso, foi contornado o problema no Keycloak (Required Actions) que gerava erros enganosos dizendo "Senha Incorreta" imediatamente após um cadastro recém-realizado (#279).
- **Melhorias de usabilidade e interface entregues:** Governança massiva do protótipo no Figma (tagging de versões oficiais e remoção de redundâncias) e refatoração da experiência de senha, adicionando validação dinâmica que responde em tempo real.

## Slide 5 e 10: O Projeto em Números / Qualidade

- **14.486 linhas de código adicionadas**
- **12 issues abertas e 12 issues resolvidas**
- **62 débitos técnicos identificados** e analisados.
- **Cobertura de Testes Alcançada:** _(Sugestão: Preencher com a métrica do SonarQube/JaCoCo do seu CI/CD, por exemplo: ~80%)_
- **172 commits realizados**
- **Bugs identificados e corrigidos antes da entrega:** Em torno de 4 a 5 bugs críticos complexos resolvidos (ex: falhas de dropdown, erro de redirecionamento 404 pós-login, e o bug impeditivo de "invalid_grant" na criação de conta).
- **Satisfação:** 100% de taxa de resolução nas issues atribuídas ao ciclo da Equipe Dourada.

## Slide 7 e 8: Saúde do Código (Débitos Técnicos Resolvidos)

Sugestão de três principais débitos técnicos para preencher os *placeholders* no Slide 8:

1. **Autenticação Keycloak Concorrente com Mocks (#179)**
   - **Antes:** Havia duas lógicas de login convivendo no mesmo código (mock vs real). Ao logar, o candidato ia para rotas inexistentes (ex: `/dashboard`) e o formulário de cadastro era falso e não criava usuários no backend.
   - **Ação:** Remoção completa dos mocks no Frontend, integração 100% real com Keycloak, proteção correta das rotas (AuthGuards) e ajuste visual na Home de estado logado.

2. **Apagão Administrativo: Endpoints 501 (#195)**
   - **Antes:** Os endpoints para administradores atualizarem status de inscrição ou gerarem relatórios retornavam apenas `501 Not Implemented`. O fluxo administrativo estava totalmente travado.
   - **Ação:** Implementação da máquina de estados no backend (Java), garantindo as transições válidas de status de inscrição, e permitindo consultas de relatórios apenas por roles de admin.

3. **Inconsistências no Protótipo e Falta de Documentação (#114 e #193)**
   - **Antes:** Figma caótico com telas duplicadas, casos de uso vazios (como a "Geração de GRU") e falta de rastreabilidade (visões do front sem documentação base).
   - **Ação:** Governança completa. Aplicação de tags (Oficial/Obsoleta), unificação da documentação Markdown com o Figma, e resolução de inconsistências visuais (ex: uso errático de *breadcrumbs*).

## Slide 9: Entrega Visual (O que mudou na prática)

**Sugestão de Prints para a tela (Antes/Depois): Refatoração da Senha (#233, #247)**
- **ANTES:** O campo de senha exibia estaticamente "Deve ter pelo menos 8 caracteres". O usuário não tinha certeza se cumpria (maiúscula, número, especial) até clicar em Salvar.
- **DEPOIS:** O placeholder convida ("Digite sua senha") e, ao digitar, surge uma lista visual de requisitos (bullets). Cada requisito fica marcado como atendido (e some ou fica verde) em tempo real conforme a pessoa digita.
- **Em uma frase:** "Antecipamos o feedback visual do formulário, eliminando a frustração de preencher tudo e descobrir que a senha não era forte o suficiente só ao final."

## Slide 11: Resultado (O valor que levamos para a fábrica)

*(Sugestões para balizar os dados faltantes do slide)*
- **[X] horas/semana economizadas:** Sem o painel administrativo pronto (#195), aprovar/recusar candidatos ou extrair listas exigia manipulação manual de banco de dados por um desenvolvedor. A automatização trouxe autonomia total à equipe de seleção.
- **Equipes diretamente impactadas:** Ao menos 3 equipes/grupos: **Candidatos** (autenticação Gov.br e painel *Meus Processos* claro), **Time de Seleção/RH** (gestão via backend operacional) e **Desenvolvedores Futuros** (que pegam um código limpo de mocks e com Figma organizado).

## Slide 12: Lições e Aprendizados

*(Você pode usar estes pontos-chave caso não tenham definido ainda)*
- **Sobre trabalho em equipe:** A importância crítica de fazer *V&V (Verificação e Validação)* juntos — parear entre as visões de Design, Produto (Casos de Uso) e Código garante que não se programe nada fora do escopo oficial.
- **Sobre priorização:** Percebemos que não dá para resolver 62 débitos técnicos em um ciclo, mas focar naqueles que bloqueiam o fluxo do usuário (ex: Login e Cadastro bugados) traz o maior impacto real.
- **Aprendizado técnico:** Compreensão avançada de como funciona o fluxo OAuth (Identity Providers) no Keycloak, gerenciando tokens e transições de estado (Required Actions).
