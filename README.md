# Projeto de TCC - Fábrica de Software

Este repositório contém o código-fonte em LaTeX para o Trabalho de Conclusão de Curso (TCC), utilizando o modelo do curso de Engenharia de Software da UFG (`UFG_INF_BES_TCC_Modelo`).

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado e rodando em sua máquina.

## Como compilar e executar o projeto com Docker

Para gerar o PDF a partir do código LaTeX de forma limpa e sem necessidade de instalar pacotes pesados do TeX na sua máquina, utilizaremos a imagem oficial do TeX Live através do Docker.

### Passo a passo para compilação

1. Abra o terminal.
2. Navegue até o diretório do modelo do TCC (onde está o arquivo `.tex` principal):
   ```bash
   cd UFG_INF_BES_TCC_Modelo
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

4. Após a conclusão sem erros, o arquivo PDF resultante (`monografia-tcc-bes.pdf`) estará disponível dentro da pasta `UFG_INF_BES_TCC_Modelo`. Você pode abri-lo com qualquer leitor de PDF de sua preferência.

### Limpando arquivos temporários

A compilação do LaTeX gera diversos arquivos auxiliares (`.aux`, `.log`, `.toc`, `.bbl`, etc.). Para limpar seu diretório e manter apenas os arquivos fonte (e o PDF gerado), você pode utilizar o comando de limpeza do `latexmk`:

```bash
docker run --rm -v "$PWD":/workdir -w /workdir texlive/texlive latexmk -c monografia-tcc-bes.tex
```

*(Dica: caso queira excluir também o PDF gerado para fazer uma limpeza completa, altere a flag `-c` minúscula para `-C` maiúscula).*
