# -*- coding: utf-8 -*-
import re
path = r"c:\Users\94512868372\Documents\Atividades-Laura\atividade-taboada.html"
with open(path, encoding="utf-8") as f:
    s = f.read()

# Remove spurious "page 9" blocks that appear BEFORE pages 5,6,7,8 (between real pages)
for next_page in (5, 6, 7, 8):
    pat = (
        r"<!-- ══════════ PÁGINA 9 — SOMA VERTICAL 3 DÍGITOS ══════════ -->"
        r".*?"
        r"</div>\s*\n\n<!-- ══════════ PÁGINA " + str(next_page) + r" ══════════ -->"
    )
    s, n = re.subn(
        pat,
        "<!-- ══════════ PÁGINA " + str(next_page) + " ══════════ -->",
        s,
        count=1,
        flags=re.DOTALL,
    )
    print("removed before page", next_page, "count", n)

with open(path, "w", encoding="utf-8") as f:
    f.write(s)
print("done, len", len(s))
