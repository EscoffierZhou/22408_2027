# Chap13 多元函数微分学

目的[1]:深刻理解多元函数的基本拓扑结构与空间几何映射，准确掌握点集、平面邻域、去心邻域的定义，掌握二重极限的定义、路径判定不存在法则以及极坐标代换、夹逼准则求二重极限的方法

目的[2]:建立偏导数、全微分、方向导数与梯度的全息几何直观，深刻理解切线斜率与切平面微元的几何映射，熟练运用判定二元函数可微性的“标准三步法”

目的[3]:融会贯通连续、偏导数存在、可微、偏导数连续四大核心概念之间的逻辑脉络与因果网络，牢记四大经典反例的构造原理与命题防坑准则

目的[4]:系统掌握多元复合函数链式求导规则（树状图分解法）与全微分形式不变性，熟练计算抽象复合函数的一阶、二阶偏导数及偏微分方程的坐标变换化简

目的[5]:系统掌握隐函数存在定理的理论内涵与边界条件，熟练运用公式法、两边偏导法和全微分形式不变性法求解一元隐函数与二元隐函数的高阶偏导数

目的[6]:系统攻克无条件极值（Fermat引理与Hessian矩阵/判别式法）、拉格朗日乘数法条件极值以及有界闭区域连续函数的最值求解模型，掌握最远（近）点公垂线几何判定定理

目的[7]:[仅数学一]系统掌握空间曲线的切线与法平面、空间曲面的切平面与法向量的解析计算，精通方向导数的方向余弦解析投影与梯度向量的几何与物理意义

## 1.多元函数的极限与连续性

###### **概念[1]:平面点集与邻域拓扑概念**

多元函数是建立在多维欧几里得空间点集基础之上的实值映射。设 $\mathbb{R}^2$ 为二维平面，点 $P(x, y)$ 为平面上的任意一点。

[1]平面邻域与去心邻域：
>(1) **$\delta$ 邻域**：
>
>点 $P_0(x_0, y_0)$ 的 $\delta$ 邻域是指与点 $P_0$ 的平面欧氏距离小于 $\delta$ 的全体点 $P(x, y)$ 构成的开圆盘区域，记作 $U(P_0, \delta)$：
>
>$$U(P_0, \delta) = \left\{(x, y) \;\middle|\; \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta \right\}$$
>
>(2) **去心 $\delta$ 邻域**：
>
>去掉中心点 $P_0$ 后的圆盘区域称为点 $P_0$ 的去心 $\delta$ 邻域，记作 $\mathring{U}(P_0, \delta)$：
>
>$$\mathring{U}(P_0, \delta) = \left\{(x, y) \;\middle|\; 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta \right\}$$
>
>(3) **点与点集的关系**：
>
>设 $E$ 为平面点集，点 $P \in \mathbb{R}^2$：
>
>[1]**内点**：若存在 $\delta > 0$，使得 $U(P, \delta) \subset E$，则称 $P$ 为 $E$ 的内点。内点必属于 $E$。
>
>[2]**外点**：若存在 $\delta > 0$，使得 $U(P, \delta) \cap E = \varnothing$，则称 $P$ 为 $E$ 的外点。
>
>[3]**边界点**：若对任意 $\delta > 0$，$U(P, \delta)$ 内既含有属于 $E$ 的点，又含有不属于 $E$ 的点，则称 $P$ 为 $E$ 的边界点。边界点可以属于 $E$，也可以不属于 $E$。
>
>[4]**开集与闭集**：若点集 $E$ 的点全部为内点，则称 $E$ 为开集；若点集 $E$ 包含其全部边界点，则称 $E$ 为闭集。

###### **概念[2]:二重极限与路径判别法则**

[1]二重极限（全面极限）的严格定义：
>设二元函数 $z = f(x, y)$ 在点 $P_0(x_0, y_0)$ 的去心邻域 $\mathring{U}(P_0, \delta)$ 内有定义。
>
>如果存在常数 $L$，对于任意给定的正数 $\varepsilon > 0$，总存在正数 $\delta > 0$，使得当 $(x, y) \in \mathring{U}(P_0, \delta)$，即满足：
>
>$$0 < \rho = \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta$$
>
>时，对应函数值均满足不等式：
>
>$$|f(x, y) - L| < \varepsilon$$
>
>则称常数 $L$ 为函数 $f(x, y)$ 当 $(x, y) \to (x_0, y_0)$ 时的二重极限，记作：
>
>$$\lim_{(x, y) \to (x_0, y_0)} f(x, y) = L \quad \text{或} \quad \lim_{\substack{x \to x_0 \\ y \to y_0}} f(x, y) = L$$

[2]二重极限的本质特征与路径无关性：
>(1) **全方位逼近性**：
>
>二重极限要求动点 $P(x, y)$ 沿平面内<font color=deeppink>任意方向、以任意曲线路径</font>逼近点 $P_0(x_0, y_0)$ 时，函数值 $f(x, y)$ 都必须收敛于同一个唯一的常数 $L$。
>
>(2) **路径判定极限不存在法则**：
>
>若选取两条不同的路径 $C_1$ 和 $C_2$（例如令 $y = kx$ 或 $y = kx^2$），使得沿不同路径趋近于 $(x_0, y_0)$ 时极限值依赖于参数 $k$，或者极限不存在，则该二重极限必不存在。
>
>(3) **二重极限与累次极限的本质区别**：
>
>累次极限 $\lim\limits_{x \to x_0} \left[ \lim\limits_{y \to y_0} f(x, y) \right]$ 与 $\lim\limits_{y \to y_0} \left[ \lim\limits_{x \to x_0} f(x, y) \right]$ 仅反映沿平行于坐标轴的特殊折线逼近，二重极限存在是两累次极限存在且相等的充分非必要条件。

###### **方法[1]:二重极限的核心求解策略**

[1]极坐标变换法（适用于分子分母为齐次多项式或含 $x^2 + y^2$）：
>令 $x = x_0 + r\cos\theta, y = y_0 + r\sin\theta$ ($r \to 0^+$)。
>
>若经化简后能分离出 $f(x, y) = g(r) h(\theta)$，且满足：
>
>$$\lim_{r \to 0^+} g(r) = 0 \quad \text{且} \quad |h(\theta)| \le M \quad (\text{有界})$$
>
>则二重极限存在且为 $0$。若极限结果中仍然含有与 $\theta$ 有关的项，则二重极限不存在。

[2]夹逼准则与基本不等式放缩法：
>利用重要初等不等式：
>
>$$|xy| \le \frac{1}{2}(x^2 + y^2) \implies \left|\frac{x^2 y}{x^2 + y^2}\right| \le \frac{1}{2}|x| \to 0$$
>
>实现高低次幂的绝对值放缩，直接判定二重极限的存在性与数值。

###### **概念[3]:多元函数的连续性与闭域性质**

[1]连续性定义：
>若函数 $z = f(x, y)$ 在点 $P_0(x_0, y_0)$ 处满足：
>
>$$\lim_{(x, y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$$
>
>则称 $f(x, y)$ 在点 $P_0(x_0, y_0)$ 处连续。

[2]有界闭区域上连续函数的三大性质：
>(1) **有界性与最大最小值定理**：在有界闭区域 $D$ 上的多元连续函数必在 $D$ 上有界，且必在 $D$ 上取得最大值和最小值。
>
>(2) **介值定理**：在连通有界闭区域 $D$ 上的多元连续函数必能取到介于其最小值与最大值之间的任意实数。
>
>(3) **零点定理**：若连通闭区域 $D$ 上连续函数在两点处函数值异号，则在该两点连线上必存在一点使其函数值为零。

## 2.偏导数与全微分体系

###### **概念[1]:偏导数的定义与几何意义**

[1]偏导数的一阶增量极限定义：
>设函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某邻域内有定义。
>
>(1) **关于 $x$ 的偏导数**：
>
>固定 $y = y_0$，将 $y$ 视作常数，一元函数 $f(x, y_0)$ 在 $x = x_0$ 处的导数称为 $f(x, y)$ 在点 $(x_0, y_0)$ 处关于 $x$ 的偏导数：
>
>$$\frac{\partial f}{\partial x}\Bigg|_{(x_0, y_0)} = f'_x(x_0, y_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x}$$
>
>(2) **关于 $y$ 的偏导数**：
>
>固定 $x = x_0$，将 $x$ 视作常数，一元函数 $f(x_0, y)$ 在 $y = y_0$ 处的导数称为 $f(x, y)$ 在点 $(x_0, y_0)$ 处关于 $y$ 的偏导数：
>
>$$\frac{\partial f}{\partial y}\Bigg|_{(x_0, y_0)} = f'_y(x_0, y_0) = \lim_{\Delta y \to 0} \frac{f(x_0, y_0 + \Delta y) - f(x_0, y_0)}{\Delta y}$$

[2]偏导数的几何直观意义：
>曲面 $S: z = f(x, y)$ 被平面 $y = y_0$ 所截得的相交曲线为 $\Gamma_x: \begin{cases} z = f(x, y) \\ y = y_0 \end{cases}$。
>
>偏导数 $f'_x(x_0, y_0)$ 的几何意义是曲线 $\Gamma_x$ 在点 $M_0(x_0, y_0, z_0)$ 处的切线对 $x$ 轴正向的斜率。同理，$f'_y(x_0, y_0)$ 是截线 $\Gamma_y$ 的切线对 $y$ 轴正向的斜率。

###### **定理[1]:高阶偏导数与二阶混合偏导对称性 (Schwarz 定理)**

设函数 $z = f(x, y)$ 的二阶混合偏导数 $f''_{xy}(x, y)$ 与 $f''_{yx}(x, y)$ 在点 $(x_0, y_0)$ 的某邻域内<font color=deeppink>连续</font>，则在该点处混合偏导数的值与求导次序无关：

$$f''_{xy}(x_0, y_0) = f''_{yx}(x_0, y_0)$$

###### **概念[2]:全微分的严格定义与几何直观**

[1]全增量与全微分的定义：
>设函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 的某邻域内有定义，自变量增量为 $\Delta x, \Delta y$。
>
>对应函数的全增量为：
>
>$$\Delta z = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)$$
>
>若存在与 $\Delta x, \Delta y$ 无关的常数 $A, B$，使得全增量可以表达为关于增量的线性函数加上高阶无穷小：
>
>$$\Delta z = A\Delta x + B\Delta y + o(\rho)$$
>
>其中 $\rho = \sqrt{(\Delta x)^2 + (\Delta y)^2} \to 0$。
>
>则称函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处**可微**，称线性主部 $A\Delta x + B\Delta y$ 为函数在点 $(x_0, y_0)$ 处的**全微分**，记作：
>
>$$\mathrm{d}z = A\Delta x + B\Delta y \quad (\text{因 } \mathrm{d}x = \Delta x, \mathrm{d}y = \Delta y \implies \mathrm{d}z = A\mathrm{d}x + B\mathrm{d}y)$$

[2]可微的必要条件与充分条件：
>(1) **可微的必要条件**：
>
>若函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处可微，则 $f(x, y)$ 在该点的偏导数 $f'_x(x_0, y_0)$ 与 $f'_y(x_0, y_0)$ 必然存在，且其系数唯一确定为：
>
>$$A = f'_x(x_0, y_0) = \frac{\partial z}{\partial x}, \quad B = f'_y(x_0, y_0) = \frac{\partial z}{\partial y}$$
>
>故全微分公式统一表达为：
>
>$$\mathrm{d}z = \frac{\partial z}{\partial x}\mathrm{d}x + \frac{\partial z}{\partial y}\mathrm{d}y$$
>
>(2) **可微的充分条件**：
>
>若偏导数 $f'_x(x, y)$ 与 $f'_y(x, y)$ 在点 $(x_0, y_0)$ 的某邻域内存在，且在点 $(x_0, y_0)$ 处<font color=deeppink>连续</font>，则函数 $f(x, y)$ 在点 $(x_0, y_0)$ 处必可微。

###### **模型[1]:多元函数四大关系核心网络与反例矩阵**

多元微积分学中，连续、偏导数存在、可微、偏导数连续四大概念之间的逻辑包含网络是考研命题的核心常客：

$$\begin{aligned}
&\text{偏导数连续} \implies \text{函数可微} \implies \text{函数连续} \\
&\Downarrow \hphantom{\implies \text{函数可微}} \Downarrow \\
&\text{偏导数存在} \hphantom{\implies} \text{偏导数存在}
\end{aligned}$$

[1]不可逆反推与四大经典反例：
>(1) **偏导数存在 $\centernot\implies$ 函数连续**：
>
>经典反例：$f(x, y) = \begin{cases} \frac{xy}{x^2 + y^2}, & (x, y) \neq (0, 0) \\ \\ 0, & (x, y) = (0, 0) \end{cases}$
>
>在点 $(0,0)$ 处沿坐标轴方向 $f(x, 0) \equiv 0, f(0, y) \equiv 0$，故偏导数 $f'_x(0, 0) = 0, f'_y(0, 0) = 0$ 均存在；但沿 $y = x$ 趋向原点时极限为 $\frac{1}{2} \neq 0$，函数甚至在该点不连续。
>
>(2) **函数连续 $\centernot\implies$ 偏导数存在**：
>
>经典反例：$f(x, y) = \sqrt{x^2 + y^2}$ 在点 $(0, 0)$ 处处连续，但在原点处沿任一坐标轴均呈现不可导的尖点，一阶偏导数不存在。
>
>(3) **偏导数存在 且 函数连续 $\centernot\implies$ 函数可微**：
>
>经典反例：$f(x, y) = \sqrt{|xy|}$ 在 $(0, 0)$ 处连续且偏导数 $f'_x(0, 0) = 0, f'_y(0, 0) = 0$；但在可微性判定中：
>
>$$\lim_{\substack{\Delta x \to 0 \\ \Delta y \to 0}} \frac{\sqrt{|\Delta x \Delta y|}}{\sqrt{(\Delta x)^2 + (\Delta y)^2}}$$
>
>沿路径 $\Delta y = \Delta x > 0$ 趋近时极限值为 $\frac{1}{\sqrt{2}} \neq 0$，故在该点不可微。
>
>(4) **函数可微 $\centernot\implies$ 偏导数连续**：
>
>经典反例：$f(x, y) = \begin{cases} (x^2 + y^2)\sin\frac{1}{x^2 + y^2}, & (x, y) \neq (0, 0) \\ \\ 0, & (x, y) = (0, 0) \end{cases}$
>
>该函数在原点处完全可微且 $\mathrm{d}z|_{(0,0)} = 0$，但其导函数包含振荡项 $\cos\frac{1}{x^2 + y^2}$，偏导数在 $(0,0)$ 处剧烈振荡而不连续。

###### **方法[2]:判定二元函数在点 $(x_0, y_0)$ 处可微性的“三步法”**

判断二元分段函数在分界点处的可微性是考研必考大题，必须严格遵循标准三步法逻辑流水线：

>[1]**第一步：利用导数定义求偏导数**：
>
>若其中任一偏导数不存在，则函数在 $(x_0, y_0)$ 处<font color=red>直接不可微</font>；若偏导数均存在，记 $A = f'_x(x_0, y_0), B = f'_y(x_0, y_0)$。
>
>[2]**第二步：写出全增量 $\Delta z$ 与线性主部**：
>
>写出全增量 $\Delta z = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)$，并构造误差商式：
>
>$$\frac{\Delta z - (A\Delta x + B\Delta y)}{\sqrt{(\Delta x)^2 + (\Delta y)^2}}$$
>
>[3]**第三步：计算该二重极限是否为零**：
>
>计算极限：
>
>$$\lim_{\substack{\Delta x \to 0 \\ \Delta y \to 0}} \frac{\Delta z - [f'_x(x_0, y_0)\Delta x + f'_y(x_0, y_0)\Delta y]}{\sqrt{(\Delta x)^2 + (\Delta y)^2}}$$
>
>若该极限存在且恒等于 $0$，则函数在 $(x_0, y_0)$ 处**可微**；若该极限不为 $0$ 或不存在，则函数在 $(x_0, y_0)$ 处**不可微**。

## 3.多元复合函数与隐函数微分法则

###### **法则[1]:多元复合函数链式求导法 (Chain Rule)**

[1]复合函数结构与变量角色分层：
>设多元复合函数 $z = f(u, v)$，其中中间变量 $u = \varphi(x, y), v = \psi(x, y)$ 均关于自变量 $x, y$ 偏导数存在。
>
>链式求导遵循“**连线相乘、分叉相加**”的树状分支原则：
>
>$$\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial x} = f'_1 \frac{\partial u}{\partial x} + f'_2 \frac{\partial v}{\partial x}$$
>
>$$\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y} + \frac{\partial z}{\partial v}\frac{\partial v}{\partial y} = f'_1 \frac{\partial u}{\partial y} + f'_2 \frac{\partial v}{\partial y}$$

[2]抽象复合函数求二阶高阶偏导数法则：
>在对一阶导数继续求偏导时，必须高度注意中间变量与自变量之间的复合层级关系。
>
>例如对 $z'_x = f'_1(u, v) \cdot u'_x + f'_2(u, v) \cdot v'_x$ 再次对 $x$ 求导：
>
>$$\frac{\partial^2 z}{\partial x^2} = \frac{\partial}{\partial x}(f'_1) \cdot u'_x + f'_1 \cdot u''_{xx} + \frac{\partial}{\partial x}(f'_2) \cdot v'_x + f'_2 \cdot v''_{xx}$$
>
>其中利用链式法则：
>
>$$\frac{\partial}{\partial x}(f'_1) = f''_{11}\frac{\partial u}{\partial x} + f''_{12}\frac{\partial v}{\partial x}$$

###### **定理[2]:全微分形式不变性 (Invariance of First-order Differential Form)**

无论是自变量 $x, y$ 还是由中间变量复合而成的中间函数 $u, v$，只要函数具有一阶连续偏导数，一阶全微分的形式始终保持为：

$$\mathrm{d}z = \frac{\partial z}{\partial u}\mathrm{d}u + \frac{\partial z}{\partial v}\mathrm{d}v$$

>全微分形式不变性是求解复杂偏微分方程、反求抽象函数偏导数的最强大算子工具。

###### **定理[3]:隐函数存在定理与求解三法**

[1]一元隐函数存在定理：
>设方程 $F(x, y) = 0$ 满足：
>
>(1) 在点 $P_0(x_0, y_0)$ 的某邻域内具有连续偏导数；
>
>(2) $F(x_0, y_0) = 0$；
>
>(3) $F'_y(x_0, y_0) \neq 0$；
>
>则在点 $P_0(x_0, y_0)$ 的某邻域内方程唯一确定单值连续可微的隐函数 $y = y(x)$，且其导数公式为：
>
>$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{F'_x(x, y)}{F'_y(x, y)}$$

[2]二元隐函数存在定理：
>设方程 $F(x, y, z) = 0$ 满足：
>
>(1) 在点 $P_0(x_0, y_0, z_0)$ 的某邻域内具有连续偏导数；
>
>(2) $F(x_0, y_0, z_0) = 0$；
>
>(3) $F'_z(x_0, y_0, z_0) \neq 0$；
>
>则在点 $P_0$ 某邻域内方程唯一确定单值连续可微的二元隐函数 $z = z(x, y)$，其偏导数公式为：
>
>$$\frac{\partial z}{\partial x} = -\frac{F'_x(x, y, z)}{F'_z(x, y, z)}, \quad \frac{\partial z}{\partial y} = -\frac{F'_y(x, y, z)}{F'_z(x, y, z)}$$

[3]隐函数求偏导的三大解题法：
>(1) **公式法**：直接将方程整理为 $F(x, y, z) = 0$，代入求导商式；
>
>(2) **链式方程求导法**：将 $z$ 视作 $x, y$ 的复合函数，在方程两端分别对 $x$ 或 $y$ 求偏导，随后解线性方程组求得未知偏导数；
>
>(3) **全微分法**：在原隐函数方程两端同时施加全微分算子 $\mathrm{d}$，整理成 $A\mathrm{d}x + B\mathrm{d}y + C\mathrm{d}z = 0$，解出 $\mathrm{d}z = -\frac{A}{C}\mathrm{d}x - \frac{B}{C}\mathrm{d}y$。

###### **定理[4]:二元函数拉格朗日中值定理与恒等式判定**

设函数 $f(x, y)$ 在包含点 $A(x_0, y_0)$ 与点 $B(x_0 + h, y_0 + k)$ 的凸区域 $D$ 上一阶偏导数连续，则存在介于 $0$ 与 $1$ 之间的实数 $\theta \in (0, 1)$，使得：

$$f(x_0 + h, y_0 + k) - f(x_0, y_0) = h f'_x(x_0 + \theta h, y_0 + \theta k) + k f'_y(x_0 + \theta h, y_0 + \theta k)$$

>注：若区域 $D$ 为连通开区域，且在 $D$ 内恒有 $f'_x(x, y) \equiv 0, f'_y(x, y) \equiv 0$，则 $f(x, y)$ 在 $D$ 内恒为常数。但如果区域非连通，则该结论不成立。

## 4.多元函数的极值与最值

###### **概念[1]:多元函数极值概念**

设函数 $z = f(x, y)$ 在点 $P_0(x_0, y_0)$ 的某邻域内有定义。

[1]极大值与极小值定义：
>若对该邻域内任意异于 $P_0$ 的点 $(x, y)$，恒有 $f(x, y) < f(x_0, y_0)$，则称点 $P_0$ 为极大值点，$f(x_0, y_0)$ 为极大值。
>
>若恒有 $f(x, y) > f(x_0, y_0)$，则称点 $P_0$ 为极小值点，$f(x_0, y_0)$ 为极小值。
>
>极大值和极小值统称为极值，极值点必须是<font color=deeppink>区域的内点</font>。

[2]二元极值与一元截面极值的关系：
>若 $f(x, y)$ 在点 $(x_0, y_0)$ 处取得极值，则一元函数 $g(x) = f(x, y_0)$ 与 $h(y) = f(x_0, y)$ 必分别在 $x = x_0$ 和 $y = y_0$ 处取得同类型的极值（必要条件）。
>
>但反之不成立！即使沿任意穿过该点的直线截面函数都取得极小值，二元函数也不一定在该点取极值（经典反例：$f(x, y) = (y - x^2)(y - 2x^2)$ 在原点处沿任何过原点的直线均取得极小值，但在抛物线之间穿越时取负值，原点不是极值点）。

###### **定理[5]:无条件极值的必要条件与充分条件**

[1]必要条件（多元 Fermat 引理）：
>设函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处具有一阶偏导数，且在该点取得极值，则必有：
>
>$$f'_x(x_0, y_0) = 0, \quad f'_y(x_0, y_0) = 0$$
>
>使一阶偏导数同时为零的点称为函数的**驻点**。
>
>极值可疑点包含两类：<font color=deeppink>一阶驻点</font> 与 <font color=red>一阶偏导数不存在的点</font>。

[2]充分条件（二阶 Hessian 判别法）：
>设 $f(x, y)$ 在点 $(x_0, y_0)$ 某邻域内有一阶及二阶连续偏导数，且 $(x_0, y_0)$ 为驻点（$f'_x = 0, f'_y = 0$）。
>
>记二阶偏导数值：
>
>$$A = f''_{xx}(x_0, y_0), \quad B = f''_{xy}(x_0, y_0), \quad C = f''_{yy}(x_0, y_0)$$
>
>定义 Hessian 判别式：$\Delta = AC - B^2$。
>
>(1) **若 $\Delta > 0$**：函数在该点取得极值。
>
>[1]当 $A < 0$（此时必有 $C < 0$）时，为**极大值**；
>
>[2]当 $A > 0$（此时必有 $C > 0$）时，为**极小值**。
>
>(2) **若 $\Delta < 0$**：函数在该点**不取极值**（该点为鞍点 Saddle Point）。
>
>(3) **若 $\Delta = 0$**：判别法失效，必须借助定义法、局部Taylor公式或路径穿插法另行判断。

###### **方法[3]:条件最值与拉格朗日乘数法 (Lagrange Multipliers)**

在实际工程与数学规划中，变量往往受到约束方程的制约。

[1]单约束条件极值模型：
>求目标函数 $u = f(x, y, z)$ 在约束条件 $\varphi(x, y, z) = 0$ 下的极值：
>
>(1) **构造拉格朗日辅助函数**：
>
>$$L(x, y, z, \lambda) = f(x, y, z) + \lambda \varphi(x, y, z)$$
>
>(2) **建立偏导数方程组**：
>
>$$\begin{cases} L'_x = f'_x + \lambda \varphi'_x = 0 \\ \\ L'_y = f'_y + \lambda \varphi'_y = 0 \\ \\ L'_z = f'_z + \lambda \varphi'_z = 0 \\ \\ L'_\lambda = \varphi(x, y, z) = 0 \end{cases}$$
>
>(3) **解方程组求驻点**：解出所有候选驻点 $P_i(x_i, y_i, z_i)$。

[2]双约束条件极值模型：
>求目标函数 $u = f(x, y, z)$ 在双约束条件 $\begin{cases} \varphi(x, y, z) = 0 \\ \psi(x, y, z) = 0 \end{cases}$ 下的最值：
>
>构造双乘子辅助函数：
>
>$$L(x, y, z, \lambda, \mu) = f(x, y, z) + \lambda \varphi(x, y, z) + \mu \psi(x, y, z)$$
>
>令五个偏导数全为零，求出所有驻点比较函数值。

###### **方法[4]:有界闭区域上连续函数的最值求解法则**

在有界闭区域 $D$ 上求解连续函数 $z = f(x, y)$ 的全局最大值与最小值：

>[1]**第一步：求区域内部可疑点**：
>
>求出区域 $D$ 内部的所有驻点以及一阶偏导数不存在的点，算出对应函数值；
>
>[2]**第二步：求区域边界上的可疑点**：
>
>将边界曲线方程代入目标函数转化为一元函数极值，或者利用拉格朗日乘数法求解边界上的条件极值驻点，并计算边界曲线端点处的函数值；
>
>[3]**第三步：全域点值大比对**：
>
>汇总内部与边界所有候选点的函数值，其中最大者即为全局最大值，最小者即为全局最小值。

###### **定理[6]:最远（近）点公垂线原理**

若 $\Gamma$ 是平面内光滑闭曲线，点 $Q$ 是曲线外的一定点。点 $P$ 是曲线 $\Gamma$ 上与点 $Q$ 距离达到最大或最小的点。

则连线 $PQ$ 必然垂直于曲线 $\Gamma$ 在点 $P$ 处的切线，即直线 $PQ$ 必落在该点处的法线上。

>该原理能将繁琐的高阶代数方程化简为法向量几何共线条件，节约大量运算时间。

## 5.空间解析几何在多元微分中的应用 (仅数学一)

###### **模型[2]:空间曲线的切线与法平面方程**

[1]参数方程形式：
>设空间曲线 $\Gamma: \begin{cases} x = x(t) \\ y = y(t) \\ z = z(t) \end{cases}$，切向量为 $\boldsymbol{\tau} = (x'(t_0), y'(t_0), z'(t_0))$。
>
>(1) **切线方程**：
>
>$$\frac{x - x_0}{x'(t_0)} = \frac{y - y_0}{y'(t_0)} = \frac{z - z_0}{z'(t_0)}$$
>
>(2) **法平面方程**（以切向量作为平面的法向量）：
>
>$$x'(t_0)(x - x_0) + y'(t_0)(y - y_0) + z'(t_0)(z - z_0) = 0$$

[2]交面形式（两隐式曲面交线）：
>设曲线由两曲面相交给出：$\begin{cases} F(x, y, z) = 0 \\ G(x, y, z) = 0 \end{cases}$。
>
>曲线切向量由两曲面法向量的外积给出：
>
>$$\boldsymbol{\tau} = \boldsymbol{n}_F \times \boldsymbol{n}_G = \begin{vmatrix} \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\ F'_x & F'_y & F'_z \\ G'_x & G'_y & G'_z \end{vmatrix}$$

###### **模型[3]:空间曲面的切平面与法线方程**

[1]隐式曲面 $F(x, y, z) = 0$：
>在点 $P_0(x_0, y_0, z_0)$ 处，曲面的法向量为梯度向量：
>
>$$\boldsymbol{n} = (F'_x, F'_y, F'_z)\Big|_{P_0}$$
>
>(1) **切平面方程**：
>
>$$F'_x(x_0, y_0, z_0)(x - x_0) + F'_y(x_0, y_0, z_0)(y - y_0) + F'_z(x_0, y_0, z_0)(z - z_0) = 0$$
>
>(2) **法线方程**：
>
>$$\frac{x - x_0}{F'_x(x_0, y_0, z_0)} = \frac{y - y_0}{F'_y(x_0, y_0, z_0)} = \frac{z - z_0}{F'_z(x_0, y_0, z_0)}$$

[2]显式曲面 $z = f(x, y)$：
>令 $F(x, y, z) = f(x, y) - z = 0$，法向量可取为 $\boldsymbol{n} = (f'_x, f'_y, -1)$。
>
>切平面方程为：
>
>$$z - z_0 = f'_x(x_0, y_0)(x - x_0) + f'_y(x_0, y_0)(y - y_0)$$

###### **概念[2]:方向导数与梯度向量**

[1]方向导数的定义与计算：
>设函数 $u = f(x, y, z)$ 在点 $P_0(x_0, y_0, z_0)$ 处可微，射线 $l$ 的方向余弦为 $(\cos\alpha, \cos\beta, \cos\gamma)$。
>
>函数沿方向 $l$ 的方向导数定义为沿射线距离的比值极限，其解析公式为：
>
>$$\frac{\partial u}{\partial \boldsymbol{l}}\Bigg|_{P_0} = \frac{\partial u}{\partial x}\cos\alpha + \frac{\partial u}{\partial y}\cos\beta + \frac{\partial u}{\partial z}\cos\gamma$$

[2]梯度向量及其物理几何本质：
>向量 $\mathrm{grad}\,u = \left(\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial u}{\partial z}\right)$ 称为函数 $u$ 在该点处的**梯度**。
>
>(1) **方向导数与梯度的内积表达**：
>
>$$\frac{\partial u}{\partial \boldsymbol{l}} = \mathrm{grad}\,u \cdot \boldsymbol{l}^0 = |\mathrm{grad}\,u| \cos\theta$$
>
>其中 $\theta$ 为梯度向量与射线方向 $l$ 的夹角。
>
>(2) **最速变化率**：
>
>[1]当 $\theta = 0$ 时，即射线方向与梯度方向一致时，方向导数达到最大值：
>
>$$\left(\frac{\partial u}{\partial \boldsymbol{l}}\right)_{\max} = |\mathrm{grad}\,u| = \sqrt{\left(\frac{\partial u}{\partial x}\right)^2 + \left(\frac{\partial u}{\partial y}\right)^2 + \left(\frac{\partial u}{\partial z}\right)^2}$$
>
>函数的梯度方向即为函数值<font color=deeppink>增长最快的方向</font>。
>
>[2]当 $\theta = \pi$ 时，沿负梯度方向函数值减少最快。
>
>[3]梯度向量与等值面（或等高线）在该点处的切平面相互垂直，即梯度指向等值面的法线正方向。
