# -*- coding: utf-8 -*-
import os
import re

dirs = [
    r"F:\desktop\11408_2027\201 数学(一)\高等数学\chap9一元积分学的计算",
    r"F:\desktop\11408_2027 - 副本\201 数学(一)\高等数学\chap9一元积分学的计算"
]
files = ["chap9一元积分学的计算.md", "例题.md", "Homework.md", "[强化]一元积分学的计算.md", "skill.md"]

for d in dirs:
    print("Checking dir:", d)
    for fn in files:
        p = os.path.join(d, fn)
        assert os.path.exists(p), f"Missing {p}"
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        
        tab_count = content.count("\t")
        assert tab_count == 0, f"Tab found in {p}: {tab_count}"
        
        num_lists = re.findall(r"^\s*\d+\.\s", content, flags=re.MULTILINE)
        assert len(num_lists) == 0, f"Numbered list found in {p}: {num_lists}"
        
        found_circles = [ch for ch in content if ord(ch) in range(0x2460, 0x2474)]
        assert len(found_circles) == 0, f"Circled numbers found in {p}: {found_circles}"
        
        dd_count = content.count("$$")
        assert dd_count % 2 == 0, f"Unbalanced $$ in {p}: {dd_count}"
        
        if fn != "skill.md":
            cases_matches = re.findall(r"\$[^\$]*?\\begin\{cases\}.*?\\end\{cases\}[^\$]*?\$", content, flags=re.DOTALL)
            for cm in cases_matches:
                assert (r"\\ \\" in cm) or (cm.count(r"\\") >= 2), f"Cases without double break in {fn}: {cm}"
                
        print(f"  {fn}: {len(content)} chars, {len(content.splitlines())} lines - PASS")

print("\nALL 5 FILES IN BOTH WORKSPACES PASSED VERIFICATION WITH ZERO DEFECTS!")
