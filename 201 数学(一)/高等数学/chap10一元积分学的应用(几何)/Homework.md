## 10.Homework

**习题[10.1]:反常无界旋转体体积计算**

求曲线 $y = \frac{1}{\sqrt{1+x^2}}$ ($x \geqslant 0$)、两坐标轴所围成的无界曲边梯形绕 $x$ 轴旋转一周所得旋转体的体积。

主要思路:建立圆盘法切片体积微元，将问题转化为 $[0, +\infty)$ 上的反常定积分，利用反正切导数公式直接计算

>[1]构建圆盘切片体积微元：
>
>垂直于 $x$ 轴切片，截面圆盘半径为 $y(x) = \frac{1}{\sqrt{1+x^2}}$，厚度为 $\mathrm{d}x$。
>
>体积微元为：
>
>$$\mathrm{d}V_x = \pi y^2(x)\,\mathrm{d}x = \pi \left(\frac{1}{\sqrt{1+x^2}}\right)^2\,\mathrm{d}x = \frac{\pi}{1+x^2}\,\mathrm{d}x$$
>
>[2]列出反常积分表达式：
>
>图形在横轴方向无界延展，自变量范围为 $x \in [0, +\infty)$：
>
>$$V_x = \pi \int_0^{+\infty} \frac{1}{1+x^2}\,\mathrm{d}x$$
>
>[3]计算极限与最终体积：
>
>$$V_x = \pi \lim_{A \to +\infty} \int_0^A \frac{1}{1+x^2}\,\mathrm{d}x = \pi \lim_{A \to +\infty} [\arctan x]_0^A = \pi \left(\frac{\pi}{2} - 0\right) = \frac{\pi^2}{2}$$

**习题[10.2]:圆盘绕外轴旋转体体积(圆环体)的双重解法**

求由圆 $x^2 + (y-b)^2 \leqslant k^2$ ($0 < k < b$) 所确定的平面圆盘区域绕 $x$ 轴旋转一周所得旋转体（圆环体 Torus）的体积。

主要思路:解法[1]利用圆环截面法（Washer method），求出上下半圆方程之平方差定积分；解法[2]利用古尔丁第二定理（Pappus-Guldin）形心转动路程秒杀

>[1]解法[1]（圆环切片法 Washer Method）：
>
>圆的上下半圆方程分别为：
>
>$$y_2(x) = b + \sqrt{k^2-x^2}, \quad y_1(x) = b - \sqrt{k^2-x^2} \quad (x \in [-k, k])$$
>
>垂直于 $x$ 轴切片，截面为圆环，内外半径分别为 $y_2(x)$ 与 $y_1(x)$。
>
>内外半径平方差为：
>
>$$y_2^2(x) - y_1^2(x) = \left(b + \sqrt{k^2-x^2}\right)^2 - \left(b - \sqrt{k^2-x^2}\right)^2 = 4b\sqrt{k^2-x^2}$$
>
>[2]定积分计算与几何对称性：
>
>$$V = \pi \int_{-k}^k [y_2^2(x) - y_1^2(x)]\,\mathrm{d}x = 4\pi b \int_{-k}^k \sqrt{k^2-x^2}\,\mathrm{d}x$$
>
>定积分 $\int_{-k}^k \sqrt{k^2-x^2}\,\mathrm{d}x$ 的几何意义为半径为 $k$ 的上半圆面积，即 $\frac{1}{2}\pi k^2$。
>
>$$V = 4\pi b \left(\frac{1}{2}\pi k^2\right) = 2\pi^2 k^2 b$$
>
>[3]解法[2]（古尔丁第二定理秒杀验证）：
>
>平面圆盘的几何对称中心（形心）位于圆心 $(0, b)$，其到旋转轴（$x$ 轴）的垂直距离为 $d_C = b$。
>
>形心绕 $x$ 轴旋转一周所经过的圆周路程为：
>
>$$L_C = 2\pi d_C = 2\pi b$$
>
>圆盘的面积为 $A = \pi k^2$。根据古尔丁第二定理：
>
>$$V = L_C \cdot A = 2\pi b \cdot \pi k^2 = 2\pi^2 k^2 b$$

**习题[10.3]:反函数型曲线弧长积分**

求曲线 $x = \frac{1}{4}y^2 - \frac{1}{2}\ln y$ ($1 \leqslant y \leqslant e$) 的弧长。

主要思路:以 $y$ 为积分自变量，套用反函数弧长公式 $\mathrm{d}s = \sqrt{1+[x'(y)]^2}\,\mathrm{d}y$，根号下配为完全平方式开方后直接积分

>[1]求导与平方和配方：
>
>对 $y$ 求导：
>
>$$x'(y) = \frac{1}{2}y - \frac{1}{2y}$$
>
>计算 $1 + [x'(y)]^2$：
>
>$$1 + [x'(y)]^2 = 1 + \left(\frac{1}{2}y - \frac{1}{2y}\right)^2 = 1 + \frac{1}{4}y^2 - \frac{1}{2} + \frac{1}{4y^2} = \frac{1}{4}y^2 + \frac{1}{2} + \frac{1}{4y^2} = \left(\frac{1}{2}y + \frac{1}{2y}\right)^2$$
>
>[2]构建弧长微元：
>
>在区间 $y \in [1, e]$ 上，$\frac{1}{2}y + \frac{1}{2y} > 0$，开方得：
>
>$$\mathrm{d}s = \sqrt{1+[x'(y)]^2}\,\mathrm{d}y = \left(\frac{1}{2}y + \frac{1}{2y}\right)\,\mathrm{d}y$$
>
>[3]定积分计算弧长：
>
>$$s = \int_1^e \left(\frac{1}{2}y + \frac{1}{2y}\right)\,\mathrm{d}y = \left[\frac{y^2}{4} + \frac{1}{2}\ln y\right]_1^e$$
>
>$$= \left(\frac{e^2}{4} + \frac{1}{2}\ln e\right) - \left(\frac{1}{4} + \frac{1}{2}\ln 1\right) = \frac{e^2}{4} + \frac{1}{2} - \frac{1}{4} = \frac{e^2+1}{4}$$

**习题[10.4]:星形线参数曲线总全长计算**

求星形线 $x = \cos^3 t, y = \sin^3 t$ 的全长。

主要思路:利用星形线在四个象限的对称性，计算第一象限弧长并乘以 4，代入参数方程弧长公式化简三角有理式

>[1]对称性与参数区间划分：
>
>星形线具有关于两坐标轴及原点的完全对称性。在第一象限，参数 $t \in \left[0, \frac{\pi}{2}\right]$。
>
>曲线总弧长为第一象限弧长的 4 倍：
>
>$$s = 4 \int_0^{\frac{\pi}{2}} \mathrm{d}s$$
>
>[2]计算导数与弧长微元：
>
>$$x'(t) = -3\cos^2 t\sin t, \quad y'(t) = 3\sin^2 t\cos t$$
>
>$$[x'(t)]^2 + [y'(t)]^2 = 9\cos^4 t\sin^2 t + 9\sin^4 t\cos^2 t = 9\sin^2 t\cos^2 t(\cos^2 t + \sin^2 t) = 9\sin^2 t\cos^2 t$$
>
>在 $t \in \left[0, \frac{\pi}{2}\right]$ 上，$\sin t \geqslant 0, \cos t \geqslant 0$：
>
>$$\mathrm{d}s = \sqrt{[x'(t)]^2 + [y'(t)]^2}\,\mathrm{d}t = 3\sin t\cos t\,\mathrm{d}t$$
>
>[3]定积分计算总长：
>
>$$s = 4 \int_0^{\frac{\pi}{2}} 3\sin t\cos t\,\mathrm{d}t = 12 \int_0^{\frac{\pi}{2}} \sin t\,\mathrm{d}(\sin t) = 12 \left[\frac{\sin^2 t}{2}\right]_0^{\frac{\pi}{2}} = 6$$

**习题[10.5]:对称无理分式在指定区间上的连续函数平均值**

求函数 $y = \frac{x^2}{\sqrt{1-x^2}}$ 在区间 $\left[\frac{1}{2}, \frac{\sqrt{3}}{2}\right]$ 上的平均值 $\overline{y}$。

主要思路:根据连续函数平均值公式 $\overline{y} = \frac{1}{b-a}\int_a^b y(x)\,\mathrm{d}x$，区间长度为 $\frac{\sqrt{3}-1}{2}$，积分采用三角代换 $x = \sin t$ 化简

>[1]计算区间长度：
>
>$$b - a = \frac{\sqrt{3}}{2} - \frac{1}{2} = \frac{\sqrt{3}-1}{2}$$
>
>[2]三角代换计算定积分：
>
>令 $x = \sin t$，当 $x = \frac{1}{2}$ 时 $t = \frac{\pi}{6}$；当 $x = \frac{\sqrt{3}}{2}$ 时 $t = \frac{\pi}{3}$。此时 $\mathrm{d}x = \cos t\,\mathrm{d}t$，$\sqrt{1-x^2} = \cos t$。
>
>$$I = \int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}} \frac{x^2}{\sqrt{1-x^2}}\,\mathrm{d}x = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{\sin^2 t}{\cos t} \cdot \cos t\,\mathrm{d}t = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sin^2 t\,\mathrm{d}t$$
>
>利用二倍角降幂：
>
>$$I = \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \frac{1 - \cos 2t}{2}\,\mathrm{d}t = \left[\frac{t}{2} - \frac{\sin 2t}{4}\right]_{\frac{\pi}{6}}^{\frac{\pi}{3}}$$
>
>$$= \left(\frac{\pi}{6} - \frac{\sqrt{3}}{8}\right) - \left(\frac{\pi}{12} - \frac{\sqrt{3}}{8}\right) = \frac{\pi}{12}$$
>
>[3]计算平均值：
>
>$$\overline{y} = \frac{I}{b-a} = \frac{\frac{\pi}{12}}{\frac{\sqrt{3}-1}{2}} = \frac{\pi}{6(\sqrt{3}-1)} = \frac{\sqrt{3}+1}{12}\pi$$

**习题[10.6]:切线动直线与抛物线围成区域面积极值优化**

在曲线 $y = \sqrt{x}$ 上求一点，过该点的切线与直线 $x = 0, x = 2$ 及曲线 $y = \sqrt{x}$ 围成的平面图形面积最小，并求出切线方程与最小面积。

主要思路:设切点横坐标为参数 $t \in (0, 2)$，建立切线方程；根据凹凸性切线位于曲线上方，构造面积函数 $S(t)$，求导求驻点锁定最小值

>[1]建立切线方程与被积式：
>
>设切点为 $(t, \sqrt{t})$ ($0 < t < 2$)。导数 $y' = \frac{1}{2\sqrt{x}}$，在切点处的切线斜率为 $k = \frac{1}{2\sqrt{t}}$。
>
>切线方程为：
>
>$$y - \sqrt{t} = \frac{1}{2\sqrt{t}}(x - t) \implies y = \frac{x}{2\sqrt{t}} + \frac{\sqrt{t}}{2}$$
>
>由于 $y = \sqrt{x}$ 的二阶导数 $y'' = -\frac{1}{4x^{3/2}} < 0$（严格上凸），其任意切线恒位于曲线的上方。
>
>[2]构建面积目标函数 $S(t)$：
>
>在区间 $[0, 2]$ 上，上边界为切线，下边界为曲线 $y = \sqrt{x}$：
>
>$$S(t) = \int_0^2 \left(\frac{x}{2\sqrt{t}} + \frac{\sqrt{t}}{2} - \sqrt{x}\right)\,\mathrm{d}x = \left[\frac{x^2}{4\sqrt{t}} + \frac{\sqrt{t}}{2}x - \frac{2}{3}x^{\frac{3}{2}}\right]_0^2$$
>
>$$= \frac{1}{\sqrt{t}} + \sqrt{t} - \frac{4\sqrt{2}}{3}$$
>
>[3]求导求极值点：
>
>对 $t$ 求导：
>
>$$S'(t) = -\frac{1}{2}t^{-\frac{3}{2}} + \frac{1}{2}t^{-\frac{1}{2}} = \frac{\sqrt{t} - \frac{1}{\sqrt{t}}}{2\sqrt{t}} = \frac{t - 1}{2t^{\frac{3}{2}}}$$
>
>令 $S'(t) = 0 \implies t = 1$。
>
>- 当 $0 < t < 1$ 时，$S'(t) < 0$，$S(t)$ 单调递减；
>- 当 $1 < t < 2$ 时，$S'(t) > 0$，$S(t)$ 单调递增。
>
>故 $t = 1$ 为区间内唯一的极小值点，亦为全局最小值点。
>
>代入 $t = 1$：切点为 $(1, 1)$，切线方程为 $y = \frac{1}{2}x + \frac{1}{2}$。
>
>最小面积为：
>
>$$S_{\min} = S(1) = 1 + 1 - \frac{4\sqrt{2}}{3} = 2 - \frac{4\sqrt{2}}{3}$$

**习题[10.7]:分块旋转体体积最大值优化与驻点判定**

设由抛物线 $y = 2x^2$、直线 $x = a, x = 2$ 及 $x$ 轴所围成的平面区域为 $D_1$ ($0 < a < 2$)，其绕 $x$ 轴旋转所得体积为 $V_1$；由抛物线 $y = 2x^2$、$x$ 轴及直线 $x = a$ 围成的区域为 $D_2$，其绕直线 $x = a$ 旋转所得体积为 $V_2$。
(1) 求体积 $V_1, V_2$；
(2) 问 $a$ 为何值时，总体积 $V = V_1 + V_2$ 取得最大值？并求出最大体积。

主要思路:(1) 分别利用圆盘切片法求 $V_1$、柱壳法求 $V_2$；(2) 建立总体积 $V(a)$ 的代数式，求导求驻点并验证单调性与极值

>[1]计算体积 $V_1$ 与 $V_2$：
>
>区域 $D_1$ 绕 $x$ 轴旋转：
>
>$$V_1 = \pi \int_a^2 (2x^2)^2\,\mathrm{d}x = 4\pi \int_a^2 x^4\,\mathrm{d}x = 4\pi \left[\frac{x^5}{5}\right]_a^2 = \frac{4\pi}{5}(32 - a^5)$$
>
>区域 $D_2$ 绕直线 $x = a$ 旋转，采用薄圆柱壳法，回转半径为 $a - x$，高度为 $2x^2$：
>
>$$V_2 = 2\pi \int_0^a (a - x)(2x^2)\,\mathrm{d}x = 4\pi \int_0^a (ax^2 - x^3)\,\mathrm{d}x = 4\pi \left[\frac{a x^3}{3} - \frac{x^4}{4}\right]_0^a$$
>
>$$= 4\pi \left(\frac{a^4}{3} - \frac{a^4}{4}\right) = \frac{\pi}{3}a^4$$
>
>[2]建立总体积函数 $V(a)$ 并求导：
>
>$$V(a) = V_1 + V_2 = \frac{4\pi}{5}(32 - a^5) + \frac{\pi}{3}a^4 = \frac{128\pi}{5} - \frac{4\pi}{5}a^5 + \frac{\pi}{3}a^4$$
>
>对 $a$ 求导：
>
>$$V'(a) = -4\pi a^4 + \frac{4\pi}{3}a^3 = 4\pi a^3 \left(\frac{1}{3} - a\right)$$
>
>[3]驻点分析与最值结论：
>
>令 $V'(a) = 0$，因 $0 < a < 2$，驻点为 $a = \frac{1}{3}$。
>
>- 当 $0 < a < \frac{1}{3}$ 时，$V'(a) > 0$，$V(a)$ 单调增加；
>- 当 $\frac{1}{3} < a < 2$ 时，$V'(a) < 0$，$V(a)$ 单调减少。
>
>故在 $a = \frac{1}{3}$ 处取得极大值，亦为最大值：
>
>$$V_{\max} = V\left(\frac{1}{3}\right) = \frac{128\pi}{5} - \frac{4\pi}{5}\left(\frac{1}{3}\right)^5 + \frac{\pi}{3}\left(\frac{1}{3}\right)^4 = \frac{128\pi}{5} + \frac{\pi}{3^5}\left(-\frac{4}{5} + 3\right) = \frac{128\pi}{5} + \frac{11\pi}{1215}$$
>
>（注：若按板书柱壳法回转半径积分设定系数，当 $V_2 = \pi a^4$ 时，驻点为 $a = 1$，对应最大体积为 $\frac{129\pi}{5}$）。

**习题[10.8]:摆线单拱绕非对称坐标轴(y轴)旋转体积圆柱壳法**

求摆线一拱 $x = a(t - \sin t), y = a(1 - \cos t)$ ($0 \leqslant t \leqslant 2\pi, a > 0$) 与 $x$ 轴围成的图形绕 $y$ 轴旋转一周所得旋转体的体积。

主要思路:摆线无法解出显式反函数 $x(y)$，采用圆柱壳法（Cylindrical Shells）微元 $\mathrm{d}V_y = 2\pi x y\,\mathrm{d}x$，代入参数方程化为对 $t$ 的定积分

>[1]构建圆柱壳体积微元：
>
>在 $x$ 处取竖直薄柱壳，旋转半径为 $x$，高度为 $y$，壁厚为 $\mathrm{d}x$。
>
>代入参数方程：
>
>$$x = a(t - \sin t), \quad y = a(1 - \cos t), \quad \mathrm{d}x = a(1 - \cos t)\,\mathrm{d}t$$
>
>体积微元为：
>
>$$\mathrm{d}V_y = 2\pi x y\,\mathrm{d}x = 2\pi a(t - \sin t) \cdot a(1 - \cos t) \cdot a(1 - \cos t)\,\mathrm{d}t = 2\pi a^3 (t - \sin t)(1 - \cos t)^2\,\mathrm{d}t$$
>
>[2]展开三角被积多项式：
>
>$$(t - \sin t)(1 - \cos t)^2 = (t - \sin t)(1 - 2\cos t + \cos^2 t)$$
>
>$$= t(1 - 2\cos t + \cos^2 t) - \sin t(1 - \cos t)^2$$
>
>分别计算两部分的积分：
>
>第二部分是直接凑微分：
>
>$$\int_0^{2\pi} \sin t(1 - \cos t)^2\,\mathrm{d}t = \int_0^{2\pi} (1 - \cos t)^2\,\mathrm{d}(1 - \cos t) = \left[\frac{(1 - \cos t)^3}{3}\right]_0^{2\pi} = 0$$
>
>第一部分展开计算：
>
>$$\int_0^{2\pi} t(1 - 2\cos t + \cos^2 t)\,\mathrm{d}t = \int_0^{2\pi} t\,\mathrm{d}t - 2\int_0^{2\pi} t\cos t\,\mathrm{d}t + \int_0^{2\pi} t\cos^2 t\,\mathrm{d}t$$
>
>- $\int_0^{2\pi} t\,\mathrm{d}t = \left[\frac{t^2}{2}\right]_0^{2\pi} = 2\pi^2$；
>- $\int_0^{2\pi} t\cos t\,\mathrm{d}t = [t\sin t]_0^{2\pi} - \int_0^{2\pi} \sin t\,\mathrm{d}t = 0 - [-\cos t]_0^{2\pi} = 0$；
>- $\int_0^{2\pi} t\cos^2 t\,\mathrm{d}t = \int_0^{2\pi} t \cdot \frac{1+\cos 2t}{2}\,\mathrm{d}t = \frac{1}{2} \cdot 2\pi^2 + \frac{1}{2}\int_0^{2\pi} t\cos 2t\,\mathrm{d}t = \pi^2 + 0 = \pi^2$。
>
>各项相加：$2\pi^2 - 0 + \pi^2 = 3\pi^2$。
>
>[3]汇总最终旋转体体积：
>
>$$V_y = 2\pi a^3 (3\pi^2) = 6\pi^3 a^3$$

**习题[10.9]:含绝对值分段折线曲边图形绕指定水平直线旋转体积**

求由曲线 $y = 3 - |x^2-1|$ 与 $x$ 轴所围成的平面图形绕水平直线 $y = 3$ 旋转一周所得旋转体的体积。

主要思路:求出图形与 $x$ 轴的交点，利用偶函数对称性简化区间；以直线 $y = 3$ 为回转轴，垂直于 $x$ 轴切片构建圆环微元并完成定积分

>[1]确定边界交点与对称性：
>
>令 $y = 3 - |x^2-1| = 0 \implies |x^2-1| = 3$。
>
>因绝对值非负：$x^2 - 1 = 3 \implies x^2 = 4 \implies x = \pm 2$。
>
>被积区域关于 $y$ 轴左右对称，定义区间为 $x \in [-2, 2]$。
>
>[2]构建绕水平直线 $y = 3$ 的圆环微元：
>
>旋转轴为水平线 $y = 3$。垂直于 $x$ 轴切片，截面为同心圆环：
>
>- 外半径（旋转轴到下边界 $y = 0$ 的距离）：$R = 3 - 0 = 3$；
>- 内半径（旋转轴到上边界 $y = 3 - |x^2-1|$ 的距离）：$r = 3 - (3 - |x^2-1|) = |x^2-1|$。
>
>圆环截面积为：
>
>$$A(x) = \pi(R^2 - r^2) = \pi [3^2 - (|x^2-1|)^2] = \pi [9 - (x^2-1)^2]$$
>
>[3]偶函数区间对称化简与定积分求解：
>
>被积函数关于 $x$ 为偶函数，利用对称性化为正半轴定积分：
>
>$$V = \int_{-2}^2 \pi [9 - (x^2-1)^2]\,\mathrm{d}x = 2\pi \int_0^2 [9 - (x^4 - 2x^2 + 1)]\,\mathrm{d}x = 2\pi \int_0^2 (8 + 2x^2 - x^4)\,\mathrm{d}x$$
>
>逐项积分：
>
>$$V = 2\pi \left[8x + \frac{2}{3}x^3 - \frac{x^5}{5}\right]_0^2 = 2\pi \left(16 + \frac{16}{3} - \frac{32}{5}\right)$$
>
>通分计算括号内数值：
>
>$$16 + \frac{16}{3} - \frac{32}{5} = \frac{240 + 80 - 96}{15} = \frac{224}{15}$$
>
>因此旋转体体积为：
>
>$$V = 2\pi \times \frac{224}{15} = \frac{448\pi}{15}$$
