# -*- coding: utf-8 -*-
"""
run_build.py
Generates and synchronizes Chapter 9 files with all refinements:
1. Double line break (\\\\ \\\\) for inline multi-line formulas
2. Replacement of all circled symbols ①-⑬ with (1)-(13)
3. Generation of [强化]一元积分学的计算.md
4. Generation of skill.md and deployment to .agents/skills and global config
"""
import os
import re
import sys

scratch_dir = os.path.dirname(os.path.abspath(__file__))
if scratch_dir not in sys.path:
    sys.path.insert(0, scratch_dir)

import build_notes
import build_examples
import build_homework
import build_reinforcement
import build_skill

TARGET_DIR_1 = r"F:\desktop\11408_2027\201 数学(一)\高等数学\chap9一元积分学的计算"
TARGET_DIR_2 = r"F:\desktop\11408_2027 - 副本\201 数学(一)\高等数学\chap9一元积分学的计算"

SKILL_DEPLOY_PATHS = [
    os.path.join(TARGET_DIR_1, "skill.md"),
    os.path.join(TARGET_DIR_2, "skill.md"),
    r"F:\desktop\11408_2027\.agents\skills\math-notes-creator\SKILL.md",
    r"F:\desktop\11408_2027 - 副本\.agents\skills\math-notes-creator\SKILL.md",
    r"C:\Users\ASUS\.gemini\config\skills\math-notes-creator\SKILL.md",
    r"C:\Users\ASUS\.gemini\antigravity\skills\math-notes-creator\SKILL.md",
]

circle_map = {
    '①': '(1)', '②': '(2)', '③': '(3)', '④': '(4)', '⑤': '(5)',
    '⑥': '(6)', '⑦': '(7)', '⑧': '(8)', '⑨': '(9)', '⑩': '(10)',
    '⑪': '(11)', '⑫': '(12)', '⑬': '(13)',
    '圈一': '(1)', '圈二': '(2)', '圈三': '(3)'
}

def refine_text(text):
    # 1. Replace circles
    for k, v in circle_map.items():
        text = text.replace(k, v)
        
    # 2. Fix inline cases to have double line breaks \\\\ \\\\
    def fix_cases(match):
        s = match.group(0)
        res = re.sub(r'\\\\\s*\\\\', 'TEMP_DOUBLE_BREAK', s)
        res = re.sub(r'\\\\\[[\d\.]+ex\]', 'TEMP_DOUBLE_BREAK', res)
        res = re.sub(r'\\\\', lambda m: r'\\ \\', res)
        res = res.replace('TEMP_DOUBLE_BREAK', r'\\ \\')
        return res
        
    text = re.sub(r'\$[^\$]*?\\begin\{cases\}.*?\\end\{cases\}[^\$]*?\$', fix_cases, text, flags=re.DOTALL)
    
    # 3. Double-check for any tab
    text = text.replace('\t', '    ')
    
    return text

def validate(name, text):
    errors = []
    # 1. No tabs
    if "\t" in text:
        errors.append(f"Contains {text.count(chr(9))} TAB characters!")
    
    # 2. No markdown numbered list
    num_list = re.findall(r"^\s*\d+\.\s.*$", text, flags=re.MULTILINE)
    if num_list:
        errors.append(f"Contains markdown numbered lists:\n" + "\n".join(num_list[:5]))
    
    # 3. No circled numbers
    found_circles = [ch for ch in text if ord(ch) in range(0x2460, 0x2474)]
    if found_circles:
        errors.append(f"Contains circled numbers: {set(found_circles)}")
        
    # 4. LaTeX $$ balance
    cnt_dd = text.count("$$")
    if cnt_dd % 2 != 0:
        errors.append(f"Unbalanced $$: found {cnt_dd} occurrences!")
        
    if errors:
        raise ValueError(f"Validation failed for [{name}]:\n" + "\n".join(errors))
    
    lines = text.splitlines()
    print(f"[SUCCESS] {name} passed validation: {len(text)} chars, {len(lines)} lines.")

def main():
    notes_content = refine_text(build_notes.get_notes_content())
    examples_content = refine_text(build_examples.get_examples_content())
    homework_content = refine_text(build_homework.get_homework_content())
    reinforcement_content = refine_text(build_reinforcement.get_reinforcement_content())
    skill_content = build_skill.get_skill_content()

    files = [
        ("chap9一元积分学的计算.md", notes_content),
        ("例题.md", examples_content),
        ("Homework.md", homework_content),
        ("[强化]一元积分学的计算.md", reinforcement_content),
    ]

    for filename, content in files:
        validate(filename, content)

    # Write chapter files to both repositories
    for target_dir in [TARGET_DIR_1, TARGET_DIR_2]:
        os.makedirs(target_dir, exist_ok=True)
        for filename, content in files:
            path = os.path.join(target_dir, filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Written: {path}")

    # Write skill.md to all deployment paths
    for p in SKILL_DEPLOY_PATHS:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(skill_content)
        print(f"Skill Deployed: {p}")

    print("\nAll refined Chapter 9 files and SKILL.md successfully written and deployed!")

if __name__ == "__main__":
    main()
