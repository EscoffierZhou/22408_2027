# 第3讲 向量组：配套精选题与课后作业全解

## 习题 3.1：方阵行列式为零与向量组相关性

### 题目
设 $A$ 是 4 阶矩阵，且 $|A| = 0$，则 $A$ 中（ ）。
>[1] (A) 必有一列元素全为 0
>
>[2] (B) 必有两列元素对应成比例
>
>[3] (C) 必有一列向量是其余列向量的线性组合
>
>[4] (D) 任一列向量是其余列向量的线性组合

---

### 主要思路
考查方阵行列式为零与列向量组线性相关性的等价性。$|A| = 0 \iff$ 方阵的列向量组线性相关 $\iff$ 向量组中至少有一列能由其余列向量线性表出。

---

### 详细解答
>[1] **理论判别依据**
>
>> 对于 $n$ 阶方阵 $A$，行列式 $|A| = 0$ 的充要条件是矩阵 $A$ 的列向量组（或行向量组）线性相关。
>
>> 根据线性相关性的判别定理 2：向量组线性相关 $\iff$ 向量组中**至少有一个向量**是其余向量的线性组合。
>
>> 故 $A$ 中必有一列向量是其余列向量的线性组合，选项 (C) 正确。
>
>[2] **反例排除干扰项**
>
>> (1) **排除 (A)、(B)**：取 $A = \begin{bmatrix} 1 & 0 & 1 & 0 \\ \\ 0 & 1 & 1 & 0 \\ \\ 0 & 0 & 0 & 1 \\ \\ 0 & 0 & 0 & 0 \end{bmatrix}$。显然 $|A| = 0$，但没有全为 0 的列，也没有两列对应成比例。故 (A)、(B) 错误。
>
>> (2) **排除 (D)**：在上例中，第 4 列为 $[0, 0, 1, 0]^T$，显然不能由前三列线性表出。定理仅保证“必存在某一列”，并非“任一列”。故 (D) 错误。
>
>[3] **结论**
>
>> 本题正确答案为 <font color=deeppink>(C)</font>。

---

## 习题 3.2：含任意常数向量组的线性相关性判定

### 题目
设 $\alpha_1 = \begin{bmatrix} 0 \\ \\ 0 \\ \\ c_1 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 0 \\ \\ 1 \\ \\ c_2 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 1 \\ \\ -1 \\ \\ c_3 \end{bmatrix}, \alpha_4 = \begin{bmatrix} -1 \\ \\ 1 \\ \\ c_4 \end{bmatrix}$，其中 $c_1, c_2, c_3, c_4$ 为任意常数，则下列向量组线性相关的是（ ）。
>[1] (A) $\alpha_1, \alpha_2, \alpha_3$
>
>[2] (B) $\alpha_1, \alpha_2, \alpha_4$
>
>[3] (C) $\alpha_1, \alpha_3, \alpha_4$
>
>[4] (D) $\alpha_2, \alpha_3, \alpha_4$

---

### 主要思路
考查向量组线性相关性的定义与特值排除法。一方面可以通过赋特值排除使得行列式非零的选项；另一方面可直接观察向量前两个分量的线性关系构造恒等线性组合。

---

### 详细解答
>[1] **特值排除法**
>
>> (1) 令 $c_1 = 1, c_2 = c_3 = c_4 = 0$：
>
>> 构造由 $\alpha_1, \alpha_2, \alpha_3$ 构成的行列式：
>
>> $$
|\alpha_1, \alpha_2, \alpha_3| = \begin{vmatrix} 0 & 0 & 1 \\ \\ 0 & 1 & -1 \\ \\ 1 & 0 & 0 \end{vmatrix} = 1 \cdot (-1) = -1 \ne 0
$$
>
>> 此时 $\alpha_1, \alpha_2, \alpha_3$ 线性无关，排除 (A)。
>
>> 同理，$|\alpha_1, \alpha_2, \alpha_4| = \begin{vmatrix} 0 & 0 & -1 \\ \\ 0 & 1 & 1 \\ \\ 1 & 0 & 0 \end{vmatrix} = 1 \ne 0$，排除 (B)。
>
>> (2) 令 $c_2 = 0, c_3 = c_4 = 1$：
>
>> $$
|\alpha_2, \alpha_3, \alpha_4| = \begin{vmatrix} 0 & 1 & -1 \\ \\ 1 & -1 & 1 \\ \\ 0 & 1 & 1 \end{vmatrix} = -1 \cdot (1 - (-1)) = -2 \ne 0
$$
>
>> 此时 $\alpha_2, \alpha_3, \alpha_4$ 线性无关，排除 (D)。
>
>[2] **理论严谨证明**
>
>> 考察向量组 $\alpha_1, \alpha_3, \alpha_4$：
>
>> 观察 $\alpha_3$ 与 $\alpha_4$ 的前两个分量：
>
>> $$
\alpha_3 + \alpha_4 = \begin{bmatrix} 1 \\ \\ -1 \\ \\ c_3 \end{bmatrix} + \begin{bmatrix} -1 \\ \\ 1 \\ \\ c_4 \end{bmatrix} = \begin{bmatrix} 0 \\ \\ 0 \\ \\ c_3 + c_4 \end{bmatrix}
$$
>
>> (1) 若 $c_1 = 0$，则 $\alpha_1 = \mathbf{0}$，含零向量的向量组必线性相关。
>
>> (2) 若 $c_1 \ne 0$，则：
>
>> $$
\alpha_3 + \alpha_4 = \frac{c_3 + c_4}{c_1}\alpha_1 \implies (c_3 + c_4)\alpha_1 - c_1(\alpha_3 + \alpha_4) = \mathbf{0}
$$
>
>> 由于 $c_1 \ne 0$，这是一组不全为零的组合系数！
>
>> 因此无论常数 $c_1, c_2, c_3, c_4$ 取何值，向量组 $\alpha_1, \alpha_3, \alpha_4$ 恒线性相关。
>
>[3] **结论**
>
>> 本题正确答案为 <font color=deeppink>(C)</font>。

---

## 习题 3.3：向量组线性表出的参数范围判定

### 题目
设 $\alpha_1 = \begin{bmatrix} \lambda \\ \\ 1 \\ \\ 1 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 1 \\ \\ \lambda \\ \\ 1 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 1 \\ \\ 1 \\ \\ \lambda \end{bmatrix}, \alpha_4 = \begin{bmatrix} 1 \\ \\ \lambda \\ \\ \lambda^2 \end{bmatrix}$。若向量组 $\alpha_1, \alpha_2, \alpha_3$ 可由 $\alpha_1, \alpha_2, \alpha_4$ 线性表示，则 $\lambda$ 的取值范围是（ ）。
>[1] (A) $\{1, -1\}$
>
>[2] (B) $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \ne 1\}$
>
>[3] (C) $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \ne -1\}$
>
>[4] (D) $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \ne 1, \lambda \ne -1\}$

---

### 主要思路
$\alpha_1, \alpha_2, \alpha_3$ 可由 $\alpha_1, \alpha_2, \alpha_4$ 线性表出，由于 $\alpha_1, \alpha_2$ 共有，条件等价于向量 $\alpha_3$ 可由 $\alpha_1, \alpha_2, \alpha_4$ 线性表出，即方程组 $[\alpha_1, \alpha_2, \alpha_4]x = \alpha_3$ 有解。计算系数矩阵行列式，对行列式为零的孤立点单独分析增广矩阵的秩。

---

### 详细解答
>[1] **计算系数矩阵行列式**
>
>> 记系数矩阵 $A = [\alpha_1, \alpha_2, \alpha_4] = \begin{bmatrix} \lambda & 1 & 1 \\ \\ 1 & \lambda & \lambda \\ \\ 1 & 1 & \lambda^2 \end{bmatrix}$。
>
>> 计算其行列式：
>
>> $$
|A| = \begin{vmatrix} \lambda & 1 & 1 \\ \\ 1 & \lambda & \lambda \\ \\ 1 & 1 & \lambda^2 \end{vmatrix} \xrightarrow{r_2 - \lambda r_1} \begin{vmatrix} \lambda & 1 & 1 \\ \\ 1 - \lambda^2 & 0 & 0 \\ \\ 1 & 1 & \lambda^2 \end{vmatrix} = -(1 - \lambda^2)\begin{vmatrix} 1 & 1 \\ \\ 1 & \lambda^2 \end{vmatrix} = (\lambda^2 - 1)(\lambda^2 - 1) = (\lambda^2 - 1)^2
$$
>
>> 从而，当 $\lambda \ne 1$ 且 $\lambda \ne -1$ 时，$|A| = (\lambda^2 - 1)^2 \ne 0$。
>
>> 此时矩阵 $A$ 可逆，$r(A) = 3$，非齐次方程组必有唯一解，即 $\alpha_3$ 必可由其线性表出。
>
>[2] **讨论退化特征点 $\lambda = 1$ 与 $\lambda = -1$**
>
>> (1) **当 $\lambda = 1$ 时**：
>
>> 此时 $\alpha_1 = \alpha_2 = \alpha_3 = \alpha_4 = [1, 1, 1]^T$。
>
>> 显然 $\alpha_3 = 1\cdot\alpha_1 + 0\cdot\alpha_2 + 0\cdot\alpha_4$，能够线性表出。
>
>> (2) **当 $\lambda = -1$ 时**：
>
>> 对增广矩阵 $\bar{A} = [A, \alpha_3]$ 作初等行变换：
>
>> $$
\bar{A} = \begin{bmatrix} -1 & 1 & 1 & 1 \\ \\ 1 & -1 & -1 & 1 \\ \\ 1 & 1 & 1 & -1 \end{bmatrix} \xrightarrow{r_2 + r_1, r_3 + r_1} \begin{bmatrix} -1 & 1 & 1 & 1 \\ \\ 0 & 0 & 0 & 2 \\ \\ 0 & 2 & 2 & 0 \end{bmatrix}
$$
>
>> 观察第 2 行可得：$r(A) = 2$，而 $r(\bar{A}) = 3$。
>
>> 此时 $r(A) \ne r(\bar{A})$，方程组无解，即 $\alpha_3$ 不能由 $\alpha_1, \alpha_2, \alpha_4$ 线性表出。
>
>[3] **结论**
>
>> 综上所述，$\lambda$ 的取值范围为 $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \ne -1\}$。
>
>> 本题正确答案为 <font color=deeppink>(C)</font>。

---

## 习题 3.4：组合向量组线性相关性与系数行列式

### 题目
设 $n(n \ge 3)$ 维向量组 $\alpha_1, \alpha_2, \alpha_3$ 线性无关，若向量组 $l\alpha_2 - \alpha_1, m\alpha_3 - 2\alpha_2, \alpha_1 - 3\alpha_3$ 线性相关，则 $m, l$ 应满足的条件是（ ）。
>[1] (A) $lm = 6$
>
>[2] (B) $lm = -6$
>
>[3] (C) $l + m = 6$
>
>[4] (D) $l + m = -6$

---

### 主要思路
利用矩阵分块乘法将新向量组用原无关向量组及系数矩阵 $K$ 表示。利用满秩乘积保秩定理，由于原向量组列满秩，新向量组线性相关等价于转换方阵 $K$ 降秩（$|K| = 0$）。

---

### 详细解答
>[1] **建立矩阵变换方程**
>
>> 将新向量组记作 $\beta_1, \beta_2, \beta_3$：
>
>> $$
[\beta_1, \beta_2, \beta_3] = [l\alpha_2 - \alpha_1, m\alpha_3 - 2\alpha_2, \alpha_1 - 3\alpha_3] = [\alpha_1, \alpha_2, \alpha_3] \begin{bmatrix} -1 & 0 & 1 \\ \\ l & -2 & 0 \\ \\ 0 & m & -3 \end{bmatrix}
$$
>
>> 记转换方阵为 $K = \begin{bmatrix} -1 & 0 & 1 \\ \\ l & -2 & 0 \\ \\ 0 & m & -3 \end{bmatrix}$。
>
>[2] **应用秩与行列式判据**
>
>> 因为 $\alpha_1, \alpha_2, \alpha_3$ 线性无关，所以矩阵 $A = [\alpha_1, \alpha_2, \alpha_3]$ 列满秩，$r(A) = 3$。
>
>> 由列满秩矩阵乘积性质，有 $r(AK) = r(K)$。
>
>> 因此，向量组 $\beta_1, \beta_2, \beta_3$ 线性相关 $\iff r(AK) < 3 \iff r(K) < 3 \iff |K| = 0$。
>
>[3] **计算行列式并解出参数关系**
>
>> 计算 3 阶行列式 $|K|$：
>
>> $$
|K| = \begin{vmatrix} -1 & 0 & 1 \\ \\ l & -2 & 0 \\ \\ 0 & m & -3 \end{vmatrix} = (-1)\begin{vmatrix} -2 & 0 \\ \\ m & -3 \end{vmatrix} + 1\begin{vmatrix} l & -2 \\ \\ 0 & m \end{vmatrix} = (-1)(6 - 0) + (lm - 0) = lm - 6
$$
>
>> 令 $|K| = 0 \implies lm - 6 = 0 \implies lm = 6$。
>
>> 故正确答案为 <font color=deeppink>(A)</font>。

---

## 习题 3.5：并集向量组的秩与线性表出关系

### 题目
设向量组 $(I): \alpha_1, \dots, \alpha_s$ 的秩为 $r_1$，向量组 $(II): \beta_1, \dots, \beta_t$ 的秩为 $r_2$，联合向量组 $(III): \alpha_1, \dots, \alpha_s, \beta_1, \dots, \beta_t$ 的秩为 $r_3$。则下列结论**不正确**的是（ ）。
>[1] (A) 若 $(I)$ 可由 $(II)$ 线性表示，则 $r_2 = r_3$
>
>[2] (B) 若 $(II)$ 可由 $(I)$ 线性表示，则 $r_1 = r_3$
>
>[3] (C) 若 $r_1 = r_3$，则 $r_2 > r_1$
>
>[4] (D) 若 $r_2 = r_3$，则 $r_1 \le r_2$

---

### 主要思路
考查向量组生成空间的包含关系与秩定理。向量组 $(III)$ 是 $(I)$ 与 $(II)$ 的并集。如果一组可由另一组线性表出，则并集的秩等于表出组的秩。反之若 $r_1 = r_3$，说明 $(II)$ 中的所有向量均可由 $(I)$ 表出，从而由定理 7 推论必有 $r_2 \le r_1$。

---

### 详细解答
>[1] **分析选项 (A) 与 (B)**
>
>> (1) 若 $(I)$ 可由 $(II)$ 线性表示，由于 $(II)$ 自身显然可由 $(II)$ 线性表示，因此联合组 $(III)$ 中所有向量均可由 $(II)$ 线性表示。
>
>> 这表明向量组 $(III)$ 与向量组 $(II)$ 等价，因此必有 $r_3 = r_2$。选项 (A) 正确。
>
>> (2) 同理，若 $(II)$ 可由 $(I)$ 线性表示，则 $(III)$ 与 $(I)$ 等价，必有 $r_1 = r_3$。选项 (B) 正确。
>
>[2] **分析选项 (C) 与 (D)**
>
>> (1) 若已知 $r_1 = r_3$：由于 $(I)$ 是 $(III)$ 的部分组，且两者秩相等，说明 $(I)$ 的极大线性无关组也是 $(III)$ 的极大线性无关组。
>
>> 从而 $(III)$ 中的所有向量（包含 $(II)$ 中的全部向量）都可由 $(I)$ 线性表出，即 $(II)$ 可由 $(I)$ 线性表出。
>
>> 由定理 7 推论（表出组的秩不小于被表出组的秩），必有：
>
>> $$
r_2 \le r_1
$$
>
>> 选项 (C) 声称“$r_2 > r_1$”，显然与理论推导绝对矛盾！故选项 (C) 不正确。
>
>> (2) 若已知 $r_2 = r_3$：同理可推得 $(I)$ 可由 $(II)$ 线性表出，必有 $r_1 \le r_2$。选项 (D) 正确。
>
>[3] **结论**
>
>> 本题要求选出不正确的一项，故选 <font color=deeppink>(C)</font>。

---

## 习题 3.6：矩阵等价与向量组等价的核心概念辨析

### 题目
设 $n$ 维向量组 $(I): \alpha_1, \alpha_2, \dots, \alpha_s$，$(II): \beta_1, \beta_2, \dots, \beta_t$。记矩阵 $A = [\alpha_1, \dots, \alpha_s], B = [\beta_1, \dots, \beta_t]$。则下列结论正确的是（ ）。
>[1] (A) 若 $r(I) = r(II)$，则 $A \cong B$
>
>[2] (B) 若 $(I)$ 可由 $(II)$ 线性表示，则 $(I) \cong (II)$
>
>[3] (C) 若 $r(A) = r(B)$，且 $(II)$ 可由 $(I)$ 线性表示，则 $(I) \cong (II)$
>
>[4] (D) 若 $r(A) = r(B)$，则 $(I) \cong (II)$

---

### 主要思路
考查矩阵等价（$A \cong B$ 要求同型且同秩）与向量组等价（$(I) \cong (II)$ 要求相互能线性表出，同秩且同空间）的深刻区别。

---

### 详细解答
>[1] **排除干扰项 (A)、(B)、(D)**
>
>> (1) **排除 (A)**：矩阵等价的前提是两矩阵必须为**同型矩阵**。向量组 $(I)$ 含有 $s$ 个向量，$(II)$ 含有 $t$ 个向量，当 $s \ne t$ 时，矩阵 $A_{n \times s}$ 与 $B_{n \times t}$ 型号不同，根本谈不上矩阵等价。故 (A) 错误。
>
>> (2) **排除 (B)**：单向线性表出不能推得等价。例如取 $(I) = \{\mathbf{0}\}, (II) = \{[1, 0]^T\}$，显然 $(I)$ 可由 $(II)$ 表出，但 $(II)$ 不能由 $(I)$ 表出，两者不等价。故 (B) 错误。
>
>> (3) **排除 (D)**：秩相等只能说明维数相同，不代表在同一个空间中。例如 $A = \begin{bmatrix} 1 & 0 \\ \\ 0 & 1 \\ \\ 0 & 0 \end{bmatrix}, B = \begin{bmatrix} 0 & 0 \\ \\ 1 & 0 \\ \\ 0 & 1 \end{bmatrix}$，有 $r(A) = r(B) = 2$，但两者不能相互表出，向量组不等价。故 (D) 错误。
>
>[2] **选项 (C) 的严格证明**
>
>> 设 $r(A) = r(B) = r$。
>
>> (1) 因为 $(II)$ 可由 $(I)$ 线性表示，所以向量组 $(II)$ 中的每个向量都落在向量组 $(I)$ 的生成空间中：
>
>> $$
\text{span}(II) \subseteq \text{span}(I)
$$
>
>> (2) 又因为两者的维数相等：$\dim(\text{span}(II)) = r(B) = r = r(A) = \dim(\text{span}(I))$。
>
>> 有限维子空间中，维数相等且具有包含关系的两个空间必然完全重合：
>
>> $$
\text{span}(II) = \text{span}(I)
$$
>
>> 这表明向量组 $(I)$ 中的每一个向量亦必然落在 $\text{span}(II)$ 中，即 $(I)$ 亦可由 $(II)$ 线性表示。
>
>> 从而 $(I)$ 与 $(II)$ 能够相互线性表示，即 $(I) \cong (II)$。
>
>[3] **结论**
>
>> 本题正确答案为 <font color=deeppink>(C)</font>。

---

## 习题 3.7：四维向量组线性无关的参数条件确定

### 题目
设向量组 $\alpha_1 = \begin{bmatrix} 1 \\ \\ 0 \\ \\ -1 \\ \\ 2 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 2 \\ \\ -1 \\ \\ -2 \\ \\ 6 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 3 \\ \\ 1 \\ \\ t \\ \\ 4 \end{bmatrix}$ 线性无关，则参数 $t$ 应满足的条件为 ________。

---

### 主要思路
构造以 $\alpha_1, \alpha_2, \alpha_3$ 为列的 $4 \times 3$ 矩阵，初等行变换化为阶梯形矩阵。向量组线性无关的充要条件为矩阵列满秩（秩等于 3）。

---

### 详细解答
>[1] **构造矩阵并初等行变换**
>
>> 构造矩阵 $A = [\alpha_1, \alpha_2, \alpha_3]$：
>
>> $$
A = \begin{bmatrix} 1 & 2 & 3 \\ \\ 0 & -1 & 1 \\ \\ -1 & -2 & t \\ \\ 2 & 6 & 4 \end{bmatrix}
$$
>
>> 执行初等行变换：$r_3 + r_1, r_4 - 2r_1$：
>
>> $$
\to \begin{bmatrix} 1 & 2 & 3 \\ \\ 0 & -1 & 1 \\ \\ 0 & 0 & t+3 \\ \\ 0 & 2 & -2 \end{bmatrix}
$$
>
>> 第 2 行乘以 $-1$：
>
>> $$
\to \begin{bmatrix} 1 & 2 & 3 \\ \\ 0 & 1 & -1 \\ \\ 0 & 0 & t+3 \\ \\ 0 & 2 & -2 \end{bmatrix}
$$
>
>> 执行 $r_4 - 2r_2$：
>
>> $$
\to \begin{bmatrix} 1 & 2 & 3 \\ \\ 0 & 1 & -1 \\ \\ 0 & 0 & t+3 \\ \\ 0 & 0 & 0 \end{bmatrix}
$$

>[2] **列满秩充要条件分析**
>
>> 矩阵 $A$ 含有 3 列。
>
>> 向量组 $\alpha_1, \alpha_2, \alpha_3$ 线性无关 $\iff r(A) = 3$。
>
>> 观察阶梯形矩阵的主元位置，前两列的主元分别为第 1 行的 1 和第 2 行的 1。
>
>> 要使矩阵的秩为 3，第 3 行的主元位置必须非零：
>
>> $$
t + 3 \ne 0 \iff t \ne -3
$$

>[3] **结论**
>
>> 应填：<font color=deeppink>$t \ne -3$</font>。

---

## 习题 3.8：含双参数非齐次向量方程组解的结构与表示

### 题目
已知 $\alpha_1 = \begin{bmatrix} 1 \\ \\ 0 \\ \\ 2 \\ \\ 3 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 1 \\ \\ 1 \\ \\ 3 \\ \\ 5 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 1 \\ \\ -1 \\ \\ a+2 \\ \\ 1 \end{bmatrix}, \alpha_4 = \begin{bmatrix} 1 \\ \\ 2 \\ \\ 4 \\ \\ a+8 \end{bmatrix}$ 及 $\beta = \begin{bmatrix} 1 \\ \\ 1 \\ \\ b+3 \\ \\ 5 \end{bmatrix}$。
>[1] $a, b$ 为何值时，$\beta$ 不能表示成 $\alpha_1, \alpha_2, \alpha_3, \alpha_4$ 的线性组合？
>
>[2] $a, b$ 为何值时，$\beta$ 有 $\alpha_1, \alpha_2, \alpha_3, \alpha_4$ 的唯一线性表示式？并写出该表示式。

---

### 主要思路
列出增广矩阵 $\bar{A} = [A, \beta]$，通过系统的初等行变换将前 4 行化为阶梯形，分析最末两行的含参表达式，讨论无解（不能表出）与唯一解（唯一表出）的参数条件。

---

### 详细解答
>[1] **对增广矩阵实施初等行变换**
>
>> 增广矩阵为：
>
>> $$
\bar{A} = \begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\ \\ 0 & 1 & -1 & 2 & 1 \\ \\ 2 & 3 & a+2 & 4 & b+3 \\ \\ 3 & 5 & 1 & a+8 & 5 \end{bmatrix}
$$
>
>> $r_3 - 2r_1, r_4 - 3r_1$：
>
>> $$
\to \begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\ \\ 0 & 1 & -1 & 2 & 1 \\ \\ 0 & 1 & a & 2 & b+1 \\ \\ 0 & 2 & -2 & a+5 & 2 \end{bmatrix}
$$
>
>> $r_3 - r_2, r_4 - 2r_2$：
>
>> $$
\to \begin{bmatrix} 1 & 1 & 1 & 1 & 1 \\ \\ 0 & 1 & -1 & 2 & 1 \\ \\ 0 & 0 & a+1 & 0 & b \\ \\ 0 & 0 & 0 & a+1 & 0 \end{bmatrix}
$$

>[2] **解答第 (1) 问：不能线性表出的条件**
>
>> 方程组无解 $\iff r(A) < r(\bar{A})$。
>
>> 观察阶梯矩阵后两行：
>
>> 当 $a + 1 = 0$，即 $a = -1$ 时，第 3 行前 4 列全为 0，第 4 行前 4 列全为 0。
>
>> 系数矩阵的秩为 $r(A) = 2$。
>
>> 此时第 3 行最右侧元素为 $b$。若 $b \ne 0$，则增广矩阵在该行产生非零主元，秩为 $r(\bar{A}) = 3 \ne r(A)$。
>
>> 故当 <font color=red>$a = -1$ 且 $b \ne 0$</font> 时，$\beta$ 不能表示成 $\alpha_1, \alpha_2, \alpha_3, \alpha_4$ 的线性组合。
>
>[3] **解答第 (2) 问：唯一线性表出的条件与表示式**
>
>> (1) 唯一线性表示式等价于方程组有唯一解 $\iff r(A) = r(\bar{A}) = 4$。
>
>> 此时主元位置必须均非零，即：
>
>> $$
a + 1 \ne 0 \iff <font color=deeppink>a \ne -1</font> \quad (b \text{ 为任意实数})
$$
>
>> (2) 此时由阶梯矩阵自底向上回代求解：
>
>> 由第 4 行：$(a+1)x_4 = 0 \implies x_4 = 0$。
>
>> 由第 3 行：$(a+1)x_3 = b \implies x_3 = \frac{b}{a+1}$。
>
>> 由第 2 行：$x_2 - x_3 + 2x_4 = 1 \implies x_2 = 1 + \frac{b}{a+1} = \frac{a+b+1}{a+1}$。
>
>> 由第 1 行：$x_1 + x_2 + x_3 + x_4 = 1 \implies x_1 = 1 - \frac{a+b+1}{a+1} - \frac{b}{a+1} = -\frac{2b}{a+1}$。
>
>> 故唯一表示式为：
>
>> $$
\beta = -\frac{2b}{a+1}\alpha_1 + \frac{a+b+1}{a+1}\alpha_2 + \frac{b}{a+1}\alpha_3 + 0\cdot\alpha_4
$$

---

## 习题 3.9：求向量组的秩、极大无关组与线性表出

### 题目
求向量组 $\alpha_1 = \begin{bmatrix} 1 \\ \\ 2 \\ \\ -5 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 2 \\ \\ -1 \\ \\ 2 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 4 \\ \\ 3 \\ \\ -8 \end{bmatrix}, \alpha_4 = \begin{bmatrix} 7 \\ \\ -1 \\ \\ 1 \end{bmatrix}$ 的秩、极大线性无关组，并将其余向量由极大线性无关组线性表示。

---

### 主要思路
将向量组按列拼成矩阵，实施初等行变换化为阶梯形及行最简形矩阵，确定主元列并读取表出系数。

---

### 详细解答
>[1] **构造矩阵并实施初等行变换**
>
>> 构造矩阵 $A = [\alpha_1, \alpha_2, \alpha_3, \alpha_4]$：
>
>> $$
A = \begin{bmatrix} 1 & 2 & 4 & 7 \\ \\ 2 & -1 & 3 & -1 \\ \\ -5 & 2 & -8 & 1 \end{bmatrix}
$$
>
>> $r_2 - 2r_1, r_3 + 5r_1$：
>
>> $$
\to \begin{bmatrix} 1 & 2 & 4 & 7 \\ \\ 0 & -5 & -5 & -15 \\ \\ 0 & 12 & 12 & 36 \end{bmatrix}
$$
>
>> $r_2 \div (-5), r_3 \div 12$：
>
>> $$
\to \begin{bmatrix} 1 & 2 & 4 & 7 \\ \\ 0 & 1 & 1 & 3 \\ \\ 0 & 1 & 1 & 3 \end{bmatrix} \xrightarrow{r_3 - r_2} \begin{bmatrix} 1 & 2 & 4 & 7 \\ \\ 0 & 1 & 1 & 3 \\ \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$
>
>> 继续化为行最简形（$r_1 - 2r_2$）：
>
>> $$
\to \begin{bmatrix} 1 & 0 & 2 & 1 \\ \\ 0 & 1 & 1 & 3 \\ \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

>[2] **确定秩与极大线性无关组**
>
>> 矩阵的非零行数为 2，故向量组的秩为：
>
>> $$
r(\alpha_1, \alpha_2, \alpha_3, \alpha_4) = 2
$$
>
>> 主元位于第 1 列和第 2 列，故一个极大线性无关组为：
>
>> $$
\{\alpha_1, \alpha_2\}
$$

>[3] **线性表出其余向量**
>
>> 由行最简形矩阵后两列的坐标分量：
>
>> 第 3 列对应为：$\alpha_3 = 2\alpha_1 + \alpha_2$。
>
>> 第 4 列对应为：$\alpha_4 = \alpha_1 + 3\alpha_2$。

---

## 习题 3.10：同秩向量组与线性表出参数求解

### 题目
已知向量组 $\beta_1 = \begin{bmatrix} 0 \\ \\ 1 \\ \\ -1 \end{bmatrix}, \beta_2 = \begin{bmatrix} a \\ \\ 2 \\ \\ 1 \end{bmatrix}, \beta_3 = \begin{bmatrix} b \\ \\ 1 \\ \\ 0 \end{bmatrix}$ 与向量组 $\alpha_1 = \begin{bmatrix} 1 \\ \\ 2 \\ \\ -3 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 3 \\ \\ 0 \\ \\ 1 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 9 \\ \\ 6 \\ \\ -7 \end{bmatrix}$ 具有相同的秩，且 $\beta_3$ 可由 $\alpha_1, \alpha_2, \alpha_3$ 线性表示，求 $a, b$ 的值。

---

### 主要思路
先分析 $\alpha$ 向量组的秩：观察发现 $\alpha_3 = 3\alpha_1 + 2\alpha_2$，且 $\alpha_1, \alpha_2$ 线性无关，故秩为 2。
由同秩条件知 $\beta$ 组的秩亦为 2，其行列式必为 0，建立 $a, b$ 的第一个方程。
再由 $\beta_3$ 可由 $\alpha_1, \alpha_2$ 线性表出，知 $\alpha_1, \alpha_2, \beta_3$ 构成的行列式为 0，解出 $b$，进而求得 $a$。

---

### 详细解答
>[1] **计算向量组 $\alpha$ 的秩**
>
>> 考察矩阵 $A = [\alpha_1, \alpha_2, \alpha_3]$：
>
>> 观察知：$3\alpha_1 + 2\alpha_2 = \begin{bmatrix} 3 \\ \\ 6 \\ \\ -9 \end{bmatrix} + \begin{bmatrix} 6 \\ \\ 0 \\ \\ 2 \end{bmatrix} = \begin{bmatrix} 9 \\ \\ 6 \\ \\ -7 \end{bmatrix} = \alpha_3$。
>
>> 且 $\alpha_1, \alpha_2$ 显然线性无关，故向量组 $\alpha_1, \alpha_2, \alpha_3$ 的秩为：
>
>> $$
r(\alpha_1, \alpha_2, \alpha_3) = 2
$$
>
>> 极大线性无关组为 $\{\alpha_1, \alpha_2\}$。
>
>[2] **利用同秩条件建立第 1 个方程**
>
>> 已知向量组 $\beta_1, \beta_2, \beta_3$ 与之具有相同的秩，故 $r(\beta_1, \beta_2, \beta_3) = 2 < 3$。
>
>> 其对应的 3 阶行列式必为 0：
>
>> $$
\begin{vmatrix} 0 & a & b \\ \\ 1 & 2 & 1 \\ \\ -1 & 1 & 0 \end{vmatrix} = 0
$$
>
>> 按第 1 行展开：
>
>> $$
-a\begin{vmatrix} 1 & 1 \\ \\ -1 & 0 \end{vmatrix} + b\begin{vmatrix} 1 & 2 \\ \\ -1 & 1 \end{vmatrix} = -a(1) + b(3) = 3b - a = 0 \implies a = 3b
$$

>[3] **利用线性表出条件求解 $a$ 和 $b$**
>
>> 因为 $\beta_3$ 可由 $\alpha_1, \alpha_2, \alpha_3$ 线性表出，而 $\alpha_1, \alpha_2$ 是其极大无关组，所以 $\beta_3$ 可由 $\alpha_1, \alpha_2$ 线性表出。
>
>> 从而向量组 $\alpha_1, \alpha_2, \beta_3$ 线性相关，其行列式必为 0：
>
>> $$
\begin{vmatrix} 1 & 3 & b \\ \\ 2 & 0 & 1 \\ \\ -3 & 1 & 0 \end{vmatrix} = 0
$$
>
>> 计算该行列式：
>
>> $$
1(0 - 1) - 3(0 - (-3)) + b(2 - 0) = -1 - 9 + 2b = 2b - 10 = 0 \implies b = 5
$$
>
>> 代入 $a = 3b$ 得：
>
>> $$
a = 3 \times 5 = 15
$$
>
>> 故所求参数值为：<font color=deeppink>$a = 15, b = 5$</font>。

---

## 习题 3.11：两两正交非零向量组线性无关性证明

### 题目
设 $\alpha_1, \alpha_2, \alpha_3$ 为两两正交的非零向量。证明：向量组 $\alpha_1, \alpha_2, \alpha_3$ 线性无关。

---

### 主要思路
利用内积定义与正交性质证明。设组合式为零向量，两边分别与 $\alpha_1, \alpha_2, \alpha_3$ 作内积，利用正交条件使得交叉项全部为 0，由非零向量自身内积严格大于 0 导出各个系数必全为零。

---

### 详细解答
>[1] **设定齐次线性组合等式**
>
>> 设有一组实数 $k_1, k_2, k_3$，使得：
>
>> $$
k_1\alpha_1 + k_2\alpha_2 + k_3\alpha_3 = \mathbf{0}
$$

>[2] **两边作内积并利用正交性消元**
>
>> 等式两边同时与向量 $\alpha_1$ 作内积：
>
>> $$
(k_1\alpha_1 + k_2\alpha_2 + k_3\alpha_3, \alpha_1) = (\mathbf{0}, \alpha_1)
$$
>
>> 由内积的线性性质展开得：
>
>> $$
k_1(\alpha_1, \alpha_1) + k_2(\alpha_2, \alpha_1) + k_3(\alpha_3, \alpha_1) = 0
$$
>
>> 因为向量两两正交，故 $(\alpha_2, \alpha_1) = 0, (\alpha_3, \alpha_1) = 0$。上式简化为：
>
>> $$
k_1(\alpha_1, \alpha_1) = 0
$$
>
>> 又因为 $\alpha_1 \ne \mathbf{0}$，由内积的正定性知 $(\alpha_1, \alpha_1) = \|\alpha_1\|^2 > 0$。
>
>> 故必有：$k_1 = 0$。
>
>[3] **同理证明其余系数并得出结论**
>
>> 同理，两边分别与 $\alpha_2$ 和 $\alpha_3$ 作内积，利用 $(\alpha_i, \alpha_j) = 0$ ($i \ne j$) 及 $(\alpha_i, \alpha_i) > 0$，可分别推得：
>
>> $$
k_2 = 0, \quad k_3 = 0
$$
>
>> 从而常数 $k_1 = k_2 = k_3 = 0$ 全为零。
>
>> 故向量组 $\alpha_1, \alpha_2, \alpha_3$ 必线性无关。

---

## 习题 3.12：过渡矩阵、坐标变换与同坐标向量

### 题目
已知 $\mathbb{R}^3$ 的两个基：
$$
\alpha_1 = \begin{bmatrix} 1 \\ \\ 0 \\ \\ -1 \end{bmatrix}, \alpha_2 = \begin{bmatrix} 2 \\ \\ 1 \\ \\ 1 \end{bmatrix}, \alpha_3 = \begin{bmatrix} 1 \\ \\ 1 \\ \\ 1 \end{bmatrix}; \quad \beta_1 = \begin{bmatrix} 0 \\ \\ 1 \\ \\ 1 \end{bmatrix}, \beta_2 = \begin{bmatrix} -1 \\ \\ 1 \\ \\ 0 \end{bmatrix}, \beta_3 = \begin{bmatrix} 1 \\ \\ 2 \\ \\ 1 \end{bmatrix}
$$
>[1] 求由基 $\alpha_1, \alpha_2, \alpha_3$ 到基 $\beta_1, \beta_2, \beta_3$ 的过渡矩阵 $C$；
>
>[2] 求向量 $\gamma = [9, 6, 5]^T$ 在这两个基下的坐标；
>
>[3] 求向量 $\delta$，使它在这两个基下有相同的坐标。

---

### 主要思路
过渡矩阵满足 $[\beta_1, \beta_2, \beta_3] = [\alpha_1, \alpha_2, \alpha_3]C \implies C = A^{-1}B$。
坐标变换公式为 $X = CY$。
两基下坐标相同即满足 $X = CX \implies (C - E)X = \mathbf{0}$。

---

### 详细解答
>[1] **求解过渡矩阵 $C$**
>
>> 记 $A = [\alpha_1, \alpha_2, \alpha_3], B = [\beta_1, \beta_2, \beta_3]$。
>
>> 构造并列增广矩阵 $[A \mid B]$ 进行初等行变换：
>
>> $$
[A \mid B] = \begin{bmatrix} 1 & 2 & 1 & 0 & -1 & 1 \\ \\ 0 & 1 & 1 & 1 & 1 & 2 \\ \\ -1 & 1 & 1 & 1 & 0 & 1 \end{bmatrix} \xrightarrow{r_3 + r_1} \begin{bmatrix} 1 & 2 & 1 & 0 & -1 & 1 \\ \\ 0 & 1 & 1 & 1 & 1 & 2 \\ \\ 0 & 3 & 2 & 1 & -1 & 2 \end{bmatrix}
$$
>
>> 行化简至最简形 $[E \mid C]$：
>
>> $$
\to \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 1 \\ \\ 0 & 1 & 0 & -1 & -3 & -2 \\ \\ 0 & 0 & 1 & 2 & 4 & 4 \end{bmatrix}
$$
>
>> 故过渡矩阵为：
>
>> $$
C = \begin{bmatrix} 0 & 1 & 1 \\ \\ -1 & -3 & -2 \\ \\ 2 & 4 & 4 \end{bmatrix}
$$

>[2] **求解 $\gamma = [9, 6, 5]^T$ 在两基下的坐标**
>
>> (1) 设在基 $\beta$ 下的坐标为 $Y = [y_1, y_2, y_3]^T$：
>
>> $$
BY = \gamma \iff \begin{bmatrix} 0 & -1 & 1 \\ \\ 1 & 1 & 2 \\ \\ 1 & 0 & 1 \end{bmatrix}\begin{bmatrix} y_1 \\ \\ y_2 \\ \\ y_3 \end{bmatrix} = \begin{bmatrix} 9 \\ \\ 6 \\ \\ 5 \end{bmatrix}
$$
>
>> 解此方程组得：$y_1 = 0, y_2 = -4, y_3 = 5$。
>
>> 故在基 $\beta_1, \beta_2, \beta_3$ 下的坐标为 $[0, -4, 5]^T$。
>
>> (2) 由坐标变换公式 $X = CY$，求在基 $\alpha$ 下的坐标 $X = [x_1, x_2, x_3]^T$：
>
>> $$
X = \begin{bmatrix} 0 & 1 & 1 \\ \\ -1 & -3 & -2 \\ \\ 2 & 4 & 4 \end{bmatrix}\begin{bmatrix} 0 \\ \\ -4 \\ \\ 5 \end{bmatrix} = \begin{bmatrix} 1 \\ \\ 2 \\ \\ 4 \end{bmatrix}
$$
>
>> 故在基 $\alpha_1, \alpha_2, \alpha_3$ 下的坐标为 $[1, 2, 4]^T$。
>
>[3] **求解具有相同坐标的向量 $\delta$**
>
>> 设 $\delta = x_1\alpha_1 + x_2\alpha_2 + x_3\alpha_3 = x_1\beta_1 + x_2\beta_2 + x_3\beta_3$。
>
>> 移项整理得：
>
>> $$
x_1(\alpha_1 - \beta_1) + x_2(\alpha_2 - \beta_2) + x_3(\alpha_3 - \beta_3) = \mathbf{0}
$$
>
>> 代入对应向量差：
>
>> $$
\alpha_1 - \beta_1 = \begin{bmatrix} 1 \\ \\ -1 \\ \\ -2 \end{bmatrix}, \quad \alpha_2 - \beta_2 = \begin{bmatrix} 3 \\ \\ 0 \\ \\ 1 \end{bmatrix}, \quad \alpha_3 - \beta_3 = \begin{bmatrix} 0 \\ \\ -1 \\ \\ 0 \end{bmatrix}
$$
>
>> 列出齐次方程组：
>
>> $$
\begin{cases} x_1 + 3x_2 = 0 \\ \\ -x_1 - x_3 = 0 \\ \\ -2x_1 + x_2 = 0 \end{cases}
$$
>
>> 由第 1、3 式立即可得 $x_1 = x_2 = 0$，进而 $x_3 = 0$。
>
>> 故只有零解 $x_1 = x_2 = x_3 = 0$。
>
>> 这说明满足条件的向量**仅有零向量** $\delta = \mathbf{0}$。
