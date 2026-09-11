# 课后作业与习题精练 (Homework)

--------------------------------------------------------------------------------

## 1. 向量点积与矩阵乘法基础精练

**习题[1]:向量内积、行乘列与方阵乘法基础运算组**

计算下列各式的值，并严格按照分步流程写出推导：
(1) $[1, 1] \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

(2) $[2, 0] \begin{bmatrix} 0 \\ -2 \end{bmatrix}$

(3) $[1, -1] \begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix}$

(4) $\begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

(5) $\begin{bmatrix} 1 \\ 1 \end{bmatrix} [1, -1]$

(6) $\begin{bmatrix} 2 \\ 0 \end{bmatrix} [0, -2]$

(7) $\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix}$

(8) $\begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$

主要思路：依据“左行乘右列、对应项相乘后求和”的基本定义，区分内积（数）、行向量、列向量与方阵的维度差异，精确展开各项。

>[1]计算第 (1) 至 (4) 式：
>
>(1) 一行乘一列（标量内积）：
>
>$$[1, 1] \begin{bmatrix} 1 \\ -1 \end{bmatrix} = 1 \times 1 + 1 \times (-1) = 1 - 1 = 0$$
>
>(2) 一行乘一列（标量内积）：
>
>$$[2, 0] \begin{bmatrix} 0 \\ -2 \end{bmatrix} = 2 \times 0 + 0 \times (-2) = 0 + 0 = 0$$
>
>(3) 一行乘两列（行向量乘方阵）：
>
>$$[1, -1] \begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix} = [1 \times 2 + (-1) \times (-1),\ 1 \times 1 + (-1) \times 3] = [2 + 1,\ 1 - 3] = [3, -2]$$
>
>(4) 两行乘一列（方阵乘列向量）：
>
>$$\begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 2 \times 1 + 1 \times (-1) \\ -1 \times 1 + 3 \times (-1) \end{bmatrix} = \begin{bmatrix} 2 - 1 \\ -1 - 3 \end{bmatrix} = \begin{bmatrix} 1 \\ -4 \end{bmatrix}$$
>
>[2]计算第 (5) 至 (6) 式（一列乘一行，外积展开）：
>
>(1) 计算第 (5) 式：
>
>$$\begin{bmatrix} 1 \\ 1 \end{bmatrix} [1, -1] = \begin{bmatrix} 1 \times 1 & 1 \times (-1) \\ 1 \times 1 & 1 \times (-1) \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ 1 & -1 \end{bmatrix}$$
>
>(2) 计算第 (6) 式：
>
>$$\begin{bmatrix} 2 \\ 0 \end{bmatrix} [0, -2] = \begin{bmatrix} 2 \times 0 & 2 \times (-2) \\ 0 \times 0 & 0 \times (-2) \end{bmatrix} = \begin{bmatrix} 0 & -4 \\ 0 & 0 \end{bmatrix}$$
>
>[3]计算第 (7) 至 (8) 式（方阵乘积与不可交换性验证）：
>
>(1) 计算第 (7) 式：
>
>$$\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix} = \begin{bmatrix} 1 \times 2 + 1 \times (-1) & 1 \times 1 + 1 \times 3 \\ -1 \times 2 + 1 \times (-1) & -1 \times 1 + 1 \times 3 \end{bmatrix} = \begin{bmatrix} 1 & 4 \\ -3 & 2 \end{bmatrix}$$
>
>(2) 计算第 (8) 式：
>
>$$\begin{bmatrix} 2 & 1 \\ -1 & 3 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 2 \times 1 + 1 \times (-1) & 2 \times 1 + 1 \times 1 \\ -1 \times 1 + 3 \times (-1) & -1 \times 1 + 3 \times 1 \end{bmatrix} = \begin{bmatrix} 1 & 3 \\ -4 & 2 \end{bmatrix}$$
>
>(3) 核心结论：
>
>第 (7) 式结果为 $\begin{bmatrix} 1 & 4 \\ -3 & 2 \end{bmatrix}$，第 (8) 式结果为 $\begin{bmatrix} 1 & 3 \\ -4 & 2 \end{bmatrix}$。二者明显不等，再次印证了矩阵乘法的<font color=red>非交换本质</font>。

--------------------------------------------------------------------------------

## 2. 几何变换矩阵与图像数据操作精练

**习题[2]:对称与伸缩矩阵对顶点数据矩阵的运算**

已知平面单位正方形的 4 个顶点排成的 $2 \times 4$ 坐标矩阵为：

$$X = \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$$

试计算下列各式，并分析其对应图形变换结果：
(1) $Y_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$
(2) $Y_2 = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$

主要思路：将 $2 \times 2$ 变换方阵与 $2 \times 4$ 数据矩阵相乘，利用左行乘右各列法则，并分析所得各列顶点坐标的几何位置迁移。

>[1]计算第 (1) 式（直线 $y=x$ 对称变换）：
>
>左侧矩阵为 $A = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$：
>
>$$Y_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 \times 0 + 1 \times 1 & 0 \times 1 + 1 \times 1 & 0 \times 1 + 1 \times 0 & 0 \times 0 + 1 \times 0 \\ 1 \times 0 + 0 \times 1 & 1 \times 1 + 0 \times 1 & 1 \times 1 + 0 \times 0 & 1 \times 0 + 0 \times 0 \end{bmatrix}$$
>
>化简得：
>
>$$Y_1 = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 0 \end{bmatrix}$$
>
>[2]计算第 (2) 式（横向拉伸变换）：
>
>左侧矩阵为 $B = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$：
>
>$$Y_2 = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 2 \times 0 + 0 \times 1 & 2 \times 1 + 0 \times 1 & 2 \times 1 + 0 \times 0 & 2 \times 0 + 0 \times 0 \\ 0 \times 0 + 1 \times 1 & 0 \times 1 + 1 \times 1 & 0 \times 1 + 1 \times 0 & 0 \times 0 + 1 \times 0 \end{bmatrix}$$
>
>化简得：
>
>$$Y_2 = \begin{bmatrix} 0 & 2 & 2 & 0 \\ 1 & 1 & 0 & 0 \end{bmatrix}$$
>
>[3]几何图形与数据意义解析：
>
>(1) 在 $Y_1$ 中，原顶点由 $(0,1), (1,1), (1,0), (0,0)$ 变为 $(1,0), (1,1), (0,1), (0,0)$，所有点的横纵坐标发生互换，实现了关于直线 $y = x$ 的轴对称变换。
>
>(2) 在 $Y_2$ 中，纵坐标保持原样（1与0），而第二、三列点的横坐标由 1 变为 2，图形横向展宽为原来的 2 倍。

--------------------------------------------------------------------------------

## 3. 刚体旋转与剪切复合变换精练

**习题[3]:平面旋转变换与保距性分析**

已知绕坐标原点逆时针旋转 $45^\circ$ 的旋转矩阵为：

$$R = \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix}$$

试求：
(1) 向量 $\alpha = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ 与 $\beta = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ 在旋转变换 $R$ 作用下的像向量；
(2) 计算变换后两个像向量的长度及它们的点积；
(3) 验证乘积 $R^\mathrm{T} R$ 是否等于单位阵 $E_2$，并指出旋转矩阵的优良性质。

主要思路：利用矩阵乘法分别求出基向量变换后的坐标，运用内积与范数公式计算其几何量，并通过矩阵转置与原矩阵相乘揭示正交矩阵的本质。

>[1]计算基向量在旋转作用下的像向量：
>
>(1) 向量 $\alpha$ 的像向量：
>
>$$R\alpha = \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2} \times 1 + \left(-\frac{\sqrt{2}}{2}\right) \times 0 \\ \frac{\sqrt{2}}{2} \times 1 + \frac{\sqrt{2}}{2} \times 0 \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} \end{bmatrix}$$
>
>(2) 向量 $\beta$ 的像向量：
>
>$$R\beta = \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2} \times 0 + \left(-\frac{\sqrt{2}}{2}\right) \times 1 \\ \frac{\sqrt{2}}{2} \times 0 + \frac{\sqrt{2}}{2} \times 1 \end{bmatrix} = \begin{bmatrix} -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} \end{bmatrix}$$
>
>[2]计算像向量的长度与点积：
>
>(1) 像向量的模长：
>
>$$\|R\alpha\| = \sqrt{\left(\frac{\sqrt{2}}{2}\right)^2 + \left(\frac{\sqrt{2}}{2}\right)^2} = \sqrt{\frac{1}{2} + \frac{1}{2}} = 1$$
>
>$$\|R\beta\| = \sqrt{\left(-\frac{\sqrt{2}}{2}\right)^2 + \left(\frac{\sqrt{2}}{2}\right)^2} = \sqrt{\frac{1}{2} + \frac{1}{2}} = 1$$
>
>(2) 像向量的点积：
>
>$$(R\alpha, R\beta) = \left(\frac{\sqrt{2}}{2}\right) \times \left(-\frac{\sqrt{2}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right) \times \left(\frac{\sqrt{2}}{2}\right) = -\frac{1}{2} + \frac{1}{2} = 0$$
>
>[3]验证 $R^\mathrm{T} R$ 及性质归纳：
>
>(1) 计算矩阵转置 $R^\mathrm{T}$：
>
>$$R^\mathrm{T} = \begin{bmatrix} \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \\ -\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix}$$
>
>(2) 计算乘积：
>
>$$R^\mathrm{T} R = \begin{bmatrix} \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \\ -\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix} \begin{bmatrix} \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \end{bmatrix} = \begin{bmatrix} \frac{1}{2} + \frac{1}{2} & -\frac{1}{2} + \frac{1}{2} \\ -\frac{1}{2} + \frac{1}{2} & \frac{1}{2} + \frac{1}{2} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = E_2$$
>
>(3) <font color=deeppink>考研性质升华：</font>
>
>满足 $R^\mathrm{T} R = E$ 的矩阵称为**正交矩阵**。正交变换保持向量的长度不变，同时保持向量之间的夹角不变（内积不变），对应几何空间中完全不失真的刚体旋转。

--------------------------------------------------------------------------------

## 4. 线性方程组逆矩阵与不可逆性探究精练

**习题[4]:不可逆矩阵与消元奇异性探析**

考查线性方程组：

$$\begin{cases} x_1 + 2x_2 = 3 \\ 2x_1 + 4x_2 = 7 \end{cases}$$

试分析：
(1) 使用高斯消元法尝试求解，说明消元过程中出现的现象；
(2) 写出该方程组的系数矩阵 $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$，说明为什么不存在逆矩阵 $A^{-1}$ 使得 $AA^{-1} = E_2$；
(3) 从几何变换和向量空间的视角解释该方程组无解的根本原因。

主要思路：通过两式相消导出矛盾方程 $0 = 1$；利用反证法证明不存在逆矩阵；从矩阵列向量共线导致二维空间被压缩为一条直线的几何视角深刻洞察奇异性。

>[1]高斯消元过程分析：
>
>设原方程组为：
>
>$$\begin{cases} x_1 + 2x_2 = 3 & (1) \\ 2x_1 + 4x_2 = 7 & (2) \end{cases}$$
>
>执行消元操作：利用 $(2) - (1) \times 2$ 得到：
>
>$$(2 - 2)x_1 + (4 - 4)x_2 = 7 - 3 \times 2 \implies 0 \cdot x_1 + 0 \cdot x_2 = 1 \implies 0 = 1$$
>
>出现了恒不成立的矛盾等式，故该方程组**无解**。
>
>[2]证明系数矩阵 $A$ 不存在逆矩阵：
>
>反证法：假设存在逆矩阵 $B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}$，使得 $AB = E_2$。
>
>则由矩阵乘法：
>
>$$\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} b_{11} + 2b_{21} & b_{12} + 2b_{22} \\ 2(b_{11} + 2b_{21}) & 2(b_{12} + 2b_{22}) \end{bmatrix}$$
>
>若其等于单位矩阵 $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$，则要求其第一列满足：
>
>$$\begin{cases} b_{11} + 2b_{21} = 1 \\ 2(b_{11} + 2b_{21}) = 0 \end{cases}$$
>
>将第一式代入第二式立即得到 $2 \times 1 = 0 \implies 2 = 0$，出现荒谬矛盾。
>
>因此，假设不成立，<font color=red>矩阵 $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ 绝不存在逆矩阵！</font>
>
>[3]几何与向量空间本质解析：
>
>(1) 矩阵变换视角：矩阵 $A$ 的两列分别为 $\alpha_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$ 与 $\alpha_2 = \begin{bmatrix} 2 \\ 4 \end{bmatrix} = 2\alpha_1$。矩阵 $A$ 作用在平面任意向量 $x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ 上的输出为：
>
>$$Ax = x_1 \alpha_1 + x_2 \alpha_2 = (x_1 + 2x_2) \begin{bmatrix} 1 \\ 2 \end{bmatrix}$$
>
>(2) 维度坍缩与信息丢失：矩阵 $A$ 将整个二维平面的无限点全部“拍扁”压缩到了直线 $y = 2x$ 之上！
>
>(3) 方程组右侧的常数向量 $b = \begin{bmatrix} 3 \\ 7 \end{bmatrix}$ 并不在直线 $y = 2x$ 上（因为 $7 \neq 2 \times 3$），因而在 $A$ 的值域之外，方程组必然无解。
>
>(4) 这种“降维压缩”导致原先二维的信息被不可逆地销毁，因而不存在任何矩阵能够将一条直线上的点还原回整个平面，这就是矩阵不可逆（奇异）的几何直观本质。
