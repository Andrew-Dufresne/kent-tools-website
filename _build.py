#!/usr/bin/env python3
"""Kent Tools Multilingual Build Script
Generates 8 languages x 4 pages = 32 HTML files.
English is root, other languages in subdirectories (alphabetical: ar, de, es, fr, ja, pt, ru).
"""

import json
import os
import re
from pathlib import Path

SRC = Path(r"C:\Users\AMD\WorkBuddy\Kent Tools")
PAGES = ["index.html", "products.html", "about.html", "contact.html"]
NON_EN = ["ar", "de", "es", "fr", "ja", "pt", "ru"]
ALL_LANGS = ["en"] + NON_EN

LANG_NAMES = {
    "en": "English", "ar": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629",
    "de": "Deutsch", "es": "Espa\u00f1ol", "fr": "Fran\u00e7ais",
    "ja": "\u65e5\u672c\u8a9e", "pt": "Portugu\u00eas", "ru": "\u0420\u0443\u0441\u0441\u043a\u0438\u0439",
}
RTL = {"ar"}

ARIA_LABELS = {
    "en": "Select language",
    "ar": "\u0627\u062e\u062a\u0631 \u0627\u0644\u0644\u063a\u0629",
    "de": "Sprache auswählen",
    "es": "Seleccionar idioma",
    "fr": "Choisir la langue",
    "ja": "\u8a00\u8a9e\u3092\u9078\u629e",
    "pt": "Selecionar idioma",
    "ru": "\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u044f\u0437\u044b\u043a",
}


def strip_gt(html):
    """Remove all Google Translate code from HTML."""
    html = re.sub(
        r'<script[^>]*>\s*function\s+googleTranslateElementInit.*?</script>',
        "", html, flags=re.DOTALL)
    html = re.sub(
        r'<script[^>]*translate\.google\.com[^>]*>\s*</script>',
        "", html)
    html = re.sub(
        r'<div id="google_translate_element"[^>]*></div>',
        "", html)
    return html


def apply_translations(html, lang, T):
    """Replace English text with translated text, longest first."""
    items = sorted(T.items(), key=lambda x: len(x[0]), reverse=True)
    for en, trans in items:
        if lang in trans and trans[lang]:
            html = html.replace(en, trans[lang])
    return html


def adjust_paths(html, lang):
    """Adjust CSS/JS/image paths for subdirectory pages."""
    if lang == "en":
        return html
    html = html.replace('href="css/', 'href="../css/')
    html = html.replace('src="js/', 'src="../js/')
    html = html.replace('src="images/', 'src="../images/')
    return html


def gen_switcher(cur_lang, page):
    """Generate language switcher <select> HTML."""
    opts = []
    for lang in ALL_LANGS:
        if lang == "en":
            url = page if cur_lang == "en" else f"../{page}"
        elif lang == cur_lang:
            url = page
        elif cur_lang == "en":
            url = f"{lang}/{page}"
        else:
            url = f"../{lang}/{page}"
        sel = " selected" if lang == cur_lang else ""
        opts.append(f'  <option value="{url}"{sel}>{LANG_NAMES[lang]}</option>')
    return (
        f'<select class="lang-switcher" onchange="window.location.href=this.value"'
        f' aria-label="{ARIA_LABELS[cur_lang]}">\n' + "\n".join(opts) + "\n</select>"
    )


def set_html_lang(html, lang):
    """Set <html lang="..." [dir="rtl"]>."""
    d = ' dir="rtl"' if lang in RTL else ""
    html = re.sub(r"<html[^>]*>", f'<html lang="{lang}"{d}>', html)
    return html


def replace_switcher(html, lang, page):
    """Replace old language switcher <select> with new one."""
    new = gen_switcher(lang, page)
    html = re.sub(
        r'<select class="lang-switcher"[^>]*>.*?</select>',
        new, html, flags=re.DOTALL)
    return html


def update_css():
    """Update style.css: safely remove any Google Translate remnants, append RTL CSS.
    The GT-comment regex is anchored so it can NEVER span across an unrelated
    /* comment opener (which previously wiped the whole stylesheet)."""
    css_path = SRC / "css" / "style.css"
    original = css_path.read_text(encoding="utf-8")
    css = original
    # Specific GT selectors (bounded, safe):
    css = re.sub(r"body\s*>\s*\.skiptranslate\s*\{[^}]*\}", "", css)
    css = re.sub(r"#google_translate_element\s*\{[^}]*\}", "", css)
    css = re.sub(r"body\s*\{\s*top:\s*0\s*!important;[^}]*\}", "", css)
    # GT comment block: only remove a comment whose OWN /*...*/ contains the marker.
    css = re.sub(r"/\*(?:(?!\*/)(?!\/\*).)*?Google Translate(?:(?!\*/).)*?\*/\s*", "", css, flags=re.DOTALL)
    # Safety guard: never let processing shrink the stylesheet catastrophically.
    if len(css) < 0.5 * len(original):
        print("  WARNING: update_css produced a drastically smaller CSS; keeping original.")
        css = original
    # Add RTL CSS
    rtl_css = """

/* ============================================================
   RTL SUPPORT (Arabic)
   ============================================================ */
[dir="rtl"] { direction: rtl; text-align: right; }
[dir="rtl"] .nav { flex-direction: row-reverse; }
[dir="rtl"] .footer-bottom { flex-direction: row-reverse; }
[dir="rtl"] .floating-contact { right: auto; left: 28px; }
[dir="rtl"] .floating-tooltip { right: auto; left: 68px; transform: translateX(-8px); }
[dir="rtl"] .floating-btn:hover .floating-tooltip { transform: translateX(0); }
[dir="rtl"] .hero-buttons { flex-direction: row-reverse; }
[dir="rtl"] .contact-item { flex-direction: row-reverse; }
[dir="rtl"] .feature-list li { padding-left: 0; padding-right: 22px; }
[dir="rtl"] .feature-list li::before { left: auto; right: 0; }
[dir="rtl"] .spec-table th { text-align: right; }
[dir="rtl"] .product-badge { left: auto; right: 12px; }
[dir="rtl"] .breadcrumb { direction: rtl; }
[dir="rtl"] .lang-switcher { margin-left: 0; margin-right: auto; }
[dir="rtl"] .carousel-prev { left: auto; right: 12px; }
[dir="rtl"] .carousel-next { right: auto; left: 12px; }
[dir="rtl"] .product-detail { direction: rtl; }
[dir="rtl"] .form-row { direction: rtl; }
[dir="rtl"] .stats-bar .container { direction: rtl; }
[dir="rtl"] .categories-grid { direction: rtl; }
[dir="rtl"] .features-grid { direction: rtl; }
[dir="rtl"] .footer-grid { direction: rtl; }
[dir="rtl"] .certs-grid { direction: rtl; }
[dir="rtl"] .products-grid { direction: rtl; }
@media (max-width: 768px) {
  [dir="rtl"] .nav { left: auto; right: 0; }
  [dir="rtl"] .floating-contact { left: 16px; }
  [dir="rtl"] .nav a { text-align: right; }
}
"""
    if "RTL SUPPORT (Arabic)" not in css:
        css = css.rstrip() + rtl_css
    css_path.write_text(css, encoding="utf-8")
    print("  Updated css/style.css (removed GT, added RTL)")


def update_js():
    """Update main.js: remove Google Translate code."""
    js_path = SRC / "js" / "main.js"
    js = js_path.read_text(encoding="utf-8")
    # Remove initTranslate() call
    js = js.replace("  // --- Google Translate: hook custom dropdown to gadget ---\n  initTranslate();\n", "")
    # Remove initTranslate function (comment block + function body up to its top-level closing brace)
    js = re.sub(
        r"/\*.*?Google Translate.*?\*/\s*function initTranslate\(\)\s*\{.*?\n\}",
        "", js, flags=re.DOTALL)
    js_path.write_text(js, encoding="utf-8")
    print("  Updated js/main.js (removed GT code)")


def build():
    # Load translations
    trans_path = SRC / "_translations.json"
    with open(trans_path, "r", encoding="utf-8") as f:
        T = json.load(f)
    print(f"Loaded {len(T)} translation entries")

    # Update shared CSS and JS
    update_css()
    update_js()

    for page in PAGES:
        orig = (SRC / page).read_text(encoding="utf-8")
        cleaned = strip_gt(orig)

        for lang in ALL_LANGS:
            html = cleaned
            if lang != "en":
                html = apply_translations(html, lang, T)
            html = adjust_paths(html, lang)
            html = set_html_lang(html, lang)
            html = replace_switcher(html, lang, page)

            if lang == "en":
                out = SRC / page
            else:
                out_dir = SRC / lang
                out_dir.mkdir(exist_ok=True)
                out = out_dir / page

            out.write_text(html, encoding="utf-8")
            print(f"  {out.relative_to(SRC)}")

    print(f"\nDone! {len(PAGES) * len(ALL_LANGS)} HTML files generated.")


if __name__ == "__main__":
    print("Building Kent Tools multilingual site...")
    build()
