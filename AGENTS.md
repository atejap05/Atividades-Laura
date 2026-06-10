# AGENTS.md

Guia para agentes de IA que trabalham neste repositório. O guia completo (objetivos,
padrão de atividade, componentes) está em **[CLAUDE.md](./CLAUDE.md)** — leia-o antes de
criar ou editar atividades. Abaixo, o essencial.

## O que é

Repositório pessoal de **atividades escolares impressas (A4)** para uma criança de 8 anos no
**2º ano do Ensino Fundamental**. Cada atividade é **um arquivo HTML autossuficiente** (CSS e
JS inline), organizada em `atividades/<disciplina>/`. **Não há** build, dependências ou
testes — abra o `.html` no navegador.

Estrutura: `atividades/{matematica,portugues,ciencias,ingles,raciocinio,multidisciplinar,producao-textual}/`,
template em `atividades/_template-atividade-a4.html`, material de referência em `recursos/`.

## Regras inegociáveis

1. **Impressão em A4 é a entrega.** Sempre valide no _print preview_ (Ctrl+P). Respeite a
   paginação: `@page { size: A4 }`, `@media print`, `.page-break`, `.avoid-break`,
   `print-color-adjust: exact`.
2. **Conteúdo em pt-BR**, adequado a 7–8 anos, lúdico e criativo. (Inglês/histórias bilíngues
   são exceção por design.)
3. **Mescle revisão + aprofundamento** e **múltipla escolha (`tag-mc`) + discursivas
   (`tag-w`)** em cada atividade.
4. **Parta do template** `atividades/_template-atividade-a4.html` ou copie o modelo canônico
   `atividades/matematica/atividade-matematica-2ano-a4.html` — não há
   código compartilhado entre arquivos; convenções são replicadas, não importadas.
5. **Inclua um gabarito** (`section.gabarito`) com respostas corretas e, quando possível,
   **códigos de habilidade da BNCC** do 2º ano. Confira todas as contas.
6. **Não edite HTML gerado por script à mão** (ex.:
   `atividades/matematica/atividade-taboada.html`) — altere os arrays/loops no `<script>`.

## Referências

- Modelo canônico: `atividades/matematica/atividade-matematica-2ano-a4.html`.
- Template em branco: `atividades/_template-atividade-a4.html`.
- Inspiração de conteúdo/didática: PDFs em `recursos/kit-super-matematica/`.
- Padrão completo de seções e componentes (capa, `.concept`, `.read-box`, `.q`, contas
  verticais `.vm`, geometria SVG, desafio, gabarito): ver **CLAUDE.md**.
