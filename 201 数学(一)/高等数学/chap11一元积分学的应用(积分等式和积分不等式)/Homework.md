## 11.Homework

**习题[11.1]:积分均值不等条件与二阶导数符号判定**

设函数 $\varphi(x)$ 在闭区间 $[1, 3]$ 上二阶可导，且满足条件：
$$\varphi(2) > \varphi(1) \quad \text{且} \quad \varphi(2) > \int_2^3 \varphi(x)\,\mathrm{d}x$$
证明：存在 $\xi \in (1, 3)$，使得 $\varphi''(\xi) < 0$。

主要思路:利用积分第一中值定理将积分条件转化为区间内部点值 $\varphi(c)$，结合 $\varphi(2) > \varphi(1)$ 在两侧分别应用拉格朗日中值定理构造正负异号的一阶导数点，再应用拉格朗日中值定理确定二阶导数的负号

>[1]应用积分第一中值定理转化积分条件：
>
>因为 $\varphi(x)$ 在 $[2, 3]$ 上连续，由积分第一中值定理，存在 $c \in (2, 3)$，使得：
>
>$$\int_2^3 \varphi(x)\,\mathrm{d}x = \varphi(c)(3 - 2) = \varphi(c)$$
>
>代入已知条件 $\varphi(2) > \int_2^3 \varphi(x)\,\mathrm{d}x$，可得：
>
>$$\varphi(2) > \varphi(c)$$
>
>结合另一已知条件 $\varphi(2) > \varphi(1)$，已知各点横坐标满足 $1 < 2 < c < 3$。
>
>[2]两次应用拉格朗日中值定理构造一阶导数正负相异点：
>
>在区间 $[1, 2]$ 上应用拉格朗日中值定理：存在 $\eta_1 \in (1, 2)$，使得：
>
>$$\varphi'(\eta_1) = \frac{\varphi(2) - \varphi(1)}{2 - 1} = \varphi(2) - \varphi(1) > 0$$
>
>在区间 $[2, c]$ 上应用拉格朗日中值定理：存在 $\eta_2 \in (2, c)$，使得：
>
>$$\varphi'(\eta_2) = \frac{\varphi(c) - \varphi(2)}{c - 2} < 0$$
>
>显然有 $1 < \eta_1 < 2 < \eta_2 < c < 3$，故 $\eta_1 < \eta_2$。
>
>[3]应用拉格朗日中值定理确定二阶导数符号：
>
>函数 $\varphi'(x)$ 在区间 $[\eta_1, \eta_2]$ 上满足拉格朗日中值定理条件，存在 $\xi \in (\eta_1, \eta_2) \subset (1, 3)$，使得：
>
>$$\varphi''(\xi) = \frac{\varphi'(\eta_2) - \varphi'(\eta_1)}{\eta_2 - \eta_1}$$
>
>因为分母 $\eta_2 - \eta_1 > 0$，而分子满足：
>
>$$\varphi'(\eta_2) < 0, \quad \varphi'(\eta_1) > 0 \implies \varphi'(\eta_2) - \varphi'(\eta_1) < 0$$
>
>所以：
>
>$$\varphi''(\xi) < 0$$
>
>命题得证。

**习题[11.2]:对称区间替换与单调核积分不等式**

证明积分不等式：
$$\int_0^{\pi/2} \frac{\cos x}{1+x^2}\,\mathrm{d}x \ge \int_0^{\pi/2} \frac{\sin x}{1+x^2}\,\mathrm{d}x$$

主要思路:考查正弦与余弦在关于 $x = \pi/4$ 的对称变换下的对偶关系，将差值积分拆为 $[0, \pi/4]$ 与 $[\pi/4, \pi/2]$ 两段并在后半段作对称代换，结合核函数 $\frac{1}{1+x^2}$ 的单调递减性判定符号

>[1]构造积分差值并拆分区间：
>
>考虑两积分的差：
>
>$$I = \int_0^{\pi/2} \frac{\cos x - \sin x}{1+x^2}\,\mathrm{d}x = \int_0^{\pi/4} \frac{\cos x - \sin x}{1+x^2}\,\mathrm{d}x + \int_{\pi/4}^{\pi/2} \frac{\cos x - \sin x}{1+x^2}\,\mathrm{d}x$$
>
>[2]对后半区间进行对称换元：
>
>对第二项积分 $I_2 = \int_{\pi/4}^{\pi/2} \frac{\cos x - \sin x}{1+x^2}\,\mathrm{d}x$，做换元 $x = \frac{\pi}{2} - t$，$\mathrm{d}x = -\mathrm{d}t$。
>
>当 $x = \pi/4$ 时 $t = \pi/4$；当 $x = \pi/2$ 时 $t = 0$。代入得：
>
>$$I_2 = \int_{\pi/4}^0 \frac{\cos(\pi/2 - t) - \sin(\pi/2 - t)}{1+(\pi/2 - t)^2}(-\mathrm{d}t) = \int_0^{\pi/4} \frac{\sin t - \cos t}{1+(\pi/2 - t)^2}\,\mathrm{d}t$$
>
>[3]合并积分并利用单调性判定非负：
>
>将两项积分合并为一个积分（将哑元统一为 $x$）：
>
>$$I = \int_0^{\pi/4} (\cos x - \sin x) \left[ \frac{1}{1+x^2} - \frac{1}{1+(\pi/2 - x)^2} \right]\,\mathrm{d}x$$
>
>在区间 $(0, \pi/4)$ 上：
>
>(1) 因 $x \in (0, \pi/4)$，恒有 $\cos x > \sin x \implies \cos x - \sin x > 0$；
>
>(2) 因 $x < \pi/2 - x$，故 $x^2 < (\pi/2 - x)^2 \implies 1 + x^2 < 1 + (\pi/2 - x)^2$；
>
>从而 $\frac{1}{1+x^2} - \frac{1}{1+(\pi/2 - x)^2} > 0$。
>
>被积函数在区间 $(0, \pi/4)$ 上严格大于零，由定积分保号性可知 $I > 0$。
>
>即：
>
>$$\int_0^{\pi/2} \frac{\cos x}{1+x^2}\,\mathrm{d}x > \int_0^{\pi/2} \frac{\sin x}{1+x^2}\,\mathrm{d}x$$
>
>命题得证。

**习题[11.3]:加权增量积分不等式证明**

设函数 $f(x)$ 在闭区间 $[0, 1]$ 上一阶连续可导，且对一切 $x \in [0, 1]$ 满足 $f'(x) > 0$。证明：
$$\int_0^1 x f(x)\,\mathrm{d}x > \frac{1}{2}\int_0^1 f(x)\,\mathrm{d}x$$

主要思路:构造变上限积分辅助函数 $F(t) = \int_0^t x f(x)\,\mathrm{d}x - \frac{t}{2}\int_0^t f(x)\,\mathrm{d}x$，通过求导与积分中值定理判定其严格单调递增，由 $F(0)=0$ 导出 $F(1)>0$

>[1]构造变上限积分辅助函数：
>
>考虑辅助函数：
>
>$$F(t) = \int_0^t x f(x)\,\mathrm{d}x - \frac{t}{2}\int_0^t f(x)\,\mathrm{d}x \quad (t \in [0, 1])$$
>
>显然 $F(0) = 0$。欲证结论即证明 $F(1) > 0$。
>
>[2]求导并应用积分第一中值定理：
>
>对 $F(t)$ 关于 $t$ 求导：
>
>$$F'(t) = t f(t) - \left( \frac{1}{2}\int_0^t f(x)\,\mathrm{d}x + \frac{t}{2}f(t) \right) = \frac{t}{2}f(t) - \frac{1}{2}\int_0^t f(x)\,\mathrm{d}x = \frac{1}{2}\int_0^t [f(t) - f(x)]\,\mathrm{d}x$$
>
>因为对一切 $x \in [0, 1]$ 恒有 $f'(x) > 0$，所以 $f(x)$ 是严格单调递增函数。
>
>当 $t > 0$ 时，对任意 $x \in [0, t)$，恒有 $f(t) > f(x) \implies f(t) - f(x) > 0$。
>
>因此，对任意 $t \in (0, 1]$，恒有 $F'(t) > 0$。
>
>[3]严格单调增导出结论：
>
>函数 $F(t)$ 在 $[0, 1]$ 上连续，且在 $(0, 1)$ 内导数严格大于零，故 $F(t)$ 在 $[0, 1]$ 上严格单调递增。
>
>结合初值 $F(0) = 0$，必有：
>
>$$F(1) > F(0) = 0$$
>
>即：
>
>$$\int_0^1 x f(x)\,\mathrm{d}x > \frac{1}{2}\int_0^1 f(x)\,\mathrm{d}x$$
>
>命题得证。

**习题[11.4]:区间对称变换与单调性加权积分不等式**

设函数 $f(x)$ 在闭区间 $[a, b]$ ($a < b$) 上连续且单调递增，证明：
$$\int_a^b x f(x)\,\mathrm{d}x \ge \frac{a+b}{2}\int_a^b f(x)\,\mathrm{d}x$$

主要思路:做区间对称变换 $x = a + b - t$，将积分自身与其对称表达相加，提取公因式构造单调增函数的对称乘积项，利用保号性完成证明

>[1]对称变换与同值积分相加：
>
>记 $J = \int_a^b x f(x)\,\mathrm{d}x$。做换元 $x = a + b - t$，$\mathrm{d}x = -\mathrm{d}t$。
>
>$$J = \int_b^a (a + b - t)f(a + b - t)(-\mathrm{d}t) = \int_a^b (a + b - x)f(a + b - x)\,\mathrm{d}x$$
>
>将两式相加：
>
>$$2J = \int_a^b [x f(x) + (a + b - x)f(a + b - x)]\,\mathrm{d}x$$
>
>[2]合并整理被积函数因式：
>
>两端同时减去 $(a + b)\int_a^b f(x)\,\mathrm{d}x$：
>
>$$2J - (a + b)\int_a^b f(x)\,\mathrm{d}x = \int_a^b [x f(x) + (a + b - x)f(a + b - x) - (a + b)f(x)]\,\mathrm{d}x$$
>
>$$= \int_a^b \left( x - \frac{a+b}{2} \right) [f(x) - f(a + b - x)]\,\mathrm{d}x$$
>
>[3]单调性判定被积函数非负：
>
>考查被积函数 $H(x) = \left( x - \frac{a+b}{2} \right) [f(x) - f(a + b - x)]$：
>
>(1) 当 $x > \frac{a+b}{2}$ 时，$x > a + b - x$。因 $f$ 单调递增，有 $f(x) \ge f(a + b - x)$，两因子同为正，乘积 $H(x) \ge 0$；
>
>(2) 当 $x < \frac{a+b}{2}$ 时，$x < a + b - x$。因 $f$ 单调递增，有 $f(x) \le f(a + b - x)$，两因子同为负，乘积 $H(x) \ge 0$；
>
>(3) 当 $x = \frac{a+b}{2}$ 时，$H(x) = 0$。
>
>因此在整个区间 $[a, b]$ 上恒有 $H(x) \ge 0$。
>
>由定积分保号性，积分非负，故 $2J \ge (a + b)\int_a^b f(x)\,\mathrm{d}x$，即：
>
>$$\int_a^b x f(x)\,\mathrm{d}x \ge \frac{a+b}{2}\int_a^b f(x)\,\mathrm{d}x$$
>
>命题得证。

**习题[11.5]:端点零值导数约束下的积分模长估计**

设函数 $f(x)$ 在闭区间 $[0, a]$ ($a > 0$) 上可导，且端点 $f(0) = 0$。记 $M = \max_{x \in [0, a]} |f'(x)|$。证明不等式：
$$\int_0^a |f(x)|\,\mathrm{d}x \le \frac{a^2}{2} M$$

主要思路:由微积分基本定理或拉格朗日中值定理建立 $|f(x)| \le M x$ 的线性上界控制，代入积分逐项放缩直接算出上界

>[1]利用拉格朗日中值定理建立点值模长上界：
>
>对任意 $x \in (0, a]$，在区间 $[0, x]$ 上对 $f$ 应用拉格朗日中值定理：
>
>$$f(x) - f(0) = f'(\xi)(x - 0) = f'(\xi)x \quad (0 < \xi < x)$$
>
>代入端点值 $f(0) = 0$，取绝对值：
>
>$$|f(x)| = |f'(\xi)|x \le M x$$
>
>显然在 $x = 0$ 处该不等式亦平凡成立。故对一切 $x \in [0, a]$，恒有 $|f(x)| \le M x$。
>
>[2]在闭区间 $[0, a]$ 上进行绝对值定积分放缩：
>
>由定积分保序性：
>
>$$\int_0^a |f(x)|\,\mathrm{d}x \le \int_0^a M x\,\mathrm{d}x = M \int_0^a x\,\mathrm{d}x$$
>
>[3]计算定积分得出最终界限：
>
>计算初等积分：
>
>$$\int_0^a x\,\mathrm{d}x = \left[ \frac{x^2}{2} \right]_0^a = \frac{a^2}{2}$$
>
>因此直接得出：
>
>$$\int_0^a |f(x)|\,\mathrm{d}x \le \frac{a^2}{2} M$$
>
>命题得证。

**习题[11.6]:下凸函数中点泰勒展开积分不等式**

设函数 $f(x)$ 在闭区间 $[0, 1]$ 上二阶可导，且对一切 $x \in [0, 1]$ 满足 $f''(x) > 0$。证明不等式：
$$\int_0^1 f(x)\,\mathrm{d}x > f\left(\frac{1}{2}\right)$$

主要思路:选取对称中心点 $x_0 = 1/2$ 作带拉格朗日余项的一阶泰勒展开，在区间 $[0, 1]$ 上逐项定积分，奇对称一次项积分精确为零，二阶正余项提供正增量

>[1]在中点 $x_0 = 1/2$ 处作带拉格朗日余项的一阶泰勒展开：
>
>对任意 $x \in [0, 1]$，将 $f(x)$ 在 $x_0 = \frac{1}{2}$ 处展开至一阶：
>
>$$f(x) = f\left(\frac{1}{2}\right) + f'\left(\frac{1}{2}\right)\left(x - \frac{1}{2}\right) + \frac{f''(\zeta)}{2}\left(x - \frac{1}{2}\right)^2$$
>
>其中 $\zeta$ 介于 $\frac{1}{2}$ 与 $x$ 之间。
>
>[2]在闭区间 $[0, 1]$ 上逐项定积分：
>
>对上式两端在 $[0, 1]$ 上求定积分：
>
>$$\int_0^1 f(x)\,\mathrm{d}x = \int_0^1 f\left(\frac{1}{2}\right)\,\mathrm{d}x + f'\left(\frac{1}{2}\right)\int_0^1 \left(x - \frac{1}{2}\right)\,\mathrm{d}x + \int_0^1 \frac{f''(\zeta)}{2}\left(x - \frac{1}{2}\right)^2\,\mathrm{d}x$$
>
>由于第一项中 $f(1/2)$ 为常数：
>
>$$\int_0^1 f\left(\frac{1}{2}\right)\,\mathrm{d}x = f\left(\frac{1}{2}\right) \cdot (1 - 0) = f\left(\frac{1}{2}\right)$$
>
>第二项关于 $x = \frac{1}{2}$ 呈奇对称，积分精确为零：
>
>$$\int_0^1 \left(x - \frac{1}{2}\right)\,\mathrm{d}x = \left[ \frac{1}{2}\left(x - \frac{1}{2}\right)^2 \right]_0^1 = \frac{1}{8} - \frac{1}{8} = 0$$
>
>[3]由二阶导数严格正性导出严格不等式：
>
>对于第三项，因为对一切 $x \in [0, 1]$ 恒有 $f''(x) > 0$，故 $\frac{f''(\zeta)}{2} > 0$。
>
>且 $(x - 1/2)^2$ 仅在孤立点 $x = 1/2$ 处为零，在其他点严格大于零。
>
>因此被积函数在 $[0, 1]$ 上连续非负且不恒为零，其定积分严格为正：
>
>$$\int_0^1 \frac{f''(\zeta)}{2}\left(x - \frac{1}{2}\right)^2\,\mathrm{d}x > 0$$
>
>综上所述：
>
>$$\int_0^1 f(x)\,\mathrm{d}x = f\left(\frac{1}{2}\right) + 0 + (\text{严格正项}) > f\left(\frac{1}{2}\right)$$
>
>命题得证。
