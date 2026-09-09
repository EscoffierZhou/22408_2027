## 8.Homework

**习题[1]:三角不等式与定积分保号性比较大小**

设 $I_1 = \int_0^{\frac{\pi}{2}} \frac{\sin x}{x}\,\mathrm{d}x$，$I_2 = \int_0^{\frac{\pi}{2}} \frac{x}{\sin x}\,\mathrm{d}x$，则 $(\quad)$

(A) $I_1 > I_2 > 1 \qquad$ (B) $1 > I_1 > I_2 \qquad$ (C) $I_2 > I_1 > 1 \qquad$ (D) $1 > I_2 > I_1$

主要思路:在开区间 $(0, \frac{\pi}{2})$ 上利用经典几何三角不等式 $\sin x < x$ 比较被积函数大小，结合若尔当不等式 $\frac{\sin x}{x} > \frac{2}{\pi}$ 对 $I_1$ 进行下界估计

>[1]比较 $I_1$ 与 $I_2$ 的大小：
>
>当 $x \in (0, \frac{\pi}{2})$ 时，经典不等式恒成立：$\sin x < x$。
>
>两边同除以正数得：
>
>$$\frac{x}{\sin x} > 1 > \frac{\sin x}{x} \implies \frac{x}{\sin x} > \frac{\sin x}{x}$$
>
>由定积分保号性可知：
>
>$$I_2 = \int_0^{\frac{\pi}{2}} \frac{x}{\sin x}\,\mathrm{d}x > \int_0^{\frac{\pi}{2}} \frac{\sin x}{x}\,\mathrm{d}x = I_1$$
>
>由此排除选项 (A) 与 (D)。
>
>[2]对 $I_1$ 进行若尔当不等式下界放缩：
>
>在 $(0, \frac{\pi}{2})$ 上，根据若尔当(Jordan)不等式 $\frac{\sin x}{x} > \frac{2}{\pi}$：
>
>$$I_1 = \int_0^{\frac{\pi}{2}} \frac{\sin x}{x}\,\mathrm{d}x > \int_0^{\frac{\pi}{2}} \frac{2}{\pi}\,\mathrm{d}x = \frac{2}{\pi} \cdot \frac{\pi}{2} = 1$$
>
>[3]综合得出结论：
>
>综合两步可得：$I_2 > I_1 > 1$。
>
>[4]故正确选项为 **(C)**。

**习题[2]:分段函数原函数存在性与变限积分可导性判定**

设 $f(x) = \begin{cases} x, & x < 0 \\ \frac{1}{2}, & x = 0 \\ 1, & x > 0 \end{cases}$，则下列命题：

(1) $f(x)$ 在 $[-1, 1]$ 上有原函数；
(2) $f(x)$ 在 $[-1, 1]$ 上可积；
(3) $F(x) = \int_0^x f(t)\,\mathrm{d}t$ 在 $x=0$ 处可导；
(4) $F(x) = \int_0^x f(t)\,\mathrm{d}t$ 在 $x=0$ 处连续但不可导。

正确命题的个数为 $(\quad)$

(A) 1 \qquad (B) 2 \qquad (C) 3 \qquad (D) 4

主要思路:检查分界点左右极限识别间断点类型，运用达布介值定理和变上限积分平滑性定理逐项分析

>[1]考察间断点类型：
>
>$\lim\limits_{x \to 0^-} f(x) = 0$，$\lim\limits_{x \to 0^+} f(x) = 1$。
>
>由于左右极限均存在但不相等，故 $x = 0$ 是 $f(x)$ 的第一类跳跃间断点。
>
>[2]分析命题(1)与(2)：
>
>命题(1)错误: 含有第一类间断点的函数在包含该点的区间上必无原函数(达布定理)；
>
>命题(2)正确: $f(x)$ 在 $[-1, 1]$ 上有界且仅有 1 个跳跃间断点，由充分条件知定积分必定存在(即可积)。
>
>[3]分析命题(3)与(4)：
>
>变上限积分 $F(x)$ 必处处连续；
>
>在跳跃间断点处，左右导数分别等于被积函数的左右极限：
>
>$$F'_-(0) = f(0^-) = 0, \quad F'_+(0) = f(0^+) = 1$$
>
>因为 $F'_-(0) \neq F'_+(0)$，故 $F(x)$ 在 $x = 0$ 处不可导。
>
>故命题(3)错误，命题(4)正确。
>
>[4]综合得出正确命题数量：
>
>正确的命题为 (2) 和 (4)，共 2 个。
>
>[5]故正确选项为 **(B)**。

**习题[3]:含对数因子的瑕积分与无穷反常积分双奇点审敛**

若反常积分 $\int_0^{+\infty} \frac{\ln x}{(1+x)x^{1-p}}\,\mathrm{d}x$ 收敛，则 $(\quad)$

(A) $p < 1 \qquad$ (B) $p > 1 \qquad$ (C) $0 < p < 1 \qquad$ (D) $0 \leqslant p < 1$

主要思路:识别积分的两个奇点 $x = 0$(瑕点)与 $x = +\infty$(无穷)，拆分为两段分别由低次项和高次项主导，应用对数阶数压制基准判别

>[1]拆分双奇点：
>
>$$I = \int_0^1 \frac{\ln x}{(1+x)x^{1-p}}\,\mathrm{d}x + \int_1^{+\infty} \frac{\ln x}{(1+x)x^{1-p}}\,\mathrm{d}x = I_1 + I_2$$
>
>原积分收敛当且仅当 $I_1$ 与 $I_2$ 同时收敛。
>
>[2]分析瑕积分 $I_1$ ($x \to 0^+$)：
>
>当 $x \to 0^+$ 时，$1+x \to 1$，被积函数主部为：
>
>$$\frac{\ln x}{(1+x)x^{1-p}} \sim \frac{\ln x}{x^{1-p}}$$
>
>由瑕积分对数基准型可知，$\int_0^1 \frac{\vert{}\ln x\vert{}}{x^k}\,\mathrm{d}x$ 收敛的充要条件为幂次 $k < 1$。
>
>这里 $k = 1 - p$，因此要求：
>
>$$1 - p < 1 \implies p > 0$$
>
>[3]分析无穷区间积分 $I_2$ ($x \to +\infty$)：
>
>当 $x \to +\infty$ 时，$1+x \sim x$，被积函数主部为：
>
>$$\frac{\ln x}{(1+x)x^{1-p}} \sim \frac{\ln x}{x \cdot x^{1-p}} = \frac{\ln x}{x^{2-p}}$$
>
>由无穷区间对数基准型可知，$\int_1^{+\infty} \frac{\ln x}{x^k}\,\mathrm{d}x$ 收敛的充要条件为幂次 $k > 1$。
>
>这里 $k = 2 - p$，因此要求：
>
>$$2 - p > 1 \implies p < 1$$
>
>[4]求交集得出参数范围：
>
>两端必须同时收敛，取交集得：$0 < p < 1$。
>
>[5]故正确选项为 **(C)**。

**习题[4]:定积分定义求解连和式极限**

$\lim\limits_{n \to \infty} \left( \frac{1}{\sqrt{n^2+n}} + \frac{1}{\sqrt{n^2+2n}} + \frac{1}{\sqrt{n^2+3n}} + \dots + \frac{1}{\sqrt{n^2+n^2}} \right) = \underline{\hspace{2.5cm}}$。

主要思路:通项中分母提取公因式 $n$，分离出 $\frac{1}{n}$ 凑自变量 $\frac{i}{n}$，严格应用定积分定义转化为连续定积分求解

>[1]求和通项分析与提取 $\frac{1}{n}$：
>
>将求和式用 $\Sigma$ 紧凑表示：
>
>$$\text{原式} = \lim_{n \to \infty} \sum_{i=1}^n \frac{1}{\sqrt{n^2+ni}}$$
>
>分母提取公因式 $n$：
>
>$$= \lim_{n \to \infty} \sum_{i=1}^n \frac{1}{n\sqrt{1 + \frac{i}{n}}} = \lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n \frac{1}{\sqrt{1 + \frac{i}{n}}}$$
>
>[2]定积分定义转化：
>
>令 $\frac{i}{n} \to x$，$\frac{1}{n} \to \mathrm{d}x$，求和指标 $i=1 \sim n$ 对应积分区间 $[0, 1]$：
>
>$$= \int_0^1 \frac{1}{\sqrt{1+x}}\,\mathrm{d}x$$
>
>[3]计算定积分值：
>
>$$= \left. 2\sqrt{1+x} \right\vert{}_0^1 = 2\sqrt{2} - 2$$
>
>[4]故最终答案为 $2\sqrt{2} - 2$。

**习题[5]:夹逼准则化归定积分定义求解微扰和式极限**

$\lim\limits_{n \to \infty} \sum\limits_{i=1}^n \frac{\sin \frac{i\pi}{n}}{n + \frac{1}{i}} = \underline{\hspace{2.5cm}}$。

主要思路:分母微扰项 $\frac{1}{i}$ 破坏了标准 $\frac{i}{n}$ 结构，利用有界放缩将其夹在两个标准定积分定义式之间，结合夹逼准则求出极限

>[1]建立不等式夹逼：
>
>由于对所有 $1 \leqslant i \leqslant n$，恒有 $0 < \frac{1}{i} \leqslant 1$，且 $\sin\frac{i\pi}{n} \geqslant 0$，故有不等式：
>
>$$\frac{\sin \frac{i\pi}{n}}{n+1} \leqslant \frac{\sin \frac{i\pi}{n}}{n + \frac{1}{i}} \leqslant \frac{\sin \frac{i\pi}{n}}{n}$$
>
>[2]对不等式求和并计算两端极限：
>
>右端极限：
>
>$$\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n \sin\left(\frac{i}{n}\pi\right) = \int_0^1 \sin(\pi x)\,\mathrm{d}x = \left. \left( -\frac{1}{\pi}\cos(\pi x) \right) \right\vert{}_0^1 = -\frac{1}{\pi}(-1 - 1) = \frac{2}{\pi}$$
>
>左端极限：
>
>$$\lim_{n \to \infty} \sum_{i=1}^n \frac{\sin \frac{i\pi}{n}}{n+1} = \lim_{n \to \infty} \frac{n}{n+1} \cdot \left[ \frac{1}{n}\sum_{i=1}^n \sin\left(\frac{i}{n}\pi\right) \right] = 1 \cdot \frac{2}{\pi} = \frac{2}{\pi}$$
>
>[3]应用夹逼准则得出结论：
>
>由夹逼准则，原极限等于 $\frac{2}{\pi}$。
>
>[4]故最终答案为 $\frac{2}{\pi}$。

**习题[6]:周期锯齿波变上限积分的单侧导数计算**

设 $F(x) = \int_0^x (t - [t])\,\mathrm{d}t$，其中 $[x]$ 表示不超过 $x$ 的最大整数，则 $F'_-(1) + F'_+(1) = \underline{\hspace{2.5cm}}$。

主要思路:被积函数为周期锯齿波，整数点均为跳跃间断点；变上限积分处处连续，分界点处的单侧导数直接对应被积函数的单侧极限

>[1]分析被积函数的间断点：
>
>记被积函数为 $f(t) = t - [t]$(表示 $t$ 的小数部分，周期为 1 的锯齿波)。
>
>在整数分界点处，$f(t)$ 产生第一类跳跃间断点，其变上限积分 $F(x)$ 处处连续。
>
>[2]计算分界点 $x = 1$ 处的单侧导数：
>
>变上限积分的单侧导数等于被积函数的单侧极限：
>
>左导数：
>
>$$F'_-(1) = \lim_{t \to 1^-} f(t) = \lim_{t \to 1^-} (t - [t]) = \lim_{t \to 1^-} (t - 0) = 1$$
>
>右导数：
>
>$$F'_+(1) = \lim_{t \to 1^+} f(t) = \lim_{t \to 1^+} (t - [t]) = \lim_{t \to 1^+} (t - 1) = 0$$
>
>[3]两单侧导数求和：
>
>$$F'_-(1) + F'_+(1) = 1 + 0 = 1$$
>
>[4]故最终答案为 $1$。

**习题[7]:含对数幂次复合反常积分的敛散性讨论**

讨论反常积分 $\int_2^{+\infty} \frac{1}{x \ln^p x}\,\mathrm{d}x$ 的敛散性，其中 $p$ 为任意实数。

主要思路:利用凑微分法将对数因子换元为基本变量 $u = \ln x$，将复合积分化为最基础的 $p$-反常积分进行分类讨论

>[1]凑微分与换元：
>
>$$\int_2^{+\infty} \frac{1}{x \ln^p x}\,\mathrm{d}x = \int_2^{+\infty} (\ln x)^{-p}\,\mathrm{d}(\ln x)$$
>
>令 $u = \ln x$。当 $x \to 2$ 时 $u \to \ln 2 > 0$；当 $x \to +\infty$ 时 $u \to +\infty$：
>
>$$= \int_{\ln 2}^{+\infty} \frac{1}{u^p}\,\mathrm{d}u$$
>
>[2]分类讨论幂次 $p$：
>
>当 $p > 1$ 时：
>
>$$\int_{\ln 2}^{+\infty} u^{-p}\,\mathrm{d}u = \left. \frac{u^{1-p}}{1-p} \right\vert{}_{\ln 2}^{+\infty} = 0 - \frac{(\ln 2)^{1-p}}{1-p} = \frac{(\ln 2)^{1-p}}{p-1} \quad (\text{收敛})$$
>
>当 $p = 1$ 时：
>
>$$\int_{\ln 2}^{+\infty} \frac{1}{u}\,\mathrm{d}u = \left. \ln u \right\vert{}_{\ln 2}^{+\infty} = +\infty \quad (\text{发散})$$
>
>当 $p < 1$ 时：
>
>$$\left. \frac{u^{1-p}}{1-p} \right\vert{}_{\ln 2}^{+\infty} = +\infty \quad (\text{发散})$$
>
>[3]结论：
>
>当 $p > 1$ 时积分收敛；当 $p \leqslant 1$ 时积分发散。

**习题[8]:柯西-施瓦茨定积分不等式证明**

设函数$f(x)$在$[0, 1]$上连续，证明：

$$\left(\int_0^1 f(x)\,\mathrm{d}x\right)^2 \le \int_0^1 f^2(x)\,\mathrm{d}x$$

并指出等号成立的充要条件。

主要思路:构造实变量$t$的二次非负多项式积分$g(t) = \int_0^1 [t f(x) + 1]^2\mathrm{d}x \ge 0$，利用二次判别法$\Delta \le 0$证得不等式

>[1]构造辅助二次函数：
>
>对任意实数$t$，考虑被积表达式$[t f(x) + 1]^2 \ge 0$。
>
>由定积分保号性，积分值恒非负：
>
>$$g(t) = \int_0^1 [t f(x) + 1]^2\,\mathrm{d}x \ge 0$$
>
>[2]展开为关于$t$的一元二次多项式：
>
>$$g(t) = \int_0^1 [t^2 f^2(x) + 2t f(x) + 1]\,\mathrm{d}x = \left(\int_0^1 f^2(x)\,\mathrm{d}x\right) t^2 + 2\left(\int_0^1 f(x)\,\mathrm{d}x\right) t + \int_0^1 1\,\mathrm{d}x$$
>
>记$A = \int_0^1 f^2(x)\,\mathrm{d}x$，$B = \int_0^1 f(x)\,\mathrm{d}x$，$C = 1$。
>
>则$g(t) = A t^2 + 2B t + 1 \ge 0$对一切实数$t$均成立。
>
>[3]利用一元二次方程判别法：
>
>二次三项式恒非负，其判别式必满足$\Delta \le 0$：
>
>$$\Delta = (2B)^2 - 4A \cdot 1 = 4B^2 - 4A \le 0 \implies B^2 \le A$$
>
>即：
>
>$$\left(\int_0^1 f(x)\,\mathrm{d}x\right)^2 \le \int_0^1 f^2(x)\,\mathrm{d}x$$
>
>[4]等号成立条件：
>
>等号成立当且仅当$\Delta = 0$，即存在实数$t_0$使得被积函数恒等于0：$t_0 f(x) + 1 \equiv 0 \implies f(x) \equiv -\frac{1}{t_0} = \text{常数}$。
>
>故等号成立当且仅当$f(x)$为常数函数。证毕。

**习题[9]:含参变量变上限积分的高阶求导运算**

设$F(x) = \int_0^x (x - t)\sin t\,\mathrm{d}t$，求$F'(x)$与$F''(x)$。

主要思路:积分内含有变上限自变量$x$，必须先将线性参变量$x$拆分提至积分号外，再应用乘积求导法则与微积分基本定理求一阶与二阶导数

>[1]参变量线性拆分：
>
>$$F(x) = \int_0^x (x\sin t - t\sin t)\,\mathrm{d}t = x \int_0^x \sin t\,\mathrm{d}t - \int_0^x t\sin t\,\mathrm{d}t$$
>
>[2]求一阶导数$F'(x)$：
>
>对两项分别求导(第一项使用乘积求导法则)：
>
>$$F'(x) = \left[ 1 \cdot \int_0^x \sin t\,\mathrm{d}t + x \cdot \sin x \right] - x\sin x = \int_0^x \sin t\,\mathrm{d}t$$
>
>[3]求二阶导数$F''(x)$：
>
>对$F'(x)$两边再求导：
>
>$$F''(x) = \frac{\mathrm{d}}{\mathrm{d}x} \int_0^x \sin t\,\mathrm{d}t = \sin x$$
>
>[4]故所求导数为：
>
>$$F'(x) = 1 - \cos x, \quad F''(x) = \sin x$$

**习题[10]:振荡型反常积分的狄利克雷审敛判定**

讨论反常积分$\int_1^{+\infty} \frac{\sin x}{x^p}\,\mathrm{d}x$在$p > 0$时的绝对收敛性与条件收敛性。

主要思路:当$p>1$时利用绝对值比较法判定绝对收敛；当$0<p\le 1$时利用狄利克雷判别法证明收敛，并利用$\sin^2 x = \frac{1-\cos 2x}{2}$证明绝对值发散，从而判定为条件收敛

>[1]分析$p > 1$时的绝对收敛性：
>
>考察绝对值积分$\int_1^{+\infty} \left\vert{}\frac{\sin x}{x^p}\right\vert{}\,\mathrm{d}x$。
>
>因$\left\vert{}\frac{\sin x}{x^p}\right\vert{} \le \frac{1}{x^p}$，且$\int_1^{+\infty} \frac{1}{x^p}\,\mathrm{d}x$在$p > 1$时收敛。
>
>由比较审敛法，$\int_1^{+\infty} \frac{\sin x}{x^p}\,\mathrm{d}x$在$p > 1$时**绝对收敛**。
>
>[2]分析$0 < p \le 1$时的收敛性(狄利克雷判别法)：
>
>- 原函数有界性：$\left\vert{}\int_1^x \sin t\,\mathrm{d}t\right\vert{} = \vert{}-\cos x + \cos 1\vert{} \le 2$在$[1, +\infty)$上有界；
>- 单调趋于0：当$p > 0$时，$g(x) = \frac{1}{x^p}$在$[1, +\infty)$上单调递减且$\lim_{x \to +\infty} \frac{1}{x^p} = 0$。
>
>由狄利克雷审敛法，反常积分$\int_1^{+\infty} \frac{\sin x}{x^p}\,\mathrm{d}x$收敛。
>
>[3]分析$0 < p \le 1$时绝对值积分的发散性：
>
>$$\vert{}\sin x\vert{} \ge \sin^2 x = \frac{1 - \cos 2x}{2}$$
>
>$$\int_1^{+\infty} \frac{\vert{}\sin x\vert{}}{x^p}\,\mathrm{d}x \ge \frac{1}{2}\int_1^{+\infty} \frac{1}{x^p}\,\mathrm{d}x - \frac{1}{2}\int_1^{+\infty} \frac{\cos 2x}{x^p}\,\mathrm{d}x$$
>
>由狄利克雷判别法，后半部分$\int_1^{+\infty} \frac{\cos 2x}{x^p}\,\mathrm{d}x$收敛；而前半部分$\int_1^{+\infty} \frac{1}{x^p}\,\mathrm{d}x$在$0 < p \le 1$时发散。
>
>故绝对值积分发散。
>
>[4]结论：
>
>当$p > 1$时，反常积分**绝对收敛**；当$0 < p \le 1$时，反常积分**条件收敛**。
