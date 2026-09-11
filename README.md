# EscoffierZhou 22408 in 2027

<p align="center">
  <a href="https://escoffierzhou.github.io/22408_2027/">
    <img src="https://img.shields.io/badge/📖_在线知识库门户-免下载·即点即看-8b5cf6?style=for-the-badge&logo=githubpages&logoColor=white" alt="Online Knowledge Base" />
  </a>
  <a href="https://github.com/EscoffierZhou/22408_2027">
    <img src="https://img.shields.io/badge/Target-2027_UCAS_22408-3b82f6?style=for-the-badge&logo=google-scholar&logoColor=white" alt="Target" />
  </a>
</p>

> 🚀 **全景在线阅读直达：** [https://escoffierzhou.github.io/22408_2027/](https://escoffierzhou.github.io/22408_2027/)  
> **特性：** 手机/iPad/电脑跨端免下载阅读，支持多级折叠侧边栏自由切换章节、全局实时搜索、HTML / PDF / Markdown 格式无缝切换与暗色主题。

> **Target:** 2027 考研 22408 | 中国科学院大学 (UCAS)  
> **科目配置:**  
> - **[101] 思想政治理论**  
> - **[204] 英语(二)** / [201] 英语(一)  
> - **[302] 数学(二)**（注：原数学一专属模块如无穷级数、多元积分学、概率论已加注 `[仅数学一]` 标签归档保留，供拓展查阅）  
> - **[408] 计算机学科专业基础**（数据结构、计算机组成原理、操作系统、计算机网络）

![cover2](./assets/cover2.png)

![cover](./assets/cover.png)

---

### 知识库体系全景速览

```text
22408 考研备考总库
├── 101 思想政治/              # 马原、毛中特、史纲、思修法基、时政热点复习体系
├── 204 英语二/                # 考研英语真题精读、核心高频词汇、语法长难句解析
├── 302 数学二/                # 考研数学二复习体系 (高等数学 Chap01~Chap15 + 线性代数 Chap00~Chap06)
│   ├── 高等数学/              # 高数 15 章标准化笔记、精选题解、课后作业、强化专题
│   ├── 线性代数/              # 行列式、矩阵、向量组、方程组、特征值、二次型深度笔记
│   └── code/                 # 自动化构建与排版自检脚本
├── 408 计算机基础/            # 计算机统考专业课四门核心知识图谱与真题总结
│   ├── 11408数据结构/         # 线性表、树与二叉树、图、查找、排序及算法模板
│   ├── 11408计算机组成及原理/  # 数据表示、运算电路、存储器层次、指令系统、CPU、总线与IO
│   ├── 11408操作系统/         # 进程与线程、内存管理、文件系统、设备IO与死锁
│   └── 11408计算机网络/       # 物理层、数据链路层、网络层、传输层、应用层协议栈
├── Leetcode/                 # 核心高频算法题型手写模板与解题复盘
├── NOTICE.md                 # 备考战略思维修正、时间节点、真实应试铁律与UCAS择校档案
├── README.md                 # 仓库主页与备考指南
├── index.html                # 全库在线阅读门户 (GitHub Pages 部署即用)
├── catalog.js                # 自动提取的全库结构化章节索引数据
└── generate_catalog.py       # 知识库目录一键自动扫描生成脚本
```

---

### 🌐 在线阅读与目录同步指引

1. **直接在线阅读**：
   - 访问 [https://escoffierzhou.github.io/22408_2027/](https://escoffierzhou.github.io/22408_2027/) 即可即点即看，无需下载任何 HTML 或 PDF。
2. **新增笔记后一键更新目录**：
   - 当你在各科目添加了新章节的 Markdown、HTML 或 PDF 后，只需在仓库根目录执行一行命令：
     ```bash
     python generate_catalog.py
     ```
   - 脚本将自动扫描全库并更新 `catalog.js`，推送代码至 GitHub 后网页端秒级生效同步。

