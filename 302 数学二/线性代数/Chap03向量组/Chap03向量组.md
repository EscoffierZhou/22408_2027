# Chap03 向量组

目的[1]:深刻理解n维向量的概念、线性运算公理体系及向量内积、模长、柯西-施瓦茨不等式与夹角的几何代数本质

目的[2]:掌握正交向量组与正交矩阵的充要条件（$Q^TQ=E$、保内积、保长度），熟练运用正交矩阵性质秒杀行列式与逆矩阵

目的[3]:融会贯通向量的线性组合与线性表出概念，掌握向量可由向量组表出的矩阵方程充要判据 $r(A)=r(A, \beta)$ 及向量组等价充要条件 $r(I)=r(II)=r(I, II)$

目的[4]:精通向量组线性相关与线性无关的严格定义，系统掌握七大判别定理（齐次解与秩判据、线性表出判据、部分与整体、高低维延长截短、以少表多必相关等）

目的[5]:系统掌握极大线性无关组与向量组的秩的概念，深刻理解矩阵“行秩=列秩=矩阵秩”的三秩相等定理及初等行变换保列相关性原理

目的[6]:掌握矩阵满秩分解定理及秩的核心不等式链（Sylvester 秩不等式、伴随矩阵秩定理、乘积秩不等式）

目的[7]:掌握向量空间、基、维数与坐标概念，精通基变换过渡矩阵与坐标变换公式（新基=旧基$C$、旧坐标=$C$新坐标），熟练运用施密特正交化算法

## 1.向量的基本概念与内积运算

###### **概念[1]:n维向量与线性运算体系**

[1]基本定义与记号：
>$n$ 个有次序的数 $a_1, a_2, \dots, a_n$ 组成的有序数组称为 **$n$ 维向量**。
>
>向量分为列向量与行向量两种书写形式。考研线性代数中，若无特殊说明，向量默认均为**列向量**：
>
>$$\alpha = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix}, \quad \alpha^T = [a_1, a_2, \dots, a_n]$$
>
>分量全为 0 的向量称为 **零向量**，记作 $0$ 或 $\mathbf{0}$。分量全取相反数的向量称为 $\alpha$ 的 **负向量**，记作 $-\alpha$。

[2]向量的线性运算：
>设 $\alpha = [a_1, a_2, \dots, a_n]^T, \beta = [b_1, b_2, \dots, b_n]^T \in \mathbb{R}^n, k \in \mathbb{R}$：
>
>(1) **向量加法**：$\alpha + \beta = [a_1 + b_1, a_2 + b_2, \dots, a_n + b_n]^T$。
>
>(2) **数乘向量**：$k\alpha = [ka_1, ka_2, \dots, ka_n]^T$。
>
>线性运算满足交换律、结合律、数乘分配律等 8 条经典向量空间代数运算公理。

###### **概念[2]:向量内积、范数与几何性质**

[1]内积定义与代数性质：
>设有两个 $n$ 维列向量 $\alpha = [a_1, a_2, \dots, a_n]^T, \beta = [b_1, b_2, \dots, b_n]^T$：
>
>实数 $(\alpha, \beta) = \alpha^T \beta = a_1 b_1 + a_2 b_2 + \dots + a_n b_n = \sum_{i=1}^n a_i b_i$ 称为向量 $\alpha$ 与 $\beta$ 的 **内积**。
>
>内积具有以下 4 条核心代数性质：
>
>(1) **对称性**：$(\alpha, \beta) = (\beta, \alpha)$。
>
>(2) **线性性**：$(k\alpha, \beta) = k(\alpha, \beta)$，$(\alpha_1 + \alpha_2, \beta) = (\alpha_1, \beta) + (\alpha_2, \beta)$。
>
>(3) **正定性**：$(\alpha, \alpha) \ge 0$，且 $(\alpha, \alpha) = 0 \iff \alpha = \mathbf{0}$。
>
>(4) **矩阵乘积内积恒等式**：$(A\alpha, \beta) = (A\alpha)^T \beta = \alpha^T A^T \beta = (\alpha, A^T \beta)$。

[2]范数、柯西-施瓦茨不等式与夹角：
>(1) **向量长度（欧氏范数）**：
>
>$$\|\alpha\| = \sqrt{(\alpha, \alpha)} = \sqrt{\sum_{i=1}^n a_i^2}$$
>
>当 $\|\alpha\| = 1$ 时称 $\alpha$ 为 **单位向量**。非零向量除以其模长称为 **单位化**：$\alpha^0 = \frac{\alpha}{\|\alpha\|}$。
>
>(2) **柯西-施瓦茨不等式**：
>
>$$|(\alpha, \beta)| \le \|\alpha\| \cdot \|\beta\|$$
>
>等号成立的充要条件是：<font color=deeppink>向量 $\alpha$ 与 $\beta$ 线性相关</font>。
>
>(3) **向量夹角与正交**：
>
>对于任意两个非零向量 $\alpha, \beta$，定义其夹角 $\theta \in [0, \pi]$：
>
>$$\cos\theta = \frac{(\alpha, \beta)}{\|\alpha\| \cdot \|\beta\|}$$
>
>若 $(\alpha, \beta) = 0$，则称向量 $\alpha$ 与 $\beta$ **正交（互相垂直）**，记作 $\alpha \perp \beta$。零向量与任意向量正交。

[3]格拉姆矩阵（Gram 矩阵）：
>设矩阵 $A = [\alpha_1, \alpha_2, \dots, \alpha_m]$，其内积对称阵（Gram 矩阵）为 $G = A^T A$。
>
>矩阵 $A^TA$ 必为实对称半正定矩阵，且有核心秩恒等式：<font color=deeppink>$r(A^TA) = r(A)$</font>。

###### **定理[1]:正交矩阵与正交变换核心性质**

[1]正交矩阵定义与四大充要判定：
>设 $Q$ 为 $n$ 阶实方阵，若满足 $Q^T Q = E$（或 $Q Q^T = E$），则称 $Q$ 为 **正交矩阵**。
>
>以下 4 个命题互为充要条件：
>
>(1) $Q$ 是正交矩阵。
>
>(2) $Q$ 可逆，且其逆矩阵等于转置矩阵：$Q^{-1} = Q^T$。
>
>(3) $Q$ 的列向量组（或行向量组）是 $\mathbb{R}^n$ 中的 **规范正交基**。
>
>(4) 线性变换 $y = Qx$ 保持内积不变，即对任意 $x, y$，恒有 $(Qx, Qy) = (x, y)$。

[2]正交矩阵的核心代数性质：
>(1) **行列式取值**：$|Q|^2 = 1 \implies <font color=red>|Q| = \pm 1</font>$。
>
>(2) **保模长性（等距变换）**：$\|Qx\| = \|x\|$。
>
>(3) **保夹角性**：$\cos\langle Qx, Qy \rangle = \cos\langle x, y \rangle$。
>
>(4) **封闭性**：若 $Q_1, Q_2$ 为同阶正交矩阵，则 $Q_1^{-1} = Q_1^T$ 以及 $Q_1 Q_2$ 亦为正交矩阵。

[3]二维刚体旋转矩阵模型：
>二维平面上逆时针旋转 $\theta$ 角的矩阵 $R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ 为典型正交矩阵，保持长度、面积与夹角完全不变，且 $|R(\theta)| = 1$。

## 2.线性组合与线性表出

###### **概念[1]:线性组合与线性表出的定义**

[1]线性组合：
>设给定向量组 $A: \alpha_1, \alpha_2, \dots, \alpha_s$，对于一组实数 $k_1, k_2, \dots, k_s$：
>
>$$\beta = k_1\alpha_1 + k_2\alpha_2 + \dots + k_s\alpha_s$$
>
>称为向量组 $A$ 的一个 **线性组合**，实数 $k_1, \dots, k_s$ 称为组合系数。

[2]线性表出：
>若存在一组实数 $k_1, \dots, k_s$，使得 $\beta = k_1\alpha_1 + \dots + k_s\alpha_s$ 成立，则称向量 $\beta$ 能由向量组 $A$ **线性表出**。

###### **定理[1]:线性表出的矩阵方程充要判据**

[1]矩阵方程等价转化：
>记矩阵 $A = [\alpha_1, \alpha_2, \dots, \alpha_s]$，系数列向量 $x = [x_1, \dots, x_s]^T$。
>
>则向量方程 $x_1\alpha_1 + \dots + x_s\alpha_s = \beta$ 等价于非齐次线性方程组 $Ax = \beta$，增广矩阵为 $\bar{A} = [A, \beta]$。

[2]线性表出充要条件与唯一性：
>(1) **可线性表出的充要条件**：$Ax = \beta$ 有解 $\iff <font color=deeppink>r(A) = r(A, \beta)</font>$。
>
>(2) **唯一线性表出的充要条件**：$Ax = \beta$ 有唯一解 $\iff <font color=deeppink>r(A) = r(A, \beta) = s</font>$（向量组线性无关）。
>
>(3) **无穷多种线性表出的充要条件**：$Ax = \beta$ 有无穷多解 $\iff <font color=deeppink>r(A) = r(A, \beta) < s</font>$（向量组线性相关）。
>
>(4) **不能线性表出的充要条件**：$Ax = \beta$ 无解 $\iff <font color=red>r(A) < r(A, \beta)</font>$。

###### **定理[2]:向量组之间的线性表出与等价**

[1]向量组间的线性表出：
>设有两个向量组 $(I): \alpha_1, \dots, \alpha_s$ 与 $(II): \beta_1, \dots, \beta_t$。
>
>若 $(II)$ 中每个向量都能由 $(I)$ 线性表出，则称向量组 $(II)$ 可由向量组 $(I)$ 线性表出。
>
>矩阵乘积形式：存在 $s \times t$ 矩阵 $K$，使得 $[\beta_1, \dots, \beta_t] = [\alpha_1, \dots, \alpha_s] K$。
>
>充要判据：<font color=deeppink>$r(\alpha_1, \dots, \alpha_s) = r(\alpha_1, \dots, \alpha_s, \beta_1, \dots, \beta_t)$</font>。

[2]向量组等价的概念与判定：
>若向量组 $(I)$ 与 $(II)$ 能够互相线性表出，则称向量组 $(I)$ 与 $(II)$ **等价**，记作 $(I) \cong (II)$。
>
>向量组等价充要条件：<font color=deeppink>$r(I) = r(II) = r(I, II)$</font>。

## 3.线性相关与线性无关的判定定理体系

###### **概念[1]:线性相关与线性无关的严格定义**

[1]线性相关定义：
>给定向量组 $\alpha_1, \dots, \alpha_s$ ($s \ge 1$)，如果存在 **不全为零** 的常数 $k_1, \dots, k_s$，使得：
>
>$$k_1\alpha_1 + k_2\alpha_2 + \dots + k_s\alpha_s = \mathbf{0}$$
>
>则称向量组 $\alpha_1, \dots, \alpha_s$ **线性相关**。

[2]线性无关定义：
>如果只有当常数 $k_1 = k_2 = \dots = k_s = 0$ 全为零时，等式 $k_1\alpha_1 + \dots + k_s\alpha_s = \mathbf{0}$ 才能成立，则称向量组 $\alpha_1, \dots, \alpha_s$ **线性无关**。

[3]特殊向量组判定：
>(1) 单个向量 $\{\alpha\}$：$\alpha = \mathbf{0} \iff$ 线性相关；$\alpha \ne \mathbf{0} \iff$ 线性无关。
>
>(2) 两个向量 $\{\alpha_1, \alpha_2\}$：线性相关 $\iff$ 对应分量成比例（几何共线）。

###### **定理[1]:线性相关性的七大核心判别定理**

[1]定理 1（齐次方程解判据 / 矩阵秩判据）：
>设 $A = [\alpha_1, \dots, \alpha_s]$：
>
>(1) 向量组线性相关 $\iff Ax = \mathbf{0}$ 有非零解 $\iff <font color=red>r(A) < s</font>$。
>
>(2) 向量组线性无关 $\iff Ax = \mathbf{0}$ 仅有零解 $\iff <font color=deeppink>r(A) = s</font>$。
>
>当 $s = n$ 时，$A$ 为方阵：相关 $\iff |A| = 0$；无关 $\iff |A| \ne 0$。

[2]定理 2（线性表出充要判据）：
>向量组 $\alpha_1, \dots, \alpha_s$ ($s \ge 2$) 线性相关的充要条件是：<font color=deeppink>向量组中至少有一个向量可以由其余 $s-1$ 个向量线性表出</font>。
>
><font color=red>【易错警示】</font> “至少有一个”不能误读为“每一个”。

[3]定理 3（部分与整体判据）：
>(1) **部分相关 $\implies$ 整体相关**（含零向量的向量组必相关）。
>
>(2) **整体无关 $\implies$ 部分无关**。

[4]定理 4（伸长与缩短判据）：
>(1) **低维无关 $\implies$ 延长高维无关**。
>
>(2) **高维相关 $\implies$ 截短低维相关**。

[5]定理 5（增维表出与唯一性判据）：
>设向量组 $\alpha_1, \dots, \alpha_s$ 线性无关，而 $\alpha_1, \dots, \alpha_s, \beta$ 线性相关：
>
>则向量 $\beta$ <font color=deeppink>必可由 $\alpha_1, \dots, \alpha_s$ 线性表出，且表出形式唯一</font>。

[6]定理 6（个数超维必相关判据）：
>在 $n$ 维向量空间 $\mathbb{R}^n$ 中，若向量个数大于维数（$s > n$），则该向量组 <font color=red>必线性相关</font>。

[7]定理 7（表出降维定理 / 考研第一定理）：
>设向量组 $(I): \alpha_1, \dots, \alpha_s$ 可由向量组 $(II): \beta_1, \dots, \beta_t$ 线性表出：
>
>(1) 若 $s > t$（以少表多），则向量组 $(I)$ <font color=red>必线性相关</font>。
>
>(2) 逆否命题：若向量组 $(I)$ 线性无关，则必有 <font color=deeppink>$s \le t$</font>。
>
>(3) 秩的推论：若 $(I)$ 可由 $(II)$ 线性表出，则必有 <font color=deeppink>$r(I) \le r(II)$</font>。

## 4.极大线性无关组与向量组的秩

###### **概念[1]:极大线性无关组与向量组的秩**

[1]极大线性无关组定义：
>设向量组 $T$，若在其部分组中存在 $r$ 个向量 $\alpha_1, \dots, \alpha_r$ 满足：
>
>(1) $\alpha_1, \dots, \alpha_r$ 线性无关；
>
>(2) 从 $T$ 中任取一个向量 $\alpha$，向量组 $\alpha_1, \dots, \alpha_r, \alpha$ 都线性相关；
>
>则称 $\alpha_1, \dots, \alpha_r$ 为向量组 $T$ 的一个 **极大线性无关组**。

[2]核心性质与秩：
>(1) **极大组非唯一，但秩唯一**：极大无关组所含向量个数 $r$ 唯一确定，称为向量组的 **秩**，记作 $r(T)$。
>
>(2) **全能表出与等价**：向量组与其任意一个极大线性无关组等价。

###### **定理[1]:三秩相等定理与行初等变换保列性**

[1]三秩相等定理：
>任意矩阵 $A_{m \times n}$ 的 **行秩**、**列秩** 与 **矩阵的秩** 完全相等：
>
>$$\text{行秩}(A) = \text{列秩}(A) = r(A)$$

[2]初等行变换保列相关性原理：
>矩阵经初等行变换化为阶梯形矩阵时：
>
>(1) 列向量组之间的线性相关性保持不变。
>
>(2) 列向量组之间的线性表出系数完全保持不变。
>
>(3) 阶梯形矩阵中主元所在的列，即对应原矩阵列向量组的一个极大线性无关组。

###### **定理[2]:满秩分解定理与秩的不等式链**

[1]满秩分解定理：
>设矩阵 $A_{m \times n}$ 的秩为 $r > 0$，则必存在列满秩矩阵 $B_{m \times r}$ 与行满秩矩阵 $C_{r \times n}$，使得：
>
>$$A = B C$$

[2]矩阵秩的核心公式与不等式：
>(1) $0 \le r(A_{m \times n}) \le \min(m, n)$。
>
>(2) $r(A) = r(A^T) = r(A^T A) = r(A A^T)$。
>
>(3) $r(A \pm B) \le r(A) + r(B)$。
>
>(4) $\max(r(A), r(B)) \le r([A, B]) \le r(A) + r(B)$。
>
>(5) **乘积秩不等式**：$r(AB) \le \min(r(A), r(B))$。
>
>(6) **Sylvester 秩不等式**：$r(AB) \ge r(A) + r(B) - n$。若 $AB = O$，则 $r(A) + r(B) \le n$。
>
>(7) **伴随矩阵秩定理**：
>
>$$r(A^*) = \begin{cases} n, & r(A) = n \\ 1, & r(A) = n - 1 \\ 0, & r(A) \le n - 2 \end{cases}$$

## 5.向量空间与正交化方法

###### **概念[1]:向量空间、基、维数与坐标**

[1]向量空间与子空间：
>设 $V$ 是 $\mathbb{R}^n$ 的非空子集，若 $V$ 对加法与数乘运算封闭（即对任意 $\alpha, \beta \in V, k \in \mathbb{R}$，恒有 $\alpha + \beta \in V$ 且 $k\alpha \in V$），则称 $V$ 为一个 **向量空间**。
>
>由向量组生成的子空间记作 $\text{span}\{\alpha_1, \dots, \alpha_m\}$。

[2]基、维数与坐标：
>若 $V$ 中存在线性无关向量 $\alpha_1, \dots, \alpha_r$，且 $V$ 中任一向量都可由其线性表出，则称其为 $V$ 的一组 **基**，$r$ 称为 $V$ 的 **维数**（$\dim V = r$）。
>
>若 $\alpha = x_1\alpha_1 + \dots + x_r\alpha_r$，则数组 $[x_1, \dots, x_r]^T$ 称为 $\alpha$ 在该基下的 **坐标**。

###### **公式[1]:基变换过渡矩阵与坐标变换公式**

[1]过渡矩阵定义：
>设基 $(II): [\beta_1, \dots, \beta_n] = [\alpha_1, \dots, \alpha_n] C$。
>
>可逆矩阵 $C$ 称为由基 $(I)$ 到基 $(II)$ 的 **过渡矩阵**：
>
>$$C = [\alpha_1, \dots, \alpha_n]^{-1} [\beta_1, \dots, \beta_n]$$

[2]坐标变换公式：
>设同一向量在基 $(I)$ 与基 $(II)$ 下的坐标分别为 $X$ 与 $Y$，则：
>
>$$<font color=deeppink>X = C Y</font> \quad \iff \quad <font color=deeppink>Y = C^{-1} X</font>$$
>
><font color=red>【记忆口诀】</font> 新基 = 旧基 $\times C$，旧坐标 = $C \times$ 新坐标。

###### **方法[1]:施密特正交化与单位化标准算法**

[1]几何投影原理：
>施密特正交化本质是不断减去当前向量在已有正交基子空间上的正交投影分量。

[2]代数递推三步算法：
>设线性无关向量组 $\alpha_1, \alpha_2, \dots, \alpha_m$：
>
>(1) **第 1 步**：$\beta_1 = \alpha_1$。
>
>(2) **第 2 步**：$\beta_2 = \alpha_2 - \frac{(\alpha_2, \beta_1)}{(\beta_1, \beta_1)}\beta_1$。
>
>(3) **第 3 步**：$\beta_3 = \alpha_3 - \frac{(\alpha_3, \beta_1)}{(\beta_1, \beta_1)}\beta_1 - \frac{(\alpha_3, \beta_2)}{(\beta_2, \beta_2)}\beta_2$。
>
>(4) **通式递推**：$\beta_m = \alpha_m - \sum_{k=1}^{m-1} \frac{(\alpha_m, \beta_k)}{(\beta_k, \beta_k)}\beta_k$。

[3]单位化（规范化）：
>$$\eta_i = \frac{\beta_i}{\|\beta_i\|} \quad (i = 1, 2, \dots, m)$$
>
>所得 $\eta_1, \dots, \eta_m$ 即为与原向量组等价的规范正交向量组。
