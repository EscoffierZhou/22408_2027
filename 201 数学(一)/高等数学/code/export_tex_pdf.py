# -*- coding: utf-8 -*-
"""
export_tex_pdf.py
Publication-Grade LaTeX / XeLaTeX Lecture Note & PDF Generator for 2027 考研数学(二) (UCAS 22408).
Converts structured Markdown notes to native LaTeX documents (.tex) and compiles to publishing-grade PDFs.

Key Design Architecture:
- Real XeLaTeX math typesetting: Crisp black vector formulas with Donald Knuth's exact mathematical typography.
- Native fraction rules in superscripts: Solves KaTeX's thick bar / bold semicolon artifact in exponents (e^{1/x}, x^{2/3}).
- Prestigious Academic Lecture Note Cover (全彩/矢量精装讲义封面): DeepPurple banner, DeepPink & GoldAccent dividing rules, 2027 watermark, UCAS 22408 metadata box.
- Table of Contents (TOC) with purple hyperref links and Roman page numbering.
- Beautiful tcolorbox environments:
  * thmbox (Deep Purple frame & title): Theorems, Formulas, Core Methods, and Concept Analysis
  * solbox (DeepPink frame & title): Solutions, Step-by-Step Derivations, and Worked Examples
  * targetbox (Amethyst Purple): Chapter Learning Objectives
- Two-way workspace synchronization between 22408_2027 and 11408_2027 - 副本.
"""

import os
import re
import sys
import shutil
import subprocess
import argparse

LATEX_PREAMBLE = r'''\documentclass[11pt,a4paper,UTF8]{ctexart}
\usepackage{geometry}
\geometry{left=18mm,right=18mm,top=24mm,bottom=24mm,headheight=22pt,footskip=12mm}
\usepackage{amsmath,amssymb,mathtools,bm,esint,extarrows}
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{hyperref}
\usepackage{tikz}
\usepackage{booktabs}
\usepackage{tabularx}

% --- Color Palette (Purple & DeepPink Academic Theme) ---
\definecolor{DeepPurple}{HTML}{4C1D95}
\definecolor{TitlePurple}{HTML}{581C87}
\definecolor{SubPurple}{HTML}{6B21A8}
\definecolor{DeepPink}{HTML}{FF1493}
\definecolor{LightPinkBg}{HTML}{FFF5F8}
\definecolor{LightPurpleBg}{HTML}{F8F5FF}
\definecolor{GoldAccent}{HTML}{D97706}
\definecolor{DarkText}{HTML}{1F2937}

\hypersetup{
    colorlinks=true,
    linkcolor=TitlePurple,
    citecolor=DeepPink,
    urlcolor=SubPurple,
    pdfborder={0 0 0}
}

% --- Typography & Spacing ---
\linespread{1.3}
\setlength{\parskip}{0.35em plus 0.1em minus 0.1em}
\setlength{\parindent}{0pt}

% --- Section Titles Styling ---
\titleformat{\section}
  {\Large\bfseries\color{TitlePurple}}{\thesection}{1em}{}
  [\vspace{1mm}{\color{TitlePurple!30}\hrule height 1pt}]
\titleformat{\subsection}
  {\large\bfseries\color{SubPurple}}{\thesubsection}{0.8em}{}
\titleformat{\subsubsection}
  {\normalsize\bfseries\color{DeepPurple}}{\thesubsubsection}{0.6em}{}

% --- tcolorbox Environments ---
% 1. Theorem / Formula / Method / Analysis Box (Deep Purple)
\newtcolorbox{thmbox}[1][]{
    enhanced,
    breakable,
    colback=LightPurpleBg,
    colframe=TitlePurple,
    arc=3pt,
    boxrule=0pt,
    leftrule=3.5pt,
    left=10pt,
    right=10pt,
    top=8pt,
    bottom=8pt,
    title=#1,
    coltitle=white,
    colbacktitle=TitlePurple,
    fonttitle=\bfseries\small,
    attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={boxrule=0pt, arc=2pt}
}

% 2. Solution / Formula / Derivation Box (DeepPink)
\newtcolorbox{solbox}[1][]{
    enhanced,
    breakable,
    colback=LightPinkBg,
    colframe=DeepPink,
    arc=3pt,
    boxrule=0pt,
    leftrule=3.5pt,
    left=10pt,
    right=10pt,
    top=8pt,
    bottom=8pt,
    title=#1,
    coltitle=white,
    colbacktitle=DeepPink,
    fonttitle=\bfseries\small,
    attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={boxrule=0pt, arc=2pt}
}

% 3. Learning Goals / Summary Box
\newtcolorbox{targetbox}[1][]{
    enhanced,
    breakable,
    colback=LightPurpleBg,
    colframe=DeepPurple,
    arc=3pt,
    boxrule=1pt,
    left=10pt,
    right=10pt,
    top=8pt,
    bottom=8pt,
    title=#1,
    coltitle=white,
    colbacktitle=DeepPurple,
    fonttitle=\bfseries\small,
    attach boxed title to top left={yshift=-2mm, xshift=4mm},
    boxed title style={boxrule=0pt, arc=2pt}
}
'''

def format_chinese_chap_title(raw):
    """Formats chapter name nicely into Chinese, e.g. chap10一元积分学... -> 第十章 一元积分学..."""
    m = re.match(r'^(?:\[.*?\])?(?:chap|Chap)(\d+)(.*)', raw)
    if m:
        c_num, c_rest = m.group(1), m.group(2)
        chinese_nums = {
            '0': '零', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五',
            '6': '六', '7': '七', '8': '八', '9': '九', '10': '十',
            '11': '十一', '12': '十二', '13': '十三', '14': '十四', '15': '十五',
            '16': '十六', '17': '十七', '18': '十八', '19': '十九', '20': '二十',
            '21': '二十一', '22': '二十二', '23': '二十三', '24': '二十四',
            '25': '二十五', '26': '二十六', '27': '二十七', '28': '二十八',
            '29': '二十九', '30': '三十'
        }
        cn_str = chinese_nums.get(c_num, c_num)
        return f"第{cn_str}章 {c_rest.strip()}"
    return raw

def generate_cover_page(doc_title, sub_title):
    return r'''
% ------------------- 讲义封面 (Cover Page) -------------------
\begin{titlepage}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
    \fill[DeepPurple] (current page.north west) rectangle ([yshift=-7cm]current page.north east);
    \draw[DeepPink, line width=3.5pt] ([yshift=-7cm]current page.north west) -- ([yshift=-7cm]current page.north east);
    \draw[GoldAccent, line width=1pt] ([yshift=-7.12cm]current page.north west) -- ([yshift=-7.12cm]current page.north east);
    
    \node[anchor=north east, opacity=0.12, text=white] at ([xshift=-1.5cm, yshift=-0.5cm]current page.north east) {
        \fontsize{70}{70}\selectfont\bfseries 2027
    };
\end{tikzpicture}

\vspace*{0.8cm}
\begin{center}
    {\color{white}\fontsize{26}{32}\selectfont\bfseries 2027 考研数学(二) 核心讲义}\\[0.6cm]
    {\color{white}\fontsize{13}{18}\selectfont\bfseries 全国硕士研究生招生考试 · 统考数学(二) 核心精讲全书}\\[1.5cm]
\end{center}

\vspace{3.5cm}
\begin{center}
    {\color{GoldAccent}\large\bfseries $\blacktriangleright$ 基础强化 · 核心题解 · 考点深水区 $\blacktriangleleft$}\\[0.8cm]
    {\color{TitlePurple}\fontsize{24}{28}\selectfont\bfseries ''' + doc_title + r'''}\\[0.6cm]
    {\color{DeepPink}\large\bfseries ''' + sub_title + r'''}\\[1.5cm]
\end{center}

\vfill

\begin{center}
\begin{tcolorbox}[
    colback=white,
    colframe=DeepPurple,
    width=0.88\textwidth,
    arc=4pt,
    boxrule=1.2pt,
    halign=center,
    drop shadow=gray!30
]
    \vspace{3mm}
    {\bfseries\large 编著团队：EscoffierZhou}\\[2.5mm]
    {\bfseries\color{TitlePurple} 目标院校：中国科学院大学 (UCAS) 计算机专硕 (22408)}\\[2.5mm]
    {\small\color{gray} 备考铁律：手算真题数字 · 错题白纸重做 · 408 客观题为王}\\[2.5mm]
    {\small 编制版本：2027 届首发版 · \today}
    \vspace{2mm}
\end{tcolorbox}
\end{center}
\vspace{0.8cm}
\end{titlepage}

% ------------------- 目录与页面主体配置 -------------------
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{gray}2027 考研数学(二) · 核心讲义系列}
\fancyhead[R]{\small\color{TitlePurple}\nouppercase{\leftmark}}
\fancyfoot[C]{\small\color{gray}— 第 \thepage\ 页 —}
\fancyfoot[R]{\small\color{gray}UCAS 22408}
\renewcommand{\headrulewidth}{0.5pt}

\pagenumbering{Roman}
\tableofcontents
\newpage
\pagenumbering{arabic}
'''

def escape_text(text):
    """Escapes LaTeX special characters in normal prose while avoiding math."""
    parts = []
    # Match both $...$ and $$...$$
    pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)
    tokens = pattern.split(text)
    
    for token in tokens:
        if token.startswith('$'):
            parts.append(token)
        else:
            t = token
            t = t.replace('&', r'\&')
            t = t.replace('%', r'\%')
            t = t.replace('_', r'\_')
            t = t.replace('#', r'\#')
            # Chinese emphasis
            t = re.sub(r'【(.*?)】', r'\\textbf{【\1】}', t)
            # Markdown bold: **text**
            t = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', t)
            # Markdown italic: *text*
            t = re.sub(r'\*(.*?)\*', r'\\textit{\1}', t)
            # Markdown inline code: `code`
            t = re.sub(r'`(.*?)`', r'\\texttt{\1}', t)
            parts.append(t)
            
    return ''.join(parts)

def convert_display_math(tex_chunk):
    """Converts $$...$$ inside text to native LaTeX equation* or align* environments."""
    def repl(m):
        content = m.group(1).strip()
        if r'\\' in content or '&' in content:
            return f"\n\\begin{{align*}}\n{content}\n\\end{{align*}}\n"
        else:
            return f"\n\\begin{{equation*}}\n{content}\n\\end{{equation*}}\n"
    
    return re.sub(r'\$\$(.*?)\$\$', repl, tex_chunk, flags=re.DOTALL)

def parse_markdown_to_tex(md_content, file_path):
    lines = md_content.splitlines()
    file_basename = os.path.basename(file_path)
    parent_dirname = os.path.basename(os.path.dirname(os.path.abspath(file_path)))
    
    # 1. Determine Title and Subtitle
    raw_title = ""
    for l in lines:
        if l.startswith('# '):
            raw_title = l[2:].strip()
            break
            
    if not raw_title or raw_title.startswith('10.') or raw_title.startswith('11.'):
        raw_title = format_chinese_chap_title(parent_dirname)
    else:
        raw_title = format_chinese_chap_title(raw_title)

    doc_title = raw_title
    sub_title = "—— 核心讲义与满分答题规范 ——"
    if "例题" in file_basename:
        sub_title = "—— 核心精讲大例题与题解三步法 ——"
    elif "homework" in file_basename.lower() or "作业" in file_basename:
        sub_title = "—— 课后精选练习题与全过程推导 ——"
    elif "强化" in file_basename:
        sub_title = "—— 考研高阶冲刺与深水区专攻 ——"
    elif "chap" in file_basename.lower():
        sub_title = "—— 体系化理论精讲与公式全景 ——"

    body_tex = []
    in_block = False
    block_env = ""    # 'solbox' or 'thmbox'
    block_title = ""  # string
    block_lines = []
    
    def flush_block():
        nonlocal in_block, block_env, block_title, block_lines
        if in_block and block_lines:
            content = '\n'.join(block_lines)
            content = convert_display_math(content)
            title_opt = f"[{block_title}]" if block_title else ""
            body_tex.append(f"\\begin{{{block_env}}}{title_opt}\n{content}\n\\end{{{block_env}}}\n")
            in_block = False
            block_env = ""
            block_title = ""
            block_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip title line
        if stripped.startswith('# '):
            i += 1
            continue
            
        # Chapter purpose / goals at beginning
        if re.match(r'^目的\[\d+\]:', stripped):
            flush_block()
            target_items = []
            while i < len(lines) and re.match(r'^目的\[\d+\]:', lines[i].strip()):
                target_items.append(escape_text(lines[i].strip()))
                i += 1
            body_tex.append("\\begin{targetbox}[本章复习目标与核心知识图谱]\n\\begin{itemize}\n")
            for item in target_items:
                body_tex.append(f"  \\item {item}\n")
            body_tex.append("\\end{itemize}\n\\end{targetbox}\n")
            continue

        # Major Headings
        if stripped.startswith('## '):
            flush_block()
            h_text = escape_text(stripped[3:].strip())
            body_tex.append(f"\n\\section{{{h_text}}}\n")
            i += 1
            continue
            
        if stripped.startswith('### '):
            flush_block()
            h_text = escape_text(stripped[4:].strip())
            body_tex.append(f"\n\\subsection{{{h_text}}}\n")
            i += 1
            continue
            
        if stripped.startswith('#### '):
            flush_block()
            h_text = escape_text(stripped[5:].strip())
            body_tex.append(f"\n\\subsubsection{{{h_text}}}\n")
            i += 1
            continue

        # Theorems / Methods / Formulas / Analysis: ###### **...**
        if stripped.startswith('######'):
            flush_block()
            h_clean = re.sub(r'^######\s*', '', stripped)
            h_clean = re.sub(r'^\*\*(.*?)\*\*$', r'\1', h_clean) # strip outer bold
            
            # Check for pattern like 辨析[1]:标题 or 定理[1]:标题
            m_thm = re.match(r'^([^\[\]:：]+)\[(.*?)\][:：](.*)', h_clean)
            if m_thm:
                cat, num, name = m_thm.group(1), m_thm.group(2), m_thm.group(3)
                box_title = f"{cat.strip()}[{num.strip()}]: {name.strip()}"
            else:
                box_title = h_clean
                
            in_block = True
            block_env = "thmbox"
            block_title = escape_text(box_title)
            i += 1
            continue

        # Example titles: **例题[10.1]:...**
        m_eg = re.match(r'^\*\*(例题|习题)\[(.*?)\][:：](.*?)\*\*', stripped)
        if m_eg:
            flush_block()
            cat, num, name = m_eg.group(1), m_eg.group(2), m_eg.group(3)
            title_clean = escape_text(name.strip())
            body_tex.append(f"\n\\subsection{{{cat} {num}: {title_clean}}}\n")
            i += 1
            continue

        # Handle Blockquotes (> and >>)
        if stripped.startswith('>'):
            if not in_block:
                in_block = True
                block_env = "solbox"
                block_title = "分步推导与答题规范"
            
            # Clean leading '>'
            q_line = re.sub(r'^>+\s?', '', line)
            
            # Sub-item tags like [1], [2], (1), (2)
            m_tag = re.match(r'^(\[\d+\]|\(\d+\))(.*)', q_line.strip())
            if m_tag:
                tag, rest = m_tag.group(1), m_tag.group(2)
                q_line = f"\\textbf{{{tag}}} {escape_text(rest)}"
            else:
                q_line = escape_text(q_line)
                
            block_lines.append(q_line)
            i += 1
            continue
        else:
            # Non-blockquote line: if we were in a solbox from blockquotes, flush
            if in_block and block_env == 'solbox':
                flush_block()

        # Regular blank lines
        if stripped == '':
            if in_block:
                block_lines.append("")
            else:
                body_tex.append("\n")
            i += 1
            continue
            
        # Standalone display math outside blockquotes
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            math_content = stripped[2:-2].strip()
            if r'\\' in math_content or '&' in math_content:
                body_tex.append(f"\n\\begin{{align*}}\n{math_content}\n\\end{{align*}}\n")
            else:
                body_tex.append(f"\n\\begin{{equation*}}\n{math_content}\n\\end{{equation*}}\n")
            i += 1
            continue

        # "主要思路:..."
        if stripped.startswith('主要思路:') or stripped.startswith('主要思路：'):
            idea_text = escape_text(stripped[5:].strip())
            body_tex.append(f"\\textbf{{\\color{{DeepPurple}}【思路点拨】}} {idea_text}\n\n")
            i += 1
            continue

        # Numbered items in prose like [1] or (1)
        m_item = re.match(r'^(\[\d+\]|\(\d+\))(.*)', stripped)
        if m_item:
            tag, rest = m_item.group(1), m_item.group(2)
            line_esc = f"\\textbf{{{tag}}} {escape_text(rest)}"
        else:
            line_esc = escape_text(line)

        if in_block:
            block_lines.append(line_esc)
        else:
            body_tex.append(line_esc + "\n")
            
        i += 1

    flush_block()
    
    full_body = "".join(body_tex)
    full_body = convert_display_math(full_body)
    
    cover_tex = generate_cover_page(doc_title, sub_title)
    full_tex = LATEX_PREAMBLE + "\n\\begin{document}\n" + cover_tex + "\n" + full_body + "\n\\end{document}\n"
    return full_tex

def compile_tex_to_pdf(tex_path):
    """Compiles a .tex file using xelatex twice to ensure TOC and references are complete."""
    work_dir = os.path.dirname(tex_path)
    tex_file = os.path.basename(tex_path)
    
    cmd = ['xelatex', '-interaction=nonstopmode', '-halt-on-error', tex_file]
    
    print(f"[*] Compiling XeLaTeX (Pass 1): {tex_file}...")
    res1 = subprocess.run(cmd, cwd=work_dir, capture_output=True)
    if res1.returncode != 0:
        print(f"[!] Compilation Pass 1 failed with code {res1.returncode}")
        log_file = os.path.splitext(tex_path)[0] + '.log'
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8', errors='replace') as lf:
                for line in lf.readlines()[-35:]:
                    print(line, end='')
        return False
        
    print(f"[*] Compiling XeLaTeX (Pass 2 for TOC): {tex_file}...")
    res2 = subprocess.run(cmd, cwd=work_dir, capture_output=True)
    
    # Clean up temporary auxiliary files
    base_no_ext = os.path.splitext(tex_path)[0]
    for ext in ['.aux', '.log', '.out', '.toc']:
        aux = base_no_ext + ext
        if os.path.exists(aux):
            try:
                os.remove(aux)
            except Exception:
                pass
                
    pdf_path = base_no_ext + '.pdf'
    if os.path.exists(pdf_path):
        print(f"[+] Successfully generated publication-grade PDF: {pdf_path}")
        return True
    else:
        print(f"[!] PDF not found: {pdf_path}")
        return False

def sync_to_mirror(file_path):
    """Synchronizes generated files between 22408_2027 and 11408_2027 - 副本."""
    d1 = r'F:\desktop\22408_2027'
    d2 = r'F:\desktop\11408_2027 - 副本'
    
    norm = os.path.abspath(file_path)
    if norm.startswith(d1):
        rel = os.path.relpath(norm, d1)
        target = os.path.join(d2, rel)
    elif norm.startswith(d2):
        rel = os.path.relpath(norm, d2)
        target = os.path.join(d1, rel)
    else:
        return
        
    os.makedirs(os.path.dirname(target), exist_ok=True)
    try:
        shutil.copy2(norm, target)
        print(f"    -> Synced to mirror: {target}")
    except Exception as e:
        print(f"    [!] Mirror sync warning: {e}")

def process_file(md_path):
    print(f"\n=======================================================")
    print(f"Processing Markdown: {md_path}")
    print(f"=======================================================")
    with open(md_path, 'r', encoding='utf-8', errors='replace') as f:
        md_content = f.read()
        
    tex_path = os.path.splitext(md_path)[0] + '.tex'
    
    tex_str = parse_markdown_to_tex(md_content, md_path)
    
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_str)
    print(f"[+] Exported LaTeX source: {tex_path}")
    sync_to_mirror(tex_path)
    
    success = compile_tex_to_pdf(tex_path)
    if success:
        pdf_path = os.path.splitext(md_path)[0] + '.pdf'
        sync_to_mirror(pdf_path)

def process_directory(dir_path):
    for f in os.listdir(dir_path):
        if f.endswith('.md') and not f.lower().startswith('readme') and not f.lower().startswith('skill'):
            md_path = os.path.join(dir_path, f)
            process_file(md_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Export Markdown to Publication-Grade LaTeX PDF")
    parser.add_argument('target', nargs='?', default=None, help="Target markdown file or directory")
    args = parser.parse_args()
    
    if args.target:
        p = os.path.abspath(args.target)
        if os.path.isdir(p):
            process_directory(p)
        elif os.path.isfile(p):
            process_file(p)
    else:
        print("Usage: python export_tex_pdf.py <path-to-markdown-or-folder>")
