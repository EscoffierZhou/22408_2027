# Chap15 微分方程

目的[1]:建立常微分方程（ODE）全局知识图谱，深入理解常微分方程、阶、线性与非线性、解、通解、特解、初始条件及积分曲线的几何与物理本质

目的[2]:熟练掌握一阶微分方程六大经典类型的识别与标准化求解方案（可分离变量、齐次型、平移型、一阶线性微分方程与积分因子、伯努利方程、反函数互换自变量因变量法、全微分方程与势函数求法）

目的[3]:掌握二阶可降阶微分方程三大形态（不显含因变量 $y''=f(x,y')$、不显含自变量 $y''=f(y,y')$、仅含导数 $y''=f(y')$）的降阶代换与完整求解流程

目的[4]:深刻领会高阶线性微分方程解的结构理论（齐次方程解的叠加原理与线性无关性、朗斯基行列式与刘维尔公式、非齐次方程特解叠加定理与解的构造分解）

目的[5]:精通高阶常系数线性齐次方程的特征方程法，以及非齐次方程的经典待定系数法与微分算子法（$D$ 算子与逆算子 $\frac{1}{F(D)}$、指数移位法则、多项式展开、正余弦共振速解）

目的[6]:(仅数学一) 熟练掌握欧拉方程（$x^2 y''+pxy'+qy=f(x)$）的标准化变量代换 $x=\pm\mathrm{e}^t$ 及其降阶化为常系数线性方程的求解技巧

目的[7]:(仅数学一、数学二) 融会贯通微分方程在平面几何（切线与法线、截距、面积、曳物线与追踪曲线）及物理动力学（牛顿第二定律变力变速运动、牛顿冷却定律、阻力滑行与混合液稀释）中的建模与求解

目的[8]:(仅数学三) 掌握函数差分运算规律与一阶常系数线性差分方程的理论、齐次通解、非齐次特解的待定系数设定与初值求解

## 1.微分方程的基本概念与解的分类

###### **概念[1]:微分方程的定义、阶与线性性**

[1]常微分方程的定义：
>含有未知函数、未知函数的导数（或微分）以及自变量的等式，称为<font color=deeppink>常微分方程</font>（Ordinary Differential Equation, ODE）。
>
>若未知函数仅为一个自变量的函数，则称为常微分方程；若含有两个或多个自变量的偏导数，则称为偏微分方程（PDE，考研高数仅在全微分方程与二元极值中略有涉及）。
>
>常微分方程的一般形式为：
>
>$$F(x, y, y', y'', \dots, y^{(n)}) = 0$$

[2]微分方程的“阶”（Order）：
>微分方程中出现的未知函数导数（或微分）的<font color=red>最高阶数</font>，称为该微分方程的阶。
>
>(1) 一阶微分方程：最高导数为一阶，如 $y' + P(x)y = Q(x)$，$(x-y)\mathrm{d}x + x\mathrm{d}y = 0$。
>
>(2) 二阶微分方程：最高导数为二阶，如 $y'' - 2y' + 4y = 0$，$yy'' - \frac{2}{3}(y')^2 = 0$。
>
>(3) $n$ 阶微分方程：最高导数为 $n$ 阶，如 $y^{(4)} - 2y''' + 5y'' = 0$ 为四阶微分方程。

[3]线性微分方程与非线性微分方程：
>若微分方程中未知函数 $y$ 及其各阶导数 $y', y'', \dots, y^{(n)}$ 全为<font color=deeppink>一次有理式</font>，且互不相乘，系数仅为自变量 $x$ 的函数或常数，则称为线性微分方程：
>
>$$a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \dots + a_1(x)y' + a_0(x)y = f(x)$$
>
>若方程中包含因变量或其导数的高次幂（如 $(y')^2$）、乘积项（如 $yy''$）、复合非线性函数（如 $\sin y$、$\mathrm{e}^{y'}$），则为<font color=red>非线性微分方程</font>。

###### **概念[2]:通解、特解、初始条件与积分曲线**

[1]解的定义：
>若将函数 $y = \varphi(x)$ 代入微分方程后恒成立，则称函数 $y = \varphi(x)$ 为该微分方程的解。

[2]通解（General Solution）：
>若微分方程的解中含有任意相互独立的常数 $C_1, C_2, \dots, C_n$，且独立任意常数的个数<font color=red>恰好等于微分方程的阶数 $n$</font>，则称该解为该微分方程的通解。
>
>(1) 必须注意：任意常数必须是本质相互独立的，不能通过代数或指数运算合并。例如 $y = C_1\mathrm{e}^{x+C_2} = (C_1\mathrm{e}^{C_2})\mathrm{e}^x = C\mathrm{e}^x$ 实际上只包含一个独立任意常数，不能作为二阶方程的通解。
>
>(2) 通解不一定涵盖微分方程的全部解。某些由于分离变量除以零而遗漏的解，称为奇解（Singular Solution）。

[3]初始条件与特解（Particular Solution）：
>确定通解中任意常数的定解条件称为<font color=deeppink>初始条件</font>（Initial Condition）。
>
>(1) 一阶方程初始条件：$y(x_0) = y_0$（或记作 $y|_{x=x_0} = y_0$）。
>
>(2) 二阶方程初始条件：$y(x_0) = y_0, y'(x_0) = y_0'$。
>
>(3) $n$ 阶方程初始条件：$y(x_0) = y_0, y'(x_0) = y_0', \dots, y^{(n-1)}(x_0) = y_0^{(n-1)}$。
>
>(4) 依据给定的初始条件确定了任意常数的值之后，得到的完全确定的解称为微分方程的<font color=deeppink>特解</font>。

[4]积分曲线（Integral Curve）：
>微分方程的解 $y = \varphi(x)$ 在平面直角坐标系中对应的平面几何曲线称为微分方程的积分曲线。微分方程的一般解代表了依赖于 $n$ 个参数的积分曲线族；给定初始条件意味着从该曲线族中挑选出穿过特定点且具有特定初斜率的唯一确定曲线。

## 2.一阶微分方程的经典类型与求解策略

###### **题型[1]:可分离变量微分方程**

[1]标准形式：
>形如 $\frac{\mathrm{d}y}{\mathrm{d}x} = f(x)g(y)$ 或 $M_1(x)N_1(y)\mathrm{d}x + M_2(x)N_2(y)\mathrm{d}y = 0$ 的方程，称为可分离变量微分方程。

[2]标准化解法流程：
>当 $g(y) \ne 0$ 时，两端同除以 $g(y)$，分离自变量与因变量：
>
>$$\frac{\mathrm{d}y}{g(y)} = f(x)\mathrm{d}x$$
>
>两边同时不定积分：
>
>$$\int \frac{1}{g(y)}\mathrm{d}y = \int f(x)\mathrm{d}x + C$$
>
>积出原函数后，尽可能化为显式解 $y = \varphi(x, C)$；若难以显化，可保留隐函数形式 $\Phi(x, y) = C$。
>
>必须单独检验令 $g(y) = 0$ 的常数解 $y = y_k$，判断是否包含在通解常数 $C$ 的取值范围内；若不包含，需单独补充说明。

###### **题型[2]:齐次型与平移代换型微分方程**

[1]齐次型微分方程：
>形如 $\frac{\mathrm{d}y}{\mathrm{d}x} = \varphi\left(\frac{y}{x}\right)$ 的微分方程，称为一阶齐次微分方程。
>
>(1) 判别技巧：若方程写为 $M(x, y)\mathrm{d}x + N(x, y)\mathrm{d}y = 0$，且 $M(tx, ty) = t^k M(x, y)$，$N(tx, ty) = t^k N(x, y)$（$M$ 和 $N$ 为同次齐次函数），则恒可化为 $\varphi(y/x)$ 形式。
>
>(2) 核心变量代换：令 $u = \frac{y}{x}$，即 $y = ux$。
>
>两端对 $x$ 求导：
>
>$$\frac{\mathrm{d}y}{\mathrm{d}x} = u + x\frac{\mathrm{d}u}{\mathrm{d}x}$$
>
>代入原方程得：
>
>$$u + x\frac{\mathrm{d}u}{\mathrm{d}x} = \varphi(u) \implies x\frac{\mathrm{d}u}{\mathrm{d}x} = \varphi(u) - u$$
>
>分离变量积分：
>
>$$\frac{\mathrm{d}u}{\varphi(u) - u} = \frac{\mathrm{d}x}{x}$$
>
>求出 $u(x)$ 后，将 $u = \frac{y}{x}$ 回代即得原方程通解。

[2]平移线性变量代换型 $\frac{\mathrm{d}y}{\mathrm{d}x} = f(ax+by+c)$：
>当方程右端依赖于 $x, y$ 的一次线性组合时（$b \ne 0$）：
>
>令复合变量 $u = ax + by + c$，两端对 $x$ 求导：
>
>$$\frac{\mathrm{d}u}{\mathrm{d}x} = a + b\frac{\mathrm{d}y}{\mathrm{d}x} = a + bf(u)$$
>
>立即化为关于 $u(x)$ 的可分离变量方程：
>
>$$\frac{\mathrm{d}u}{a + bf(u)} = \mathrm{d}x$$
>
>积出后回代 $u = ax + by + c$ 即可。

###### **题型[3]:一阶常系数与变系数线性微分方程（积分因子法）**

[1]标准形式：
>形如 $\frac{\mathrm{d}y}{\mathrm{d}x} + P(x)y = Q(x)$ 的方程称为一阶线性微分方程。
>
>当 $Q(x) \equiv 0$ 时，称为一阶齐次线性微分方程；
>
>当 $Q(x) \not\equiv 0$ 时，称为一阶非齐次线性微分方程。

[2]常数变易法与积分因子推导：
>首先解对应的齐次方程 $\frac{\mathrm{d}y}{\mathrm{d}x} + P(x)y = 0 \implies \frac{\mathrm{d}y}{y} = -P(x)\mathrm{d}x$：
>
>$$\ln|y| = -\int P(x)\mathrm{d}x + C_0 \implies y = C\mathrm{e}^{-\int P(x)\mathrm{d}x}$$
>
>应用常数变易法，设非齐次方程的解为 $y = u(x)\mathrm{e}^{-\int P(x)\mathrm{d}x}$，代入非齐次方程：
>
>$$u'(x)\mathrm{e}^{-\int P(x)\mathrm{d}x} - u(x)P(x)\mathrm{e}^{-\int P(x)\mathrm{d}x} + P(x)u(x)\mathrm{e}^{-\int P(x)\mathrm{d}x} = Q(x)$$
>
>化简得 $u'(x) = Q(x)\mathrm{e}^{\int P(x)\mathrm{d}x} \implies u(x) = \int Q(x)\mathrm{e}^{\int P(x)\mathrm{d}x}\mathrm{d}x + C$。

[3]一阶线性微分方程通用通解公式：
>$$y(x) = \mathrm{e}^{-\int P(x)\mathrm{d}x} \left( \int Q(x)\mathrm{e}^{\int P(x)\mathrm{d}x}\mathrm{d}x + C \right)$$
>
>定积分初值形式（满足初值 $y(x_0) = y_0$）：
>
>$$y(x) = \mathrm{e}^{-\int_{x_0}^x P(t)\mathrm{d}t} \left( \int_{x_0}^x Q(t)\mathrm{e}^{\int_{x_0}^t P(s)\mathrm{d}s}\mathrm{d}t + y_0 \right)$$
>
>其中 $\mu(x) = \mathrm{e}^{\int P(x)\mathrm{d}x}$ 称为该方程的<font color=deeppink>积分因子</font>。方程两边同乘以 $\mu(x)$ 后左端恒为全导数 $[\mu(x)y]' = \mu(x)Q(x)$。

###### **题型[4]:伯努利微分方程与非线性变换**

[1]标准形式：
>形如 $\frac{\mathrm{d}y}{\mathrm{d}x} + P(x)y = Q(x)y^n$ ($n \ne 0, 1$) 的方程称为伯努利方程。
>
>注意：当 $n = 0$ 时为一阶线性非齐次方程；当 $n = 1$ 时为一阶齐次线性方程。

[2]降次线性化法：
>两端同时除以 $y^n$：
>
>$$y^{-n}\frac{\mathrm{d}y}{\mathrm{d}x} + P(x)y^{1-n} = Q(x)$$
>
>令新变量 $z = y^{1-n}$，对 $x$ 求导得：
>
>$$\frac{\mathrm{d}z}{\mathrm{d}x} = (1-n)y^{-n}\frac{\mathrm{d}y}{\mathrm{d}x} \implies y^{-n}\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{1-n}\frac{\mathrm{d}z}{\mathrm{d}x}$$
>
>代入原方程后得到关于 $z(x)$ 的一阶线性微分方程：
>
>$$\frac{\mathrm{d}z}{\mathrm{d}x} + (1-n)P(x)z = (1-n)Q(x)$$
>
>按一阶线性公式求出 $z(x)$，最后回代 $z = y^{1-n}$ 即得通解。

###### **题型[5]:互换自变量与因变量法（反函数视角）**

[1]适用场景：
>若方程中关于 $y$ 为高次或非线性，但关于自变量 $x$ 及其微分 $\mathrm{d}x$ 表现为严格的一阶线性形式（或伯努利形式），此时视 $x$ 为因变量、$y$ 为自变量。

[2]导数转换规则：
>$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{1}{\frac{\mathrm{d}x}{\mathrm{d}y}}$$
>
>原方程写为对 $y$ 求导的标准一阶线性方程：
>
>$$\frac{\mathrm{d}x}{\mathrm{d}y} + P(y)x = Q(y)$$
>
>其通解公式为：
>
>$$x(y) = \mathrm{e}^{-\int P(y)\mathrm{d}y} \left( \int Q(y)\mathrm{e}^{\int P(y)\mathrm{d}y}\mathrm{d}y + C \right)$$

###### **题型[6]:全微分方程与积分因子（势函数与格林公式切入）**

[1]全微分方程定义与判别：
>对于一阶微分方程 $P(x, y)\mathrm{d}x + Q(x, y)\mathrm{d}y = 0$，若存在二元可微函数 $u(x, y)$，使得：
>
>$$\mathrm{d}u(x, y) = P(x, y)\mathrm{d}x + Q(x, y)\mathrm{d}y$$
>
>则该方程称为<font color=deeppink>全微分方程</font>（恰当方程），其通解显为 $u(x, y) = C$。
>
>在单连通域内，全微分方程的充要条件为：
>
>$$\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

[2]原函数（势函数）$u(x, y)$ 的求解方案：
>(1) **分项组合凑全微分法**：利用常用全微分组合公式：
>
>$$x\mathrm{d}y + y\mathrm{d}x = \mathrm{d}(xy), \quad \frac{x\mathrm{d}y - y\mathrm{d}x}{x^2} = \mathrm{d}\left(\frac{y}{x}\right), \quad \frac{x\mathrm{d}y - y\mathrm{d}x}{x^2+y^2} = \mathrm{d}\left(\arctan\frac{y}{x}\right)$$
>
>(2) **折线积分法（路径无关性）**：
>
>$$u(x, y) = \int_{x_0}^x P(t, y_0)\mathrm{d}t + \int_{y_0}^y Q(x, t)\mathrm{d}t = C$$
>
>(3) **偏积分求偏导法**：
>
>$$u(x, y) = \int P(x, y)\mathrm{d}x + \varphi(y)$$
>
>再令 $\frac{\partial u}{\partial y} = Q(x, y)$ 反解出 $\varphi(y)$。

## 3.二阶可降阶微分方程的化简体系

###### **题型[1]:不显含因变量 $y$ 的方程 $y''=f(x, y')$**

[1]降阶代换法则：
>方程特征：方程中只含有自变量 $x$ 及导数 $y', y''$，缺少未知函数 $y$ 本身。
>
>代换公式：
>
>$$p = y' = \frac{\mathrm{d}y}{\mathrm{d}x}, \quad y'' = p' = \frac{\mathrm{d}p}{\mathrm{d}x}$$
>
>原方程化为关于自变量 $x$、因变量 $p$ 的一阶微分方程：
>
>$$\frac{\mathrm{d}p}{\mathrm{d}x} = f(x, p)$$
>
>解此一阶方程求出 $p = \varphi(x, C_1)$，再作一次不定积分即得最终通解：
>
>$$y = \int \varphi(x, C_1)\mathrm{d}x + C_2$$

###### **题型[2]:不显含自变量 $x$ 的方程 $y''=f(y, y')$**

[1]降阶代换法则：
>方程特征：方程中只含有因变量 $y$ 及导数 $y', y''$，缺少自变量 $x$。
>
>代换公式（利用复合函数链式求导法，视 $y$ 为新自变量）：
>
>$$p = y' = \frac{\mathrm{d}y}{\mathrm{d}x}, \quad y'' = \frac{\mathrm{d}p}{\mathrm{d}x} = \frac{\mathrm{d}p}{\mathrm{d}y}\cdot\frac{\mathrm{d}y}{\mathrm{d}x} = p\frac{\mathrm{d}p}{\mathrm{d}y}$$
>
>原方程化为关于自变量 $y$、因变量 $p$ 的一阶微分方程：
>
>$$p\frac{\mathrm{d}p}{\mathrm{d}y} = f(y, p)$$
>
>解此方程求得 $p = \psi(y, C_1)$。
>
>由于 $p = \frac{\mathrm{d}y}{\mathrm{d}x}$，分离变量：
>
>$$\frac{\mathrm{d}y}{\psi(y, C_1)} = \mathrm{d}x \implies \int \frac{\mathrm{d}y}{\psi(y, C_1)} = x + C_2$$

###### **题型[3]:仅显含导数项 $y''=f(y')$**

[1]降阶策略：
>此类型既不含 $x$ 也不含 $y$，既可以令 $y'' = \frac{\mathrm{d}p}{\mathrm{d}x}$ 对 $x$ 求解，也可以令 $y'' = p\frac{\mathrm{d}p}{\mathrm{d}y}$ 对 $y$ 求解。通常优先选用 $\frac{\mathrm{d}p}{\mathrm{d}x} = f(p)$ 直接分离变量积分。

## 4.高阶线性微分方程的解的结构理论

###### **理论[1]:齐次线性微分方程解的线性相关性与朗斯基行列式**

[1]线性齐次微分方程的标准形式：
>$$y^{(n)} + a_1(x)y^{(n-1)} + \dots + a_{n-1}(x)y' + a_n(x)y = 0$$

[2]线性无关与朗斯基行列式（Wronskian）：
>若函数组 $y_1(x), y_2(x), \dots, y_n(x)$ 为该方程的 $n$ 个解，其朗斯基行列式定义为：
>
>$$W(x) = W[y_1, y_2, \dots, y_n](x) = \begin{vmatrix} y_1 & y_2 & \dots & y_n \\ y_1' & y_2' & \dots & y_n' \\ \vdots & \vdots & \ddots & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \dots & y_n^{(n-1)} \end{vmatrix}$$
>
>(1) **刘维尔公式（Liouville-Ostrogradski Formula）**：
>
>$$W(x) = W(x_0)\exp\left(-\int_{x_0}^x a_1(t)\mathrm{d}t\right)$$
>
>(2) **判别准则**：在区间 $I$ 上，微分方程的解组 $y_1, \dots, y_n$ 线性无关的充要条件是在该区间上任意一点 $x_0 \in I$ 处 $W(x_0) \ne 0$（要么处处不为零，要么恒等于零）。

[3]齐次方程通解构造定理：
>若 $y_1(x), y_2(x), \dots, y_n(x)$ 是 $n$ 阶齐次线性微分方程的 $n$ 个线性无关解（基础解系），则该方程的通解为：
>
>$$Y(x) = C_1 y_1(x) + C_2 y_2(x) + \dots + C_n y_n(x)$$
>
>其中 $C_1, C_2, \dots, C_n$ 为任意常数。

###### **理论[2]:非齐次线性微分方程解的叠加原理与结构分解定理**

[1]非齐次方程解的结构定理：
>设 $y^*(x)$ 是非齐次线性微分方程：
>
>$$y^{(n)} + a_1(x)y^{(n-1)} + \dots + a_n(x)y = f(x)$$
>
>的一个已知特解，而 $Y(x) = \sum\limits_{i=1}^n C_i y_i(x)$ 是对应齐次方程的通解，则非齐次微分方程的全部通解为：
>
>$$y(x) = Y(x) + y^*(x) = C_1 y_1(x) + C_2 y_2(x) + \dots + C_n y_n(x) + y^*(x)$$

[2]特解叠加原理：
>若方程的右端自由项可分解为若干项之和 $f(x) = f_1(x) + f_2(x)$，且 $y_1^*(x)$ 与 $y_2^*(x)$ 分别为右端为 $f_1(x)$ 与 $f_2(x)$ 时的特解，则：
>
>$$y^*(x) = y_1^*(x) + y_2^*(x)$$
>
>即为原非齐次方程的一个特解。

[3]解的线性组合重要推论（反求通解与齐次特解）：
>(1) 设 $y_1, y_2, y_3$ 为二阶非齐次线性微分方程的三个互不相同的特解，则：
>
>$$\bar{y}_1 = y_1 - y_3, \quad \bar{y}_2 = y_2 - y_3$$
>
>恒为对应齐次方程的两个解；若 $\bar{y}_1, \bar{y}_2$ 线性无关，则原方程通解为：
>
>$$y = C_1(y_1 - y_3) + C_2(y_2 - y_3) + y_3$$
>
>(2) 一般组合法则：$\lambda_1 y_1 + \lambda_2 y_2 + \dots + \lambda_k y_k$ 是非齐次方程的解 $\iff \sum\limits_{i=1}^k \lambda_i = 1$；当 $\sum\limits_{i=1}^k \lambda_i = 0$ 时，该线性组合必为对应齐次方程的解。

## 5.高阶常系数线性微分方程的解析解法

###### **题型[1]:常系数齐次线性微分方程与特征方程法**

[1]二阶常系数齐次方程 $y'' + py' + qy = 0$：
>代入试验解 $y = \mathrm{e}^{rx}$，得到对应的<font color=deeppink>特征方程</font>：
>
>$$r^2 + pr + q = 0$$
>
>特征根判别式 $\Delta = p^2 - 4q$，解的情形分类：
>
>(1) **两个不相等的实根** $r_1 \ne r_2$（$\Delta > 0$）：
>
>$$y = C_1\mathrm{e}^{r_1 x} + C_2\mathrm{e}^{r_2 x}$$
>
>(2) **两个相等的实根** $r_1 = r_2 = r$（$\Delta = 0$）：
>
>$$y = (C_1 + C_2 x)\mathrm{e}^{rx}$$
>
>(3) **一对共轭复根** $r_{1,2} = \alpha \pm \beta i$（$\Delta < 0$）：
>
>$$y = \mathrm{e}^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)$$

[2]$n$ 阶常系数齐次线性微分方程的通解构造：
>特征方程 $P_n(r) = r^n + a_1 r^{n-1} + \dots + a_n = 0$：
>
>(1) 单实根 $r$：贡献基础解 $\mathrm{e}^{rx}$。
>
>(2) $k$ 重实根 $r$：贡献 $k$ 个线性无关解 $\mathrm{e}^{rx}, x\mathrm{e}^{rx}, x^2\mathrm{e}^{rx}, \dots, x^{k-1}\mathrm{e}^{rx}$。
>
>(3) 单对共轭复根 $\alpha \pm \beta i$：贡献两个解 $\mathrm{e}^{\alpha x}\cos\beta x, \mathrm{e}^{\alpha x}\sin\beta x$。
>
>(4) $k$ 重共轭复根 $\alpha \pm \beta i$：贡献 $2k$ 个线性无关解：
>
>$$\mathrm{e}^{\alpha x}\cos\beta x, x\mathrm{e}^{\alpha x}\cos\beta x, \dots, x^{k-1}\mathrm{e}^{\alpha x}\cos\beta x$$
>
>$$\mathrm{e}^{\alpha x}\sin\beta x, x\mathrm{e}^{\alpha x}\sin\beta x, \dots, x^{k-1}\mathrm{e}^{\alpha x}\sin\beta x$$

###### **题型[2]:常系数非齐次线性微分方程的待定系数法**

[1]第一类自由项：$f(x) = P_m(x)\mathrm{e}^{\lambda x}$
>特解形式设定为：
>
>$$y^*(x) = x^k Q_m(x)\mathrm{e}^{\lambda x}$$
>
>其中：
>- $Q_m(x) = b_m x^m + b_{m-1}x^{m-1} + \dots + b_1 x + b_0$ 为与 $P_m(x)$ 同次的待定多项式；
>- $k$ 为实数 $\lambda$ 作为特征方程根的重数：
>  - 若 $\lambda$ 不是特征根，则 $k = 0$；
>  - 若 $\lambda$ 是单特征根，则 $k = 1$；
>  - 若 $\lambda$ 是二重特征根，则 $k = 2$。

[2]第二类自由项：$f(x) = \mathrm{e}^{\alpha x}[P_l(x)\cos\beta x + P_n(x)\sin\beta x]$
>特解形式设定为：
>
>$$y^*(x) = x^k \mathrm{e}^{\alpha x}[Q_m^{(1)}(x)\cos\beta x + Q_m^{(2)}(x)\sin\beta x]$$
>
>其中：
>- $m = \max\{l, n\}$，$Q_m^{(1)}(x)$ 与 $Q_m^{(2)}(x)$ 是两个独立的 $m$ 次待定多项式；
>- $k$ 为复数 $\alpha + \beta i$ 作为特征方程根的重数：
>  - 若 $\alpha + \beta i$ 不是特征根，则 $k = 0$；
>  - 若 $\alpha + \beta i$ 是特征方程的单根，则 $k = 1$。

###### **题型[3]:常系数非齐次微分方程的微分算子法（$D$ 算子速解）**

[1]微分算子与逆算子定义：
>记微分算子 $D = \frac{\mathrm{d}}{\mathrm{d}x}$，$D^k = \frac{\mathrm{d}^k}{\mathrm{d}x^k}$，微分多项式 $F(D) = D^n + a_1 D^{n-1} + \dots + a_n$。
>
>微分方程记为 $F(D)y = f(x)$，特解形式记为：
>
>$$y^* = \frac{1}{F(D)}f(x)$$

[2]算子计算四大金科玉律：
>(1) **指数法则**：若 $F(\lambda) \ne 0$，则：
>
>$$\frac{1}{F(D)}\mathrm{e}^{\lambda x} = \frac{1}{F(\lambda)}\mathrm{e}^{\lambda x}$$
>
>(2) **指数移位法则（$D$-Shift Theorem）**：
>
>$$\frac{1}{F(D)}\left[\mathrm{e}^{\lambda x} v(x)\right] = \mathrm{e}^{\lambda x} \frac{1}{F(D + \lambda)} v(x)$$
>
>当 $F(\lambda) = 0$ 时，设 $F(D) = (D-\lambda)^k G(D)$ 且 $G(\lambda) \ne 0$，则：
>
>$$\frac{1}{F(D)}\mathrm{e}^{\lambda x} = \mathrm{e}^{\lambda x}\frac{1}{(D)^k G(D+\lambda)} 1 = \mathrm{e}^{\lambda x}\frac{1}{G(\lambda)}\frac{x^k}{k!}$$
>
>(3) **正余弦法则**：若 $F(-a^2) \ne 0$，则：
>
>$$\frac{1}{F(D^2)}\sin ax = \frac{1}{F(-a^2)}\sin ax, \quad \frac{1}{F(D^2)}\cos ax = \frac{1}{F(-a^2)}\cos ax$$
>
>(4) **多项式长除展开法则**：求 $\frac{1}{F(D)}P_m(x)$ 时，将 $\frac{1}{F(D)}$ 按 $D$ 的升幂进行 Taylor 展开至 $D^m$ 项，直接作用于多项式。

## 6.欧拉方程（变系数常态化化简，仅数学一）

###### **理论[1]:欧拉方程的标准型与换元原理**

[1]标准型定义：
>形如：
>
>$$x^n y^{(n)} + p_1 x^{n-1} y^{(n-1)} + \dots + p_{n-1} x y' + p_n y = f(x)$$
>
>的方程称为欧拉方程（Euler Equation），其系数特点为未知函数的 $k$ 阶导数项前乘着自变量的 $k$ 次幂 $x^k$。

[2]对数自变量换元法：
>当 $x > 0$ 时，令 $x = \mathrm{e}^t$（即 $t = \ln x$）；当 $x < 0$ 时，令 $x = -\mathrm{e}^t$（即 $t = \ln(-x)$）。
>
>以 $x > 0$ 为例，根据链式法则推导导数变换公式：
>
>(1) 一阶导数：
>
>$$\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t} \implies x\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}t}$$
>
>(2) 二阶导数：
>
>$$\frac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \frac{\mathrm{d}}{\mathrm{d}x}\left(\frac{1}{x}\frac{\mathrm{d}y}{\mathrm{d}t}\right) = -\frac{1}{x^2}\frac{\mathrm{d}y}{\mathrm{d}t} + \frac{1}{x}\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}y}{\mathrm{d}t}\right)\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{1}{x^2}\left(\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t}\right)$$
>
>$$x^2\frac{\mathrm{d}^2 y}{\mathrm{d}x^2} = \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t}$$
>
>(3) 记微分算子 $D_t = \frac{\mathrm{d}}{\mathrm{d}t}$，则：
>
>$$x^k y^{(k)} = D_t(D_t - 1)(D_t - 2)\dots(D_t - k + 1)y$$
>
>代入原方程后，$x$ 的幂次与分母的导数乘子恰好完全抵消，方程蜕化为以 $t$ 为自变量的<font color=red>常系数线性微分方程</font>。
>
>求出 $y(t)$ 后，务必牢记用 $t = \ln|x|$ 将自变量回代为 $x$。

## 7.微分方程的几何与物理建模应用（仅数学一、数学二）

###### **应用[1]:几何应用——切线法线、面积截距与曳物线（追踪问题）**

[1]切线与法线方程的微分表达式：
>设曲线 $y = y(x)$ 上任意一点为 $M(x, y)$，切线斜率为 $y'$。
>
>(1) 切线方程：$Y - y = y'(X - x)$。
>- 切线在 $X$ 轴上的截距：令 $Y = 0 \implies X_T = x - \frac{y}{y'}$；
>- 切线在 $Y$ 轴上的截距：令 $X = 0 \implies Y_T = y - xy'$。
>
>(2) 法线方程：$Y - y = -\frac{1}{y'}(X - x)$。
>- 法线在 $X$ 轴上的截距：令 $Y = 0 \implies X_N = x + y y'$；
>- 法线在 $Y$ 轴上的截距：令 $X = 0 \implies Y_N = y + \frac{x}{y'}$。

[2]追踪曲线（曳物线 Tractrix）数学建模：
>当牵引点 $P(0, Y)$ 沿着某直线（如 $y$ 轴）运动，被牵引质点 $Q(x, y)$ 与 $P$ 之间的距离始终保持恒定长度 $L$（即 $|PQ| = L$），且绳索始终处于拉直状态（即 $QP$ 方向永远指向曲线在点 $Q$ 处的切线切向）：
>
>$$x^2 + (y - Y)^2 = L^2 \implies y - Y = -\sqrt{L^2 - x^2}$$
>
>由于切线斜率满足 $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{y - Y}{x}$，立即导出经典的曳物线微分方程：
>
>$$\frac{\mathrm{d}y}{\mathrm{d}x} = -\frac{\sqrt{L^2 - x^2}}{x}$$
>
>通过三角换元 $x = L\sin t$ 积分可得完整轨迹方程。

###### **应用[2]:物理应用——变力牛顿动力学、牛顿冷却定律与变化率模型**

[1]牛顿第二定律与三种加速度表达转换：
>质点质量为 $m$，合外力为 $F$，由牛顿第二定律 $F = ma$：
>
>(1) **位移-时间模型**：若外力为时间或位置的函数，$a = \frac{\mathrm{d}^2 x}{\mathrm{d}t^2} \implies m\frac{\mathrm{d}^2 x}{\mathrm{d}t^2} = F$。
>
>(2) **速度-时间模型**：若外力为速度与时间的函数，$a = \frac{\mathrm{d}v}{\mathrm{d}t} \implies m\frac{\mathrm{d}v}{\mathrm{d}t} = F(t, v)$。
>
>(3) **速度-位移模型**：利用复合函数链式求导法消去时间参数 $t$：
>
>$$a = \frac{\mathrm{d}v}{\mathrm{d}t} = \frac{\mathrm{d}v}{\mathrm{d}x}\cdot\frac{\mathrm{d}x}{\mathrm{d}t} = v\frac{\mathrm{d}v}{\mathrm{d}x} \implies mv\frac{\mathrm{d}v}{\mathrm{d}x} = F(x, v)$$
>
>此转换是处理滑行阻力、制动距离等考研题目的核心破题利器。

[2]牛顿冷却定律（Newton's Law of Cooling）：
>温度为 $T(t)$ 的物体置于恒温为 $T_0$ 的介质中，物体温度的变化率与该时刻物体和介质的温差成正比：
>
>$$\frac{\mathrm{d}T}{\mathrm{d}t} = -k(T - T_0) \quad (k > 0)$$
>
>式中负号代表当物体温度高于环境温度（$T > T_0$）时，温度随时间衰减（$\frac{\mathrm{d}T}{\mathrm{d}t} < 0$）。
>
>分离变量积分可得指数衰减解：
>
>$$T(t) = T_0 + (T(0) - T_0)\mathrm{e}^{-kt}$$

[3]容器变浓度混合液体模型：
>设容器容积为 $V$，原有溶质质量为 $Q_0$。浓度为 $c_{in}$ 的溶液以流速 $r_{in}$ 流入容器，充分混合后以流速 $r_{out}$ 流出。
>
>在微小时间段 $[t, t+\mathrm{d}t]$ 内建立溶质质量微元守恒方程：
>
>$$\mathrm{d}Q = (\text{流入量}) - (\text{流出量}) = c_{in} r_{in}\mathrm{d}t - \frac{Q(t)}{V(t)} r_{out}\mathrm{d}t$$
>
>从而导出关于溶质质量 $Q(t)$ 的一阶线性微分方程。

## 8.一阶常系数线性差分方程（仅数学三）

###### **理论[1]:差分的定义与基本性质**

[1]差分的定义：
>设离散函数（数列）为 $y_t = f(t)$（$t = 0, 1, 2, \dots$）：
>
>(1) 一阶差分：
>
>$$\Delta y_t = y_{t+1} - y_t$$
>
>(2) 二阶差分：
>
>$$\Delta^2 y_t = \Delta(\Delta y_t) = \Delta y_{t+1} - \Delta y_t = (y_{t+2} - y_{t+1}) - (y_{t+1} - y_t) = y_{t+2} - 2y_{t+1} + y_t$$

[2]差分的基本运算性质：
>与微分运算完全对偶：
>
>(1) 线性性质：$\Delta(a y_t + b z_t) = a\Delta y_t + b\Delta z_t$。
>
>(2) 幂函数差分：$\Delta(t) = 1$。
>
>(3) 指数函数差分：$\Delta(a^t) = a^{t+1} - a^t = (a - 1)a^t$。

###### **题型[1]:一阶常系数线性差分方程的通解与特解确定法**

[1]标准形式：
>$$y_{t+1} + ay_t = f(t) \quad (a \ne 0 \text{ 为常数})$$

[2]齐次差分方程 $y_{t+1} + ay_t = 0$ 的通解：
>设试探解为 $y_t = \lambda^t$，代入得特征方程：
>
>$$\lambda + a = 0 \implies \lambda = -a$$
>
>齐次通解为：
>
>$$y_c(t) = C(-a)^t \quad (C \text{ 为任意常数})$$

[3]非齐次方程特解 $y_t^*$ 的待定形式规则表：
>总通解结构为：$y_t = y_c(t) + y_t^* = C(-a)^t + y_t^*$。
>
>(1) **当自由项为 $f(t) = d^t P_m(t)$ 时**：
>- 若 $a + d \ne 0$（即 $d \ne -a$，$d$ 不是特征根），设特解为：
>  $$y_t^* = d^t Q_m(t)$$
>- 若 $a + d = 0$（即 $d = -a$，$d$ 为特征根），设特解为：
>  $$y_t^* = t\cdot d^t Q_m(t)$$
>  其中 $Q_m(t)$ 为与 $P_m(t)$ 同阶的待定多项式。
>
>(2) **当自由项为 $f(t) = b_1\cos\omega t + b_2\sin\omega t$ 时**：
>构造判别行列式：
>
>$$D = \begin{vmatrix} a + \cos\omega & \sin\omega \\ -\sin\omega & a + \cos\omega \end{vmatrix} = (a + \cos\omega)^2 + \sin^2\omega = a^2 + 2a\cos\omega + 1$$
>
>- 若 $D \ne 0$，设特解为：
>  $$y_t^* = \alpha\cos\omega t + \beta\sin\omega t$$
>- 若 $D = 0$，设特解为：
>  $$y_t^* = t(\alpha\cos\omega t + \beta\sin\omega t)$$
>  其中 $\alpha, \beta$ 为待定实常数。
