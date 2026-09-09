# Chap8 一元函数积分学的概念与性质

目的[1]:掌握原函数与不定积分的基本概念、原函数存在定理及导函数的形态限制(达布定理)

目的[2]:掌握定积分黎曼和定义、几何代数意义及可积性的必要条件与四大充分条件

目的[3]:熟练运用定积分保号性、估值定理、积分第一中值定理分析积分等式与不等式

目的[4]:深刻理解变上限积分函数的连续性、可导性与间断点传导规律(积分升阶定理)

目的[5]:掌握反常积分(无穷区间型与瑕积分)敛散性判别法、两大标准p-积分基准与阶数压制模型

## 1.不定积分与原函数存在性

###### **概念[1]:原函数与不定积分的基本概念**

[1]原函数定义: 设函数 $f(x)$ 定义在区间 $I$ 上，若存在可导函数 $F(x)$，对于该区间上任意一点都有 $F'(x) = f(x)$，则称 $F(x)$ 是 $f(x)$ 在区间 $I$ 上的一个原函数。

[2]不定积分定义: 称 $\int f(x)\,\mathrm{d}x = F(x) + C$ 为 $f(x)$ 在区间 $I$ 上的不定积分(表示全体原函数的集合)。

>注: 谈到原函数与不定积分，必须指明定义区间。

###### **定理[1]:原函数(不定积分)存在定理与导函数的形态限制**

[1]存在充分条件(必有): 若 $f(x)$ 在区间 $I$ 上连续，则 $f(x)$ 必有原函数。

>构造性证明: 设 $F(x) = \int_a^x f(t)\,\mathrm{d}t$(变上限积分)，由积分中值定理可证 $F'(x) = f(x)$。

[2]不存在充分条件(必无): 含有第一类间断点(可去、跳跃)或无穷间断点的函数，在包含该间断点的区间内必无原函数。

>[1]达布定理(导数介值性): 若 $F(x)$ 在 $[a, b]$ 可导，则导函数 $F'(x)$ 在区间内介于任意两导数值之间的值都能取到，因此导函数不能出现跳跃。
>
>[2]洛必达求导法则的反证: 若假设可去、跳跃或无穷间断点处存在原函数，根据导数定义 $\lim\limits_{x \to x_0} \frac{F(x)-F(x_0)}{x-x_0} \stackrel{\text{洛}}{=} \lim\limits_{x \to x_0} F'(x)$，必导出矛盾。

[3]不定情况(可能有，也可能没有): 含有振荡间断点的函数。

>[1]有原函数的例子: $f(x) = \begin{cases} 2x\sin\frac{1}{x} - \cos\frac{1}{x}, & x \neq 0 \\ 0, & x = 0 \end{cases}$，原函数为 $F(x) = \begin{cases} x^2\sin\frac{1}{x}, & x \neq 0 \\ 0, & x = 0 \end{cases}$。
>
>[2]无原函数的例子: $f(x) = \begin{cases} \frac{1}{x}\sin\frac{1}{x}, & x \neq 0 \\ 0, & x = 0 \end{cases}$。

###### **原理[1]:【核心直观与小故事总结】导数为什么不会突变？振荡间断点真的“断”了吗？**

>关于连续、导数与振荡间断点的微观几何小故事：
>
>[1]导函数的“点点相依”: 普通函数的值可以脱节独立(如跳跃点、孤立点)，但导数是差商的极限，它的存在天然要求两点之间“依附并充分靠近”。因此，如果导函数在某点的极限存在，这个极限值必须严格等于该点的导数值，导函数绝不可能产生第一类突变。
>
>[2]切线不会瞬时折断: 几何上，一条处处有切线的平滑曲线，切线斜率绝对无法在某一点发生瞬时跳跃。
>
>[3]振荡间断点并没有“断开”: 以典型反例 $f(x) = \sin\frac{1}{x}$ 为例，它被称为“间断”，仅仅是因为极限 $\lim\limits_{x \to 0} \sin\frac{1}{x}$ 不存在，不满足微积分中严格的“极限值 = 函数值”代数定义。若在显微镜下把 $x$ 轴无限放大无穷倍，其曲线仍然是一条连续蜿蜒、绵延不绝的完整曲线，点与点之间从未像跳跃间断那样撕开。正因如此，可导函数的导函数才被允许拥有这种虽然剧烈抖动、但实则紧密相连的“振荡间断”。

## 2.定积分的概念、几何意义与可积性

###### **概念[1]:黎曼定积分的定义(四步法)**

设函数 $f(x)$ 在闭区间 $[a, b]$ 上有界。

[1]分割: 在 $(a, b)$ 内任意插入 $n-1$ 个分点 $x_i$，将 $[a, b]$ 分成 $n$ 个小区间 $[x_{k-1}, x_k]$，记小区间的长度 $\Delta x_k = x_k - x_{k-1}$，并记模 $\lambda = \max\limits_{1 \leqslant k \leqslant n} \{\Delta x_k\}$。

[2]近似: 在每个小区间 $[x_{k-1}, x_k]$ 上任取一点 $\xi_k$，用矩形面积近似曲边梯形小条: $f(\xi_k)\Delta x_k$。

[3]求和: 将所有小矩形面积累加，得到黎曼和 $\sum\limits_{k=1}^n f(\xi_k)\Delta x_k$。

[4]取极限: 当 $\lambda \to 0$ 时，若极限 $\lim\limits_{\lambda \to 0} \sum\limits_{k=1}^n f(\xi_k)\Delta x_k$ 存在，且该极限值与分点 $x_i$ 的划分法及点 $\xi_k$ 的取法均无关，则称 $f(x)$ 在 $[a, b]$ 上黎曼可积，此极限值称为定积分：

$$\int_a^b f(x)\,\mathrm{d}x = \lim_{\lambda \to 0} \sum_{k=1}^n f(\xi_k)\Delta x_k$$

###### **原理[1]:历史与符号背景小记**

[1]积分符号 $\int$ 由德国数学家莱布尼茨(G. W. Leibniz)创立，源于拉丁文“总和(summa)”的首字母 $S$ 的拉长变形。

[2]定积分的现代严格定义是由德国数学家黎曼(B. Riemann)给出的，故通常称为黎曼积分。

###### **原理[2]:定积分的几何意义(代数和)**

[1]若 $f(x) \geqslant 0$，$\int_a^b f(x)\,\mathrm{d}x$ 表示曲边梯形的面积 $S$。

[2]若 $f(x) \leqslant 0$，$\int_a^b f(x)\,\mathrm{d}x$ 表示曲边梯形面积的负值 $-S$。

[3]若 $f(x)$ 符号变动，$\int_a^b f(x)\,\mathrm{d}x = S_{\text{上}} - S_{\text{下}}$($x$ 轴上方图形面积减去下方图形面积)。

###### **方法[1]:经典特取法与“定积分定义求极限”的标准型**

由于定积分的存在性独立于区间划分与介点选取，令“$n$ 等分”且“取每个小区间右端点 $\xi_k = a + \frac{b-a}{n}k$”：

$$\lim_{n \to \infty} \sum_{k=1}^n f\left(a + \frac{b-a}{n}k\right)\frac{b-a}{n} = \int_a^b f(x)\,\mathrm{d}x$$

标准 SOP 转化公式(区间 $[0, 1]$)：

$$\lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n f\left(\frac{i}{n}\right) = \int_0^1 f(x)\,\mathrm{d}x$$

>凑定义三部曲：
>
>[1]提公因子 $\frac{1}{n}$(视作 $\mathrm{d}x$)；
>
>[2]凑自变量形如 $\frac{i}{n}$(视作 $x$)；
>
>[3]确定求和指标范围，转化为 $\int_0^1 f(x)\,\mathrm{d}x$。

###### **原理[3]:积分与哑变量无关**

$$\int_a^b f(x)\,\mathrm{d}x = \int_a^b f(t)\,\mathrm{d}t = \int_a^b f(u)\,\mathrm{d}u$$

定积分的值是一个确定的实数值，仅取决于被积表达式与积分区间，与积分变量所用的字母符号无关。

###### **定理[1]:可积性(定积分存在定理)**

常义定积分的立足基础是区间有限且函数有界。

[1]必要条件: 若 $f(x)$ 在 $[a, b]$ 上可积，则 $f(x)$ 在 $[a, b]$ 上必有界。

>反之不成立: 有界函数不一定可积(例如狄利克雷函数在 $[0,1]$ 上有界但处处不可积)。

[2]充分条件(满足其一即必可积):

>[1]$f(x)$ 在 $[a, b]$ 上连续；
>
>[2]$f(x)$ 在 $[a, b]$ 上单调(单调函数必有界)；
>
>[3]$f(x)$ 在 $[a, b]$ 上有界，且只有有限个间断点；
>
>[4]$f(x)$ 在 $[a, b]$ 上只有有限个第一类间断点(第一类间断点处必局部有界)。

###### **定理[2]:定积分的运算性质**

设下列涉及的定积分均存在：

[1]零区间与换限规定:

>$\int_a^a f(x)\,\mathrm{d}x = 0$
>
>$\int_a^b f(x)\,\mathrm{d}x = -\int_b^a f(x)\,\mathrm{d}x$(当 $a > b$ 时)

[2]区间长度: $\int_a^b 1\,\mathrm{d}x = b - a$

[3]线性性质: $\int_a^b [k_1 f(x) \pm k_2 g(x)]\,\mathrm{d}x = k_1\int_a^b f(x)\,\mathrm{d}x \pm k_2\int_a^b g(x)\,\mathrm{d}x$

[4]区间可加性: 无论 $a, b, c$ 相对大小如何，总有 $\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x$

[5]保号性与单调性:

>[1]若在 $[a, b]$ 上 $f(x) \leqslant g(x)$(且 $a < b$)，则 $\int_a^b f(x)\,\mathrm{d}x \leqslant \int_a^b g(x)\,\mathrm{d}x$。
>
>[2]绝对值不等式: $\left\vert{}\int_a^b f(x)\,\mathrm{d}x\right\vert{} \leqslant \int_a^b \vert{}f(x)\vert{}\,\mathrm{d}x$。
>
>[3]严格不等式推论: 设 $f(x)$ 在 $[a, b]$ 上连续、非负($f(x) \geqslant 0$)且 $f(x) \not\equiv 0$，则 $\int_a^b f(x)\,\mathrm{d}x > 0$。

[6]估值定理: 设 $M, m$ 分别为 $f(x)$ 在 $[a, b]$ 上的最大值和最小值，$L = b - a$，则：

$$m(b - a) \leqslant \int_a^b f(x)\,\mathrm{d}x \leqslant M(b - a)$$

[7]积分中值定理: 若 $f(x)$ 在 $[a, b]$ 上连续，则至少存在一点 $\xi \in [a, b]$，使得：

$$\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b - a)$$

>注: 若要求严格开区间 $\xi \in (a, b)$，可通过设变上限积分 $F(x) = \int_a^x f(t)\,\mathrm{d}t$，并在 $[a, b]$ 上应用拉格朗日中值定理严格导出。

## 3.变限积分函数

###### **概念[1]:变上限积分函数的定义**

当 $x$ 在 $[a, b]$ 上变动时，定积分 $\int_a^x f(t)\,\mathrm{d}t$ 确定了一个以积分上限 $x$ 为自变量的单值函数：

$$F(x) = \int_a^x f(t)\,\mathrm{d}t \quad (a \leqslant x \leqslant b)$$

同理可定义变下限积分 $\int_x^b f(t)\,\mathrm{d}t$ 及双限积分 $\int_{\varphi_1(x)}^{\varphi_2(x)} f(t)\,\mathrm{d}t$。

###### **定理[1]:关键性质与平滑性规律(积分升阶定理)**

变限积分运算会使原函数的性质“提升一级”：

[1]$f(x)$ 可积 $\implies F(x)$ 必处处连续:

>若 $f(x)$ 在区间 $I$ 上可积(例如有界且仅含有限个间断点)，则 $F(x) = \int_a^x f(t)\,\mathrm{d}t$ 在区间 $I$ 上处处连续。

[2]$f(x)$ 连续 $\implies F(x)$ 处处可导:

>若 $f(x)$ 在区间 $I$ 上连续，则 $F(x)$ 处处可导，且其导数为被积函数本身：
>
>$$F'(x) = \left[ \int_a^x f(t)\,\mathrm{d}t \right]' = f(x)$$

[3]被积函数间断点对变限积分可导性的映射规律:

>[1]跳跃间断点 $\to$ 尖点(不可导点):
>
>>若 $x = x_0$ 是 $f(x)$ 的跳跃间断点，则 $F(x)$ 在 $x = x_0$ 处不可导。
>>
>>其左右导数分别等于被积函数的左右极限：
>>
>>$$F'_-(x_0) = \lim_{x \to x_0^-} f(x) = f(x_0^-), \quad F'_+(x_0) = \lim_{x \to x_0^+} f(x) = f(x_0^+)$$
>>
>>因左右极限不相等，故 $F'(x_0)$ 不存在。
>
>[2]可去间断点 $\to$ 可导点(导数等于极限值):
>
>>若 $x = x_0$ 是 $f(x)$ 的可去间断点，则 $F(x)$ 在 $x = x_0$ 处处处可导，且：
>>
>>$$F'(x_0) = \lim_{x \to x_0} f(x) \neq f(x_0)$$
>>
>>注: 此时虽然 $F'(x_0)$ 存在，但 $F'(x_0) \neq f(x_0)$，说明 $F(x)$ 并不是 $f(x)$ 的原函数(原函数要求 $F'(x) = f(x)$ 严格成立)。

## 4.反常积分(广义积分)

常义定积分基于“有限区间”与“有界函数”。破坏这两个条件即产生反常积分。奇点与无穷统称为反常积分的奇点。

>重要原则: 一个积分号内只能含有一个奇点，多于一个奇点必须拆分。

###### **概念[1]:无穷区间反常积分**

[1]单侧无穷上限: $\int_a^{+\infty} f(x)\,\mathrm{d}x = \lim\limits_{x \to +\infty} F(x) - F(a)$(极限存在则收敛，否则发散)

[2]单侧无穷下限: $\int_{-\infty}^b f(x)\,\mathrm{d}x = F(b) - \lim\limits_{x \to -\infty} F(x)$

[3]双侧无穷区间: $\int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = \int_{-\infty}^{c} f(x)\,\mathrm{d}x + \int_c^{+\infty} f(x)\,\mathrm{d}x$

>两端必须同时收敛才收敛，只要有一侧发散即严格发散。

###### **概念[2]:无界函数的反常积分(瑕积分)**

若被积函数在积分点附近趋向无穷，该点称为瑕点：

[1]$x = a$ 为唯一瑕点: $\int_a^b f(x)\,\mathrm{d}x = F(b) - \lim\limits_{x \to a^+} F(x)$

[2]$x = b$ 为唯一瑕点: $\int_a^b f(x)\,\mathrm{d}x = \lim\limits_{x \to b^-} F(x) - F(a)$

[3]$x = c \in (a, b)$ 为区间内部瑕点: $\int_a^b f(x)\,\mathrm{d}x = \int_a^c f(x)\,\mathrm{d}x + \int_c^b f(x)\,\mathrm{d}x$(两侧必须均收敛)

###### **定理[1]:敛散性比较判别法与极限形式**

设 $f(x), g(x)$ 非负：

[1]比较审敛准则: 大收则小收，小发则大发。

[2]极限形式(设 $\lim \frac{f(x)}{g(x)} = \lambda$):

>[1]$0 < \lambda < +\infty$: $\int f$ 与 $\int g$ 同敛散；
>
>[2]$\lambda = 0$: 若 $\int g$ 收敛，则 $\int f$ 必收敛；
>
>[3]$\lambda = +\infty$: 若 $\int g$ 发散，则 $\int f$ 必发散。

###### **定理[2]:考研必背的两大标准 $p$-积分**

| **类型** | **积分形式** | **收敛条件** | **发散条件** | **记忆直观内核** |
| :--- | :--- | :--- | :--- | :--- |
| **无穷区间型** | $\int_a^{+\infty} \frac{1}{x^p}\,\mathrm{d}x \quad (a > 0)$ | **$p > 1$** | **$p \leqslant 1$** | 趋向无穷大时，分母次数越大，衰减到 $0$ 的速度越快，面积越容易收敛。 |
| **瑕积分型** | $\int_0^a \frac{1}{x^p}\,\mathrm{d}x \quad (a > 0)$ | **$0 < p < 1$** | **$p \geqslant 1$** | 趋向零点时，分母次数越小，冲向无穷大的速度越慢，面积越容易被圈住收敛。 |

对称区间奇偶性结论(若反常积分 $\int_0^{+\infty} f(x)\,\mathrm{d}x$ 收敛)：

>[1]$f(x)$ 为偶函数 $\implies \int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = 2\int_0^{+\infty} f(x)\,\mathrm{d}x$
>
>[2]$f(x)$ 为奇函数 $\implies \int_{-\infty}^{+\infty} f(x)\,\mathrm{d}x = 0$

## 5.核心解题方法体系总结

###### **方法[1]:反常积分审敛的“阶数压制”与四大基准型**

反常积分的敛散性本质是比较收敛或发散的速度。对含有对数因子 $\ln x$ 的积分，牢记：对数是“最弱无穷大”和“最弱无穷小”，在多项式阶数面前任何正幂次 $\varepsilon > 0$ 都可以将其实质压制。

[1]基准一(无穷区间标准型):

$$\int_a^{+\infty} \frac{1}{x^p}\,\mathrm{d}x \begin{cases} \text{收敛}, & p > 1 \\ \text{发散}, & p \leqslant 1 \end{cases} \qquad \int_a^{+\infty} \frac{\ln x}{x^p}\,\mathrm{d}x \begin{cases} \text{收敛}, & p > 1 \\ \text{发散}, & p \leqslant 1 \end{cases}$$

[2]基准二(瑕积分标准型):

$$\int_0^a \frac{1}{x^p}\,\mathrm{d}x \begin{cases} \text{收敛}, & 0 < p < 1 \\ \text{发散}, & p \geqslant 1 \end{cases} \qquad \int_0^a \frac{\vert{}\ln x\vert{}}{x^p}\,\mathrm{d}x \begin{cases} \text{收敛}, & 0 \leqslant p < 1 \\ \text{发散}, & p \geqslant 1 \end{cases}$$

[3]补充(复合对数型，利用直接积分):

$$\int_2^{+\infty} \frac{1}{x \ln^p x}\,\mathrm{d}x = \int_{\ln 2}^{+\infty} \frac{1}{u^p}\,\mathrm{d}u \begin{cases} \text{收敛}, & p > 1 \\ \text{发散}, & p \leqslant 1 \end{cases}$$

###### **方法[2]:“定积分定义求和式极限”标准操作SOP**

遇到 $n$ 项和极限 $\lim\limits_{n \to \infty} \sum$，判定依据：

[1]定积分定义法标志: 分子分母中变量 $i$ 与 $n$ 的最高次数相同，能凑出公因子 $\frac{1}{n}$ 与变量 $\frac{i}{n}$。

>[1]提公因子: 提取 $\frac{1}{n} \to \mathrm{d}x$；
>
>[2]换元映射: 将余下表达式中的 $\frac{i}{n}$ 全换为自变量 $x$；
>
>[3]确定积分限: 求和范围 $i=1 \sim n$ 对应积分区间 $[0, 1]$。

[2]夹逼准则标志: 首尾项差异小，或者无法凑出统一的 $\frac{i}{n}$ 时，先放缩分子或分母后应用夹逼准则。

## 6.经典例题精析

**例题[1]:原函数与复合求导还原**

当 $0 < x < 1$ 时，$\int (1-x^2)f(x^2)\,\mathrm{d}x = \arcsin x + C$，则 $f(x) = (\quad)$

(A) $(1-x)^{\frac{3}{2}} \qquad$ (B) $(1-x)^{-\frac{3}{2}} \qquad$ (C) $\frac{1}{2}(1-x)^{-\frac{1}{2}} \qquad$ (D) $\frac{1}{2}(1-x)^{-\frac{3}{2}}$

主要思路:两端关于自变量 $x$ 求导消去不定积分号，解出被积复合表达式，再通过简单换元还原函数 $f(x)$

>[1]等式两端关于 $x$ 求导：
>
>根据不定积分与微分的互逆运算性质，方程两边对 $x$ 求导：
>
>$$\frac{\mathrm{d}}{\mathrm{d}x}\left[ \int (1-x^2)f(x^2)\,\mathrm{d}x \right] = \frac{\mathrm{d}}{\mathrm{d}x}(\arcsin x + C)$$
>
>直接脱去积分号得：
>
>$$(1-x^2)f(x^2) = \frac{1}{\sqrt{1-x^2}}$$
>
>[2]解出复合表达式：
>
>$$f(x^2) = \frac{1}{(1-x^2)\sqrt{1-x^2}} = (1-x^2)^{-\frac{3}{2}}$$
>
>[3]换元还原自变量：
>
>令 $u = x^2$，因为 $0 < x < 1$，所以 $0 < u < 1$，代入得：
>
>$$f(u) = (1-u)^{-\frac{3}{2}} \implies f(x) = (1-x)^{-\frac{3}{2}}$$
>
>[4]故正确选项为 **(B)**。

**例题[2]:分段函数的原函数求解与分段常数匹配**

设 $f(x) = \begin{cases} \frac{1}{\sqrt{1+x^2}}, & x \leqslant 0 \\ (x+1)\cos x, & x > 0 \end{cases}$，则 $f(x)$ 的一个原函数为 $(\quad)$

(A) $F(x) = \begin{cases} \ln(\sqrt{1+x^2}-x), & x \leqslant 0 \\ (x+1)\cos x - \sin x, & x > 0 \end{cases}$
(B) $F(x) = \begin{cases} \ln(\sqrt{1+x^2}+x) + 1, & x \leqslant 0 \\ (x+1)\sin x + \cos x, & x > 0 \end{cases}$
(C) $F(x) = \begin{cases} \ln(\sqrt{1+x^2}+x), & x \leqslant 0 \\ (x+1)\sin x + \cos x, & x > 0 \end{cases}$
(D) $F(x) = \begin{cases} \ln(\sqrt{1+x^2}-x) + 1, & x \leqslant 0 \\ (x+1)\cos x + \sin x, & x > 0 \end{cases}$

主要思路:对两侧区间分别求不定积分引入独立常数，根据原函数在分段点处必须严格连续确定分段常数间的约束关系

>[1]分段求不定积分：
>
>当 $x < 0$ 时：
>
>$$F_1(x) = \int \frac{1}{\sqrt{1+x^2}}\,\mathrm{d}x = \ln(x + \sqrt{1+x^2}) + C_1$$
>
>当 $x > 0$ 时，应用分部积分法：
>
>$$F_2(x) = \int (x+1)\cos x\,\mathrm{d}x = \int (x+1)\,\mathrm{d}(\sin x) = (x+1)\sin x - \int \sin x\,\mathrm{d}x = (x+1)\sin x + \cos x + C_2$$
>
>[2]利用连续性匹配常数：
>
>因为 $f(x)$ 在 $\mathbb{R}$ 上处处连续，其原函数 $F(x)$ 必处处可导，因而在分界点 $x = 0$ 处必连续：
>
>$$\lim_{x \to 0^-} F_1(x) = \lim_{x \to 0^+} F_2(x) = F(0)$$
>
>左极限：$\lim\limits_{x \to 0^-} [\ln(x + \sqrt{1+x^2}) + C_1] = \ln 1 + C_1 = C_1$
>
>右极限：$\lim\limits_{x \to 0^+} [(x+1)\sin x + \cos x + C_2] = 0 + 1 + C_2 = 1 + C_2$
>
>故要求：$C_1 = 1 + C_2$。
>
>[3]选取特定常数：
>
>取 $C_2 = 0$，则 $C_1 = 1$，得到原函数：
>
>$$F(x) = \begin{cases} \ln(x + \sqrt{1+x^2}) + 1, & x \leqslant 0 \\ (x+1)\sin x + \cos x, & x > 0 \end{cases}$$
>
>[4]故正确选项为 **(B)**。

**例题[3]:符号函数原函数与可积性判定**

在 $[-1, 2]$ 上，下列关于函数性质的命题中正确的个数为 $(\quad)$

① $f(x) = \begin{cases} 2, & x > 0 \\ 1, & x = 0 \\ -1, & x < 0 \end{cases}$ 无原函数，但定积分存在；
② $f(x) = \begin{cases} 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2}, & x \neq 0 \\ 0, & x = 0 \end{cases}$ 有原函数，但定积分不存在；
③ $f(x) = \frac{1}{x}$ 在 $[-1, 2]$ 上既无原函数，定积分也不存在；
④ 只要函数在闭区间上有界，就必定存在原函数。

(A) 1 \qquad (B) 2 \qquad (C) 3 \qquad (D) 4

主要思路:紧扣原函数存在定理(达布定理与第一类间断点必无原函数)与定积分存在定理(有界性必要条件与有限间断点充分条件)逐一研判

>[1]分析命题①：
>
>$x = 0$ 是 $f(x)$ 的第一类跳跃间断点，根据达布定理，导函数不能跳跃，故在包含 $0$ 的区间内必无原函数；但 $f(x)$ 在 $[-1, 2]$ 上有界且仅有 1 个间断点，由充分条件知定积分必定存在。命题①正确。
>
>[2]分析命题②：
>
>构造函数 $F(x) = \begin{cases} x^2\sin\frac{1}{x^2}, & x \neq 0 \\ 0, & x = 0 \end{cases}$。由导数定义：
>
>$$F'(0) = \lim_{x \to 0} \frac{x^2\sin(1/x^2) - 0}{x} = \lim_{x \to 0} x\sin\frac{1}{x^2} = 0 = f(0)$$
>
>当 $x \neq 0$ 时求导：$F'(x) = 2x\sin\frac{1}{x^2} - \frac{2}{x}\cos\frac{1}{x^2} = f(x)$。故 $F(x)$ 是全区间上的原函数。
>
>但当 $x \to 0$ 时 $-\frac{2}{x}\cos\frac{1}{x^2}$ 无界，常义定积分要求被积函数必须有界，故定积分不存在。命题②正确。
>
>[3]分析命题③：
>
>$x = 0$ 是无穷间断点，含有无穷间断点的函数必无原函数；函数在 $[-1, 2]$ 上无界，定积分必不存在。命题③正确。
>
>[4]分析命题④：
>
>命题①中的跳跃间断点函数在 $[-1, 2]$ 上有界，但无原函数，故有界不能保证原函数存在。命题④错误。
>
>[5]综上，正确的命题为 ①②③，共 3 个。故正确选项为 **(C)**。

**例题[4]:严格递增反函数积分与矩形面积大小比较(杨不等式几何直观)**

设可导函数 $y = f(x)$ 在 $[0, +\infty)$ 上的值域为 $[0, +\infty)$，$f(0) = 0$，$f'(x) > 0$。$x = \varphi(y)$ 是 $y = f(x)$ 的反函数。记 $I = \int_0^a f(x)\,\mathrm{d}x + \int_0^b \varphi(y)\,\mathrm{d}y$。若 $a, b > 0$ 且 $a < \varphi(b)$，则 $(\quad)$

(A) $I > ab \qquad$ (B) $I < ab \qquad$ (C) $I = ab \qquad$ (D) $I$ 与 $ab$ 的大小关系不确定

主要思路:将两个定积分分别对应为以 $x$ 轴与以 $y$ 轴为底的曲边梯形面积，根据反函数单调性及点与曲线位置关系分析几何重叠

>[1]几何意义对应：
>
>$\int_0^a f(x)\,\mathrm{d}x$ 表示曲线 $y = f(x)$、直线 $x = a$ 与 $x$ 轴围成的图形面积；
>
>$\int_0^b \varphi(y)\,\mathrm{d}y$ 表示曲线 $x = \varphi(y)$、直线 $y = b$ 与 $y$ 轴围成的图形面积。
>
>[2]分析点与曲线位置关系：
>
>已知 $f'(x) > 0$，$f(x)$ 严格单调增加，其反函数 $\varphi(y)$ 亦严格单调增加。
>
>$$a < \varphi(b) \iff f(a) < b$$
>
>这表明点 $(a, b)$ 严格位于曲线 $y = f(x)$ 的上方。
>
>[3]面积拼接与杨不等式：
>
>以原点 $(0, 0)$ 和点 $(a, b)$ 为对角顶点的矩形面积为 $S_{\text{矩形}} = ab$。
>
>观察两部分积分区域的几何拼接：两部分曲边梯形完全覆盖了该矩形，并且在点 $(a, f(a))$ 到 $(a, b)$ 之间超出了矩形边界，多出了凸起区域：
>
>$$I = \int_0^a f(x)\,\mathrm{d}x + \int_0^b \varphi(y)\,\mathrm{d}y = ab + \int_{f(a)}^b [\varphi(y) - a]\,\mathrm{d}y$$
>
>因为当 $y \in (f(a), b)$ 时恒有 $\varphi(y) > a$，多出的积分严格大于 0：
>
>$$\int_{f(a)}^b [\varphi(y) - a]\,\mathrm{d}y > 0 \implies I > ab$$
>
>[4]故正确选项为 **(A)**。

**例题[5]:振荡衰减函数拱形面积级数求和**

曲线 $y = e^{-x}\sin x$ 在 $[0, +\infty)$ 上与 $x$ 轴围成的所有拱形区域的总面积记为 $S$，求其表达式与具体数值。

主要思路:定积分几何面积需加绝对值，将全区间按正弦零点拆分为无穷多个正负交替的小拱形，计算单拱面积后转化为无穷等比级数求和

>[1]确定拱形分界点：
>
>曲线与 $x$ 轴的交点由 $\sin x = 0$ 决定，零点为 $x_k = k\pi$ ($k = 0, 1, 2, \dots$)。
>
>在每个区间 $[k\pi, (k+1)\pi]$ 内，被积函数符号恒定，围成的单拱面积为：
>
>$$S_k = \int_{k\pi}^{(k+1)\pi} \vert{}e^{-x}\sin x\vert{}\,\mathrm{d}x = \int_{k\pi}^{(k+1)\pi} e^{-x} (-1)^k \sin x\,\mathrm{d}x$$
>
>[2]变量代换计算第 $k$ 拱面积：
>
>令 $t = x - k\pi$，则 $x = t + k\pi$，$\mathrm{d}x = \mathrm{d}t$：
>
>$$S_k = \int_0^\pi e^{-(t+k\pi)} (-1)^k \sin(t+k\pi)\,\mathrm{d}t = e^{-k\pi} \int_0^\pi e^{-t}\sin t\,\mathrm{d}t$$
>
>[3]计算首拱定积分：
>
>利用常用分部积分公式：
>
>$$\int_0^\pi e^{-t}\sin t\,\mathrm{d}t = \left. \frac{e^{-t}(-\sin t - \cos t)}{(-1)^2 + 1^2} \right\vert{}_0^\pi = \frac{e^{-\pi}(1) - (-1)}{2} = \frac{1 + e^{-\pi}}{2}$$
>
>故各拱面积构成公比为 $q = e^{-\pi} < 1$ 的等比数列：
>
>$$S_k = \frac{1 + e^{-\pi}}{2} (e^{-\pi})^k$$
>
>[4]等比级数求和：
>
>$$S = \sum_{k=0}^\infty S_k = \frac{1 + e^{-\pi}}{2} \sum_{k=0}^\infty (e^{-\pi})^k = \frac{1 + e^{-\pi}}{2} \cdot \frac{1}{1 - e^{-\pi}} = \frac{e^\pi + 1}{2(e^\pi - 1)}$$
>
>[5]结论：总面积表达式为 $\int_0^{+\infty} e^{-x}\vert{}\sin x\vert{}\,\mathrm{d}x = \frac{e^\pi + 1}{2(e^\pi - 1)}$。

**例题[6]:定积分定义求解连和式极限的标准型转化**

$\lim\limits_{n \to \infty} \left( \frac{n+1}{n^2+1^2} + \frac{n+2}{n^2+2^2} + \frac{n+3}{n^2+3^2} + \dots + \frac{n+n}{n^2+n^2} \right) = (\quad)$

(A) $\int_0^1 \frac{1+x}{1+x^2}\,\mathrm{d}x \qquad$ (B) $\int_0^1 \frac{1}{1+x}\,\mathrm{d}x \qquad$ (C) $\int_0^1 \frac{x}{1+x^2}\,\mathrm{d}x \qquad$ (D) $\int_0^1 \frac{2x}{1+x^2}\,\mathrm{d}x$

主要思路:用 $\Sigma$ 符号写出紧凑通项，提公因子 $\frac{1}{n}$ 对应微分 $\mathrm{d}x$，凑自变量 $\frac{i}{n}$ 对应 $x$，由定积分定义完成转化

>[1]用求和符号表示并提公因子：
>
>$$\text{原式} = \lim_{n \to \infty} \sum_{i=1}^n \frac{n+i}{n^2+i^2}$$
>
>分子分母同时提取 $n^2$：
>
>$$= \lim_{n \to \infty} \sum_{i=1}^n \frac{n\left(1 + \frac{i}{n}\right)}{n^2\left[1 + \left(\frac{i}{n}\right)^2\right]} = \lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n \frac{1 + \frac{i}{n}}{1 + \left(\frac{i}{n}\right)^2}$$
>
>[2]套用定积分定义：
>
>令 $\frac{i}{n} \to x$，$\frac{1}{n} \to \mathrm{d}x$，求和范围 $i=1 \sim n$ 对应积分限 $[0, 1]$：
>
>$$= \int_0^1 \frac{1+x}{1+x^2}\,\mathrm{d}x$$
>
>[3]求出极限值：
>
>$$\int_0^1 \frac{1+x}{1+x^2}\,\mathrm{d}x = \int_0^1 \frac{1}{1+x^2}\,\mathrm{d}x + \frac{1}{2}\int_0^1 \frac{\mathrm{d}(1+x^2)}{1+x^2} = \left. \left[ \arctan x + \frac{1}{2}\ln(1+x^2) \right] \right\vert{}_0^1 = \frac{\pi}{4} + \frac{1}{2}\ln 2$$
>
>[4]故正确选项为 **(A)**。

**例题[7]:非负连续非恒零函数积分严格保号性证明**

设 $f(x)$ 在 $[a, b]$ 上非负连续，且 $f(x) \not\equiv 0$，证明：$\int_a^b f(x)\,\mathrm{d}x > 0$。

主要思路:因非恒零必存在一处严格大于零的点，由连续函数局部保号性锁定一个闭正邻域，将全区间积分拆分放缩，说明积分值严格大于零

>[1]锁定正值点并应用局部保号性：
>
>因为 $f(x) \geqslant 0$ 且 $f(x) \not\equiv 0$，必存在点 $x_0 \in (a, b)$，使得 $f(x_0) = \sigma > 0$。
>
>由 $f(x)$ 在点 $x_0$ 处的连续性，取 $\varepsilon = \frac{\sigma}{2} > 0$，存在 $\delta > 0$(可设 $[x_0-\delta, x_0+\delta] \subset [a, b]$)，使得当 $x \in [x_0-\delta, x_0+\delta]$ 时，恒有：
>
>$$f(x) \geqslant \frac{\sigma}{2} > 0$$
>
>[2]拆分积分区间进行放缩：
>
>由定积分的区间可加性：
>
>$$\int_a^b f(x)\,\mathrm{d}x = \int_a^{x_0-\delta} f(x)\,\mathrm{d}x + \int_{x_0-\delta}^{x_0+\delta} f(x)\,\mathrm{d}x + \int_{x_0+\delta}^b f(x)\,\mathrm{d}x$$
>
>因为 $f(x) \geqslant 0$，第一项和第三项积分均 $\geqslant 0$：
>
>$$\geqslant \int_{x_0-\delta}^{x_0+\delta} f(x)\,\mathrm{d}x \geqslant \int_{x_0-\delta}^{x_0+\delta} \frac{\sigma}{2}\,\mathrm{d}x = \frac{\sigma}{2} \cdot 2\delta = \sigma \delta > 0$$
>
>[3]结论：故严格证得 $\int_a^b f(x)\,\mathrm{d}x > 0$。

**例题[8]:积分第一中值定理与介值定理严格证明**

设 $f(x)$ 在 $[a, b]$ 上连续，证明：存在 $\xi \in [a, b]$，使得 $\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$。

主要思路:利用闭区间连续函数必能取得最值进行估值，由介值定理直接说明均值必能在区间上被取得

>[1]最值定理与积分估值：
>
>因为 $f(x)$ 在闭区间 $[a, b]$ 上连续，由最值定理可知 $f(x)$ 在 $[a, b]$ 上必有最大值 $M$ 和最小值 $m$，对任意 $x \in [a, b]$ 恒有：
>
>$$m \leqslant f(x) \leqslant M$$
>
>两端同时在 $[a, b]$ 上积分：
>
>$$\int_a^b m\,\mathrm{d}x \leqslant \int_a^b f(x)\,\mathrm{d}x \leqslant \int_a^b M\,\mathrm{d}x \implies m(b-a) \leqslant \int_a^b f(x)\,\mathrm{d}x \leqslant M(b-a)$$
>
>两端除以区间长度 $(b-a > 0)$：
>
>$$m \leqslant \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x \leqslant M$$
>
>[2]应用介值定理得出结论：
>
>实数 $\mu = \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x$ 介于最小值 $m$ 与最大值 $M$ 之间。由闭区间连续函数的介值定理，在 $[a, b]$ 上至少存在一点 $\xi \in [a, b]$，使得：
>
>$$f(\xi) = \mu \implies \int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$$
>
>[3]补充(严格开区间深化)：
>
>若需证明 $\xi \in (a, b)$，构造辅助函数 $F(x) = \int_a^x f(t)\,\mathrm{d}t$。因 $F(x)$ 在 $[a, b]$ 上连续，在 $(a, b)$ 内可导且 $F'(x) = f(x)$，由拉格朗日中值定理：
>
>$$F(b) - F(a) = F'(\xi)(b-a) \implies \int_a^b f(t)\,\mathrm{d}t = f(\xi)(b-a) \quad (\xi \in (a, b))$$

**例题[9]:定积分大小比较与被积函数不等式链**

设 $I_1 = \int_0^{\frac{\pi}{4}} \frac{\tan x}{x}\,\mathrm{d}x$，$I_2 = \int_0^{\frac{\pi}{4}} \frac{x}{\tan x}\,\mathrm{d}x$，$I_3 = \int_0^{\frac{\pi}{4}} \frac{\sin x}{x}\,\mathrm{d}x$，则 $(\quad)$

(A) $I_1 > I_2 > I_3 \qquad$ (B) $I_1 > I_3 > I_2 \qquad$ (C) $I_3 > I_1 > I_2 \qquad$ (D) $I_2 > I_1 > I_3$

主要思路:在区间 $(0, \frac{\pi}{4})$ 内利用经典几何三角不等式链比较被积函数大小，结合定积分保序性直接排序

>[1]建立不等式链：
>
>当 $x \in (0, \frac{\pi}{4})$ 时，根据经典三角几何不等式：
>
>$$\sin x < x < \tan x$$
>
>[2]分析各被积函数与常数 1 的关系：
>
>- 对于 $I_1$：因 $\tan x > x > 0$，故 $\frac{\tan x}{x} > 1$；
>- 对于 $I_2$：因 $x < \tan x$，故 $\frac{x}{\tan x} < 1$；
>- 对于 $I_3$：因 $\sin x < x$，故 $\frac{\sin x}{x} < 1$。
>
>由此立即锁定 $I_1$ 最大(排除 C、D)。
>
>[3]比较 $I_2$ 与 $I_3$ 的被积函数：
>
>在 $(0, \frac{\pi}{4})$ 上恒有 $\cos x < \frac{\sin x}{x} \implies \frac{x}{\tan x} < 1$。
>
>进一步由泰勒展开：$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \dots$，$\frac{x}{\tan x} = 1 - \frac{x^2}{3} + \dots$。
>
>故在 $(0, \frac{\pi}{4})$ 上恒有：
>
>$$\frac{\tan x}{x} > 1 > \frac{\sin x}{x} > \frac{x}{\tan x}$$
>
>[4]积分保序性得出结论：
>
>$$I_1 > I_3 > I_2$$
>
>[5]故正确选项为 **(B)**。

**例题[10]:三角复合函数单调性与区间对称换元比较**

设 $M = \int_0^{\frac{\pi}{2}} \sin(\sin x)\,\mathrm{d}x$，$N = \int_0^{\frac{\pi}{2}} \cos(\cos x)\,\mathrm{d}x$，则 $(\quad)$

(A) $M < 1 < N \qquad$ (B) $M < N < 1 \qquad$ (C) $N < M < 1 \qquad$ (D) $1 < M < N$

主要思路:对 $M$ 利用 $\sin x < x$ 及正弦单调性放缩；对 $N$ 进行区间再现换元 $x = \frac{\pi}{2} - t$，利用余弦单调性放缩

>[1]估计积分 $M$ 的上界：
>
>当 $x \in (0, \frac{\pi}{2})$ 时，由三角不等式知 $\sin x < x$。
>
>因为正弦函数在 $(0, 1)$ 上严格单调递增，故：
>
>$$\sin(\sin x) < \sin x$$
>
>两端同时在 $[0, \frac{\pi}{2}]$ 上积分：
>
>$$M = \int_0^{\frac{\pi}{2}} \sin(\sin x)\,\mathrm{d}x < \int_0^{\frac{\pi}{2}} \sin x\,\mathrm{d}x = \left. (-\cos x) \right\vert{}_0^{\frac{\pi}{2}} = 1$$
>
>[2]估计积分 $N$ 的下界：
>
>对积分 $N$ 做区间再现变量代换，令 $x = \frac{\pi}{2} - t$：
>
>$$N = \int_0^{\frac{\pi}{2}} \cos\left(\cos\left(\frac{\pi}{2}-t\right)\right)\,\mathrm{d}t = \int_0^{\frac{\pi}{2}} \cos(\sin t)\,\mathrm{d}t$$
>
>在 $(0, \frac{\pi}{2})$ 上，$\sin t < t$。
>
>因为余弦函数在 $(0, \frac{\pi}{2})$ 上严格单调递减，自变量较小者函数值更大：
>
>$$\cos(\sin t) > \cos t$$
>
>两端同时积分：
>
>$$N = \int_0^{\frac{\pi}{2}} \cos(\sin t)\,\mathrm{d}t > \int_0^{\frac{\pi}{2}} \cos t\,\mathrm{d}t = \left. (\sin t) \right\vert{}_0^{\frac{\pi}{2}} = 1$$
>
>[3]综合得出结论：
>
>$$M < 1 < N$$
>
>[4]故正确选项为 **(A)**。

**例题[11]:间断点在变上限积分中的连续性与可导性传导**

设函数 $y = f(x)$ 在 $[-1, 3]$ 上的图像已知，其中 $x = 0$ 为可去间断点，$x = 2$ 为跳跃间断点。分析变上限积分 $F(x) = \int_0^x f(t)\,\mathrm{d}t$ 的图形特征。

主要思路:根据变上限积分平滑性定理，有界可积函数的变上限积分处处连续，可去间断点处光滑可导，跳跃间断点处不可导（呈现尖点）

>[1]全区间连续性分析：
>
>由于 $f(x)$ 在 $[-1, 3]$ 上只有有限个第一类间断点(可去间断点与跳跃间断点)，故 $f(x)$ 有界且可积。
>
>根据变上限积分平滑性定理，$F(x) = \int_0^x f(t)\,\mathrm{d}t$ 在整个闭区间 $[-1, 3]$ 上必处处连续，曲线绝无断开。
>
>[2]可去间断点 $x = 0$ 处的可导性：
>
>在可去间断点处，极限值 $A = \lim\limits_{x \to 0} f(x)$ 存在。
>
>根据导数定义与洛必达法则：
>
>$$F'(0) = \lim_{x \to 0} \frac{F(x) - F(0)}{x} = \lim_{x \to 0} \frac{\int_0^x f(t)\,\mathrm{d}t}{x} \stackrel{\text{洛}}{=} \lim_{x \to 0} f(x) = A$$
>
>故 $F(x)$ 在 $x = 0$ 处处处可导，其几何图像在 $x = 0$ 处平滑且具有切线。
>
>[3]跳跃间断点 $x = 2$ 处的不可导性：
>
>在跳跃间断点处，左右极限存在但不相等：$f(2^-) \neq f(2^+)$。
>
>变上限积分的单侧导数严格等于被积函数的单侧极限：
>
>$$F'_-(2) = f(2^-), \quad F'_+(2) = f(2^+)$$
>
>因为 $F'_-(2) \neq F'_+(2)$，左右导数不相等，故 $F'(2)$ 不存在。
>
>几何图像在 $x = 2$ 处形成尖点(折角)。
>
>[4]结论：$F(x)$ 曲线在全区间处处连续，在 $x = 0$ 处光滑可导，在 $x = 2$ 处不可导且形成尖点。

**例题[12]:分段函数变上限积分的可导性与导数计算**

设 $f(x) = \begin{cases} \cos x, & 0 \leqslant x < \pi \\ 1, & \pi \leqslant x \leqslant 2\pi \end{cases}$，$F(x) = \int_0^x f(t)\,\mathrm{d}t$，则 $(\quad)$

(A) $x = \pi$ 是函数 $F(x)$ 的跳跃间断点
(B) $x = \pi$ 是函数 $F(x)$ 的可去间断点
(C) $F(x)$ 在 $x = \pi$ 处连续且可导
(D) $F(x)$ 在 $x = \pi$ 处连续但不可导

主要思路:检查分界点处被积函数的间断点类型，结合变上限积分对间断点的升阶作用进行判定

>[1]判定被积函数在分界点的性态：
>
>$\lim\limits_{x \to \pi^-} f(x) = \lim\limits_{x \to \pi^-} \cos x = \cos \pi = -1$
>
>$\lim\limits_{x \to \pi^+} f(x) = \lim\limits_{x \to \pi^+} 1 = 1$
>
>因为左右极限均存在但不相等，所以 $x = \pi$ 是被积函数 $f(x)$ 的第一类跳跃间断点。
>
>[2]变限积分的连续性与可导性：
>
>变限积分 $F(x)$ 在定义域上必定处处连续，故 $x = \pi$ 绝不是间断点(排除 A、B)；
>
>在跳跃间断点处，变上限积分的左右导数分别等于被积函数的左右极限：
>
>$$F'_-( \pi ) = f(\pi^-) = -1, \quad F'_+(\pi) = f(\pi^+) = 1$$
>
>因为 $F'_-( \pi ) \neq F'_+(\pi)$，导数不存在。
>
>[3]结论：$F(x)$ 在 $x = \pi$ 处连续但不可导。
>
>[4]故正确选项为 **(D)**。

**例题[13]:可去间断点函数变上限积分的处处可导性**

设 $f(x) = \begin{cases} e^{x^2} + x^2, & x \neq 0 \\ a, & x = 0 \end{cases}$，$a$ 为实常数，$F(x) = \int_0^x f(t)\,\mathrm{d}t$。讨论 $F(x)$ 在 $x = 0$ 处的可导性。

主要思路:利用导数定义转化为极限，被积函数在可去间断点处的极限存在即可保证变限积分可导，其导数值与孤立点定义值 $a$ 无关

>[1]考察被积函数的极限：
>
>$$\lim_{x \to 0} f(x) = \lim_{x \to 0} (e^{x^2} + x^2) = e^0 + 0 = 1$$
>
>若 $a \neq 1$，$x = 0$ 是可去间断点；若 $a = 1$，$f(x)$ 处处连续。
>
>[2]按导数定义计算 $F'(0)$：
>
>$$F'(0) = \lim_{x \to 0} \frac{F(x) - F(0)}{x - 0} = \lim_{x \to 0} \frac{\int_0^x f(t)\,\mathrm{d}t}{x}$$
>
>这是 $\frac{0}{0}$ 型未定式。根据洛必达法则：
>
>$$= \lim_{x \to 0} \frac{f(x)}{1} = \lim_{x \to 0} (e^{x^2} + x^2) = 1$$
>
>[3]结论分析：
>
>无论常数 $a$ 取何值(哪怕 $a \neq 1$)，极限始终存在且等于 1。
>
>故 $F(x)$ 在 $x = 0$ 处必定可导，且恒有 $F'(0) = 1$。
>
>注: 当 $a = 1$ 时 $F'(0) = f(0)$，$F(x)$ 是原函数；当 $a \neq 1$ 时，$F(x)$ 虽然可导，但 $F'(0) \neq f(0)$，不是原函数。

**例题[14]:变上限积分函数有界性证明(结合积分均值与指数衰减)**

设 $a > 0$，$f(x)$ 在 $[0, +\infty)$ 上有界，$C$ 为任意常数。证明：$y = e^{-ax}\left[ \int_0^x f(t)e^{at}\,\mathrm{d}t + C \right]$ 在 $[0, +\infty)$ 上有界。

主要思路:设出函数界的正数 $M$，将衰减因子 $e^{-ax}$ 乘入积分号内部，利用三角不等式与直接积分进行上界放大

>[1]设出函数界限：
>
>因为 $f(x)$ 在 $[0, +\infty)$ 上有界，存在常数 $M > 0$，使得对任意 $x \geqslant 0$，恒有 $\vert{}f(x)\vert{} \leqslant M$。
>
>[2]绝对值放大与拆分：
>
>$$\vert{}y\vert{} = \left\vert{} e^{-ax}\int_0^x f(t)e^{at}\,\mathrm{d}t + C e^{-ax} \right\vert{} \leqslant e^{-ax}\int_0^x \vert{}f(t)\vert{}e^{at}\,\mathrm{d}t + \vert{}C\vert{}e^{-ax}$$
>
>[3]代入上界进行积分估算：
>
>$$\leqslant M e^{-ax} \int_0^x e^{at}\,\mathrm{d}t + \vert{}C\vert{} \cdot 1 = M e^{-ax} \left[ \frac{e^{ax} - 1}{a} \right] + \vert{}C\vert{} = \frac{M}{a}(1 - e^{-ax}) + \vert{}C\vert{}$$
>
>[4]确定全局上界：
>
>因为对所有 $x \geqslant 0$，$a > 0$，恒有 $0 \leqslant 1 - e^{-ax} < 1$，所以：
>
>$$\vert{}y\vert{} < \frac{M}{a} + \vert{}C\vert{}$$
>
>右端为与自变量 $x$ 无关的确定正实数，故证得 $y$ 在 $[0, +\infty)$ 上有界。

**例题[15]:双奇点反常积分的拆分与参数收敛充要条件**

设 $a > b > 0$，讨论反常积分 $\int_0^{+\infty} \frac{1}{x^a + x^b}\,\mathrm{d}x$ 收敛的充要条件。

(A) $a > 1$ 且 $b > 1 \qquad$ (B) $a > 1$ 且 $b < 1 \qquad$ (C) $a < 1$ 且 $b < 1 \qquad$ (D) $a < 1$ 且 $b > 1$

主要思路:识别积分的两个奇点 $x = 0$(瑕点)与 $x = +\infty$(无穷)，拆分为两段分别由低次项和高次项主导，应用两大标准 $p$-积分判定

>[1]拆分双奇点：
>
>$$\int_0^{+\infty} \frac{1}{x^a + x^b}\,\mathrm{d}x = \int_0^1 \frac{1}{x^a + x^b}\,\mathrm{d}x + \int_1^{+\infty} \frac{1}{x^a + x^b}\,\mathrm{d}x = I_1 + I_2$$
>
>原积分收敛当且仅当 $I_1$ 与 $I_2$ 同时收敛。
>
>[2]分析瑕积分 $I_1$ ($x \to 0^+$)：
>
>当 $x \in (0, 1)$ 时，因为 $a > b > 0$，低次幂 $x^b$ 趋向 0 的速度慢于 $x^a$，起决定性主导作用：
>
>$$\frac{1}{x^a + x^b} = \frac{1}{x^b(1 + x^{a-b})} \sim \frac{1}{x^b} \quad (x \to 0^+)$$
>
>由标准瑕积分 $\int_0^1 \frac{1}{x^b}\,\mathrm{d}x$ 收敛充要条件可知：$b < 1$。
>
>[3]分析无穷积分 $I_2$ ($x \to +\infty$)：
>
>当 $x \to +\infty$ 时，较高次幂 $x^a$ 增长更快，起决定性主导作用：
>
>$$\frac{1}{x^a + x^b} = \frac{1}{x^a(1 + x^{b-a})} \sim \frac{1}{x^a} \quad (x \to +\infty)$$
>
>由标准无穷积分 $\int_1^{+\infty} \frac{1}{x^a}\,\mathrm{d}x$ 收敛充要条件可知：$a > 1$。
>
>[4]求交集得出充要条件：
>
>两端同时收敛的充要条件为：$a > 1$ 且 $b < 1$。
>
>[5]故正确选项为 **(B)**。

**例题[16]:等价无穷小代换与反常积分参数审敛**

反常积分 $\int_1^{+\infty} \left( e^{\frac{\cos\frac{1}{x}}{x}} - e^{\frac{1}{x}} \right) x^k\,\mathrm{d}x$ 收敛，则参数 $k$ 的取值范围是 $\underline{\hspace{2.5cm}}$。

主要思路:当 $x \to +\infty$ 时 $\frac{1}{x} \to 0$，利用等价无穷小与泰勒展开提取主部，比照无穷区间 $p$-积分基准确定参数范围

>[1]换元提取无穷小量：
>
>当 $x \to +\infty$ 时，令 $u = \frac{1}{x} \to 0^+$。被积表达式为：
>
>$$f(x) = \left( e^{u\cos u} - e^u \right) \cdot \frac{1}{u^k} = e^u \left( e^{u(\cos u - 1)} - 1 \right) \cdot \frac{1}{u^k}$$
>
>[2]展开主部无穷小：
>
>当 $u \to 0$ 时，$\cos u - 1 \sim -\frac{1}{2}u^2$：
>
>$$u(\cos u - 1) \sim u\left(-\frac{1}{2}u^2\right) = -\frac{1}{2}u^3$$
>
>由等价无穷小 $e^v - 1 \sim v$：
>
>$$e^{u(\cos u - 1)} - 1 \sim -\frac{1}{2}u^3$$
>
>因为 $e^u \to 1$，故被积函数的主部渐近行为为：
>
>$$f(x) \sim 1 \cdot \left(-\frac{1}{2}u^3\right) \cdot \frac{1}{u^k} = -\frac{1}{2} u^{3-k} = -\frac{1}{2} \cdot \frac{1}{x^{3-k}}$$
>
>[3]比照无穷区间 $p$-积分基准：
>
>反常积分 $\int_1^{+\infty} \frac{1}{x^{3-k}}\,\mathrm{d}x$ 收敛的充要条件是幂次严格大于 1：
>
>$$3 - k > 1 \implies k < 2$$
>
>[4]故参数 $k$ 的取值范围为 $k < 2$。

**例题[17]:反常积分敛散性的综合比较与判定**

下列反常积分中发散的是 $(\quad)$

(A) $\int_1^{+\infty} \left[ \ln\left(1 + \frac{1}{x}\right) - \frac{1}{1+x} \right]\,\mathrm{d}x$
(B) $\int_0^{+\infty} \frac{\ln x}{1+x^2}\,\mathrm{d}x$
(C) $\int_0^{+\infty} \frac{\arctan x}{x\sqrt{x}}\,\mathrm{d}x$
(D) $\int_1^{+\infty} \frac{1}{x\ln x}\,\mathrm{d}x$

主要思路:逐项检查各积分奇点处的阶数与渐近行为，运用泰勒展开及基准 $p$-积分判断敛散性

>[1]分析选项 (A)：
>
>当 $x \to +\infty$ 时，利用泰勒展开：
>
>$$\ln\left(1 + \frac{1}{x}\right) = \frac{1}{x} - \frac{1}{2x^2} + O\left(\frac{1}{x^3}\right)$$
>
>$$\frac{1}{1+x} = \frac{1}{x\left(1+\frac{1}{x}\right)} = \frac{1}{x} - \frac{1}{x^2} + O\left(\frac{1}{x^3}\right)$$
>
>两式相减，一次项消去：
>
>$$\ln\left(1 + \frac{1}{x}\right) - \frac{1}{1+x} = \frac{1}{2x^2} + O\left(\frac{1}{x^3}\right) \sim \frac{1}{2x^2}$$
>
>因为 $p = 2 > 1$，由极限比较审敛法知该积分收敛。
>
>[2]分析选项 (B)：
>
>包含 $x = 0$ 与 $x = +\infty$ 两个奇点：在 $x \to 0^+$ 处被积函数 $\sim \ln x$($p=0$ 对数瑕积分收敛)；在 $x \to +\infty$ 处被积函数 $\sim \frac{\ln x}{x^2}$($p=2>1$ 收敛)。故该积分收敛。
>
>[3]分析选项 (C)：
>
>在 $x \to 0^+$ 处，$\arctan x \sim x$，被积函数 $\sim \frac{x}{x^{3/2}} = \frac{1}{\sqrt{x}}$($p = 1/2 < 1$ 瑕积分收敛)；
>
>在 $x \to +\infty$ 处，$\arctan x \to \frac{\pi}{2}$，被积函数 $\sim \frac{\pi/2}{x^{3/2}}$($p = 3/2 > 1$ 无穷积分收敛)。故该积分收敛。
>
>[4]分析选项 (D)：
>
>应用凑微分法直接计算原函数：
>
>$$\int_1^{+\infty} \frac{1}{x\ln x}\,\mathrm{d}x = \int_1^{+\infty} \frac{\mathrm{d}(\ln x)}{\ln x} = \left. \ln(\ln x) \right\vert{}_1^{+\infty} = +\infty$$
>
>积分严格发散。
>
>[5]故正确选项为 **(D)**。

**例题[18]:瑕积分对数基准型的参数分类讨论**

已知 $\alpha > 0$，则对于瑕积分 $\int_0^1 \frac{\ln x}{x^\alpha}\,\mathrm{d}x$ 敛散性的判别，正确的是 $(\quad)$

(A) 当 $\alpha \geqslant 1$ 时收敛 \qquad (B) 当 $\alpha < 1$ 时收敛 \qquad (C) 恒收敛 \qquad (D) 恒发散

主要思路:应用分部积分法求出带有参数的原函数表达式，利用洛必达法则求极限，分析其收敛的充要条件

>[1]分部积分求原函数：
>
>当 $\alpha \neq 1$ 时：
>
>$$\int \frac{\ln x}{x^\alpha}\,\mathrm{d}x = \int \ln x\,\mathrm{d}\left( \frac{x^{1-\alpha}}{1-\alpha} \right) = \frac{x^{1-\alpha}\ln x}{1-\alpha} - \frac{1}{1-\alpha}\int x^{1-\alpha} \cdot \frac{1}{x}\,\mathrm{d}x = \frac{x^{1-\alpha}\ln x}{1-\alpha} - \frac{x^{1-\alpha}}{(1-\alpha)^2}$$
>
>[2]代入上下限考察 $x \to 0^+$ 时的极限：
>
>$$\int_0^1 \frac{\ln x}{x^\alpha}\,\mathrm{d}x = \left. \left[ \frac{x^{1-\alpha}\ln x}{1-\alpha} - \frac{x^{1-\alpha}}{(1-\alpha)^2} \right] \right\vert{}_0^1 = -\frac{1}{(1-\alpha)^2} - \lim_{x \to 0^+} \frac{x^{1-\alpha}\ln x}{1-\alpha}$$
>
>[3]分析极限存在性：
>
>只有当 $1 - \alpha > 0$(即 $\alpha < 1$) 时，利用洛必达法则：
>
>$$\lim_{x \to 0^+} x^{1-\alpha}\ln x = \lim_{x \to 0^+} \frac{\ln x}{x^{\alpha-1}} \stackrel{\text{洛}}{=} \lim_{x \to 0^+} \frac{\frac{1}{x}}{(\alpha-1)x^{\alpha-2}} = \lim_{x \to 0^+} \frac{x^{1-\alpha}}{\alpha-1} = 0$$
>
>极限值有限，反常积分收敛；当 $\alpha \geqslant 1$ 时极限发散。
>
>[4]故正确选项为 **(B)**。

**例题[19]:无穷区间对数反常积分的阶数压制与参数判定**

已知 $\alpha > 0$，则对于反常积分 $\int_1^{+\infty} \frac{\ln x}{x^\alpha}\,\mathrm{d}x$ 敛散性的判别，正确的是 $(\quad)$

(A) 当 $0 < \alpha \leqslant 1$ 时积分收敛
(B) 当 $\alpha > 1$ 时积分收敛
(C) 敛散性与 $\alpha$ 无关，必收敛
(D) 敛散性与 $\alpha$ 无关，必发散

主要思路:运用对数是“最弱发散函数”的阶数压制法则，构造介于 $1$ 与 $\alpha$ 之间的微小量进行极限形式比较审敛

>[1]当 $\alpha > 1$ 时的收敛性证明：
>
>因为 $\alpha > 1$，可取充分小的正数 $\varepsilon > 0$，使得 $\alpha - \varepsilon > 1$。
>
>考察被积函数与参考基准 $\frac{1}{x^{\alpha-\varepsilon}}$ 的比值极限：
>
>$$\lim_{x \to +\infty} \frac{\frac{\ln x}{x^\alpha}}{\frac{1}{x^{\alpha-\varepsilon}}} = \lim_{x \to +\infty} \frac{\ln x}{x^\varepsilon} \stackrel{\text{洛}}{=} \lim_{x \to +\infty} \frac{\frac{1}{x}}{\varepsilon x^{\varepsilon-1}} = \lim_{x \to +\infty} \frac{1}{\varepsilon x^\varepsilon} = 0$$
>
>因为 $\alpha - \varepsilon > 1$，基准积分 $\int_1^{+\infty} \frac{1}{x^{\alpha-\varepsilon}}\,\mathrm{d}x$ 收敛。由极限比较审敛法，原积分 $\int_1^{+\infty} \frac{\ln x}{x^\alpha}\,\mathrm{d}x$ 必收敛。
>
>[2]当 $0 < \alpha \leqslant 1$ 时的发散性证明：
>
>当 $x \geqslant e$ 时，恒有 $\ln x \geqslant 1$。
>
>因此：
>
>$$\frac{\ln x}{x^\alpha} \geqslant \frac{1}{x^\alpha} \geqslant \frac{1}{x}$$
>
>因为基准积分 $\int_1^{+\infty} \frac{1}{x}\,\mathrm{d}x$ 发散，由比较审敛法知原积分必发散。
>
>[3]故正确选项为 **(B)**。
