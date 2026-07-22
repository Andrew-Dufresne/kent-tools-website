#!/usr/bin/env python3
"""Extract exact English body-text strings needing translation from EN pages."""
import re, json
from pathlib import Path

SRC = Path(r"C:\Users\AMD\WorkBuddy\Kent Tools")
PAGES = ["index.html", "products.html", "about.html", "contact.html"]

out = []
for page in PAGES:
    html = (SRC/page).read_text(encoding="utf-8")
    # title
    m = re.search(r"<title>(.*?)</title>", html, re.DOTALL)
    if m: out.append((page, "title", m.group(1).strip()))
    # meta description
    m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, re.DOTALL)
    if m: out.append((page, "meta", m.group(1).strip()))
    # block elements (exclude td/th spec cells - keep technical/English)
    for tag in ["h1", "h2", "h3", "h4", "p", "li", "blockquote"]:
        for m in re.finditer(rf"<{tag}\b[^>]*>(.*?)</{tag}>", html, re.DOTALL):
            txt = m.group(1)
            # strip inner tags for a quick content check, but keep RAW for key
            plain = re.sub(r"<[^>]+>", "", txt)
            plain = plain.strip()
            if not plain:
                continue
            # skip pure-number / pure-symbol
            if re.fullmatch(r"[\d\s\W]+", plain):
                continue
            # only consider if it has ascii letters (english-ish) AND at least 2 english words
            if re.search(r"[A-Za-z]{3,}", plain) and len(re.findall(r"[A-Za-z]{2,}", plain)) >= 2:
                out.append((page, tag, txt.strip()))

# dedupe by raw text, keep first page
seen = {}
for page, tag, txt in out:
    if txt not in seen:
        seen[txt] = (page, tag)

with open(SRC/"_extract.txt", "w", encoding="utf-8") as f:
    for i, (txt, (page, tag)) in enumerate(seen.items()):
        f.write(f"### {i:03d} | {page} | <{tag}>\n")
        f.write(txt + "\n\n")

print(f"Extracted {len(seen)} unique body strings -> _extract.txt")
