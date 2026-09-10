# -*- coding: utf-8 -*-
"""
export_tex_pdf.py
Publication-Grade LaTeX / XeLaTeX Lecture Note & PDF Generator for 2027 考研数学(二) (UCAS 22408).
Converts structured Markdown notes to native LaTeX documents (.tex) and compiles to publishing-grade PDFs.

Key Design Architecture:
- Real XeLaTeX math typesetting: Crisp black vector formulas with Donald Knuth's exact mathematical typography.
- Native fraction rules in superscripts: Solves KaTeX's thick bar / bold semicolon artifact in exponents (e^{1/x}, x^{2/3}).
- Auto-sanitizes inline & display math: Wraps Chinese words in \text{...} and ensures control sequences have trailing spaces.
- Prestigious Academic Lecture Note Cover (全彩/矢量精装讲义封面): DeepPurple banner, DeepPink & GoldAccent dividing rules, 2027 watermark, UCAS 22408 metadata box.
- Table of Contents (TOC) with purple hyperref links and Roman page numbering.
- Beautiful tcolorbox environments:
  * thmbox (Deep Purple frame & title): Theorems, Formulas, Core Methods, and Concept Analysis
  * solbox (DeepPink frame & title): Solutions, Step-by-Step Derivations, and Worked Examples
  * targetbox (Amethyst Purple): Chapter Learning Objectives
- Two-way workspace synchronization between 22408_2027 and 11408_2027 - 副本.
- CLI supports:
  * python export_tex_pdf.py --all
  * python export_tex_pdf.py --chap 1 2 3 4
  * python export_tex_pdf.py <path>
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
\usepackage{amsmath,amssymb,mathtools,bm,esint,extarrows,centernot}
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
    title={#1},
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
    title={#1},
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
        clean_rest = c_rest.strip()
        return f"第{cn_str}章 {clean_rest}"
    return raw

def generate_cover_page(doc_title, sub_title):
    doc_title = doc_title.replace('&', r'\&').replace('_', r'\_').replace('%', r'\%').replace('#', r'\#')
    sub_title = sub_title.replace('&', r'\&').replace('_', r'\_').replace('%', r'\%').replace('#', r'\#')
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

def clean_math(math_content):
    """Sanitizes math strings: ensures spaces after macros, wraps Chinese in \text{...}."""
    # 1. Insert space after control sequence if followed by Chinese
    s = re.sub(r'(\\[a-zA-Z]+)([\u4e00-\u9fa5])', r'\1 \2', math_content)
    
    # 2. Wrap Chinese character sequences that are not already inside \text{...}
    parts = re.split(r'(\\text\{.*?\})', s)
    out = []
    for p in parts:
        if p.startswith(r'\text{'):
            out.append(p)
        else:
            out.append(re.sub(r'[\u4e00-\u9fa5]+', lambda m: f"\\text{{{m.group(0)}}}", p))
    return ''.join(out)

def escape_text(text):
    """Escapes LaTeX special characters in normal prose while sanitizing math."""
    parts = []
    pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)
    tokens = pattern.split(text)
    
    for token in tokens:
        if token.startswith('$$'):
            inner = clean_math(token[2:-2])
            parts.append(f"$${inner}$$")
        elif token.startswith('$'):
            inner = clean_math(token[1:-1])
            parts.append(f"${inner}$")
        else:
            t = token
            t = t.replace(r'\[', '[')
            t = t.replace(r'\]', ']')
            t = t.replace(r'\(', '(')
            t = t.replace(r'\)', ')')
            t = t.replace('&', r'\&')
            t = t.replace('%', r'\%')
            t = t.replace('_', r'\_')
            t = t.replace('#', r'\#')
            t = t.replace('{', r'\{')
            t = t.replace('}', r'\}')
            t = t.replace('^', r'\textasciicircum{}')
            
            # HTML font colors: <font color=red>...</font>
            def font_repl(m):
                c = m.group(1).strip().lower()
                body = m.group(2)
                if c == 'deeppink':
                    c = 'DeepPink'
                elif c == 'purple':
                    c = 'TitlePurple'
                return f"\\textcolor{{{c}}}{{{body}}}"
            t = re.sub(r'<font\s+color=["\']?([a-zA-Z]+)["\']?>(.*?)</font>', font_repl, t, flags=re.DOTALL)
            
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
        content = m.group(1).strip().replace('$', '')
        content = clean_math(content)
        if r'\\' in content or '&' in content:
            return f"\n\\begin{{align*}}\n{content}\n\\end{{align*}}\n"
        else:
            return f"\n\\begin{{equation*}}\n{content}\n\\end{{equation*}}\n"
    
    return re.sub(r'\$\$(.*?)\$\$', repl, tex_chunk, flags=re.DOTALL)

def fix_adjacent_inline_dollars(line):
    res = []
    i = 0
    n = len(line)
    in_inline = False
    
    while i < n:
        if i + 1 < n and line[i] == '$' and line[i+1] == '$':
            if in_inline:
                if i + 2 < n and line[i+2] not in (' ', '\t', '\n', '$'):
                    res.append('$ $')
                    in_inline = True
                    i += 2
                    continue
                else:
                    res.append('$')
                    in_inline = False
                    i += 1
                    continue
            else:
                res.append('$$')
                i += 2
                continue
        elif line[i] == '$':
            res.append('$')
            in_inline = not in_inline
            i += 1
        else:
            res.append(line[i])
            i += 1
            
    return "".join(res)

def is_bare_math_line(line):
    stripped = line.strip()
    if not stripped:
        return False
    prose = re.sub(r'^[>\s]+', '', stripped).strip()
    if not prose:
        return False
    if '$' in prose:
        return False
    if prose.startswith('#') or prose.startswith('![') or prose.startswith('---') or prose.startswith('<'):
        return False
    if re.search(r'[\u4e00-\u9fa5]', prose):
        return False
    if 'msedge.exe' in prose or prose.startswith('msedge') or re.match(r'^\([A-D]\)\s+\d+', prose):
        return False
        
    has_math_macro = bool(re.search(r'\\(Delta|alpha|beta|gamma|lambda|mu|nu|xi|pi|rho|sigma|tau|phi|chi|psi|omega|frac|int|iint|iiint|oint|sum|prod|lim|sqrt|mathrm|mathbf|left|right|begin\{aligned\}|end\{aligned\}|le|ge|leqslant|geqslant|to|times|cdot|approx|equiv|neq|infty|partial|quad|qquad|ln|sin|cos|tan|cot|sec|csc|arcsin|arccos|arctan)\b', prose))
    has_math_eq = bool(re.search(r'^[a-zA-Z0-9\(\)\'\"\_]+(\([a-zA-Z0-9\,\s\+\-\*\/\'\"]+\))?\s*(=|<|>|\\le|\\ge|\\leqslant|\\geqslant)', prose))
    return has_math_macro or has_math_eq

def wrap_bare_math(line):
    if is_bare_math_line(line):
        stripped = line.strip()
        if stripped.startswith('>'):
            m = re.match(r'^(>+\s*)', line)
            if m:
                q_prefix = m.group(1)
                math_part = line[len(q_prefix):].strip()
                return f"{q_prefix}$${math_part}$$"
        return f"$${stripped}$$"
    return line

def parse_markdown_to_tex(md_content, file_path):
    # Strip invisible zero-width unicode characters
    md_content = md_content.replace('\u200b', '').replace('\ufeff', '').replace('\u200e', '').replace('\u200f', '')
    raw_lines = md_content.splitlines()
    lines = [wrap_bare_math(fix_adjacent_inline_dollars(l)) for l in raw_lines]
    file_basename = os.path.basename(file_path)
    parent_dirname = os.path.basename(os.path.dirname(os.path.abspath(file_path)))
    
    # 1. Determine Title and Subtitle
    raw_title = ""
    for l in lines:
        if l.startswith('# '):
            raw_title = l[2:].strip()
            break
            
    if not raw_title or re.match(r'^\d+\.', raw_title):
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
            title_opt = f"[{{{block_title}}}]" if block_title else ""
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
            
        # Handle Fenced Code Blocks (```math or ```)
        if stripped.startswith('```'):
            flush_block()
            lang = stripped[3:].strip().lower()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1  # consume closing ```
                
            if lang in ('math', 'latex'):
                math_content = '\n'.join(code_lines).strip()
                while math_content.startswith('$$') and math_content.endswith('$$') and len(math_content) >= 4:
                    math_content = math_content[2:-2].strip()
                while math_content.startswith('$') and math_content.endswith('$') and len(math_content) >= 2:
                    math_content = math_content[1:-1].strip()
                math_content = clean_math(math_content)
                if r'\\' in math_content or '&' in math_content:
                    body_tex.append(f"\n\\begin{{align*}}\n{math_content}\n\\end{{align*}}\n")
                else:
                    body_tex.append(f"\n\\begin{{equation*}}\n{math_content}\n\\end{{equation*}}\n")
            else:
                box_content = []
                for cl in code_lines:
                    cl_s = cl.strip()
                    if cl_s:
                        cl_esc = escape_text(cl_s)
                        box_content.append(cl_esc + r"\\[1mm]")
                    else:
                        box_content.append(r"\vspace{1mm}")
                body_tex.append("\n\\begin{tcolorbox}[colback=LightPurpleBg,colframe=TitlePurple!60,arc=2pt,boxrule=0.8pt]\n" + "\n".join(box_content) + "\n\\end{tcolorbox}\n")
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
            h_clean = re.sub(r'^\*\*(.*?)\*\*$', r'\1', h_clean)
            
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
            
            q_line = re.sub(r'^>+\s?', '', line)
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
            math_content = stripped[2:-2].strip().replace('$', '')
            math_content = clean_math(math_content)
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
                enc = sys.stdout.encoding or 'utf-8'
                for line in lf.readlines()[-35:]:
                    sys.stdout.buffer.write(line.encode(enc, errors='replace'))
                    sys.stdout.flush()
        return False
        
    print(f"[*] Compiling XeLaTeX (Pass 2 for TOC): {tex_file}...")
    res2 = subprocess.run(cmd, cwd=work_dir, capture_output=True)
    
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

def get_math_base():
    return r'F:\desktop\22408_2027\201 数学(一)\高等数学'

def run_by_chapter_numbers(chap_nums):
    base = get_math_base()
    all_dirs = [d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and d != 'code']
    
    matched_dirs = []
    for num in chap_nums:
        for d in all_dirs:
            if re.match(rf'^(?:\[.*?\])?chap0*{num}(?!\d)', d, re.IGNORECASE):
                if d not in matched_dirs:
                    matched_dirs.append(d)

    print(f"[*] Processing chapters: {matched_dirs}")
    for d in matched_dirs:
        p = os.path.join(base, d)
        process_directory(p)

def run_all():
    base = get_math_base()
    all_dirs = sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and d != 'code'])
    for d in all_dirs:
        p = os.path.join(base, d)
        mds = [f for f in os.listdir(p) if f.endswith('.md') and not f.lower().startswith('readme') and not f.lower().startswith('skill')]
        if mds:
            print(f"\n>>>>>>> Processing Chapter Folder: {d} ({len(mds)} files) <<<<<<<")
            process_directory(p)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Export Markdown to Publication-Grade LaTeX PDF")
    parser.add_argument('target', nargs='?', default=None, help="Target markdown file or directory")
    parser.add_argument('--chap', nargs='+', type=str, help="List of chapter numbers to process (e.g. --chap 1 2 3 4)")
    parser.add_argument('--all', action='store_true', help="Process all chapters that contain markdown notes")
    args = parser.parse_args()
    
    if args.all:
        run_all()
    elif args.chap:
        run_by_chapter_numbers(args.chap)
    elif args.target:
        p = os.path.abspath(args.target)
        if os.path.isdir(p):
            process_directory(p)
        elif os.path.isfile(p):
            process_file(p)
    else:
        print("Usage:")
        print("  python export_tex_pdf.py --all")
        print("  python export_tex_pdf.py --chap 1 2 3 4")
        print("  python export_tex_pdf.py <path-to-markdown-or-folder>")
