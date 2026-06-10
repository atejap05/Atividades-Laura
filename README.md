# Atividades da Laura

Atividades escolares impressas, criativas e pensadas para ajudar a Laura (8 anos, **2º ano do
Ensino Fundamental**) a revisar e aprofundar conteúdos de forma divertida. Cada atividade é
uma folha pronta para **imprimir em A4** (ou salvar em PDF).

## Filosofia das atividades

Cada folha procura:

- **Mesclar revisão e aprofundamento** — relembrar o conteúdo e dar um passo além.
- Combinar **questões de múltipla escolha** (estilo prova/simulado) com **questões
  discursivas** (desenvolvimento de escrita).
- Ter um **tema lúdico** (super-heróis, animais, histórias) que prende a atenção de uma
  criança de 7–8 anos.
- Trazer um **gabarito** ao final, com as respostas e, quando aplicável, as habilidades da
  **BNCC** correspondentes.

## Como usar

1. Abra o arquivo `.html` da atividade no navegador.
2. Clique em **"Imprimir / Salvar em PDF"** (ou `Ctrl + P`) e escolha **A4**.
3. Imprima ou salve o PDF para entregar à criança.

Os arquivos são **autossuficientes** (HTML com CSS e JS embutidos): não precisam de internet,
instalação ou build.

## Estrutura do repositório

```
atividades/
  _template-atividade-a4.html   ← esqueleto em branco para começar uma atividade nova
  matematica/      modelo, tabuada, geometria, lógica, revisão 1º ano
  portugues/       revisão de português
  ciencias/        ciências (inclui temas como "Cavaleiros do Zodíaco")
  ingles/          inglês e histórias bilíngues
  raciocinio/      lógica / raciocínio crítico ("Mistério de Mara")
  multidisciplinar/ provas que cruzam disciplinas (Português + Matemática)
  producao-textual/ escrita e elaboração de pequenos textos (ver README da pasta)
recursos/          PDFs de apoio e workbooks "Super Matemática" (1º ao 4º ano)
```

O modelo de referência do padrão é
`atividades/matematica/atividade-matematica-2ano-a4.html` (capa, seções de revisão +
exercícios, contas armadas, geometria, desafio e gabarito).

## Criando uma atividade nova

Copie `atividades/_template-atividade-a4.html` para a pasta da disciplina, preencha os
`{{PLACEHOLDERS}}` e siga o padrão descrito em [`CLAUDE.md`](./CLAUDE.md). Em resumo:
documento A4 com `@media print`, capa com cabeçalho, seções `Parte N — Tema` (conceito →
texto → questões de múltipla escolha e discursivas), desafio final e gabarito. Nomeie como
`atividade-<disciplina>-<ano>ano-a4.html` (ou um nome descritivo em kebab-case).

> Para assistentes de IA: as instruções de trabalho estão em [`CLAUDE.md`](./CLAUDE.md),
> [`AGENTS.md`](./AGENTS.md) e `.cursor/rules/`.
