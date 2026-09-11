# Chap00 线性代数入门

--------------------------------------------------------------------------------

## 1. 考研线性代数知识体系大观

全国硕士研究生招生考试数学二大纲中，线性代数部分占卷面总分的关键比重。线性代数并非零散孤立的计算技巧堆叠，而是一套高度抽象且逻辑极其严密的现代化代数结构。

从考研宏观架构审视，线性代数全书体系可系统划分为三大核心知识版块：

| 知识版块 | 涵盖章节与核心概念 | 考研定位与逻辑功能 |
| :--- | :--- | :--- |
| **基础版块** | 行列式、矩阵、矩阵运算与初等变换 | **代数运算工具与语言基石**：提供全书的基础运算法则与工具载体 |
| **主题版块** | 向量组、线性相关性、线性方程组的解空间 | **代数结构核心骨架**：研究向量空间的基、维数、线性表出与方程组结构定理 |
| **应用版块** | 特征值与特征向量、相似对角化、二次型 | **几何主轴化与坐标变换**：通过正交变换化二次型为标准形，解决代数与几何极值 |

>线性代数研究的本质：
>
>线性代数是一种以<font color=deeppink>向量空间（Vector Space）</font>为基石的代数结构。
>
>通俗而言，我们在向量空间这一统一舞台中，深入探究<font color=red>向量与向量之间的关系</font>、<font color=deeppink>空间到空间的映射法则</font>，以及<font color=red>方程系统的代数解集结构</font>。

--------------------------------------------------------------------------------

## 2. 对象（元素）：向量 (Vector)

###### **概念[1]:向量的数学定义**

>[1]定义：
>
>拼在一起的一组有序数组称为**向量**。
>
>通常表示为行向量形式 $\alpha = [a_1, a_2, \dots, a_n]$ 或列向量形式 $\beta = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}$。

###### **概念[2]:向量的维数**

>[1]维数定义：
>
>向量中所包含的实数（或复数）的个数，称为向量的**维数**。
>
>例如：$[-1, 1]$ 包含 2 个实数，称为 2 维向量；$[x_1, x_2, \dots, x_n]^\mathrm{T}$ 包含 $n$ 个数，称为 $n$ 维向量。

###### **概念[3]:向量的本质意义——数据与信息的数学载体**

>[1]信息载体功能：
>
>在现代计算机科学与工程技术中，纯粹的一维标量只能描述单一物理量，而向量通过有序组织多个数值分量，能够精准承载多维度的现实系统信息。
>
>[2]现实案例解析：
>
>假设一个人对于“运动”和“音乐”的兴趣程度分别划分为三种状态：
>
>(1) 不喜欢：记为 $-1$；
>
>(2) 无所谓：记为 $0$；
>
>(3) 喜欢：记为 $1$。
>
>此时即可构建表征某人兴趣偏好的 2 维特征向量：
>
>$$[\text{运动兴趣程度}, \text{音乐兴趣程度}]$$
>
>例如：
>
>(1) 向量 $[-1, 1]$ 精准代表：该个体“不喜欢运动，喜欢音乐”；
>
>(2) 向量 $[0, 1]$ 精准代表：该个体“对运动无所谓，喜欢音乐”；
>
>(3) 向量 $[1, -1]$ 精准代表：该个体“喜欢运动，不喜欢音乐”。
>
>由此可见，向量是数学抽象与真实世界信息之间的第一道坚固桥梁。

--------------------------------------------------------------------------------

## 3. 向量的运算体系 (Operations on Vectors)

向量空间中的核心运算由三大层次依次递进：**线性运算**、**点积运算**与**线性变换**。

### 3.1 线性运算 (Linear Operations)

###### **法则[1]:向量加法**

>[1]代数定义：
>
>同维数向量对应分量分别相加。设 $\alpha = [a_1, a_2]^\mathrm{T}$，$\beta = [b_1, b_2]^\mathrm{T}$，则：
>
>$$\alpha + \beta = \begin{bmatrix} a_1 + b_1 \\ a_2 + b_2 \end{bmatrix}$$
>
>[2]几何意义：
>
>在二维与三维欧几里得几何中，向量加法完美服从**平行四边形法则**或**三角形连加法则**。

###### **法则[2]:数乘向量**

>[1]代数定义：
>
>实数 $k$ 与向量 $\alpha$ 的数乘为将实数乘到向量的每一个分量：
>
>$$k\alpha = \begin{bmatrix} ka_1 \\ ka_2 \end{bmatrix}$$
>
>[2]几何意义：
>
>数乘运算在几何上对应于向量沿其所在直线的伸长、缩短以及反向（当 $k < 0$ 时）。

### 3.2 点积运算 (Dot Product / 向量内积)

###### **定义[1]:点积与内积运算**

>[1]内积定义：
>
>$(\alpha, \beta)$ 称为向量 $\alpha$ 与向量 $\beta$ 的点积（内积）运算。
>
>其代数本质是将两个向量的所有对应分量相乘后再求和：
>
>$$(\alpha, \beta) = \alpha^\mathrm{T} \beta = a_1 b_1 + a_2 b_2 + \dots + a_n b_n = \sum_{i=1}^n a_i b_i$$
>
>例如：设 $\alpha = [-1, 1]^\mathrm{T}, \beta = [0, -1]^\mathrm{T}$，则：
>
>$$(\alpha, \beta) = (-1) \times 0 + 1 \times (-1) = -1$$

###### **架构[1]:点积维度的递进结构**

>[1]一行乘一列：
>
>$$[a_1, a_2] \begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = a_1 b_1 + a_2 b_2$$
>
>计算结果为一个纯数（标量）。
>
>[2]一行乘多列：
>
>$$[a_1, a_2] \begin{bmatrix} b_1 & c_1 \\ b_2 & c_2 \end{bmatrix} = [a_1 b_1 + a_2 b_2,\ a_1 c_1 + a_2 c_2]$$
>
>每一项内部为乘积再求和，本质依然是由数乘与加法组合而成的线性运算。计算结果为一个行向量。
>
>[3]多行乘一列：
>
>$$\begin{bmatrix} a_1 & a_2 \\ b_1 & b_2 \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} a_1 c_1 + a_2 c_2 \\ b_1 c_1 + b_2 c_2 \end{bmatrix}$$
>
>左侧矩阵每一行分别与右侧列向量作点积，构成结果列向量的各个分量。这是后续线性方程组左端的核心形式。
>
>[4]多行乘多列（矩阵乘法）：
>
>$$\begin{bmatrix} a_1 & a_2 \\ b_1 & b_2 \end{bmatrix} \begin{bmatrix} c_1 & d_1 \\ c_2 & d_2 \end{bmatrix} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}$$
>
>其中乘积矩阵的第 $i$ 行第 $j$ 列元素满足：
>
>$$a_{ij} = (\text{左矩阵第 } i \text{ 行}) \cdot (\text{右矩阵第 } j \text{ 列})$$
>
>具体分量展开为：
>
>$$a_{11} = a_1 c_1 + a_2 c_2,\quad a_{12} = a_1 d_1 + a_2 d_2$$
>
>$$a_{21} = b_1 c_1 + b_2 c_2,\quad a_{22} = b_1 d_1 + b_2 d_2$$
>
>[5]一列乘一行（外积/秩1矩阵）：
>
>$$\begin{bmatrix} a_1 \\ a_2 \end{bmatrix} [b_1, b_2] = \begin{bmatrix} a_1 b_1 & a_1 b_2 \\ a_2 b_1 & a_2 b_2 \end{bmatrix}$$
>
>两向量的外积产生一个方阵，且该矩阵的每一行（列）均成比例，其秩必然不超过 1。

--------------------------------------------------------------------------------

## 4. 矩阵的初识与线性变换映射观

### 4.1 矩阵的本质：系统信息的组织载体

矩阵不仅仅是一张用中括号括起来的二维数表，它具有严格的行列语义与空间位置锁定特性：

>[1]矩阵表达系统信息：
>
>考查矩阵 $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$：
>
>(1) 角度一（个体喜好信息系统）：若横向解读，$[1, 0]$ 代表个体喜欢运动、对音乐无所谓；$[0, -1]$ 代表个体对运动无所谓、且不喜欢音乐。
>
>(2) 角度二（投篮结果状态系统）：假设一个人投篮两次，投中记为 1，未投中记为 0，卡在篮筐上记为 $-1$。则 $[1, 0]$ 代表第一次投中、第二次未投中；$[0, -1]$ 代表第一次未投中、第二次卡在篮筐上。
>
>[2]矩阵中位置不可随意改动的铁律：
>
>若矩阵 $\begin{bmatrix} 40 & 15 \\ 12 & 8 \end{bmatrix}$ 的第一行表示商品价格（40与15），第二行表示卡路里含量（12与8）；
>
>一旦随意将数字调换为 $\begin{bmatrix} 40 & 12 \\ 15 & 8 \end{bmatrix}$，则语义彻底变为商品价格为 40 与 12，卡路里为 15 与 8。
>
><font color=red>结论：矩阵中元素的位置是语义的绝对约束，不可任意调换。</font>

### 4.2 线性变换映射观 (Linear Transformation)

在高等数学与微积分中，核心研究工具是单变量或多变量函数映射：

$$y = f(x)$$

其中 $x$ 是自变量（纯数），$f$ 是对应法则，$y$ 是输出结果。

而在高等代数与线性代数中，核心工具全面升级为矩阵与向量的线性作用：

$$A\alpha = \beta$$

>[1]高数与线代的映射对齐结构：
>
>$$\begin{aligned} \text{高等数学} &\quad\longleftrightarrow\quad \text{线性代数} \\ x \text{ (标量自变量)} &\quad\longleftrightarrow\quad \alpha \text{ (输入向量)} \\ f \text{ (函数映射法则)} &\quad\longleftrightarrow\quad A \text{ (变换矩阵算子)} \\ y \text{ (标量因变量)} &\quad\longleftrightarrow\quad \beta \text{ (输出向量)} \end{aligned}$$
>
>[2]映射的几何直观：
>
>矩阵 $A$ 作用在输入空间中的向量 $\alpha$ 上，通过矩阵乘法法则输出目标空间中的新向量 $\beta$。

### 4.3 二维平面五大基础几何变换全景

为了透彻建立线性变换的直观图像，考查二维平面上由原点出发的单位正方形（四个顶点坐标为 $(0,0), (1,0), (1,1), (0,1)$，写为顶点坐标矩阵 $\begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$ 或笑脸图形）在左乘各类特殊矩阵后的几何流变：

###### **模型[1]:对称变换 (Reflection)**

>[1]关于 $x$ 轴对称矩阵：
>
>$$A_1 = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 1 & 0 \\ -1 & -1 & 0 & 0 \end{bmatrix}$$
>
>几何效果：图形沿 $x$ 轴发生翻转对称，落在第四象限。
>
>[2]关于 $y$ 轴对称矩阵：
>
>$$A_2 = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -1 & -1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$$
>
>几何效果：图形沿 $y$ 轴发生翻转对称，落在第二象限。
>
>[3]关于坐标原点中心对称矩阵：
>
>$$A_3 = \begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -1 & -1 & 0 \\ -1 & -1 & 0 & 0 \end{bmatrix}$$
>
>几何效果：图形沿原点作中心对称，落在第三象限。
>
>[4]关于直线 $y = x$ 对称矩阵：
>
>$$A_4 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \end{bmatrix}$$
>
>几何效果：$x$ 与 $y$ 坐标互换，图形关于主对角线 $y=x$ 翻转。
>
>[5]关于直线 $y = -x$ 对称矩阵：
>
>$$A_5 = \begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} -1 & -1 & 0 & 0 \\ 0 & -1 & -1 & 0 \end{bmatrix}$$
>
>几何效果：图形关于副对角线 $y = -x$ 发生翻转。

###### **模型[2]:伸缩与压缩变换 (Scaling)**

>[1]横向伸长与压缩矩阵：
>
>$$S_x(k_x) = \begin{bmatrix} k_x & 0 \\ 0 & 1 \end{bmatrix}$$
>
>(1) 当 $k_x = 2$ 时，图形沿 $x$ 轴拉伸为原宽度的 2 倍：
>
>$$\begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 2 & 2 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$$
>
>(2) 当 $k_x = \frac{1}{2}$ 时，图形沿 $x$ 轴压缩为原宽度的 $\frac{1}{2}$：
>
>$$\begin{bmatrix} \frac{1}{2} & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$$
>
>[2]纵向伸长与压缩矩阵：
>
>$$S_y(k_y) = \begin{bmatrix} 1 & 0 \\ 0 & k_y \end{bmatrix}$$
>
>(1) 当 $k_y = 2$ 时，纵坐标翻倍，纵向拉伸；
>
>(2) 当 $k_y = \frac{1}{2}$ 时，纵坐标减半，纵向压缩。

###### **模型[3]:剪切变换 (Shear Transformation)**

>[1]水平剪切矩阵：
>
>$$K_x = \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$$
>
>几何效果：图形顶端保持在 $y=1$，底端保持在 $y=0$，但各点沿横向发生偏移，使正方形变形为水平倾斜的平行四边形。
>
>[2]垂直剪切矩阵：
>
>$$K_y = \begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}$$
>
>作用验证：
>
>$$\begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & -1 & 0 \end{bmatrix}$$
>
>几何效果：图形沿竖直方向产生倾斜滑移。

###### **模型[4]:旋转变换 (Rotation Transformation)**

>[1]二维平面标准旋转矩阵：
>
>平面内绕原点逆时针旋转 $\theta$ 角的标准变换矩阵为：
>
>$$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
>
>[2]旋转 $\theta = \frac{\pi}{4}\ (45^\circ)$ 实例验证：
>
>$$R\left(\frac{\pi}{4}\right) = \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix}$$
>
>作用于顶点坐标矩阵：
>
>$$\begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} -\frac{\sqrt{2}}{2} & 0 & \frac{\sqrt{2}}{2} & 0 \\ \frac{\sqrt{2}}{2} & \sqrt{2} & \frac{\sqrt{2}}{2} & 0 \end{bmatrix}$$
>
>几何效果：整个图形以原点为轴心，严格逆时针旋转 $45^\circ$，图形的面积与各边长度完美保持不变（正交刚体旋转）。

--------------------------------------------------------------------------------

## 5. 线性方程组求解：从消元法走向逆矩阵

### 5.1 线性方程组的矩阵表达

考查一般的二元非齐次线性方程组：

$$\begin{cases} x_1 + 2x_2 = 3 \\ 4x_1 + 7x_2 = 10 \end{cases}$$

利用向量的点积形式，该系统可等价写为：

$$\begin{bmatrix} 1 & 2 \\ 4 & 7 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 3 \\ 10 \end{bmatrix}$$

即抽象的矩阵方程：

$$Ax = b$$

其中分项定义如下：

(1) $A = \begin{bmatrix} 1 & 2 \\ 4 & 7 \end{bmatrix}$ 为系数矩阵；

(2) $x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ 为未知解向量；

(3) $b = \begin{bmatrix} 3 \\ 10 \end{bmatrix}$ 为常数项向量。

### 5.2 两种解法的深层哲学对比

###### **方法[1]:初等消元法（高斯消元法）**

>[1]核心机制：
>
>通过方程之间的倍加相消，逐个消除未知数，得到阶梯形方程组，再由底向上逐层回代。
>
>[2]优劣分析：
>
>在未知数较少（2元、3元）时非常直观，容易手工完成；但在大型复杂系统或需要反复对不同常数向量 $b$ 求解时，消元过程高度依赖具体数值，缺乏全局结构解。

###### **方法[2]:大学逆矩阵解法 (Inverse Matrix Method)**

>[1]思想来源：
>
>类比中学标量一次方程：
>
>$$2x = 3 \implies 2^{-1} \cdot 2x = 2^{-1} \cdot 3 \implies x = \frac{3}{2}$$
>
>在矩阵代数中，寻找一个特殊矩阵 $A^{-1}$（称为 $A$ 的逆矩阵），满足：
>
>$$A^{-1} A = A A^{-1} = E$$
>
>其中 $E$ 为单位矩阵。
>
>[2]求解步骤：
>
>在矩阵方程 $Ax = b$ 两端**同时从左侧乘以** $A^{-1}$（前提是 $A$ 可逆）：
>
>$$A^{-1}(Ax) = A^{-1}b \implies (A^{-1}A)x = A^{-1}b \implies Ex = A^{-1}b \implies x = A^{-1}b$$
>
>[3]单位矩阵定义：
>
>主对角线全为 1，其余元素全为 0 的方阵称为单位矩阵：
>
>$$E_1 = 1,\quad E_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix},\quad E_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
>
>[4]逆矩阵验证与求解：
>
>对于系数矩阵 $A = \begin{bmatrix} 1 & 2 \\ 4 & 7 \end{bmatrix}$，其逆矩阵为 $A^{-1} = \begin{bmatrix} -7 & 2 \\ 4 & -1 \end{bmatrix}$。
>
>直接相乘验证：
>
>$$\begin{bmatrix} 1 & 2 \\ 4 & 7 \end{bmatrix} \begin{bmatrix} -7 & 2 \\ 4 & -1 \end{bmatrix} = \begin{bmatrix} -7+8 & 2-2 \\ -28+28 & 8-7 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = E_2$$
>
>于是解向量直接通过一次矩阵乘法产出：
>
>$$\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = A^{-1}b = \begin{bmatrix} -7 & 2 \\ 4 & -1 \end{bmatrix} \begin{bmatrix} 3 \\ 10 \end{bmatrix} = \begin{bmatrix} -21 + 20 \\ 12 - 10 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$$

<font color=deeppink>考研核心启示：</font>
逆矩阵将复杂的方程求解转化为**算子逆映射**。一旦算子求出逆 $A^{-1}$，无论常数向量 $b$ 如何改变，只需做一次乘法即可瞬间得到解向量，构成了现代计算数学与考研高分复习的根基框架。
