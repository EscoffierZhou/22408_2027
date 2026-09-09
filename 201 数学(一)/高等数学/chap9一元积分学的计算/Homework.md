## 9.Homework

**习题[9.1]:积分方程求导与反求不定积分**

若 $\int xf(x)\,\mathrm{d}x = \arcsin x + C$，求 $\int \frac{1}{f(x)}\,\mathrm{d}x$。

主要思路:对已知不定积分两端求导还原被积表达式 $xf(x)$，解出 $f(x)$ 倒数后凑微分求原函数

>[1]两边求导解出 $xf(x)$：
>
>对 $\int xf(x)\,\mathrm{d}x = \arcsin x + C$ 两端对 $x$ 求导：
>
>$$xf(x) = (\arcsin x + C)' = \frac{1}{\sqrt{1-x^2}}$$
>
>[2]求 $\frac{1}{f(x)}$ 的表达式：
>
>两边取倒数并调整：
>
>$$\frac{1}{f(x)} = x\sqrt{1-x^2}$$
>
>[3]凑微分计算积分：
>
>$$\int \frac{1}{f(x)}\,\mathrm{d}x = \int x\sqrt{1-x^2}\,\mathrm{d}x = -\frac{1}{2}\int (1-x^2)^{\frac{1}{2}}\,\mathrm{d}(1-x^2)$$
>
>$$= -\frac{1}{2} \cdot \frac{2}{3}(1-x^2)^{\frac{3}{2}} + C_1 = -\frac{1}{3}(1-x^2)^{\frac{3}{2}} + C_1$$

**习题[9.2]:常数设元法求解积分方程**

若 $f(x) = \frac{1}{1+x^2} + x^3 \int_0^1 f(x)\,\mathrm{d}x$，求 $\int_0^1 f(x)\,\mathrm{d}x$。

主要思路:定积分 $\int_0^1 f(x)\,\mathrm{d}x$ 是一个常数，在已知方程两端同时在 $[0, 1]$ 上积分，建立一元一次线性代数方程直接解出定积分常数

>[1]等式两端在 $[0, 1]$ 上求积分：
>
>$$\int_0^1 f(x)\,\mathrm{d}x = \int_0^1 \frac{1}{1+x^2}\,\mathrm{d}x + \left(\int_0^1 f(x)\,\mathrm{d}x\right) \int_0^1 x^3\,\mathrm{d}x$$
>
>[2]分别计算两已知定积分：
>
>- $\int_0^1 \frac{1}{1+x^2}\,\mathrm{d}x = [\arctan x]_0^1 = \frac{\pi}{4}$；
>- $\int_0^1 x^3\,\mathrm{d}x = \left[ \frac{x^4}{4} \right]_0^1 = \frac{1}{4}$。
>
>[3]解代数方程：
>
>记 $A = \int_0^1 f(x)\,\mathrm{d}x$，代入得：
>
>$$A = \frac{\pi}{4} + \frac{1}{4}A \implies \frac{3}{4}A = \frac{\pi}{4} \implies A = \frac{\pi}{3}$$
>
>故 $\int_0^1 f(x)\,\mathrm{d}x = \frac{\pi}{3}$。

**习题[9.3]:变限积分洛必达法则与重要极限**

计算极限 $\lim_{x \to +\infty} \frac{\int_c^x \left(1-\frac{1}{t}\right)^t e^{et}\,\mathrm{d}t}{e^{ex}}$。

主要思路:极限属于 $\frac{\infty}{\infty}$ 型，应用洛必达法则对分子分母求导，结合重要极限 $\lim_{t \to +\infty} (1-\frac{1}{t})^t = e^{-1}$ 求解

>[1]洛必达法则求导：
>
>分子求导：$\frac{\mathrm{d}}{\mathrm{d}x}\int_c^x \left(1-\frac{1}{t}\right)^t e^{et}\,\mathrm{d}t = \left(1-\frac{1}{x}\right)^x e^{ex}$。
>
>分母求导：$(e^{ex})' = e \cdot e^{ex}$。
>
>[2]求极限：
>
>$$\lim_{x \to +\infty} \frac{\left(1-\frac{1}{x}\right)^x e^{ex}}{e \cdot e^{ex}} = \lim_{x \to +\infty} \frac{\left(1-\frac{1}{x}\right)^x}{e}$$
>
>[3]代入第二重要极限：
>
>由于 $\lim_{x \to +\infty} \left(1-\frac{1}{x}\right)^x = e^{-1}$：
>
>$$= \frac{e^{-1}}{e} = \frac{1}{e^2}$$

**习题[9.4]:原函数与导数乘积的分部积分**

设 $f(x)$ 的一个原函数为 $\ln^2 x$，求 $\int x f'(x)\,\mathrm{d}x$。

主要思路:被积函数含 $f'(x)$，运用分部积分法将其转移给 $x$，再利用已知原函数关系还原

>[1]分部积分转换结构：
>
>$$\int x f'(x)\,\mathrm{d}x = \int x\,\mathrm{d}[f(x)] = x f(x) - \int f(x)\,\mathrm{d}x$$
>
>[2]由已知原函数确定各部分：
>
>已知 $f(x)$ 的一个原函数为 $\ln^2 x$，故：
>
>$$\int f(x)\,\mathrm{d}x = \ln^2 x + C_1$$
>
>求导得：$f(x) = (\ln^2 x)' = 2\ln x \cdot \frac{1}{x} = \frac{2\ln x}{x}$。
>
>[3]代入化简：
>
>$$x f(x) = x \cdot \frac{2\ln x}{x} = 2\ln x$$
>
>代入分部积分式：
>
>$$= 2\ln x - \ln^2 x + C$$

**习题[9.5]:根式代换消根与反三角分部积分**

计算不定积分 $\int \frac{\arcsin\sqrt{x}}{\sqrt{x}}\,\mathrm{d}x$。

主要思路:被积函数中含有 $\sqrt{x}$，令 $t = \sqrt{x}$ 消除根号，转化为反三角标准分部积分

>[1]根式代换消根：
>
>令 $t = \sqrt{x} \ (t > 0)$，则 $x = t^2$，$\mathrm{d}x = 2t\,\mathrm{d}t$。
>
>$$\int \frac{\arcsin\sqrt{x}}{\sqrt{x}}\,\mathrm{d}x = \int \frac{\arcsin t}{t} \cdot 2t\,\mathrm{d}t = 2\int \arcsin t\,\mathrm{d}t$$
>
>[2]分部积分计算：
>
>$$2\int \arcsin t\,\mathrm{d}t = 2t\arcsin t - 2\int t\,\mathrm{d}(\arcsin t) = 2t\arcsin t - 2\int \frac{t}{\sqrt{1-t^2}}\,\mathrm{d}t$$
>
>$$= 2t\arcsin t + \int (1-t^2)^{-\frac{1}{2}}\,\mathrm{d}(1-t^2) = 2t\arcsin t + 2\sqrt{1-t^2} + C$$
>
>[3]回代 $t = \sqrt{x}$：
>
>$$= 2\sqrt{x}\arcsin\sqrt{x} + 2\sqrt{1-x} + C$$

**习题[9.6]:根式代换与反正切反常积分**

计算反常积分 $\int_2^{+\infty} \frac{\mathrm{d}x}{(x+7)\sqrt{x-2}}$。

主要思路:根号下为线性单项 $x-2$，令 $t = \sqrt{x-2}$ 消除根式，换限后转化为标准反正切函数在无穷远处的极限

>[1]根式换元：
>
>令 $t = \sqrt{x-2}$，则 $x = t^2 + 2$，$\mathrm{d}x = 2t\,\mathrm{d}t$。
>
>换限：当 $x=2$ 时 $t=0$；当 $x \to +\infty$ 时 $t \to +\infty$。
>
>分母代换：$(x+7)\sqrt{x-2} = (t^2+2+7)t = (t^2+9)t$。
>
>[2]列出新积分式并求极限：
>
>$$\int_2^{+\infty} \frac{\mathrm{d}x}{(x+7)\sqrt{x-2}} = \int_0^{+\infty} \frac{2t\,\mathrm{d}t}{(t^2+9)t} = 2\int_0^{+\infty} \frac{\mathrm{d}t}{t^2+3^2}$$
>
>$$= \lim_{b \to +\infty} \left[ \frac{2}{3}\arctan\frac{t}{3} \right]_0^b = \frac{2}{3} \cdot \frac{\pi}{2} - 0 = \frac{\pi}{3}$$

**习题[9.7]:三角代换脱根与正切分部积分**

计算不定积分 $\int \arcsin\sqrt{\frac{x}{a+x}}\,\mathrm{d}x$ ($a > 0$)。

主要思路:令 $t = \arcsin\sqrt{\frac{x}{a+x}}$，反解出 $x = a\tan^2 t$，利用三角导数将复杂的反三角积分转化为三角有理式分部积分

>[1]换元脱壳：
>
>令 $t = \arcsin\sqrt{\frac{x}{a+x}}$，则 $\sin t = \sqrt{\frac{x}{a+x}}$。
>
>两边平方：$\sin^2 t = \frac{x}{a+x} \implies x(1-\sin^2 t) = a\sin^2 t \implies x = a\frac{\sin^2 t}{\cos^2 t} = a\tan^2 t$。
>
>求微分：$\mathrm{d}x = \mathrm{d}(a\tan^2 t)$。
>
>[2]分部积分计算：
>
>$$\int \arcsin\sqrt{\frac{x}{a+x}}\,\mathrm{d}x = \int t\,\mathrm{d}(a\tan^2 t) = a t \tan^2 t - a\int \tan^2 t\,\mathrm{d}t$$
>
>由于 $\tan^2 t = \sec^2 t - 1$：
>
>$$= a t \tan^2 t - a\int (\sec^2 t - 1)\,\mathrm{d}t = a t \tan^2 t - a(\tan t - t) + C$$
>
>$$= a t(\tan^2 t + 1) - a\tan t + C = a t \sec^2 t - a\tan t + C$$
>
>[3]回代 $x$：
>
>由 $\tan^2 t = \frac{x}{a}$，知 $\tan t = \sqrt{\frac{x}{a}}$，$\sec^2 t = 1 + \frac{x}{a} = \frac{a+x}{a}$。
>
>代入整理得：
>
>$$= a \cdot \frac{a+x}{a} \arcsin\sqrt{\frac{x}{a+x}} - a\sqrt{\frac{x}{a}} + C = (a+x)\arcsin\sqrt{\frac{x}{a+x}} - \sqrt{ax} + C$$

**习题[9.8]:分部积分法与换元法双解比较**

求不定积分 $\int \frac{\arctan e^x}{e^x}\,\mathrm{d}x$。

主要思路:提供两种标准解法：方法一直接利用分部积分法将 $e^{-x}$ 移入微分；方法二令 $e^x = t$ 化为有理代数式分部积分

>[1]方法一(分部积分法)：
>
>$$\int \frac{\arctan e^x}{e^x}\,\mathrm{d}x = -\int \arctan e^x\,\mathrm{d}(e^{-x}) = -e^{-x}\arctan e^x + \int e^{-x}\,\mathrm{d}(\arctan e^x)$$
>
>$$= -e^{-x}\arctan e^x + \int e^{-x} \cdot \frac{e^x}{1+e^{2x}}\,\mathrm{d}x = -e^{-x}\arctan e^x + \int \frac{1}{1+e^{2x}}\,\mathrm{d}x$$
>
>分子改写凑微分：
>
>$$\int \frac{1}{1+e^{2x}}\,\mathrm{d}x = \int \left(1 - \frac{e^{2x}}{1+e^{2x}}\right)\,\mathrm{d}x = x - \frac{1}{2}\int \frac{\mathrm{d}(1+e^{2x})}{1+e^{2x}} = x - \frac{1}{2}\ln(1+e^{2x})$$
>
>合并得：
>
>$$= -e^{-x}\arctan e^x + x - \frac{1}{2}\ln(1+e^{2x}) + C$$
>
>[2]方法二(换元法)：
>
>令 $e^x = t$，则 $x = \ln t$，$\mathrm{d}x = \frac{1}{t}\,\mathrm{d}t$。
>
>$$\int \frac{\arctan e^x}{e^x}\,\mathrm{d}x = \int \frac{\arctan t}{t^2}\,\mathrm{d}t = -\int \arctan t\,\mathrm{d}\left(\frac{1}{t}\right)$$
>
>$$= -\frac{1}{t}\arctan t + \int \frac{1}{t(1+t^2)}\,\mathrm{d}t = -\frac{1}{t}\arctan t + \int \left(\frac{1}{t} - \frac{t}{1+t^2}\right)\,\mathrm{d}t$$
>
>$$= -\frac{1}{t}\arctan t + \ln t - \frac{1}{2}\ln(1+t^2) + C$$
>
>回代 $t = e^x$：
>
>$$= -\frac{1}{e^x}\arctan e^x + x - \frac{1}{2}\ln(1+e^{2x}) + C$$

**习题[9.9]:分段函数不定积分常数连续性拼接**

求不定积分 $\int \max\{1, |x|\}\,\mathrm{d}x$。

主要思路:先将分段函数严格拆分，分段求出每段上的原函数，根据原函数处处可导必处处连续的性质，在分界点处严格联立解出各积分常数的约束关系

>[1]拆分被积函数：
>
>$$f(x) = \max\{1, |x|\} = \begin{cases} -x, & x < -1 \\ \\ 1, & -1 \leqslant x \leqslant 1 \\ \\ x, & x > 1 \end{cases}$$
>
>由于 $f(x)$ 在整个实数域 $(-\infty, +\infty)$ 上连续，因此必存在处处可导的连续原函数 $F(x)$。
>
>[2]分段积分并设立待定常数：
>
>$$F(x) = \begin{cases} -\frac{x^2}{2} + C_1, & x < -1 \\ \\ x + C_2, & -1 \leqslant x \leqslant 1 \\ \\ \frac{x^2}{2} + C_3, & x > 1 \end{cases}$$
>
>[3]利用分界点处连续性拼接常数：
>
>- 在 $x = -1$ 处连续：$\lim_{x \to -1^-} F(x) = F(-1)$：
>
>$$-\frac{(-1)^2}{2} + C_1 = -1 + C_2 \implies -\frac{1}{2} + C_1 = -1 + C_2 \implies C_2 = C_1 + \frac{1}{2}$$
>
>- 在 $x = 1$ 处连续：$\lim_{x \to 1^+} F(x) = F(1)$：
>
>$$\frac{1^2}{2} + C_3 = 1 + C_2 \implies \frac{1}{2} + C_3 = 1 + C_2 \implies C_3 = C_2 + \frac{1}{2} = C_1 + 1$$
>
>[4]令 $C_1 = C$ 给出最终统一形式：
>
>$$\int \max\{1, |x|\}\,\mathrm{d}x = \begin{cases} -\frac{x^2}{2} + C, & x < -1 \\ \\ x + \frac{1}{2} + C, & -1 \leqslant x \leqslant 1 \\ \\ \frac{x^2}{2} + 1 + C, & x > 1 \end{cases}$$

**习题[9.10]:三角有理式分段换元与奇异点跨越陷阱**

求定积分 $\int_0^{\frac{3}{4}\pi} \frac{1}{1+\cos^2 x}\,\mathrm{d}x$。

主要思路:区间 $[0, \frac{3\pi}{4}]$ 跨过了余弦零点 $x = \frac{\pi}{2}$，若用正切代换 $t = \tan x$，正切函数在 $\frac{\pi}{2}$ 处趋于无穷大断开，必须严格在 $\frac{\pi}{2}$ 处拆成两段分别换元

>[1]拆分区间避开正切无定义点：
>
>$$\int_0^{\frac{3}{4}\pi} \frac{1}{1+\cos^2 x}\,\mathrm{d}x = \int_0^{\frac{\pi}{2}} \frac{1}{1+\cos^2 x}\,\mathrm{d}x + \int_{\frac{\pi}{2}}^{\frac{3}{4}\pi} \frac{1}{1+\cos^2 x}\,\mathrm{d}x$$
>
>[2]分子分母同除以 $\cos^2 x$ 凑微分：
>
>$$\frac{1}{1+\cos^2 x}\,\mathrm{d}x = \frac{\sec^2 x}{\sec^2 x + 1}\,\mathrm{d}x = \frac{\mathrm{d}(\tan x)}{\tan^2 x + 2}$$
>
>[3]分别计算两段定积分：
>
>- 第一段：$x \in [0, \frac{\pi}{2})$，令 $t = \tan x$，从 $0$ 变到 $+\infty$：
>
>$$\int_0^{+\infty} \frac{\mathrm{d}t}{t^2 + (\sqrt{2})^2} = \left[ \frac{1}{\sqrt{2}}\arctan\frac{t}{\sqrt{2}} \right]_0^{+\infty} = \frac{1}{\sqrt{2}} \cdot \frac{\pi}{2} = \frac{\pi}{2\sqrt{2}}$$
>
>- 第二段：$x \in (\frac{\pi}{2}, \frac{3\pi}{4}]$，令 $t = \tan x$，从 $-\infty$ 变到 $-1$：
>
>$$\int_{-\infty}^{-1} \frac{\mathrm{d}t}{t^2 + (\sqrt{2})^2} = \left[ \frac{1}{\sqrt{2}}\arctan\frac{t}{\sqrt{2}} \right]_{-\infty}^{-1} = \frac{1}{\sqrt{2}}\left(-\arctan\frac{1}{\sqrt{2}} - \left(-\frac{\pi}{2}\right)\right) = \frac{1}{\sqrt{2}}\left(\frac{\pi}{2} - \arctan\frac{1}{\sqrt{2}}\right)$$
>
>[4]两段求和：
>
>$$= \frac{\pi}{2\sqrt{2}} + \frac{1}{\sqrt{2}}\left(\frac{\pi}{2} - \arctan\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}\left(\pi - \arctan\frac{1}{\sqrt{2}}\right)$$

**习题[9.11]:导数逆运算识别与定积分快速计算**

计算定积分 $\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} e^{\frac{x}{2}} \frac{\cos x - \sin x}{\sqrt{\cos x}}\,\mathrm{d}x$。

主要思路:遇到结构复杂的积分，先观察是否为基本初等复合函数乘积的导数形式，通过乘积求导法则逆运算直接还原原函数

>[1]考察复合函数导数：
>
>考察函数 $G(x) = e^{\frac{x}{2}}\sqrt{\cos x}$ 的导数：
>
>$$G'(x) = \left(e^{\frac{x}{2}}\right)'\sqrt{\cos x} + e^{\frac{x}{2}}(\sqrt{\cos x})' = \frac{1}{2}e^{\frac{x}{2}}\sqrt{\cos x} + e^{\frac{x}{2}}\frac{-\sin x}{2\sqrt{\cos x}}$$
>
>$$= \frac{e^{\frac{x}{2}}}{2}\left(\frac{\cos x - \sin x}{\sqrt{\cos x}}\right)$$
>
>[2]锁定被积函数原函数：
>
>原被积函数恰好等于 $2 G'(x)$：
>
>$$e^{\frac{x}{2}} \frac{\cos x - \sin x}{\sqrt{\cos x}} = \frac{\mathrm{d}}{\mathrm{d}x}\left(2 e^{\frac{x}{2}}\sqrt{\cos x}\right)$$
>
>[3]代入上下限求值：
>
>$$\int_{\frac{\pi}{4}}^{\frac{\pi}{2}} e^{\frac{x}{2}} \frac{\cos x - \sin x}{\sqrt{\cos x}}\,\mathrm{d}x = \left[ 2 e^{\frac{x}{2}}\sqrt{\cos x} \right]_{\frac{\pi}{4}}^{\frac{\pi}{2}}$$
>
>$$= 2 e^{\frac{\pi}{4}}\sqrt{\cos\frac{\pi}{2}} - 2 e^{\frac{\pi}{8}}\sqrt{\cos\frac{\pi}{4}} = 0 - 2 e^{\frac{\pi}{8}} \cdot \left(\frac{\sqrt{2}}{2}\right)^{\frac{1}{2}} = -2 \cdot 2^{-\frac{1}{4}} e^{\frac{\pi}{8}} = -2^{\frac{3}{4}}e^{\frac{\pi}{8}}$$

**习题[9.12]:区间再现公式标准应用**

计算定积分 $I = \int_0^\pi \frac{x\sin x}{1+\cos^2 x}\,\mathrm{d}x$。

主要思路:经典的消 $x$ 模型，令 $x = \pi - t$ 应用区间再现公式，两式相加除以二转化为对称三角凑微分

>[1]区间再现换元：
>
>令 $x = \pi - t$，则 $\mathrm{d}x = -\mathrm{d}t$。换限后：
>
>$$I = \int_0^\pi \frac{(\pi - t)\sin(\pi - t)}{1 + \cos^2(\pi - t)}\,\mathrm{d}t = \int_0^\pi \frac{(\pi - t)\sin t}{1 + \cos^2 t}\,\mathrm{d}t$$
>
>$$= \pi\int_0^\pi \frac{\sin t}{1 + \cos^2 t}\,\mathrm{d}t - I$$
>
>[2]移项合并：
>
>$$2I = \pi\int_0^\pi \frac{\sin x}{1 + \cos^2 x}\,\mathrm{d}x$$
>
>[3]凑微分计算：
>
>$$2I = -\pi\int_0^\pi \frac{\mathrm{d}(\cos x)}{1 + \cos^2 x} = -\pi\left[ \arctan(\cos x) \right]_0^\pi$$
>
>$$= -\pi\left[ \arctan(-1) - \arctan(1) \right] = -\pi\left[ -\frac{\pi}{4} - \frac{\pi}{4} \right] = -\pi\left(-\frac{\pi}{2}\right) = \frac{\pi^2}{2}$$
>
>解得：$I = \frac{\pi^2}{4}$。

**习题[9.13]:对称区间奇偶拆项与有理换元**

求定积分 $\int_{-1}^1 \frac{x+1}{1+\sqrt[3]{x^2}}\,\mathrm{d}x$。

主要思路:在对称区间 $[-1, 1]$ 上将分子拆为奇函数项与偶函数项，奇项积分为0，偶项变为两倍半区间积分后再用根式代换

>[1]拆项利用奇偶性：
>
>$$\int_{-1}^1 \frac{x+1}{1+x^{\frac{2}{3}}}\,\mathrm{d}x = \int_{-1}^1 \frac{x}{1+x^{\frac{2}{3}}}\,\mathrm{d}x + \int_{-1}^1 \frac{1}{1+x^{\frac{2}{3}}}\,\mathrm{d}x$$
>
>因第一项被积函数为奇函数，在对称区间 $[-1, 1]$ 上积分为 0；第二项被积函数为偶函数：
>
>$$= 0 + 2\int_0^1 \frac{1}{1+x^{\frac{2}{3}}}\,\mathrm{d}x$$
>
>[2]根式代换消分母指数：
>
>令 $x = u^3$，则 $\mathrm{d}x = 3u^2\,\mathrm{d}u$。换限：$x=0 \implies u=0$；$x=1 \implies u=1$。
>
>$$2\int_0^1 \frac{1}{1+x^{\frac{2}{3}}}\,\mathrm{d}x = 2\int_0^1 \frac{3u^2}{1+u^2}\,\mathrm{d}u = 6\int_0^1 \frac{u^2+1-1}{1+u^2}\,\mathrm{d}u$$
>
>$$= 6\int_0^1 \left(1 - \frac{1}{1+u^2}\right)\,\mathrm{d}u = 6\left[ u - \arctan u \right]_0^1 = 6\left(1 - \frac{\pi}{4}\right) = 6 - \frac{3\pi}{2}$$

**习题[9.14]:分段函数定积分计算**

设 $f(x) = \begin{cases} \frac{1}{1+\sin x}, & x \geqslant 0 \\ \\ \frac{1}{1+e^x}, & x < 0 \end{cases}$，求 $\int_{-1}^{\frac{\pi}{4}} f(x)\,\mathrm{d}x$。

主要思路:在分界点 $x=0$ 处拆分积分区间，左侧做指数凑微分，右侧利用同角三角函数共轭分子化简

>[1]拆分区间：
>
>$$\int_{-1}^{\frac{\pi}{4}} f(x)\,\mathrm{d}x = \int_{-1}^0 \frac{1}{1+e^x}\,\mathrm{d}x + \int_0^{\frac{\pi}{4}} \frac{1}{1+\sin x}\,\mathrm{d}x$$
>
>[2]计算负半轴指数积分：
>
>分子分母同乘 $e^{-x}$：
>
>$$\int_{-1}^0 \frac{e^{-x}}{e^{-x}+1}\,\mathrm{d}x = -\left[ \ln(e^{-x}+1) \right]_{-1}^0 = -\ln 2 + \ln(e+1) = \ln\left(\frac{1+e}{2}\right)$$
>
>[3]计算正半轴三角积分：
>
>分子分母同乘 $1-\sin x$：
>
>$$\int_0^{\frac{\pi}{4}} \frac{1-\sin x}{\cos^2 x}\,\mathrm{d}x = \int_0^{\frac{\pi}{4}} (\sec^2 x - \sec x\tan x)\,\mathrm{d}x = \left[ \tan x - \sec x \right]_0^{\frac{\pi}{4}}$$
>
>$$= (1 - \sqrt{2}) - (0 - 1) = 2 - \sqrt{2}$$
>
>[4]求和：
>
>$$= \ln\left(\frac{1+e}{2}\right) + 2 - \sqrt{2}$$

**习题[9.15]:含绝对值被积函数的变限积分解析式**

设 $x \geqslant -1$，求变限积分函数 $F(x) = \int_{-1}^x (1-|t|)\,\mathrm{d}t$。

主要思路:绝对值拐点为 $t=0$ 与 $t=1$，根据上限 $x$ 所处位置分区间讨论去绝对值计算

>[1]当 $-1 \leqslant x < 0$ 时：
>
>$t \in [-1, x] \subseteq [-1, 0]$，故 $|t| = -t$：
>
>$$F(x) = \int_{-1}^x (1+t)\,\mathrm{d}t = \left[ t + \frac{t^2}{2} \right]_{-1}^x = \left(x + \frac{x^2}{2}\right) - \left(-1 + \frac{1}{2}\right) = \frac{x^2}{2} + x + \frac{1}{2}$$
>
>[2]当 $0 \leqslant x < 1$ 时：
>
>$$F(x) = \int_{-1}^0 (1+t)\,\mathrm{d}t + \int_0^x (1-t)\,\mathrm{d}t = \frac{1}{2} + \left[ t - \frac{t^2}{2} \right]_0^x = -\frac{x^2}{2} + x + \frac{1}{2}$$
>
>[3]当 $x \geqslant 1$ 时：
>
>$$F(x) = \int_{-1}^1 (1-|t|)\,\mathrm{d}t + \int_1^x (1-t)\,\mathrm{d}t = 1 + \left[ t - \frac{t^2}{2} \right]_1^x = 1 + \left(x - \frac{x^2}{2}\right) - \frac{1}{2} = -\frac{x^2}{2} + x + \frac{1}{2}$$
>
>[4]综合结论：
>
>$$F(x) = \begin{cases} \frac{x^2}{2} + x + \frac{1}{2}, & -1 \leqslant x < 0 \\ \\ -\frac{x^2}{2} + x + \frac{1}{2}, & x \geqslant 0 \end{cases}$$

**习题[9.16]:积分方程换元求导与微分方程求解**

求连续函数 $f(x)$，使其满足积分方程 $\int_0^1 f(tx)\,\mathrm{d}t = f(x) + x\sin x$。

主要思路:换元令 $u = tx$ 把自变量 $x$ 提至积分上限，两端关于 $x$ 求导建立一阶微分方程求解

>[1]换元分离自变量：
>
>当 $x \neq 0$ 时，令 $u = tx$，则 $\mathrm{d}t = \frac{\mathrm{d}u}{x}$：
>
>$$\int_0^1 f(tx)\,\mathrm{d}t = \frac{1}{x}\int_0^x f(u)\,\mathrm{d}u$$
>
>原积分方程改写为：
>
>$$\int_0^x f(u)\,\mathrm{d}u = x f(x) + x^2 \sin x$$
>
>[2]两端对 $x$ 求导：
>
>$$f(x) = f(x) + x f'(x) + 2x\sin x + x^2 \cos x$$
>
>化简得：
>
>$$x f'(x) + 2x\sin x + x^2\cos x = 0$$
>
>因 $x \neq 0$ 且函数连续，同除以 $x$：
>
>$$f'(x) = -2\sin x - x\cos x$$
>
>[3]积分还原 $f(x)$：
>
>$$f(x) = \int (-2\sin x - x\cos x)\,\mathrm{d}x = 2\cos x - \int x\,\mathrm{d}(\sin x)$$
>
>$$= 2\cos x - \left(x\sin x - \int \sin x\,\mathrm{d}x\right) = 2\cos x - x\sin x - \cos x + C = \cos x - x\sin x + C$$
>
>其中 $C$ 为任意实常数。

**习题[9.17]:含参绝对值变限积分的导数**

设 $f(x) = \int_0^1 t|t-x|\,\mathrm{d}t$，求 $f'(x)$。

主要思路:根据 $x$ 与区间 $[0, 1]$ 的相对位置分三段去绝对值化为代数多项式，再逐段求导

>[1]当 $x \leqslant 0$ 时：
>
>对任意 $t \in [0, 1]$，都有 $t - x \geqslant 0$，故 $|t-x| = t-x$：
>
>$$f(x) = \int_0^1 t(t-x)\,\mathrm{d}t = \int_0^1 (t^2 - xt)\,\mathrm{d}t = \frac{1}{3} - \frac{1}{2}x \implies f'(x) = -\frac{1}{2}$$
>
>[2]当 $0 < x < 1$ 时：
>
>$$f(x) = \int_0^x t(x-t)\,\mathrm{d}t + \int_x^1 t(t-x)\,\mathrm{d}t$$
>
>$$= \left[ \frac{x t^2}{2} - \frac{t^3}{3} \right]_0^x + \left[ \frac{t^3}{3} - \frac{x t^2}{2} \right]_x^1 = \frac{x^3}{6} + \left(\frac{1}{3} - \frac{x}{2} + \frac{x^3}{6}\right) = \frac{x^3}{3} - \frac{x}{2} + \frac{1}{3}$$
>
>求导得：
>
>$$f'(x) = x^2 - \frac{1}{2}$$
>
>[3]当 $x \geqslant 1$ 时：
>
>对任意 $t \in [0, 1]$，都有 $t - x \leqslant 0$，故 $|t-x| = x-t$：
>
>$$f(x) = \int_0^1 t(x-t)\,\mathrm{d}t = \frac{1}{2}x - \frac{1}{3} \implies f'(x) = \frac{1}{2}$$
>
>[4]检查分界点处导数连续性：
>
>- 在 $x = 0$ 处：$f'_-(0) = -\frac{1}{2}$，$f'_+(0) = 0^2 - \frac{1}{2} = -\frac{1}{2}$；
>- 在 $x = 1$ 处：$f'_-(1) = 1^2 - \frac{1}{2} = \frac{1}{2}$，$f'_+(1) = \frac{1}{2}$。
>
>故 $f'(x)$ 在全实数域连续，统一写作：
>
>$$f'(x) = \begin{cases} -\frac{1}{2}, & x \leqslant 0 \\ \\ x^2 - \frac{1}{2}, & 0 < x < 1 \\ \\ \frac{1}{2}, & x \geqslant 1 \end{cases}$$
