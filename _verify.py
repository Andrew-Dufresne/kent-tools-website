#!/usr/bin/env python3
"""Audit Kent Tools multilingual site: GT remnants, RTL, paths, switcher links, translation leaks."""
import os, re, json
from pathlib import Path

SRC = Path(r"C:\Users\AMD\WorkBuddy\Kent Tools")
PAGES = ["index.html", "products.html", "about.html", "contact.html"]
NON_EN = ["ar", "de", "es", "fr", "ja", "pt", "ru"]
ALL = ["en"] + NON_EN
T = json.load(open(SRC / "_translations.json", encoding="utf-8"))

issues = []
info = []

# 1. Google Translate remnants (html + css + js)
for p in list(SRC.rglob("*.html")) + [SRC/"css/style.css", SRC/"js/main.js"]:
    if ".git" in str(p): continue
    if not p.exists(): continue
    txt = p.read_text(encoding="utf-8")
    if re.search(r"google_translate|googleTranslateElementInit|translate\.google\.com", txt, re.I):
        issues.append(f"[GT] remnant in {p.relative_to(SRC)}")

# 2. RTL correctness
for lang in NON_EN:
    for page in PAGES:
        p = SRC/lang/page
        if not p.exists():
            issues.append(f"[MISSING] {lang}/{page}"); continue
        txt = p.read_text(encoding="utf-8")
        has = 'dir="rtl"' in txt
        if lang == "ar" and not has:
            issues.append(f"[RTL] ar missing dir=rtl: {page}")
        if lang != "ar" and has:
            issues.append(f"[RTL] {lang} unexpected dir=rtl: {page}")

# 3. Asset path prefixes
for lang in NON_EN:
    for page in PAGES:
        txt = (SRC/lang/page).read_text(encoding="utf-8")
        for a in ["css/style.css", "js/main.js", "images/"]:
            if a in txt and f"../{a}" not in txt:
                issues.append(f"[PATH] {lang}/{page}: '{a}' not prefixed with ../")
for page in PAGES:
    txt = (SRC/page).read_text(encoding="utf-8")
    if "../css" in txt or "../js" in txt or "../images" in txt:
        issues.append(f"[PATH] en/{page}: unexpected ../ prefix")

# 4. Switcher link integrity + selected correctness
for lang in ALL:
    base = SRC if lang == "en" else SRC/lang
    for page in PAGES:
        p = base/page
        txt = p.read_text(encoding="utf-8")
        m = re.search(r'<select class="lang-switcher"[^>]*>(.*?)</select>', txt, re.DOTALL)
        if not m:
            issues.append(f"[SWITCH] {lang}/{page}: no lang-switcher"); continue
        opts = re.findall(r'<option value="([^"]+)"', m.group(1))
        if len(opts) != 8:
            issues.append(f"[SWITCH] {lang}/{page}: expected 8 options, got {len(opts)}")
        for url in opts:
            target = (base/url).resolve()
            if not (target.exists() and target.is_file()):
                issues.append(f"[SWITCH] {lang}/{page}: broken link -> {url}")
        # selected option should point to current lang's own page
        sel = re.search(r'<option value="([^"]+)" selected>', m.group(1))
        if sel:
            sv = sel.group(1)
            expect = page if lang == "en" else f"../{page}"
            # for non-en pages, the selected url is the page itself (relative)
            if lang == "en" and sv != page:
                issues.append(f"[SWITCH] en/{page}: selected should be '{page}', got '{sv}'")
            if lang != "en" and sv != page:
                issues.append(f"[SWITCH] {lang}/{page}: selected should be '{page}', got '{sv}'")

# 5. Translation leaks: per page, which en keys still appear in non-en pages
# Use word-boundary matching so inflections/cognates (Contacto, Model→Modelo) and
# brand names (WhatsApp) are NOT false-flagged.
product_re = re.compile(r"\b(HZT|HL|RT|HZ|WS|HC|S\d|C\d|F\d|A\d|WSC)\d", re.I)
BRAND_WHITELIST = {"WhatsApp"}
# (lang, key) pairs verified as correct identical words / intentional trade jargon:
ACCEPTED = {
    "de": {"24/7 Support", "Heavy-Duty", "OEM / ODM Service", "FAQ",
           "Motor", "Display", "System", "Material"},
    "es": {"Motor", "Material"},
    "fr": {"Menu", "Contact", "Portable", "Construction", "Applications",
           "Certifications", "Message *", "FAQ"},
    "pt": {"Menu", "Motor", "Display", "Material"},
}
leak_report = {}
for page in PAGES:
    en_txt = (SRC/page).read_text(encoding="utf-8")
    keys_on_page = [k for k in T if k in en_txt and k not in BRAND_WHITELIST]
    for lang in NON_EN:
        ne_txt = (SRC/lang/page).read_text(encoding="utf-8")
        leaked = []
        for k in keys_on_page:
            if k in ACCEPTED.get(lang, set()):
                continue
            # standalone Latin token: not preceded/followed by another Latin letter
            pat = re.compile(r"(?<![A-Za-z])" + re.escape(k) + r"(?![A-Za-z])")
            if pat.search(ne_txt):
                leaked.append(k)
        if leaked:
            ui = [k for k in leaked if not product_re.search(k)]
            prod = [k for k in leaked if product_re.search(k)]
            leak_report.setdefault(lang, {}).setdefault(page, {"ui": ui, "prod": prod})

# ---- Report ----
print("="*60)
print("STRUCTURAL ISSUES (must be 0):", len(issues))
for i in issues: print("  ", i)
print("="*60)
print("TRANSLATION LEAKS (UI = likely untranslated, PROD = product name, usually OK):")
if not leak_report:
    print("  NONE — all UI strings translated in every non-en page.")
else:
    for lang in NON_EN:
        if lang in leak_report:
            for page, d in leak_report[lang].items():
                if d["ui"]:
                    print(f"  [{lang}/{page}] UI leaked: {d['ui']}")
                if d["prod"]:
                    print(f"  [{lang}/{page}] PROD (expected EN): {d['prod']}")
print("="*60)
# Title/meta language check
print("PAGE <title> per language (note: build does not translate titles):")
for lang in ALL:
    base = SRC if lang=="en" else SRC/lang
    t = (base/"index.html").read_text(encoding="utf-8")
    mt = re.search(r"<title>(.*?)</title>", t)
    print(f"  {lang}: {mt.group(1) if mt else 'NONE'}")
