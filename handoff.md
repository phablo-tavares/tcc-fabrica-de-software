# Handoff: Status Atual do TCC - Phablo Tavares Paixão

Este documento serve como um guia de transferência de contexto (Handoff). Se você é um agente de IA (Antigravity) iniciando uma nova sessão de contexto, **leia este arquivo com atenção**. Ele define o estado atual do Trabalho de Conclusão de Curso (TCC) e fornece as diretrizes para continuá-lo.

## 1. Visão Geral do Projeto
- **Autor:** Phablo Tavares Paixão
- **Orientadora:** Profa. Dra. Sofia Larissa da Costa Paiva
- **Coorientador:** Prof. Dr. Juliano Lopes de Oliveira
- **Contexto:** Relato de Experiência e Pesquisa-Ação sobre a evolução e refatoração *full-stack* do sistema **SIPROS**, conduzido durante a disciplina de Fábrica de Software (UFG) no semestre 2026/1 com a "Equipe Dourada".
- **Foco Técnico:** Segurança em SPAs (OAuth 2.0, Keycloak, PKCE), Verificação e Validação (V&V), Garantia de Qualidade (Testes Automatizados, Code Review) e uso de metodologias inspiradas em práticas ágeis.

## 2. Estrutura do Repositório
- `base_de_conhecimento_phablo_sipros/`: Contém arquivos vitais como `perguntas_tcc_phablo.md`. **Sempre leia a base de conhecimento antes de propor qualquer conteúdo.**
- `tcc_phablo_tavares/`: Diretório que contém os arquivos `.tex` (LaTeX) em desenvolvimento.
- `tcc-fabrica-de-software/README.md`: Contém comandos e orientações gerais do projeto.

## 3. Estado Atual do TCC (O que JÁ FOI FEITO)
O TCC já possui sua estrutura principal finalizada. Toda a narrativa foi construída usando um tom acadêmico, impessoal (terceira pessoa), diplomático e construtivo (evitando atacar o código legado e focando na oportunidade de evolução arquitetural).

*   **Configuração e Pré-textuais:**
    *   Metadados do autor, orientadores e perfil profissional preenchidos.
    *   Agradecimentos redigidos. Dedicatória e Epígrafe desativadas.
    *   **Resumo e Abstract** escritos e alinhados com o escopo do projeto.
    *   Listas geradas e configuradas com sucesso (`\tabelas[figtabcod]` no template) limpas e sem páginas fantasmas de algoritmos. O pacote `babel` também foi ajustado para `brazilian` para evitar *warnings*.
*   **Capítulo 1 (Introdução) - `tex/cap_introducao.tex`:**
    *   Concluído. Apresenta a motivação, o contexto da equipe, os objetivos gerais e específicos, a metodologia acadêmica (pesquisa-ação) e reforça que a organização da equipe foi *inspirada* no Scrum/Kanban (sem aderência obrigatória de 100%).
*   **Capítulo 2 (Bases Teóricas) - `tex/cap_fundamentos.tex`:**
    *   Concluído. Cobre as bases de segurança web (OAuth 2.0 / PKCE), normativas de Qualidade (ISO 25010) e V&V (SWEBOK). Discute criticamente as ferramentas (Keycloak, Angular, Docker, GitHub).
    *   Contém o Diagrama de Sequência do Fluxo de Autenticação OAuth 2.0 (PKCE) gerado via Mermaid/Kroki.
*   **Capítulo 3 (Relato de Experiência) - `tex/cap_relato.tex`:**
    *   Concluído. Relata a evolução da base legada que possuía dados *mockados*. Detalha a implementação do Google via Keycloak, o mapeamento de Casos de Uso vs Figma (V&V), e as políticas de *Code Review* e testes de unidade.
    *   Rico em recursos visuais e técnicos: Possui Tabelas (Matriz de Intervenções e V\&V), Figuras (Quadro Kanban, PR de Code Review) e Blocos de Código (Interceptador Angular e Estrutura de Teste de Unidade), com margens corrigidas para evitar *Overfull hbox/vbox*.
*   **Capítulo 4 (Conclusões) - `tex/cap_conclusoes.tex`:**
    *   Concluído. Comprova o atingimento dos objetivos. Traz reflexões sobre a evolução de *hard* e *soft skills*. Lista conselhos para futuros alunos (lidar bem com código legado, focar em testes desde o início) e projeta trabalhos futuros (testes E2E, cobertura 100% no *back-end*).
*   **Referências Bibliográficas - `bib/referencias-tcc.bib`:**
    *   Arquivo limpo. Contém estritamente as 7 referências reais citadas no texto (RFCs, SWEBOK, ISO/IEC, Scrum Guide, Documentações oficiais). As chamadas `\cite{}` já estão integradas no texto.

## 4. Como Compilar o TCC
O TCC é compilado isoladamente via Docker. Utilize o seguinte comando na raiz de `tcc_phablo_tavares/`:
```bash
docker run --rm -v "$PWD":/workdir -w /workdir texlive/texlive latexmk -pdf monografia-tcc-bes.tex
```

## 5. Próximos Passos (Para a IA)
Ao assumir este contexto, suas responsabilidades prováveis serão:
1. Auxiliar em pequenos refinamentos gramaticais e de coesão, ou possíveis correções demandadas pela banca avaliadora.
2. Auxiliar na inclusão de novas referências científicas ou eventuais formatações solicitadas.
3. Se necessário, gerar ou atualizar novos apêndices ou materiais suplementares.

**Comportamento Exigido da IA:**
- Seja **objetivo e direto**.
- **Jamais edite arquivos de código sem o aval explícito do usuário.** Caso a demanda seja complexa, crie um plano de implementação.
- Mantenha sempre um tom diplomático ao referenciar o projeto SIPROS.
- Consulte ativamente os arquivos LaTeX existentes para garantir consistência.
