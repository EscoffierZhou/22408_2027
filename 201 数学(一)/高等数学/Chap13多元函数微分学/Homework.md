## 13.Homework

**习题[13.1]:二元初等分段函数的极限与连续性判定**

设二元函数 $f(x, y) = \begin{cases} \frac{x^2 y}{x^2 + y^2}, & x^2 + y^2 \neq 0 \\ \\ 0, & x^2 + y^2 = 0 \end{cases}$，下列结论中正确的是：
(A) $\lim\limits_{(x, y) \to (0, 0)} f(x, y)$ 不存在
(B) 函数在点 $(0, 0)$ 处不连续
(C) 函数在点 $(0, 0)$ 处连续
(D) 函数在点 $(0, 0)$ 处关于 $x$ 的偏导数不存在

主要思路:利用基本不等式 $|xy| \le \frac{1}{2}(x^2 + y^2)$ 进行绝对值放缩夹逼，证明二重极限存在且恒等于 $0$，从而由极限值等于函数值判定连续性

>[1]极限放缩与夹逼估计：
>
>当 $(x, y) \neq (0, 0)$ 时，考查函数的绝对值表达式：
>
>$$|f(x, y) - 0| = \left| \frac{x^2 y}{x^2 + y^2} \right| = |x| \cdot \frac{|xy|}{x^2 + y^2}$$
>
>由基本均值不等式 $|xy| \le \frac{1}{2}(x^2 + y^2)$，有：
>
>$$\frac{|xy|}{x^2 + y^2} \le \frac{1}{2}$$
>
>因此得到严格的不等式夹逼链：
>
>$$0 \le |f(x, y)| \le \frac{1}{2}|x|$$
>
>[2]计算二重极限：
>
>当 $(x, y) \to (0, 0)$ 时，$|x| \to 0$，从而 $\lim\limits_{(x, y) \to (0, 0)} \frac{1}{2}|x| = 0$。
>
>由夹逼准则（Squeeze Theorem），得到：
>
>$$\lim_{(x, y) \to (0, 0)} f(x, y) = 0$$
>
>[3]连续性检验与结论：
>
>因为极限存在且 $\lim\limits_{(x, y) \to (0, 0)} f(x, y) = 0 = f(0, 0)$，所以函数在点 $(0, 0)$ 处连续。
>
>故正确选项为 (C)。

**习题[13.2]:根据偏导数符号判定多元函数值大小**

设二元函数 $f(x, y)$ 在平面上有定义，且一阶偏导数恒满足 $f'_x(x, y) > 0, f'_y(x, y) < 0$。记 $A = f(1, 2), B = f(2, 1), C = f(1, 1), D = f(2, 2)$，则下列大小关系正确的是：
(A) $A > B > C > D$
(B) $B > A > D > C$
(C) $D > B > A > C$
(D) $B > C > A$ 且 $B > D > A$

主要思路:一阶偏导数的正负符号直接对应二元函数沿平行于坐标轴截线方向的单调递增或递减性，通过在平面上构造网格路径逐点比对函数值

>[1]利用偏导数分析单调性：
>
>因 $f'_x(x, y) > 0$，表明当固定 $y$ 时，$f(x, y)$ 是关于自变量 $x$ 的严格单调递增函数；
>
>因 $f'_y(x, y) < 0$，表明当固定 $x$ 时，$f(x, y)$ 是关于自变量 $y$ 的严格单调递减函数。
>
>[2]沿坐标轴路径比对函数值：
>
>(1) 比较 $C(1, 1)$ 与 $A(1, 2)$：
>
>固定 $x = 1$，因 $y$ 从 $1$ 增大到 $2$ 且 $f'_y < 0$，故：
>
>$$C = f(1, 1) > f(1, 2) = A$$
>
>(2) 比较 $B(2, 1)$ 与 $C(1, 1)$：
>
>固定 $y = 1$，因 $x$ 从 $1$ 增大到 $2$ 且 $f'_x > 0$，故：
>
>$$B = f(2, 1) > f(1, 1) = C$$
>
>(3) 比较 $B(2, 1)$ 与 $D(2, 2)$ 以及 $D(2, 2)$ 与 $A(1, 2)$：
>
>固定 $x = 2$，因 $y$ 增大函数值递减，故 $B = f(2, 1) > f(2, 2) = D$；
>
>固定 $y = 2$，因 $x$ 增大函数值递增，故 $D = f(2, 2) > f(1, 2) = A$。
>
>[3]综合链式比对：
>
>由 $B > C > A$ 且 $B > D > A$，最大值为 $B$，最小值为 $A$。
>
>故正确选项为 (D)。

**习题[13.3]:经典开方函数在原点的偏导与可微性辨析**

设函数 $f(x, y) = \sqrt{|xy|}$，则在点 $(0, 0)$ 处：
(A) 偏导数不存在，不可微
(B) 偏导数存在，不可微
(C) 偏导数存在，可微
(D) 偏导数不存在，可微

主要思路:通过偏导数差商定义验证 $f'_x(0, 0) = 0, f'_y(0, 0) = 0$；进而将增量商代入可微性极限，通过沿直线 $y = x$ 趋近证明极限非零从而不可微

>[1]求在原点处的偏导数：
>
>由偏导数增量极限定义：
>
>$$f'_x(0, 0) = \lim_{x \to 0} \frac{f(x, 0) - f(0, 0)}{x} = \lim_{x \to 0} \frac{\sqrt{|x \cdot 0|} - 0}{x} = \lim_{x \to 0} 0 = 0$$
>
>$$f'_y(0, 0) = \lim_{y \to 0} \frac{f(0, y) - f(0, 0)}{y} = \lim_{y \to 0} \frac{\sqrt{|0 \cdot y|} - 0}{y} = \lim_{y \to 0} 0 = 0$$
>
>两偏导数均存在且值均为 $0$。
>
>[2]检验可微性极限条件：
>
>若函数在 $(0, 0)$ 可微，必须满足：
>
>$$\lim_{\substack{\Delta x \to 0 \\ \Delta y \to 0}} \frac{f(\Delta x, \Delta y) - f(0, 0) - [f'_x(0, 0)\Delta x + f'_y(0, 0)\Delta y]}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0$$
>
>代入得：
>
>$$\lim_{\substack{\Delta x \to 0 \\ \Delta y \to 0}} \frac{\sqrt{|\Delta x \Delta y|}}{\sqrt{(\Delta x)^2 + (\Delta y)^2}}$$
>
>[3]路径法判别极限非零：
>
>取趋近路径 $\Delta y = \Delta x > 0$：
>
>$$\lim_{\Delta x \to 0^+} \frac{\sqrt{\Delta x \cdot \Delta x}}{\sqrt{(\Delta x)^2 + (\Delta x)^2}} = \lim_{\Delta x \to 0^+} \frac{\Delta x}{\sqrt{2}\Delta x} = \frac{1}{\sqrt{2}} \neq 0$$
>
>误差极限不为零，故函数在 $(0, 0)$ 处不可微。正确选项为 (B)。

**习题[13.4]:抽象复合函数偏导算子化简**

设 $z = f\left( x - y, \frac{y}{x} \right)$，其中 $f(u, v)$ 具有一阶连续偏导数，则 $x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y}$ 等于：
(A) $(x - y)f'_1$
(B) $(x - y)f'_1$
(C) $f'_2$
(D) $0$

主要思路:设 $u = x - y, v = \frac{y}{x}$，利用链式求导法则分别求出 $\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$，乘以各自系数相加后观察交叉项的相消与合并

>[1]求偏导数 $\frac{\partial z}{\partial x}$：
>
>$$\frac{\partial z}{\partial x} = f'_1 \frac{\partial u}{\partial x} + f'_2 \frac{\partial v}{\partial x} = f'_1 \cdot 1 + f'_2 \cdot \left( -\frac{y}{x^2} \right) = f'_1 - \frac{y}{x^2}f'_2$$
>
>[2]求偏导数 $\frac{\partial z}{\partial y}$：
>
>$$\frac{\partial z}{\partial y} = f'_1 \frac{\partial u}{\partial y} + f'_2 \frac{\partial v}{\partial y} = f'_1 \cdot (-1) + f'_2 \cdot \left( \frac{1}{x} \right) = -f'_1 + \frac{1}{x}f'_2$$
>
>[3]代入线性组合式相加化简：
>
>$$x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y} = x\left( f'_1 - \frac{y}{x^2}f'_2 \right) + y\left( -f'_1 + \frac{1}{x}f'_2 \right)$$
>
>$$= x f'_1 - \frac{y}{x}f'_2 - y f'_1 + \frac{y}{x}f'_2 = (x - y)f'_1$$
>
>含 $f'_2$ 的项精确相消，最终结果为 $(x - y)f'_1$。正确选项为 (A)。

**习题[13.5]:含绝对值二元函数极值点判定**

考察两个二元函数：$z_1 = |x + y|$ 与 $z_2 = x^2 + y^2 - 2x - 4y + 5$。关于点 $(-1, 1)$ 与点 $(1, 2)$ 的极值性质，下列说法正确的是：
(A) $(-1, 1)$ 不是 $z_1$ 的极值点，$(1, 2)$ 是 $z_2$ 的极小值点
(B) $(-1, 1)$ 是 $z_1$ 的极大值点，$(1, 2)$ 是 $z_2$ 的极大值点
(C) $(-1, 1)$ 是 $z_1$ 的极小值点，$(1, 2)$ 是 $z_2$ 的极大值点
(D) $(-1, 1)$ 是 $z_1$ 的极小值点，$(1, 2)$ 是 $z_2$ 的极小值点

主要思路:对于含绝对值函数利用定义法与非负性判定极小值；对于二次多项式利用配方法或 Hessian 判别式判定驻点的极值性质

>[1]分析 $z_1 = |x + y|$ 在点 $(-1, 1)$ 处的性质：
>
>在点 $(-1, 1)$ 处，$z_1(-1, 1) = |-1 + 1| = 0$。
>
>对于平面上任意点 $(x, y)$，恒有绝对值非负：$z_1(x, y) = |x + y| \ge 0 = z_1(-1, 1)$。
>
>由极值定义，点 $(-1, 1)$ 为函数的**极小值点**（实际上整条直线 $x + y = 0$ 上的所有点均为非严格极小值点）。
>
>[2]分析 $z_2$ 在点 $(1, 2)$ 处的性质：
>
>通过完全平方配方：
>
>$$z_2 = (x^2 - 2x + 1) + (y^2 - 4y + 4) = (x - 1)^2 + (y - 2)^2$$
>
>在点 $(1, 2)$ 处，$z_2(1, 2) = 0$。
>
>对任意 $(x, y) \neq (1, 2)$，恒有 $(x - 1)^2 + (y - 2)^2 > 0$。
>
>故 $(1, 2)$ 为函数 $z_2$ 的严格**极小值点**。
>
>[3]结论判定：
>
>两者均为极小值点。正确选项为 (D)。

**习题[13.6]:多元经济学需求价格弹性计算**

设市场上有两种相互竞争的商品 $A$ 和 $B$，商品 $A$ 的需求量函数为 $Q_A = 100 P_A^{-0.4} P_B^{0.2}$，其中 $P_A, P_B$ 分别为两种商品的价格。求商品 $A$ 对自身价格的需求价格弹性 $\eta_{AA}$。

主要思路:根据微积分经济学中需求价格弹性的标准定义公式 $\eta = -\frac{\partial Q_A}{\partial P_A} \frac{P_A}{Q_A}$ 进行偏导数计算并化简

>[1]写出偏导数表达式：
>
>将 $P_B$ 视作常数，对自身价格 $P_A$ 求偏导数：
>
>$$\frac{\partial Q_A}{\partial P_A} = 100(-0.4)P_A^{-1.4} P_B^{0.2} = -40 P_A^{-1.4} P_B^{0.2}$$
>
>[2]代入弹性定义公式：
>
>需求价格弹性为：
>
>$$\eta_{AA} = -\frac{\partial Q_A}{\partial P_A} \frac{P_A}{Q_A} = -\left( -40 P_A^{-1.4} P_B^{0.2} \right) \frac{P_A}{100 P_A^{-0.4} P_B^{0.2}}$$
>
>[3]指数运算法则化简：
>
>$$\eta_{AA} = \frac{40}{100} \frac{P_A^{-0.4} P_B^{0.2}}{P_A^{-0.4} P_B^{0.2}} = 0.4$$
>
>弹性值为恒常数 $0.4$，表明商品 $A$ 属于缺乏价格弹性的商品。

**习题[13.7]:初等二元商式的全微分计算**

求函数 $z = \left( 1 + \frac{x}{y} \right)^2$ 在点 $(1, 1)$ 处的全微分 $\mathrm{d}z\Big|_{(1, 1)}$。

主要思路:分别求出函数关于 $x$ 和 $y$ 的偏导数，代入指定点 $(1, 1)$ 确定偏微分系数，代入全微分公式 $\mathrm{d}z = f'_x\,\mathrm{d}x + f'_y\,\mathrm{d}y$

>[1]求偏导数 $\frac{\partial z}{\partial x}$：
>
>$$\frac{\partial z}{\partial x} = 2\left( 1 + \frac{x}{y} \right) \cdot \frac{1}{y} = \frac{2(x + y)}{y^2}$$
>
>在点 $(1, 1)$ 处：
>
>$$\frac{\partial z}{\partial x}\Bigg|_{(1, 1)} = \frac{2(1 + 1)}{1^2} = 4$$
>
>[2]求偏导数 $\frac{\partial z}{\partial y}$：
>
>$$\frac{\partial z}{\partial y} = 2\left( 1 + \frac{x}{y} \right) \cdot \left( -\frac{x}{y^2} \right) = -\frac{2x(x + y)}{y^3}$$
>
>在点 $(1, 1)$ 处：
>
>$$\frac{\partial z}{\partial y}\Bigg|_{(1, 1)} = -\frac{2(1)(1 + 1)}{1^3} = -4$$
>
>[3]合成全微分：
>
>$$\mathrm{d}z\Big|_{(1, 1)} = 4\,\mathrm{d}x - 4\,\mathrm{d}y = 4(\mathrm{d}x - \mathrm{d}y)$$

**习题[13.8]:复合抽象单变量函数的全微分**

设 $z = f(4x^2 - y^2)$，其中 $f(u)$ 可导且 $f'(0) = \frac{1}{2}$。求全微分 $\mathrm{d}z\Big|_{(1, 2)}$。

主要思路:设 $u = 4x^2 - y^2$，利用一阶全微分形式不变性 $\mathrm{d}z = f'(u)\,\mathrm{d}u$，结合指定点处的增量微分求解

>[1]求中间变量的数值与微分：
>
>令 $u = 4x^2 - y^2$。
>
>在点 $(1, 2)$ 处：$u = 4(1)^2 - (2)^2 = 4 - 4 = 0$。
>
>对应导数值为 $f'(0) = \frac{1}{2}$。
>
>[2]计算微分微元 $\mathrm{d}u$：
>
>$$\mathrm{d}u = 8x\,\mathrm{d}x - 2y\,\mathrm{d}y$$
>
>代入 $(x, y) = (1, 2)$：
>
>$$\mathrm{d}u\Big|_{(1, 2)} = 8(1)\,\mathrm{d}x - 2(2)\,\mathrm{d}y = 8\,\mathrm{d}x - 4\,\mathrm{d}y$$
>
>[3]计算全微分 $\mathrm{d}z$：
>
>$$\mathrm{d}z\Big|_{(1, 2)} = f'(0)\,\mathrm{d}u\Big|_{(1, 2)} = \frac{1}{2}(8\,\mathrm{d}x - 4\,\mathrm{d}y) = 4\,\mathrm{d}x - 2\,\mathrm{d}y$$

**习题[13.9]:指数幂型隐函数的一阶偏导数计算**

设隐函数 $z = z(x, y)$ 由方程 $(z + y)^x = x^z$ 确定，求在点 $(1, 1)$ 处的偏导数 $\frac{\partial z}{\partial x}\Bigg|_{(1, 1)}$。

主要思路:先将自变量数值代入原方程求出隐函数在对应点的因变量初值 $z(1, 1)$；再对原方程两端取对数将幂指形式化为代数乘积形式，两边对 $x$ 求偏导求解

>[1]求对应点 $z$ 的取值：
>
>将 $x = 1, y = 1$ 代入原方程：
>
>$$(z + 1)^1 = 1^z \implies z + 1 = 1 \implies z(1, 1) = 0$$
>
>[2]两端取自然对数化简：
>
>对 $(z + y)^x = x^z$ 取对数：
>
>$$x \ln(z + y) = z \ln x$$
>
>[3]两端对 $x$ 求偏导数并代入数值：
>
>$$\ln(z + y) + x \cdot \frac{1}{z + y} \frac{\partial z}{\partial x} = \frac{\partial z}{\partial x} \ln x + z \cdot \frac{1}{x}$$
>
>将 $x = 1, y = 1, z = 0$ 代入上式：
>
>$$\ln(0 + 1) + 1 \cdot \frac{1}{0 + 1} \frac{\partial z}{\partial x} = \frac{\partial z}{\partial x} \ln 1 + 0 \cdot \frac{1}{1}$$
>
>$$0 + 1 \cdot \frac{\partial z}{\partial x} = 0 + 0 \implies \frac{\partial z}{\partial x}\Bigg|_{(1, 1)} = 0$$
>
>（若原题常数项或移项有偏置项，严格按上述代入流程解得唯一确定实数值）。

**习题[13.10]:多元复合函数的二阶偏导数展开**

设函数 $z = f(x^2 y^2, e^{xy})$，其中 $f(u, v)$ 具有二阶连续偏导数，求 $z''_{xx}$。

主要思路:设 $u = x^2 y^2, v = e^{xy}$，利用复合求导链式法则先求一阶偏导数 $z'_x$，再乘积求导与链式求导展开求二阶偏导数 $z''_{xx}$

>[1]求一阶偏导数 $z'_x$：
>
>$$u = x^2 y^2, \quad v = e^{xy}$$
>
>$$u'_x = 2x y^2, \quad v'_x = y e^{xy}$$
>
>$$\frac{\partial z}{\partial x} = f'_1(2x y^2) + f'_2(y e^{xy})$$
>
>[2]对 $x$ 再次求偏导：
>
>$$z''_{xx} = \frac{\partial}{\partial x}\left[ f'_1 \cdot 2xy^2 \right] + \frac{\partial}{\partial x}\left[ f'_2 \cdot y e^{xy} \right]$$
>
>应用乘积法则：
>
>$$z''_{xx} = \frac{\partial(f'_1)}{\partial x} \cdot 2xy^2 + f'_1 \cdot (2y^2) + \frac{\partial(f'_2)}{\partial x} \cdot y e^{xy} + f'_2 \cdot (y^2 e^{xy})$$
>
>[3]链式展开高阶项并合并：
>
>$$\frac{\partial(f'_1)}{\partial x} = f''_{11}(2xy^2) + f''_{12}(y e^{xy})$$
>
>$$\frac{\partial(f'_2)}{\partial x} = f''_{21}(2xy^2) + f''_{22}(y e^{xy})$$
>
>代入得：
>
>$$z''_{xx} = [2xy^2 f''_{11} + y e^{xy} f''_{12}](2xy^2) + 2y^2 f'_1 + [2xy^2 f''_{21} + y e^{xy} f''_{22}](y e^{xy}) + y^2 e^{xy} f'_2$$
>
>$$= 4x^2 y^4 f''_{11} + 4xy^3 e^{xy} f''_{12} + y^2 e^{2xy} f''_{22} + 2y^2 f'_1 + y^2 e^{xy} f'_2$$

**习题[13.11]:隐函数与变限定积分联立的全导数**

设函数 $u(x)$ 由方程 $u - \int_0^{x+u} e^{-t^2}\,\mathrm{d}t = 0$ 确定，求全导数 $\frac{\mathrm{d}u}{\mathrm{d}x}$。

主要思路:将 $u$ 视作自变量 $x$ 的复合隐函数，方程两端对 $x$ 直接求全导数，利用变上限积分对上限求导公式建立代数方程并解出 $\frac{\mathrm{d}u}{\mathrm{d}x}$

>[1]方程两端关于 $x$ 求全导数：
>
>记上限为 $v = x + u$。
>
>$$\frac{\mathrm{d}}{\mathrm{d}x}\left( u - \int_0^{x+u} e^{-t^2}\,\mathrm{d}t \right) = \frac{\mathrm{d}u}{\mathrm{d}x} - e^{-(x+u)^2} \cdot \frac{\mathrm{d}(x + u)}{\mathrm{d}x} = 0$$
>
>[2]展开导数项：
>
>$$\frac{\mathrm{d}u}{\mathrm{d}x} - e^{-(x+u)^2}\left( 1 + \frac{\mathrm{d}u}{\mathrm{d}x} \right) = 0$$
>
>$$\frac{\mathrm{d}u}{\mathrm{d}x}\left[ 1 - e^{-(x+u)^2} \right] = e^{-(x+u)^2}$$
>
>[3]解出未知全导数：
>
>$$\frac{\mathrm{d}u}{\mathrm{d}x} = \frac{e^{-(x+u)^2}}{1 - e^{-(x+u)^2}} = \frac{1}{e^{(x+u)^2} - 1}$$

**习题[13.12]:二元对数多项式函数的无条件极值**

求二元函数 $f(x, y) = x^2 y^2 + x\ln x$ ($x > 0$) 的极值。

主要思路:先令一阶偏导数同时为零求出定义域内的唯一驻点；再计算驻点处的二阶偏导数 $A, B, C$，利用 Hessian 判别式 $\Delta = AC - B^2$ 判定极小值

>[1]求一阶偏导数并确定驻点：
>
>$$f'_x = 2x y^2 + \ln x + x \cdot \frac{1}{x} = 2xy^2 + \ln x + 1$$
>
>$$f'_y = 2x^2 y$$
>
>令 $\begin{cases} f'_x = 0 \\ f'_y = 0 \end{cases}$。
>
>因 $x > 0$，由 $f'_y = 2x^2 y = 0$ 必得 $y = 0$。
>
>代入 $f'_x = 0 + \ln x + 1 = 0 \implies \ln x = -1 \implies x = \frac{1}{e}$。
>
>得到定义域内的唯一驻点为 $\left( \frac{1}{e}, 0 \right)$。
>
>[2]计算二阶偏导数数值：
>
>$$f''_{xx} = 2y^2 + \frac{1}{x}$$
>
>$$f''_{xy} = 4xy$$
>
>$$f''_{yy} = 2x^2$$
>
>在驻点 $\left( \frac{1}{e}, 0 \right)$ 处：
>
>$$A = f''_{xx}\left( \frac{1}{e}, 0 \right) = 0 + \frac{1}{1/e} = e > 0$$
>
>$$B = f''_{xy}\left( \frac{1}{e}, 0 \right) = 0$$
>
>$$C = f''_{yy}\left( \frac{1}{e}, 0 \right) = 2\left( \frac{1}{e} \right)^2 = \frac{2}{e^2} > 0$$
>
>[3]利用充分条件判据验证极值：
>
>$$\Delta = AC - B^2 = e \cdot \frac{2}{e^2} - 0 = \frac{2}{e} > 0$$
>
>且 $A = e > 0$。
>
>因此函数在点 $\left( \frac{1}{e}, 0 \right)$ 处取得**极小值**，极小值为：
>
>$$f\left( \frac{1}{e}, 0 \right) = \left(\frac{1}{e}\right)^2 (0)^2 + \frac{1}{e}\ln\frac{1}{e} = 0 + \frac{1}{e}(-1) = -\frac{1}{e}$$

**习题[13.13]:偏导数方程积分反求函数与极值**

设函数 $f(x, y)$ 满足偏导数方程 $f''_{xy}(x, y) = (2y + 2)e^x$，且满足初始条件 $f(x, 0) = xe^x, f(0, y) = y^2 + 2y$。求 $f(x, y)$ 的解析式并求其极值。

主要思路:通过两步偏积分还原原函数结构，利用边值条件定出解析式；进而求驻点并利用二阶判别式判定极值

>[1]积分反求原函数解析式：
>
>对 $x$ 偏积分：
>
>$$\frac{\partial f}{\partial y} = \int (2y + 2)e^x\,\mathrm{d}x = (2y + 2)e^x + \varphi(y)$$
>
>再对 $y$ 偏积分：
>
>$$f(x, y) = (y^2 + 2y)e^x + \Phi(y) + \psi(x)$$
>
>代入 $f(x, 0) = 0 + \Phi(0) + \psi(x) = xe^x \implies \psi(x) = xe^x - \Phi(0)$。
>
>代入 $f(0, y) = (y^2 + 2y) + \Phi(y) + \psi(0) = (y^2 + 2y) + \Phi(y) - \Phi(0) = y^2 + 2y \implies \Phi(y) = \Phi(0)$。
>
>因此原函数为：
>
>$$f(x, y) = (x + y^2 + 2y)e^x$$
>
>[2]求一阶偏导数与驻点：
>
>$$f'_x = 1 \cdot e^x + (x + y^2 + 2y)e^x = (x + y^2 + 2y + 1)e^x$$
>
>$$f'_y = (2y + 2)e^x$$
>
>令 $\begin{cases} f'_x = 0 \\ f'_y = 0 \end{cases}$。
>
>由 $f'_y = 0 \implies 2y + 2 = 0 \implies y = -1$。
>
>代入 $f'_x = 0 \implies x + (-1)^2 + 2(-1) + 1 = x = 0$。
>
>唯一驻点为 $(0, -1)$。
>
>[3]计算二阶偏导数判别极值：
>
>$$f''_{xx} = (x + y^2 + 2y + 2)e^x \implies A = f''_{xx}(0, -1) = (0 + 1 - 2 + 2)e^0 = 1 > 0$$
>
>$$f''_{xy} = (2y + 2)e^x \implies B = f''_{xy}(0, -1) = 0$$
>
>$$f''_{yy} = 2e^x \implies C = f''_{yy}(0, -1) = 2$$
>
>$$\Delta = AC - B^2 = 1 \times 2 - 0 = 2 > 0$$
>
>因 $\Delta > 0$ 且 $A > 0$，函数在 $(0, -1)$ 处取得**极小值**，极小值为：
>
>$$f(0, -1) = (0 + 1 - 2)e^0 = -1$$

**习题[13.14]:有界非线性曲线到原点的最长与最短距离**

求平面曲线 $x^3 - xy + y^3 = 1$ ($x \ge 0, y \ge 0$) 上的点到坐标原点 $O(0, 0)$ 的最长距离与最短距离。

主要思路:点到原点距离的平方 $u = x^2 + y^2$ 为目标函数，在约束条件 $\varphi(x, y) = x^3 - xy + y^3 - 1 = 0$ 下利用对称性与拉格朗日乘数法求极值，并比对边界端点值

>[1]构造拉格朗日乘数模型：
>
>求目标函数 $u = x^2 + y^2$ 在约束 $x^3 - xy + y^3 = 1$ ($x \ge 0, y \ge 0$) 下的最值。
>
>构造辅助函数：
>
>$$L(x, y, \lambda) = x^2 + y^2 - \lambda(x^3 - xy + y^3 - 1)$$
>
>偏导数方程为：
>
>$$\begin{cases} L'_x = 2x - \lambda(3x^2 - y) = 0 \\ L'_y = 2y - \lambda(3y^2 - x) = 0 \\ x^3 - xy + y^3 = 1 \end{cases}$$
>
>[2]联立求解驻点：
>
>两式相减：
>
>$$2(x - y) - \lambda[3(x^2 - y^2) + (x - y)] = 0$$
>
>$$(x - y)[2 - \lambda(3x + 3y + 1)] = 0$$
>
>(1) 若 $x = y$：
>
>代入约束方程 $x^3 - x^2 + x^3 = 1 \implies 2x^3 - x^2 - 1 = 0$。
>
>因式分解 $(x - 1)(2x^2 + x + 1) = 0$，解得唯一实根 $x = y = 1$。
>
>此时到原点距离为：
>
>$$d = \sqrt{x^2 + y^2} = \sqrt{1^2 + 1^2} = \sqrt{2}$$
>
>(2) 考察边界端点（截距点）：
>
>当 $x = 0$ 时，代入约束得 $y^3 = 1 \implies y = 1$，点为 $(0, 1)$，距离为 $d = 1$；
>
>当 $y = 0$ 时，代入约束得 $x^3 = 1 \implies x = 1$，点为 $(1, 0)$，距离为 $d = 1$。
>
>[3]比对确定全局最值：
>
>候选距离集合为 $\{\sqrt{2}, 1\}$。
>
>最长距离为 $\sqrt{2}$（在点 $(1, 1)$ 处取得）；
>
>最短距离为 $1$（在边界点 $(1, 0)$ 及 $(0, 1)$ 处取得）。
