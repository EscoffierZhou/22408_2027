# Chap11 一元积分学的应用(积分等式和积分不等式)

目的[1]:深刻理解定积分中值定理与广义定积分中值定理的严格柯西中值定理证明，厘清连续型介值定理联用机理与中值依赖性 $\xi = \xi(x), \xi = \xi(n)$ 的易错陷阱

目的[2]:熟练掌握变限积分与导数中值定理（罗尔、拉格朗日、柯西）的深度嵌套转化体系，掌握多点导数符号判别与二阶中值定理综合推导

目的[3]:融会贯通积分等式证明的五大王牌技巧（辅助函数构建法、两端求导微分方程法、变上限积分变换法、泰勒展开内插积分法、分部积分降阶消项法）

目的[4]:系统掌握夹逼准则求积分极限的核心技术路线（函数有界放缩、局部多项式放缩、周期跳跃间断点阶梯放缩）与普遍性定理 $\lim\limits_{n\to\infty} \int_a^b x^n f(x)\,\mathrm{d}x = 0$

目的[5]:彻底掌握积分不等式证明的四大神技（构造辅助函数求导单调性法、被积函数局部放缩法与切线不等式、柯西-施瓦茨积分不等式、变量代换对称消除法）

目的[6]:建立从定积分基本性质、牛顿-莱布尼茨公式到绝对值积分估计与能量积分控制的完整考研解题方法论

## 1.积分中值定理体系及其深度推导

###### **定理[1]:第一定积分中值定理与连续介值性**

设函数 $f(x)$ 在闭区间 $[a, b]$ 上连续，则在 $[a, b]$ 上至少存在一点 $\xi \in [a, b]$，使得：

$$\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$$

若进一步加强条件，可以证明至少存在一点 $\xi \in (a, b)$（开区间）满足上式。

[1]闭区间存在性的介值定理证明：
>因为 $f(x)$ 在闭区间 $[a, b]$ 上连续，由闭区间上连续函数的极值定理，必存在最大值 $M$ 与最小值 $m$：
>
>$$m \leqslant f(x) \leqslant M, \quad \forall x \in [a, b]$$
>
>由定积分的保号性与保序性，两边在 $[a, b]$ 上积分得：
>
>$$\int_a^b m\,\mathrm{d}x \leqslant \int_a^b f(x)\,\mathrm{d}x \leqslant \int_a^b M\,\mathrm{d}x$$
>
>即：
>
>$$m(b-a) \leqslant \int_a^b f(x)\,\mathrm{d}x \leqslant M(b-a)$$
>
>由于 $b > a$，两边同除以 $(b-a)$：
>
>$$m \leqslant \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x \leqslant M$$
>
>根据闭区间上连续函数的介值定理，函数 $f(x)$ 必能取到介于最小值 $m$ 与最大值 $M$ 之间的任何实数。因此，必存在某个 $\xi \in [a, b]$，使得：
>
>$$f(\xi) = \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x$$
>
>即 $\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$。

[2]开区间内点存在性的微分中值定理证明：
>若要求 $\xi \in (a, b)$，可构造变上限积分函数：
>
>$$F(x) = \int_a^x f(t)\,\mathrm{d}t, \quad x \in [a, b]$$
>
>因为 $f(t)$ 连续，所以 $F(x)$ 在 $[a, b]$ 上连续，在 $(a, b)$ 内可导，且 $F'(x) = f(x)$。
>
>在闭区间 $[a, b]$ 上对 $F(x)$ 应用拉格朗日中值定理，必存在 $\xi \in (a, b)$，使得：
>
>$$\frac{F(b) - F(a)}{b - a} = F'(\xi)$$
>
>将 $F(a) = 0, F(b) = \int_a^b f(x)\,\mathrm{d}x, F'(\xi) = f(\xi)$ 代入，即得：
>
>$$\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a), \quad \xi \in (a, b)$$

###### **定理[2]:广义积分中值定理（加权中值定理）与柯西中值定理推导**

设函数 $f(x), g(x)$ 在闭区间 $[a, b]$ 上连续，且权函数 $g(x)$ 在 $[a, b]$ 上不变号（即恒有 $g(x) \geqslant 0$ 或恒有 $g(x) \leqslant 0$），则至少存在一点 $\xi \in (a, b)$，使得：

$$\int_a^b f(x)g(x)\,\mathrm{d}x = f(\xi)\int_a^b g(x)\,\mathrm{d}x$$

[1]柯西中值定理的标准证明：
>(1) **退化情形**：
>
>若 $g(x) \equiv 0$，则两边均为 0，等式对任意 $\xi \in (a, b)$ 恒成立。
>
>(2) **非退化情形**：
>
>若 $g(x) \not\equiv 0$，不妨设 $g(x) \geqslant 0$ 且存在点使 $g(x) > 0$。由连续函数积分性质可知：
>
>$$\int_a^b g(x)\,\mathrm{d}x > 0$$
>
>构造两个变上限辅助函数：
>
>$$F(x) = \int_a^x f(t)g(t)\,\mathrm{d}t, \quad G(x) = \int_a^x g(t)\,\mathrm{d}t$$
>
>易知 $F(x), G(x)$ 在 $[a, b]$ 上连续，在 $(a, b)$ 内可导，且导函数分别为：
>
>$$F'(x) = f(x)g(x), \quad G'(x) = g(x)$$
>
>在 $[a, b]$ 上对 $F(x)$ 与 $G(x)$ 应用柯西中值定理，存在 $\xi \in (a, b)$，使得：
>
>$$\frac{F(b) - F(a)}{G(b) - G(a)} = \frac{F'(\xi)}{G'(\xi)}$$
>
>将两端展开：
>
>$$\frac{\int_a^b f(x)g(x)\,\mathrm{d}x - 0}{\int_a^b g(x)\,\mathrm{d}x - 0} = \frac{f(\xi)g(\xi)}{g(\xi)} = f(\xi)$$
>
>两边同乘以 $\int_a^b g(x)\,\mathrm{d}x$，即证得：
>
>$$\int_a^b f(x)g(x)\,\mathrm{d}x = f(\xi)\int_a^b g(x)\,\mathrm{d}x, \quad \xi \in (a, b)$$

[2]广义积分中值定理与第一中值定理的关系：
>当在广义中值定理中取特例权函数 $g(x) \equiv 1$ 时，$\int_a^b g(x)\,\mathrm{d}x = b - a$，立即退化为第一积分中值定理。因此广义积分中值定理是其高维推广。考研大题中，广义积分中值定理可以直接作为公理化定理使用。

###### **辨析[1]:积分中值的依赖性与极限陷阱**

在涉及中值的积分极限与渐近分析中，必须高度警惕中值对自变量与参数的依赖关系：

[1]区间变动时中值的动态性：
>若考虑积分 $\int_a^x f(t)\,\mathrm{d}t = f(\xi)(x - a)$，当上限 $x$ 改变时，中值 $\xi$ 必然随着 $x$ 的变化而变化，即 $\xi = \xi(x)$。
>
>当 $x \to a$ 时，由挤压原理 $a < \xi(x) < x$ 可知 $\lim\limits_{x \to a}\xi(x) = a$。

[2]被积函数含参数 $n$ 时中值的动态性：
>在积分 $\int_a^b f_n(x)\,\mathrm{d}x = f_n(\xi_n)(b-a)$ 中，中值 $\xi_n$ 随着正整数 $n$ 的变动而变动，即 $\xi_n = \xi(n)$。
>
>致命易错点：对于积分 $\int_1^2 \mathrm{e}^{-x^n}\,\mathrm{d}x = \mathrm{e}^{-\xi_n^n}(2-1) = \mathrm{e}^{-\xi_n^n}$，虽然 $1 < \xi_n < 2$，但由于我们完全不知道序列 $\xi_n$ 逼近 1 的收敛速度，**绝对不能**主观臆断 $\lim\limits_{n\to\infty}\mathrm{e}^{-\xi_n^n} = 0$！必须使用被积函数放缩法与夹逼准则严格求解。

###### **模型[1]:变限积分中值与微分中值定理的嵌套转化链**

考研高分核心大题往往将“积分中值定理”作为第一层踏板，将“微分中值定理（罗尔、拉格朗日、柯西）”作为第二层或第三层推导工具，形成链式推理：

[1]“积出一值，再寻多导”转化模式：
>给定包含积分的等式条件（如 $\int_a^b f(x)g(x)\,\mathrm{d}x = C$），先利用积分中值定理求出区间内某点 $\eta \in (a, b)$ 处的函数值 $f(\eta)$。
>
>将点 $\eta$ 与原题中给定的端点值（如 $f(a), f(b)$）相组合：
>(1) **若三点函数值相等**（$f(a) = f(\eta) = f(b)$）：在 $[a, \eta]$ 和 $[\eta, b]$ 上分别使用罗尔定理，得到两导数零点 $f'(\xi_1) = f'(\xi_2) = 0$，再对 $f'(x)$ 在 $[\xi_1, \xi_2]$ 上使用罗尔定理，即得二阶导数零点 $f''(\xi) = 0$。
>(2) **若三点函数值不等**：分别在两段小区间上使用拉格朗日中值定理得到不同符号的导数值 $f'(\xi_1) > 0, f'(\xi_2) < 0$，再次对导函数应用拉格朗日中值定理，推导出二阶导数符号 $f''(\xi) < 0$。

## 2.积分极限与夹逼准则核心解题法

###### **方法[1]:夹逼准则求定积分极限的标准三部曲**

当待求极限为 $\lim\limits_{n\to\infty}\int_a^b f(x, n)\,\mathrm{d}x$ 或 $\lim\limits_{x\to+\infty}\frac{1}{x}\int_0^x f(t)\,\mathrm{d}t$ 时，若无法直接写出原函数，夹逼准则为最核心武器。

[1]标准三步法实施流程：
>(1) **局部不等式放缩**：利用被积函数在积分区间上的单调性、最值、初等不等式（如 $\mathrm{e}^u \geqslant 1+u$、$\ln(1+u) \leqslant u$、$|\sin u| \leqslant |u|$）建立被积函数的上下夹逼界：
>
>$$\phi_n(x) \leqslant f(x, n) \leqslant \psi_n(x), \quad \forall x \in [a, b]$$
>
>(2) **逐项积分求值**：利用定积分的保序性两端同时积分：
>
>$$\int_a^b \phi_n(x)\,\mathrm{d}x \leqslant \int_a^b f(x, n)\,\mathrm{d}x \leqslant \int_a^b \psi_n(x)\,\mathrm{d}x$$
>
>(3) **两端取极限锁定**：若 $\lim\limits_{n\to\infty}\int_a^b \phi_n(x)\,\mathrm{d}x = \lim\limits_{n\to\infty}\int_a^b \psi_n(x)\,\mathrm{d}x = L$，则原积分极限必为 $L$。

###### **定理[3]:多项式乘积型积分极限的普遍收敛定理**

设函数 $f(x)$ 在 $[0, 1]$ 上连续，则恒有：

$$\lim_{n\to\infty}\int_0^1 x^n f(x)\,\mathrm{d}x = 0$$

[1]定理的严格证明：
>因为 $f(x)$ 在闭区间 $[0, 1]$ 上连续，必存在有界常数 $M = \max\limits_{0\leqslant x\leqslant 1}|f(x)|$。
>
>由定积分绝对值不等式与保号性：
>
>$$\left|\int_0^1 x^n f(x)\,\mathrm{d}x\right| \leqslant \int_0^1 |x^n f(x)|\,\mathrm{d}x \leqslant M\int_0^1 x^n\,\mathrm{d}x = M\left[\frac{x^{n+1}}{n+1}\right]_0^1 = \frac{M}{n+1}$$
>
>当 $n \to \infty$ 时，$\lim\limits_{n\to\infty}\frac{M}{n+1} = 0$。由夹逼定理知：
>
>$$\lim_{n\to\infty}\int_0^1 x^n f(x)\,\mathrm{d}x = 0$$

###### **方法[2]:含周期/跳跃间断点函数的积分极限处理技术**

对于含有取整函数（如 $f(x) = x - [x]$）、方波等具有跳跃间断点的被积函数，由于不满足洛必达法则对导数存在性的要求，必须借助整数分段夹逼：

[1]整数阶梯夹逼法：
>设 $x \to +\infty$，设整数 $n = [x]$，则有 $n \leqslant x < n+1$。
>
>(1) **分母单调放缩**：$\frac{1}{n+1} < \frac{1}{x} \leqslant \frac{1}{n}$；
>
>(2) **分子面积累加**：根据函数周期性 $T = 1$，
>
>$$\int_0^n f(t)\,\mathrm{d}t \leqslant \int_0^x f(t)\,\mathrm{d}t < \int_0^{n+1} f(t)\,\mathrm{d}t$$
>
>其中 $\int_0^n f(t)\,\mathrm{d}t = n\int_0^1 f(t)\,\mathrm{d}t$。
>
>(3) **不等式同向相乘**：两边不等式各项均为正，相乘得到上下界，当 $n \to \infty$ 时两端极限一致，从而定出积分平均极限值。

## 3.积分等式证明的五大王牌方法

###### **方法[3]:辅助函数与零点定理/罗尔定理法**

[1]移项作差构建原函数：
>若要证明形如 $\int_a^b f(x)\,\mathrm{d}x = g(\xi)$ 的等式，常将目标中的常数或中值点抽象为自变量 $x$：
>
>$$H(x) = \int_a^x f(t)\,\mathrm{d}t - G(x)$$
>
>检验端点值 $H(a), H(b)$ 的正负号或是否相等，利用零点存在定理或罗尔中值定理证明导数零点的存在性。

###### **方法[4]:两端求导微分方程法（变上限积分转化）**

[1]消除积分符号，归结为常微分方程初值问题：
>当等式中含有变上限积分 $\int_a^x f(t)\,\mathrm{d}t$、未知函数 $f(x)$ 及其导数时，对等式两端关于 $x$ 求导。
>
>利用 Leibniz 求导法则：
>
>$$\frac{\mathrm{d}}{\mathrm{d}x}\left[\int_{\alpha(x)}^{\beta(x)} f(x, t)\,\mathrm{d}t\right] = f(x, \beta(x))\beta'(x) - f(x, \alpha(x))\alpha'(x) + \int_{\alpha(x)}^{\beta(x)} \frac{\partial f(x, t)}{\partial x}\,\mathrm{d}t$$
>
>求导后转化为一阶或二阶线性微分方程，结合初始条件代入特殊点（如 $x=a$ 时积分为 0）确定任意常数，从而直接求解出未知函数的精确解析式。

###### **方法[5]:分部积分降阶消项法**

[1]利用分部积分法将积分等式向高阶导数或低阶函数转移：
>对于包含乘积项 $\int_a^b u(x)v'(x)\,\mathrm{d}x$ 的积分等式，利用分部积分公式：
>
>$$\int_a^b u(x)\,\mathrm{d}v(x) = [u(x)v(x)]_a^b - \int_a^b v(x)\,\mathrm{d}u(x)$$
>
>典型考研应用：
>(1) 出现 $f''(x)$ 与 $f(x)$，连续使用两次分部积分法，并巧妙选取代数多项式因式使其端点值为 0，从而使边际项 $[uv]_a^b$ 消失；
>(2) 出现三角震荡因子 $\sin nx$ 或 $\cos nx$，凑微分降出因子 $\frac{1}{n}$，使求极限或放缩变得清晰透明。

###### **方法[6]:泰勒展开内插积分法**

[1]多项式局部代换与余项积分：
>当条件给出函数的高阶导数（如二阶连续可导 $f''(x)$），且给出了区间内特定点的值（如中点 $x_0 = \frac{a+b}{2}$ 处的值或一阶导数值），在 $x_0$ 处展开为带拉格朗日余项或积分型余项的泰勒公式：
>
>$$f(x) = f(x_0) + f'(x_0)(x-x_0) + \dots + \frac{f^{(n)}(\xi)}{(n)!}(x-x_0)^n$$
>
>两端同时在 $[a, b]$ 上逐项积分。若选取中点 $x_0 = \frac{a+b}{2}$，所有关于 $(x-x_0)$ 的奇数次幂积分在对称区间上自动积分为 0：
>
>$$\int_a^b (x-x_0)\,\mathrm{d}x = 0, \quad \int_a^b (x-x_0)^3\,\mathrm{d}x = 0$$
>
>从而以最精简的形式建立定积分与高阶导数之间的精确等式或最优常数不等式。

## 4.积分不等式证明的四大王牌方法

###### **方法[7]:构造辅助函数求导单调性法**

[1]上限变量化与单调性传递准则：
>若要证明 $[a, b]$ 上的积分不等式 $A \leqslant B$：
>
>(1) 将不等式一端的定积分上限改为动点变量 $x \in [a, b]$；
>
>(2) 移项构造单变量辅助函数 $F(x)$，使得 $F(a) = 0$；
>
>(3) 对 $F(x)$ 求导计算 $F'(x)$，利用题目中的增减性、不等式条件判定 $F'(x)$ 在 $(a, b)$ 内的符号；
>
>(4) 若 $F'(x) \geqslant 0$（单调递增），则由 $x > a \implies F(x) \geqslant F(a) = 0$；特别地，取 $x = b$ 即证得 $F(b) \geqslant 0$。

###### **方法[8]:被积函数局部放缩法与切线不等式**

[1]切线不等式（支撑线放缩）：
>若函数 $f(x)$ 在区间上为凸函数（$f''(x) \geqslant 0$），则其图像恒在任意切线的上方。在点 $x_0$ 处的切线方程为：
>
>$$y = f(x_0) + f'(x_0)(x-x_0)$$
>
>切线不等式为：
>
>$$f(x) \geqslant f(x_0) + f'(x_0)(x-x_0), \quad \forall x$$
>
>两端同时在 $[a, b]$ 上积分。若选取中点 $x_0 = \frac{a+b}{2}$，线性项积分消失，立即得到中点积分下界：
>
>$$\int_a^b f(x)\,\mathrm{d}x \geqslant f\left(\frac{a+b}{2}\right)(b-a)$$

[2]割线不等式（弦线放缩）：
>若函数 $f(x)$ 在 $[a, b]$ 上下凸（$f''(x) \geqslant 0$），其图像恒在连接端点 $(a, f(a))$ 与 $(b, f(b))$ 的割线下方：
>
>$$f(x) \leqslant f(a) + \frac{f(b)-f(a)}{b-a}(x-a)$$
>
>两端积分即得到梯形面积上界：
>
>$$\int_a^b f(x)\,\mathrm{d}x \leqslant \frac{f(a)+f(b)}{2}(b-a)$$
>
>结合切线与割线，构成了考研著名的“中点-梯形双边夹逼不等式”：
>
>$$f\left(\frac{a+b}{2}\right)(b-a) \leqslant \int_a^b f(x)\,\mathrm{d}x \leqslant \frac{f(a)+f(b)}{2}(b-a)$$

###### **方法[9]:柯西-施瓦茨（Cauchy-Schwarz）积分不等式秒杀法**

[1]连续型柯西不等式形式：
>设 $f(x), g(x)$ 在 $[a, b]$ 上平方可积，则：
>
>$$\left(\int_a^b f(x)g(x)\,\mathrm{d}x\right)^2 \leqslant \left(\int_a^b f^2(x)\,\mathrm{d}x\right) \left(\int_a^b g^2(x)\,\mathrm{d}x\right)$$
>
>等号成立的充分必要条件是存在不全为 0 的实数 $\lambda, \mu$ 使得 $\lambda f(x) + \mu g(x) = 0$ 几乎处处成立。

[2]经典秒杀应用：
>若遇到含根号被积函数或倒数分母（如形如 $\int_a^b \frac{1}{f(x)}\,\mathrm{d}x \cdot \int_a^b f(x)\,\mathrm{d}x$）：
>
>令 $u(x) = \sqrt{f(x)}, v(x) = \frac{1}{\sqrt{f(x)}}$，代入柯西不等式：
>
>$$\left(\int_a^b \sqrt{f(x)} \cdot \frac{1}{\sqrt{f(x)}}\,\mathrm{d}x\right)^2 \leqslant \left(\int_a^b f(x)\,\mathrm{d}x\right)\left(\int_a^b \frac{1}{f(x)}\,\mathrm{d}x\right)$$
>
>左边为 $\left(\int_a^b 1\,\mathrm{d}x\right)^2 = (b-a)^2$，立即秒出：
>
>$$\left(\int_a^b f(x)\,\mathrm{d}x\right)\left(\int_a^b \frac{1}{f(x)}\,\mathrm{d}x\right) \geqslant (b-a)^2$$

###### **方法[10]:变量代换（区间再现与对称化）消除法**

[1]区间再现核心公式：
>作变量代换 $x = a + b - t$（即 $\mathrm{d}x = -\mathrm{d}t$），积分区间不变：
>
>$$\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(a+b-t)\,\mathrm{d}t = \int_a^b f(a+b-x)\,\mathrm{d}x$$
>
>两式相加除以 2：
>
>$$\int_a^b f(x)\,\mathrm{d}x = \frac{1}{2}\int_a^b [f(x) + f(a+b-x)]\,\mathrm{d}x$$

[2]对称消除高难三角与分母因式：
>对于两端对称结构的积分不等式证明（如习题11.2与习题11.4），通过折半积分并作区间对称代换 $x = \frac{\pi}{2}-t$ 或两式相加减，将被积函数转化为对称差分形式 $(u(x) - u(a+b-x))(v(x) - v(a+b-x))$，若两函数同单调，其乘积必然恒非负，从而瞬间完成不等式定号与降维证明。
