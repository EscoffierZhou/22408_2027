# -*- coding: utf-8 -*-
"""
export_pdf.py
Universal Markdown to High-Fidelity PDF converter with KaTeX math rendering and dual-workspace synchronization.
Design Specifications:
- Purple academic headings (h1, h2, h3, h6)
- Crisp black math formulas (.katex, .katex-display: #111827)
- DeepPink formula blocks / solution cards (border-left: 4px solid #ff1493; background-color: #fff1f7)
- Breathable, comfortable typography (13.8px, line-height 1.68, 16mm margins)
- Bulletproof KaTeX loading without defer timing issues
- Headless Edge / Chrome PDF rendering without default headers/footers
"""

import os
import re
import sys
import shutil
import subprocess
import argparse
import markdown

CSS_STYLE = '''
@page {
    size: A4;
    margin: 16mm 15mm 16mm 15mm;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    font-size: 13.8px;
    line-height: 1.68;
    color: #1f2937;
    background-color: #ffffff;
    padding: 0;
    margin: 0;
}

/* Purple Headings */
h1 {
    font-size: 22px;
    border-bottom: 2px solid #9333ea;
    padding-bottom: 6px;
    margin-top: 16px;
    margin-bottom: 12px;
    color: #581c87;
    page-break-after: avoid;
}

h2 {
    font-size: 17px;
    border-bottom: 1px solid #e9d5ff;
    padding-bottom: 4px;
    margin-top: 16px;
    margin-bottom: 10px;
    color: #6b21a8;
    page-break-after: avoid;
}

h3 {
    font-size: 15px;
    margin-top: 14px;
    margin-bottom: 8px;
    color: #7e22ce;
    page-break-after: avoid;
}

h6 {
    font-size: 13.8px;
    font-weight: 700;
    margin-top: 12px;
    margin-bottom: 6px;
    color: #6b21a8;
    page-break-after: avoid;
}

p {
    margin-top: 5px;
    margin-bottom: 5px;
    text-align: justify;
}

/* DeepPink Formula Blocks / Blockquotes */
blockquote {
    margin: 8px 0;
    padding: 6px 14px;
    color: #1f2937;
    background-color: #fff1f7;
    border-left: 4px solid #ff1493;
    border-radius: 0 5px 5px 0;
    page-break-inside: avoid;
}

blockquote blockquote {
    background-color: #fdf2f8;
    border-left-color: #f43f5e;
    margin: 4px 0;
}

blockquote p {
    margin: 4px 0;
}

/* Tables */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 10px 0;
    page-break-inside: avoid;
    font-size: 13px;
}

th, td {
    border: 1px solid #fbcfe8;
    padding: 6px 10px;
    text-align: left;
}

th {
    background-color: #fdf2f8;
    font-weight: 600;
    color: #581c87;
}

tr:nth-child(even) {
    background-color: #fff1f7;
}

/* Code & Pre */
pre {
    background-color: #faf5ff;
    border: 1px solid #e9d5ff;
    border-radius: 4px;
    padding: 8px 10px;
    overflow-x: auto;
    font-size: 12.5px;
    page-break-inside: avoid;
}

code {
    font-family: Consolas, Monaco, "Courier New", monospace;
    font-size: 12.5px;
    background-color: #f3e8ff;
    padding: 1px 4px;
    border-radius: 3px;
    color: #7e22ce;
}

pre code {
    background-color: transparent;
    padding: 0;
    color: inherit;
}

/* Display Math: Formula text is crisp BLACK, formula block is styled */
.katex-display {
    margin: 8px 0 !important;
    overflow-x: visible !important;
    page-break-inside: avoid;
    color: #111827 !important;
}

.katex-display .katex {
    color: #111827 !important;
}

.katex {
    color: #111827 !important;
    font-size: 1.05em;
}

hr {
    border: 0;
    border-top: 1px solid #f3e8ff;
    margin: 14px 0;
}
'''

def get_browser_path():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def convert_md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    math_blocks = []
    def save_display_math(match):
        idx = len(math_blocks)
        math_blocks.append(match.group(0))
        return f'XYZMATHBLOCK{idx}XYZ'

    math_inlines = []
    def save_inline_math(match):
        idx = len(math_inlines)
        math_inlines.append(match.group(0))
        return f'XYZMATHINLINE{idx}XYZ'

    # Protect display math
    s = re.sub(r'\$\$.*?\$\$', save_display_math, content, flags=re.DOTALL)
    # Protect inline math
    s = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', save_inline_math, s, flags=re.DOTALL)

    html_body = markdown.markdown(s, extensions=['tables', 'fenced_code', 'nl2br'])

    # Restore display math
    for i, m in enumerate(math_blocks):
        html_body = html_body.replace(f'XYZMATHBLOCK{i}XYZ', m)
    # Restore inline math
    for i, m in enumerate(math_inlines):
        html_body = html_body.replace(f'XYZMATHINLINE{i}XYZ', m)

    title = os.path.splitext(os.path.basename(md_path))[0]
    full_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
    <style>
    {CSS_STYLE}
    </style>
</head>
<body>
{html_body}
    <script>
    function renderMath() {{
        if (typeof renderMathInElement !== 'undefined') {{
            renderMathInElement(document.body, {{
                delimiters: [
                    {{left: "$$", right: "$$", display: true}},
                    {{left: "$", right: "$", display: false}}
                ],
                throwOnError: false
            }});
        }}
    }}
    if (document.readyState === 'complete') {{
        renderMath();
    }} else {{
        window.addEventListener('load', renderMath);
        document.addEventListener('DOMContentLoaded', renderMath);
    }}
    </script>
</body>
</html>'''

    temp_html = md_path + ".temp.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)

    browser = get_browser_path()
    if not browser:
        print("Error: No Edge or Chrome executable found for PDF generation.")
        return False

    abs_pdf = os.path.abspath(pdf_path)
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=6000",
        f"--print-to-pdf={abs_pdf}",
        os.path.abspath(temp_html)
    ]
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)

    # Sync to copy dir if applicable
    if "11408_2027" in abs_pdf and "11408_2027 - 副本" not in abs_pdf:
        copy_pdf = abs_pdf.replace("11408_2027", "11408_2027 - 副本")
        os.makedirs(os.path.dirname(copy_pdf), exist_ok=True)
        shutil.copy2(abs_pdf, copy_pdf)

    return os.path.exists(abs_pdf)

def process_file(md_path):
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"
    print(f"Exporting: {os.path.basename(md_path)} -> {os.path.basename(pdf_path)}...", end=" ", flush=True)
    ok = convert_md_to_pdf(md_path, pdf_path)
    if ok:
        print(f"[DONE] ({os.path.getsize(pdf_path)} bytes)")
    else:
        print("[FAILED]")

def main():
    parser = argparse.ArgumentParser(description="Export math markdown notes to PDF")
    parser.add_argument("target", nargs="*", default=["."], help="Markdown files or directories to process")
    parser.add_argument("--all", action="store_true", help="Recursively process all markdown notes")
    args = parser.parse_args()

    ignore_files = {"Readme.md", "skill.md", "file_list.txt"}
    targets = args.target if args.target else ["."]

    for tgt in targets:
        if os.path.isfile(tgt):
            process_file(os.path.abspath(tgt))
        else:
            search_dir = os.path.abspath(tgt)
            for root, _, files in os.walk(search_dir):
                for f in files:
                    if f.endswith(".md") and f not in ignore_files:
                        process_file(os.path.join(root, f))

if __name__ == "__main__":
    main()
