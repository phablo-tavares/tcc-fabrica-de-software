# Projeto de TCC - Fábrica de Software (SIPROS)

Este repositório contém o código-fonte em LaTeX para o Trabalho de Conclusão de Curso (TCC) de **Phablo Tavares Paixão**, do curso de Engenharia de Software da Universidade Federal de Goiás (UFG). O documento baseia-se no modelo oficial `UFG_INF_BES_TCC_Modelo`.

## Contextualização e Objetivos

O trabalho documenta a experiência prática vivida na disciplina de **Prática em Engenharia de Software (Fábrica de Software)** durante o semestre **2026/1**, desenvolvendo o sistema SIPROS (Sistema Integrado de Processos Seletivos).

O **Objetivo Geral** deste TCC é descrever e analisar a evolução e refatoração full-stack do sistema SIPROS no contexto da Fábrica de Software acadêmica, com ênfase na implementação de mecanismos robustos de segurança (Keycloak e PKCE), evolução de interface (Angular) e na adoção de práticas para elevação da qualidade do software (V&V e testes automatizados). A pesquisa classifica-se como uma **Pesquisa-Ação**.

## Estrutura do Repositório

- `tcc_phablo_tavares/`: Diretório de trabalho principal contendo os arquivos LaTeX e imagens do TCC.
- `UFG_INF_BES_TCC_Modelo/`: Diretório com o modelo limpo original (para fins de backup/referência).
- `base_de_conhecimento_phablo_sipros/`: Base de dados crua e artefatos de pesquisa (relatórios, respostas a questionários) que dão embasamento à redação.

---

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado e rodando em sua máquina.

## Como compilar e executar o projeto com Docker

Para gerar o PDF a partir do código LaTeX de forma limpa e sem necessidade de instalar pacotes pesados do TeX na sua máquina, utilizaremos a imagem oficial do TeX Live através do Docker.

### Passo a passo para compilação

1. Abra o terminal.
2. Navegue até o diretório do seu TCC (onde está o arquivo `.tex` principal):
   ```bash
   cd tcc_phablo_tavares
   ```

3. Execute o comando de compilação. Este comando monta o diretório atual dentro de um container e executa a compilação:

   **Opção 1 (Recomendada): Usando `latexmk`**
   O utilitário `latexmk` compila automaticamente o documento quantas vezes forem necessárias para resolver sumário, referências cruzadas e citações bibliográficas.
   ```bash
   docker run --rm -v "$PWD":/workdir -w /workdir texlive/texlive latexmk -pdf monografia-tcc-bes.tex
   ```

   **Opção 2: Usando `pdflatex` + `bibtex` (manual)**
   Caso prefira rodar passo a passo para ver exatamente o processo do LaTeX:
   ```bash
   docker run --rm -v "$PWD":/workdir -w /workdir texlive/texlive sh -c "pdflatex monografia-tcc-bes.tex && bibtex monografia-tcc-bes && pdflatex monografia-tcc-bes.tex && pdflatex monografia-tcc-bes.tex"
   ```

4. Após a conclusão sem erros, o arquivo PDF resultante (`monografia-tcc-bes.pdf`) estará disponível dentro da pasta `tcc_phablo_tavares`. Você pode abri-lo com qualquer leitor de PDF de sua preferência.

### Limpando arquivos temporários

A compilação do LaTeX gera diversos arquivos auxiliares (`.aux`, `.log`, `.toc`, `.bbl`, etc.). Para limpar seu diretório e manter apenas os arquivos fonte (e o PDF gerado), você pode utilizar o comando de limpeza do `latexmk`:

```bash
docker run --rm -v "$PWD":/workdir -w /workdir texlive/texlive latexmk -c monografia-tcc-bes.tex
```

*(Dica: caso queira excluir também o PDF gerado para fazer uma limpeza completa, altere a flag `-c` minúscula para `-C` maiúscula).*
