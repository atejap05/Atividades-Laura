# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> Documentação em português porque todo o conteúdo das atividades é pt-BR e o público (pai + filha) é brasileiro.

## Objetivo do repositório

Repositório pessoal para criar **atividades escolares impressas** que ajudam a Laura (8 anos,
atualmente no **2º ano do Ensino Fundamental**) a estudar. As atividades devem:

- **Mesclar revisão e aprofundamento** do conteúdo — relembrar o que já foi visto e ir um
  passo além.
- Combinar **questões de múltipla escolha** (estilo prova/simulado) com **questões
  discursivas / de desenvolvimento de escrita**.
- Ser **inteligentes, divertidas e criativas** — temas lúdicos (super-heróis, animais,
  histórias) que envolvem uma criança de 7–8 anos.
- Sair **impressas em A4** com qualidade (a entrega final é o PDF / folha impressa).

Referências de bom formato: o modelo canônico é
`atividades/matematica/atividade-matematica-2ano-a4.html` e os PDFs em
`recursos/kit-super-matematica/` (workbooks "Super Matemática" por ano-escolar usados como
inspiração de conteúdo e didática).

O mantenedor é desenvolvedor web experiente — pode-se ser técnico e direto.

## Estrutura do repositório

```
atividades/
  _template-atividade-a4.html   ← esqueleto em branco para novas atividades
  matematica/  portugues/  ciencias/  ingles/  raciocinio/
  multidisciplinar/             ← atividades que cruzam disciplinas
  producao-textual/             ← escrita / elaboração de pequenos textos (ver README local)
recursos/                       ← material de referência (não gerado): PDFs, kit-super-matematica/
README.md  CLAUDE.md  AGENTS.md  .cursor/rules/
```

Cada atividade vive em `atividades/<disciplina>/`. Os PDFs e workbooks de apoio ficam em
`recursos/`. Ao criar uma atividade nova, coloque-a na pasta da disciplina e nomeie como
`atividade-<disciplina>-<ano>ano-a4.html` (ou um nome descritivo em kebab-case).

## Natureza técnica

Cada atividade é **um único arquivo HTML autossuficiente**: todo o CSS fica em um
`<style>` inline e qualquer lógica em `<script>` inline. **Não há** build, gerenciador de
pacotes, framework ou testes. Para trabalhar, abra o `.html` no navegador.

- **Preview/validação:** abra no navegador e **sempre confira no _print preview_** (Ctrl+P →
  "Salvar como PDF"). A quebra de página em A4 é o que importa — algo que parece certo na
  tela pode quebrar feio na folha.
- Arquivos são **independentes**; não há CSS/JS compartilhado. Convenções são copiadas entre
  arquivos, não importadas. Ao criar uma atividade nova, **parta do template**
  `atividades/_template-atividade-a4.html` ou copie um irmão (o modelo canônico é
  `atividades/matematica/atividade-matematica-2ano-a4.html`) em vez de começar do zero.
- `recursos/` (incluindo `kit-super-matematica/`) contém entregáveis estáticos de referência,
  não gerados a partir do código.

## Padrão de atividade (o "como" — derivado do modelo canônico)

Toda atividade nova deve seguir este esqueleto. Detalhes de implementação (nomes de classe,
SVGs de geometria, contas verticais) estão prontos para copiar no modelo canônico.

**Documento base**
- `<html lang="pt-BR">`, `<meta charset="UTF-8">`, viewport, `<title>` descritivo.
- Bloco `@page { size: A4; margin: … }` + `@media print` que: esconde `.no-print`, remove
  toolbar/sombras, e usa `.page-break` (`page-break-before: always`) e `.avoid-break`
  (`break-inside: avoid`) para controlar a paginação. Inclua `print-color-adjust: exact`
  para preservar as cores dos cards na impressão.
- Tema via `:root` (`--ink`, `--paper`, `--accent`, `--blue`, `--green`, `--yellow`…) —
  reestilize por variável, não com cores fixas.
- `.toolbar.no-print` com `<button onclick="window.print()">Imprimir / Salvar em PDF</button>`.
- Conteúdo dentro de `<main class="sheet">`.

**Estrutura pedagógica (na ordem)**
1. **Capa/header:** `<h1>` com nome temático e criativo; `.subtitle` no formato
   `Disciplina — Revisão e aprofundamento | 2º ano do Ensino Fundamental`; `.header-line`
   com inputs Nome/Data/Turma; `.intro-box` "Como usar esta atividade".
2. **Seções `<section>` por tema**, cada uma com:
   - `<h2>Parte N — Tema</h2>`
   - `.concept` — explicação curta do conceito (a parte de **revisão**).
   - `.read-box` ("Leia com atenção") — pequeno texto/contexto lúdico que ancora as questões.
   - Cards `.q` de questão, cada um com `.q-num` + uma tag:
     - `.tag.tag-mc` "Múltipla escolha" → alternativas em `<ul class="mc">` no formato
       `<li>( ) A) …</li>`.
     - `.tag.tag-w` "Resposta escrita" → linhas para responder com `<span class="line">`
       (use `.line.short` ou `style="min-width:…"` conforme o espaço).
   - Separe páginas com `<div class="page-break"></div>` entre seções longas.
3. **Desafio final** — seção que combina vários temas (a parte de **aprofundamento**).
4. **Gabarito** — `<section class="gabarito page-break">` "Gabarito (professor)" com
   `table.data` de respostas e **referências de habilidades BNCC** do 2º ano (ex.: EF02MA01,
   EF02MA05/06, EF02MA14/15 para matemática). Sempre que possível, alinhe as questões a
   habilidades da BNCC e cite os códigos no gabarito.

**Componentes prontos no modelo canônico** (copie quando precisar):
- Contas verticais armadas (`.vm`/`.vm-grid`) com colunas Dez./Un., quadradinhos de "vai 1"
  (`.carry-box`) e linha de resposta — para adição/subtração até 99.
- Figuras geométricas em SVG: planas 2D (`.geo-2d`) e espaciais 3D (`.geo-3d` com gradientes
  e `drop-shadow` para dar profundidade).
- `table.data` para tabelas de preenchimento; `.ordinal-row` para sequências; `.two-col`
  para comparações lado a lado.

## Convenções de conteúdo

- Linguagem **pt-BR**, vocabulário e enunciados adequados a 7–8 anos; frases curtas.
  (Atividades de inglês — `atividades/ingles/` — e histórias bilíngues são bilíngues por
  design.)
- Todo conteúdo matemático e gabarito devem estar **corretos**; confira as contas antes de
  finalizar.
- Exercícios gerados por dados (ex.: `atividades/matematica/atividade-taboada.html`) ficam em arrays/loops dentro
  de `<script>` (ex.: `const p = [[3,4],[5,2], …]` renderizado em `.exercises-grid`). Para
  mudar as questões, edite os arrays — não edite o HTML renderizado à mão.

## Commits

Histórico mistura português e inglês, em geral estilo Conventional Commits (`feat:`,
`Refactor …`). Acompanhe o tom existente. Nomeie arquivos novos no padrão
`atividade-<disciplina>-<ano>ano-a4.html`.
