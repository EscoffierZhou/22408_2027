## 8.Homework

**习题[8.1]:三角不等式与定积分保号性比较大小**

设 $I_1 = \int_0^{\frac{\pi}{2}} \frac{\sin x}{x}\,\mathrm{d}x$，$I_2 = \int_0^{\frac{\pi}{2}} \frac{x}{\sin x}\,\mathrm{d}x$，则下列关系正确的是：
(A) $I_1 > I_2 > 1$
(B) $1 > I_1 > I_2$
(C) $I_2 > I_1 > 1$
(D) $1 > I_2 > I_1$

主要思路:在开区间 $(0, \frac{\pi}{2})$ 上利用经典几何三角不等式 $\sin x < x$ 比较被积函数大小，结合若尔当不等式 $\frac{\sin x}{x} > \frac{2}{\pi}$ 对 $I_1$ 进行下界估计

>[1]比较 $I_1$ 与 $I_2$ 的大小：
>
>当 $x \in (0, \frac{\pi}{2})$ 时，经典三角不等式恒成立：$\sin x < x$。
>
>两边同除以正数得：
>
>$$\frac{x}{\sin x} > 1 > \frac{\sin x}{x} \implies \frac{x}{\sin x} > \frac{\sin x}{x}$$
>
>由定积分的保号性可知：
>
>$$I_2 = \int_0^{\frac{\pi}{2}} \frac{x}{\sin x}\,\mathrm{d}x > \int_0^{\frac{\pi}{2}} \frac{\sin x}{x}\,\mathrm{d}x = I_1$$
>
>由此可排除选项 (A) 与 (D)。
>
>[2]对 $I_1$ 进行若尔当不等式下界放缩：
>
>在 $(0, \frac{\pi}{2})$ 上，根据若尔当（Jordan）不等式 $\frac{\sin x}{x} > \frac{2}{\pi}$：
>
>$$I_1 = \int_0^{\frac{\pi}{2}} \frac{\sin x}{x}\,\mathrm{d}x > \int_0^{\frac{\pi}{2}} \frac{2}{\pi}\,\mathrm{d}x = \frac{2}{\pi} \cdot \frac{\pi}{2} = 1$$
>
>[3]综合得出结论：
>
>结合上述两步放缩分析，得到：
>
>$$I_2 > I_1 > 1$$
>
>故正确选项为 (C)。

**习题[8.2]:分段函数原函数存在性与变限积分可导性判定**

设 $f(x) = \begin{cases} x, & x < 0 \\ \frac{1}{2}, & x = 0 \\ 1, & x > 0 \end{cases}$，则下列命题：
(1) $f(x)$ 在 $[-1, 1]$ 上有原函数；
(2) $f(x)$ 在 $[-1, 1]$ 上可积；
(3) $F(x) = \int_0^x f(t)\,\mathrm{d}t$ 在 $x=0$ 处可导；
(4) $F(x) = \int_0^x f(t)\,\mathrm{d}t$ 在 $x=0$ 处连续但不可导。
正确命题的个数为：
(A) 1
(B) 2
(C) 3
(D) 4

主要思路:检查分界点左右极限识别间断点类型，运用达布介值定理和变上限积分平滑性定理逐项分析

>[1]考察间断点类型：
>
>分别考查 $f(x)$ 在 $x = 0$ 处的单侧极限：
>
>$$\lim_{x \to 0^-} f(x) = 0, \quad \lim_{x \to 0^+} f(x) = 1$$
>
>由于左右极限均存在但不相等，故 $x = 0$ 是 $f(x)$ 的第一类跳跃间断点。
>
>[2]分析原函数存在性与可积性：
>
>(1) 命题(1)错误：含有第一类跳跃间断点的函数在包含该点的区间上必然没有原函数（根据达布定理，导函数不能具有第一类间断点）；
>
>(2) 命题(2)正确：$f(x)$ 在 $[-1, 1]$ 上有界且仅有 1 个跳跃间断点，由定积分存在的充分条件可知定积分必然存在（即黎曼可积）。
>
>[3]分析变上限积分的平滑性与结论：
>
>变上限积分 $F(x)$ 必然处处连续。在跳跃间断点 $x = 0$ 处，左右导数分别等于被积函数的左右极限：
>
>$$F'_-(0) = f(0^-) = 0, \quad F'_+(0) = f(0^+) = 1$$
>
>因为 $F'_-(0) \neq F'_+(0)$，故 $F(x)$ 在 $x = 0$ 处不可导。命题(3)错误，命题(4)正确。
>
>正确的命题为 (2) 和 (4)，共 2 个。故正确选项为 (B)。

**习题[8.3]:含对数因子的瑕积分与无穷反常积分双奇点审敛**

若反常积分 $\int_0^{+\infty} \frac{\ln x}{(1+x)x^{1-p}}\,\mathrm{d}x$ 收敛，则参数 $p$ 的取值范围是：
(A) $p < 1$
(B) $p > 1$
(C) $0 < p < 1$
(D) $0 \le p < 1$

主要思路:识别积分的两个奇点 $x = 0$（瑕点）与 $x = +\infty$（无穷），拆分为两段分别由低次项和高次项主导，应用对数阶数压制基准判别

>[1]拆分双奇点：
>
>将积分在 $x = 1$ 处拆分为两段：
>
>$$I = \int_0^1 \frac{\ln x}{(1+x)x^{1-p}}\,\mathrm{d}x + \int_1^{+\infty} \frac{\ln x}{(1+x)x^{1-p}}\,\mathrm{d}x = I_1 + I_2$$
>
>原积分收敛当且仅当 $I_1$ 与 $I_2$ 同时收敛。
>
>[2]分析瑕积分 $I_1$ ($x \to 0^+$)：
>
>当 $x \to 0^+$ 时，$1 + x \sim 1$，被积函数满足：
>
>$$\frac{|\ln x|}{(1+x)x^{1-p}} \sim \frac{|\ln x|}{x^{1-p}}$$
>
>由瑕积分对数基准敛散性，当且仅当幂指数满足 $1 - p < 1 \implies p > 0$ 时，$I_1$ 绝对收敛。
>
>[3]分析无穷反常积分 $I_2$ ($x \to +\infty$) 与汇总：
>
>当 $x \to +\infty$ 时，$1 + x \sim x$，被积函数满足：
>
>$$\frac{\ln x}{(1+x)x^{1-p}} \sim \frac{\ln x}{x \cdot x^{1-p}} = \frac{\ln x}{x^{2-p}}$$
>
>由无穷区间反常积分对数基准敛散性，当且仅当分母幂指数满足 $2 - p > 1 \implies p < 1$ 时，$I_2$ 收敛。
>
>综合 $I_1$ 与 $I_2$ 的收敛条件，必有 $0 < p < 1$。故正确选项为 (C)。

**习题[8.4]:定积分定义化和式极限计算**

计算极限：

$$\lim_{n \to \infty} \left( \frac{1}{\sqrt{n^2+n}} + \frac{1}{\sqrt{n^2+2n}} + \frac{1}{\sqrt{n^2+3n}} + \dots + \frac{1}{\sqrt{n^2+n^2}} \right)$$

主要思路:通过提取分母公因式 $n$，凑出步长 $\frac{1}{n}$ 与网格自变量 $\frac{i}{n}$，严格应用定积分定义转化为标准定积分求解

>[1]提取通项中的公因式 $\frac{1}{n}$：
>
>将原和式用求和号 $\sum$ 表达：
>
>$$\lim_{n \to \infty} \sum_{i=1}^n \frac{1}{\sqrt{n^2+ni}} = \lim_{n \to \infty} \sum_{i=1}^n \frac{1}{n\sqrt{1 + \frac{i}{n}}} = \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n \frac{1}{\sqrt{1 + \frac{i}{n}}}$$
>
>[2]转化为定积分形式：
>
>取区间 $[0, 1]$ 进行 $n$ 等分，步长 $\Delta x_i = \frac{1}{n}$，分点 $\xi_i = \frac{i}{n}$。
>
>由黎曼定积分定义，上述和式极限转化为：
>
>$$\int_0^1 \frac{1}{\sqrt{1 + x}}\,\mathrm{d}x$$
>
>[3]计算定积分值：
>
>$$\int_0^1 (1 + x)^{-\frac{1}{2}}\,\mathrm{d}x = \left[ 2\sqrt{1 + x} \right]_0^1 = 2\sqrt{2} - 2$$
>
>故原极限的值为 $2\sqrt{2} - 2$。

**习题[8.5]:分母微扰和式极限的夹逼准则与定积分计算**

计算极限：

$$\lim_{n \to \infty} \sum_{i=1}^n \frac{\sin \frac{i\pi}{n}}{n + \frac{1}{i}}$$

主要思路:分母中微扰项 $\frac{1}{i}$ 破坏了标准 $\frac{i}{n}$ 结构，通过放大缩小将其夹在两个标准定积分和式之间，结合夹逼准则完成计算

>[1]建立不等式夹逼：
>
>对于任意 $1 \le i \le n$，恒有 $0 < \frac{1}{i} \le 1$。
>
>且当 $i \in [1, n]$ 时，$\frac{i\pi}{n} \in (0, \pi]$，分子 $\sin\frac{i\pi}{n} \ge 0$。
>
>因此建立严格的双侧不等式：
>
>$$\frac{\sin \frac{i\pi}{n}}{n+1} \le \frac{\sin \frac{i\pi}{n}}{n + \frac{1}{i}} \le \frac{\sin \frac{i\pi}{n}}{n}$$
>
>[2]两端对 $i$ 从 $1$ 到 $n$ 求和并求极限：
>
>对右端和式应用定积分定义：
>
>$$\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^n \sin \frac{i\pi}{n} = \int_0^1 \sin(\pi x)\,\mathrm{d}x = \left[ -\frac{1}{\pi}\cos(\pi x) \right]_0^1 = -\frac{1}{\pi}(-1 - 1) = \frac{2}{\pi}$$
>
>对左端和式提取因子：
>
>$$\lim_{n \to \infty} \frac{1}{n+1} \sum_{i=1}^n \sin \frac{i\pi}{n} = \lim_{n \to \infty} \frac{n}{n+1} \left( \frac{1}{n} \sum_{i=1}^n \sin \frac{i\pi}{n} \right) = 1 \cdot \frac{2}{\pi} = \frac{2}{\pi}$$
>
>[3]应用夹逼定理得出结论：
>
>两端极限均存在且相等，由夹逼准则（Squeeze Theorem）：
>
>$$\lim_{n \to \infty} \sum_{i=1}^n \frac{\sin \frac{i\pi}{n}}{n + \frac{1}{i}} = \frac{2}{\pi}$$

**习题[8.6]:周期锯齿波变限积分的单侧导数计算**

设 $F(x) = \int_0^x (t - [t])\,\mathrm{d}t$，其中 $[x]$ 表示不超过 $x$ 的最大整数。求单侧导数之和 $F'_-(1) + F'_+(1)$ 的值。

主要思路:被积函数为周期锯齿波，在整数分界点处具有跳跃间断点，变限积分在整数分界点处的单侧导数直接对应被积函数的单侧极限

>[1]分析被积函数性质：
>
>被积函数为 $f(t) = t - [t]$（表示 $t$ 的小数部分，周期为 $1$ 的锯齿波函数）。
>
>在整数分界点处，$f(t)$ 具有第一类跳跃间断点，但因为有界可积，变限积分 $F(x)$ 处处连续。
>
>[2]计算分界点 $x = 1$ 处的单侧导数：
>
>变上限积分的单侧导数等于被积函数在对应侧的单侧极限：
>
>$$F'_-(1) = \lim_{t \to 1^-} f(t) = \lim_{t \to 1^-} (t - [t]) = \lim_{t \to 1^-} (t - 0) = 1$$
>
>$$F'_+(1) = \lim_{t \to 1^+} f(t) = \lim_{t \to 1^+} (t - [t]) = \lim_{t \to 1^+} (t - 1) = 0$$
>
>[3]求和得出最终结果：
>
>$$F'_-(1) + F'_+(1) = 1 + 0 = 1$$

**习题[8.7]:含对数复合无穷反常积分的敛散性判别**

讨论反常积分 $\int_2^{+\infty} \frac{1}{x \ln^p x}\,\mathrm{d}x$ 的敛散性，其中 $p$ 为任意实数。

主要思路:利用凑微分法引入变量代换 $u = \ln x$，将反常积分转化为标准 $p$-反常积分进行敛散性分析

>[1]凑微分与变量代换：
>
>$$\int_2^{+\infty} \frac{1}{x \ln^p x}\,\mathrm{d}x = \int_2^{+\infty} (\ln x)^{-p}\,\mathrm{d}(\ln x)$$
>
>令 $u = \ln x$。当 $x \to 2$ 时 $u \to \ln 2 > 0$；当 $x \to +\infty$ 时 $u \to +\infty$。
>
>积分转化为：
>
>$$\int_{\ln 2}^{+\infty} \frac{1}{u^p}\,\mathrm{d}u$$
>
>[2]按幂次 $p$ 分类讨论：
>
>(1) 当 $p > 1$ 时：
>
>$$\int_{\ln 2}^{+\infty} u^{-p}\,\mathrm{d}u = \left[ \frac{u^{1-p}}{1 - p} \right]_{\ln 2}^{+\infty} = 0 - \frac{(\ln 2)^{1-p}}{1 - p} = \frac{(\ln 2)^{1-p}}{p - 1}$$
>
>反常积分收敛。
>
>(2) 当 $p \le 1$ 时：
>
>若 $p = 1$，$\int_{\ln 2}^{+\infty} \frac{1}{u}\,\mathrm{d}u = [\ln u]_{\ln 2}^{+\infty} = +\infty$，积分发散；
>
>若 $p < 1$，$1 - p > 0$，$\lim\limits_{A \to +\infty} u^{1-p} = +\infty$，积分发散。
>
>[3]总结结论：
>
>当且仅当 $p > 1$ 时，反常积分收敛；当 $p \le 1$ 时，反常积分发散。

**习题[8.8]:柯西-施瓦茨定积分不等式证明与等号条件**

设连续函数 $f(x)$ 在 $[0, 1]$ 上连续，证明不等式：

$$\left(\int_0^1 f(x)\,\mathrm{d}x\right)^2 \le \int_0^1 f^2(x)\,\mathrm{d}x$$

并指出等号成立的充要条件。

主要思路:对任意实数 $t$ 构造非负二次函数积分 $g(t) = \int_0^1 [t f(x) + 1]^2\,\mathrm{d}x \ge 0$，利用二次型判别式 $\Delta \le 0$ 证明不等式

>[1]构造非负辅助二次函数：
>
>对于任意实数 $t$，显然被积函数满足 $[t f(x) + 1]^2 \ge 0$。
>
>由定积分保号性，积分函数非负：
>
>$$g(t) = \int_0^1 [t f(x) + 1]^2\,\mathrm{d}x \ge 0$$
>
>[2]展开为关于 $t$ 的一元二次多项式：
>
>$$g(t) = \int_0^1 [t^2 f^2(x) + 2t f(x) + 1]\,\mathrm{d}x = \left(\int_0^1 f^2(x)\,\mathrm{d}x\right) t^2 + 2\left(\int_0^1 f(x)\,\mathrm{d}x\right) t + \int_0^1 1\,\mathrm{d}x$$
>
>记 $A = \int_0^1 f^2(x)\,\mathrm{d}x, \; B = \int_0^1 f(x)\,\mathrm{d}x, \; C = 1$。
>
>则 $g(t) = A t^2 + 2B t + 1 \ge 0$ 对任意 $t \in \mathbb{R}$ 恒成立。
>
>[3]利用判别式得出不等式与等号条件：
>
>二次函数恒非负的充要条件是判别式满足 $\Delta \le 0$：
>
>$$\Delta = (2B)^2 - 4A(1) \le 0 \implies 4B^2 - 4A \le 0 \implies B^2 \le A$$
>
>即：
>
>$$\left(\int_0^1 f(x)\,\mathrm{d}x\right)^2 \le \int_0^1 f^2(x)\,\mathrm{d}x$$
>
>等号成立当且仅当存在常数 $t_0$ 使得 $t_0 f(x) + 1 \equiv 0$，即 $f(x) \equiv C$ 为常数函数。

**习题[8.9]:二重变限积分的高阶导数计算**

设 $F(x) = \int_0^x (x - t)\sin t\,\mathrm{d}t$，求 $F'(x)$ 与 $F''(x)$。

主要思路:被积函数中含有求导自变量 $x$，先将线性参变量 $x$ 拆分至积分号外，再应用乘积求导法则与微积分基本定理求一阶导与二阶导

>[1]拆分参变量：
>
>$$F(x) = \int_0^x (x\sin t - t\sin t)\,\mathrm{d}t = x \int_0^x \sin t\,\mathrm{d}t - \int_0^x t\sin t\,\mathrm{d}t$$
>
>[2]求一阶导数 $F'(x)$：
>
>应用乘积求导法则：
>
>$$F'(x) = \left[ 1 \cdot \int_0^x \sin t\,\mathrm{d}t + x \cdot \sin x \right] - x\sin x = \int_0^x \sin t\,\mathrm{d}t$$
>
>交叉项 $x\sin x$ 精确抵消。
>
>[3]求二阶导数 $F''(x)$：
>
>对 $F'(x) = \int_0^x \sin t\,\mathrm{d}t$ 直接应用微积分基本定理求导：
>
>$$F''(x) = \sin x$$

**习题[8.10]:振荡反常积分的绝对收敛与条件收敛判别**

讨论反常积分 $\int_1^{+\infty} \frac{\sin x}{x^p}\,\mathrm{d}x$ 在 $p > 0$ 时的收敛性与绝对收敛性。

主要思路:当 $p > 1$ 时利用绝对值比较审敛法证明绝对收敛；当 $0 < p \le 1$ 时利用狄利克雷判别法证明收敛，结合倍角公式 $\sin^2 x = \frac{1-\cos 2x}{2}$ 证明绝对值发散，从而判定为条件收敛

>[1]当 $p > 1$ 时的绝对收敛性：
>
>考查绝对值积分 $\int_1^{+\infty} \left| \frac{\sin x}{x^p} \right|\,\mathrm{d}x$。
>
>因为 $\left| \frac{\sin x}{x^p} \right| \le \frac{1}{x^p}$，且 $\int_1^{+\infty} \frac{1}{x^p}\,\mathrm{d}x$ 在 $p > 1$ 时收敛。
>
>由比较审敛法，$\int_1^{+\infty} \left| \frac{\sin x}{x^p} \right|\,\mathrm{d}x$ 收敛，故原积分**绝对收敛**。
>
>[2]当 $0 < p \le 1$ 时的收敛性证明：
>
>变上限积分 $\left| \int_1^A \sin x\,\mathrm{d}x \right| = |\cos 1 - \cos A| \le 2$ 有界。
>
>函数 $g(x) = \frac{1}{x^p}$ 在 $[1, +\infty)$ 上单调递减且 $\lim\limits_{x \to +\infty} \frac{1}{x^p} = 0$。
>
>由狄利克雷判别法，原积分 $\int_1^{+\infty} \frac{\sin x}{x^p}\,\mathrm{d}x$ **收敛**。
>
>[3]证明绝对值发散与最终结论：
>
>利用不等式 $|\sin x| \ge \sin^2 x = \frac{1 - \cos 2x}{2}$：
>
>$$\int_1^A \frac{|\sin x|}{x^p}\,\mathrm{d}x \ge \frac{1}{2}\int_1^A \frac{1}{x^p}\,\mathrm{d}x - \frac{1}{2}\int_1^A \frac{\cos 2x}{x^p}\,\mathrm{d}x$$
>
>当 $A \to +\infty$ 时，第二项由狄利克雷判别法收敛，而第一项发散（$p \le 1$）。
>
>因此绝对值积分发散。
>
>综上所述：当 $p > 1$ 时原积分**绝对收敛**；当 $0 < p \le 1$ 时原积分**条件收敛**。
