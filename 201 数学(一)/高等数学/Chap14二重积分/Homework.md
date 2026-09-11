## 14.Homework

**习题[14.1]:二重和式的黎曼极限转化为定积分**

极限 $\lim\limits_{n \to \infty} \sum_{i=1}^n \sum_{j=1}^n \frac{n}{(n+i)(n^2+j^2)}$ 的值为：
(A) $\frac{\pi}{2}\ln 2$
(B) $\frac{\pi}{4}$
(C) $\ln 2$
(D) $\frac{\pi}{4}\ln 2$

主要思路:通过提取公因子将二重离散和式变形为标准的二重黎曼和，识别积分区域为单位正方形 $[0, 1] \times [0, 1]$，化为累次积分计算

>[1]和式结构因式分解与配凑黎曼和：
>
>考查通项表达式，提取分母中的 $n$ 与 $n^2$：
>
>$$\frac{n}{(n+i)(n^2+j^2)} = \frac{n}{n\left(1 + \frac{i}{n}\right) \cdot n^2\left(1 + \left(\frac{j}{n}\right)^2\right)} = \frac{1}{n^2} \cdot \frac{1}{\left(1 + \frac{i}{n}\right)\left(1 + \left(\frac{j}{n}\right)^2\right)}$$
>
>令 $x_i = \frac{i}{n}, \; y_j = \frac{j}{n}$，小区域面积微元 $\Delta\sigma_{ij} = \Delta x_i \Delta y_j = \frac{1}{n} \times \frac{1}{n} = \frac{1}{n^2}$。
>
>[2]转化为二重积分：
>
>当 $n \to \infty$ 时，网格直径 $\lambda = \frac{\sqrt{2}}{n} \to 0$。
>
>由二重积分的黎曼和定义：
>
>$$\lim_{n \to \infty} \sum_{i=1}^n \sum_{j=1}^n \frac{1}{\left(1 + \frac{i}{n}\right)\left(1 + \left(\frac{j}{n}\right)^2\right)} \frac{1}{n^2} = \iint_D \frac{1}{(1 + x)(1 + y^2)}\,\mathrm{d}x\mathrm{d}y$$
>
>其中积分区域为单位闭正方形 $D = [0, 1] \times [0, 1]$。
>
>[3]分离变量积分与判定选项：
>
>被积函数变量完全解耦：
>
>$$\iint_D \frac{1}{(1 + x)(1 + y^2)}\,\mathrm{d}x\mathrm{d}y = \left( \int_0^1 \frac{1}{1 + x}\,\mathrm{d}x \right) \left( \int_0^1 \frac{1}{1 + y^2}\,\mathrm{d}y \right)$$
>
>$$= [\ln(1 + x)]_0^1 \cdot [\arctan y]_0^1 = \ln 2 \cdot \frac{\pi}{4} = \frac{\pi}{4}\ln 2$$
>
>因此，正确选项为 (D)。

**习题[14.2]:偏心圆区域直角坐标化为极坐标累次积分**

设二元连续函数 $f(u)$，区域 $D = \{(x, y) \mid x^2 + y^2 \le 2y\}$，则二重积分 $\iint_D f(xy)\,\mathrm{d}\sigma$ 化为极坐标形式为：
(A) $\int_0^{\frac{\pi}{2}} \mathrm{d}\theta \int_0^{2\sin\theta} f(r^2\sin\theta\cos\theta) r\,\mathrm{d}r$
(B) $\int_0^\pi \mathrm{d}\theta \int_0^{2\cos\theta} f(r^2\sin\theta\cos\theta) r\,\mathrm{d}r$
(C) $\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} \mathrm{d}\theta \int_0^{2\sin\theta} f(r^2\sin\theta\cos\theta) r\,\mathrm{d}r$
(D) $\int_0^\pi \mathrm{d}\theta \int_0^{2\sin\theta} f(r^2\sin\theta\cos\theta) r\,\mathrm{d}r$

主要思路:画出切于原点且位于上半平面的偏心圆，分析切线夹角确定极角范围，利用射线穿线法确定极径上下限

>[1]偏心圆方程化为极坐标方程：
>
>直角坐标方程配方：$x^2 + (y - 1)^2 \le 1$。
>
>圆心为 $(0, 1)$，半径为 $1$，在原点 $(0, 0)$ 与 $x$ 轴相切且除切点外全位于上半平面。
>
>代入直角与极坐标关系 $x = r\cos\theta, y = r\sin\theta$：
>
>$$r^2 \le 2r\sin\theta \implies 0 \le r \le 2\sin\theta$$
>
>[2]确定极角 $\theta$ 的变化区间：
>
>因为区域位于上半平面，极角 $\theta$ 从切线 $\theta = 0$（正向 $x$ 轴）扫描至切线 $\theta = \pi$（负向 $x$ 轴）。
>
>故极角范围为 $0 \le \theta \le \pi$。
>
>对于任意给定的 $\theta \in (0, \pi)$，射线自原点 $r = 0$ 穿入区域，穿出边界圆周 $r = 2\sin\theta$。
>
>[3]写出累次积分并匹配选项：
>
>自变量代入：$u = xy = r\cos\theta \cdot r\sin\theta = r^2\sin\theta\cos\theta$。
>
>面积微元：$\mathrm{d}\sigma = r\,\mathrm{d}r\mathrm{d}\theta$。
>
>累次积分表达式为：
>
>$$\int_0^\pi \mathrm{d}\theta \int_0^{2\sin\theta} f(r^2\sin\theta\cos\theta) r\,\mathrm{d}r$$
>
>故正确选项为 (D)。

**习题[14.3]:极坐标累次积分逆转化为直角坐标累次积分**

累次积分 $I = \int_0^{\frac{\pi}{2}}\mathrm{d}\theta \int_0^{\cos\theta} f(r\cos\theta, r\sin\theta)r\,\mathrm{d}r$ 等于：
(A) $\int_0^1 \mathrm{d}y \int_0^{\sqrt{y-y^2}} f(x, y)\,\mathrm{d}x$
(B) $\int_0^1 \mathrm{d}x \int_0^{\sqrt{1-x^2}} f(x, y)\,\mathrm{d}y$
(C) $\int_0^{\frac{1}{2}} \mathrm{d}x \int_0^{\sqrt{x-x^2}} f(x, y)\,\mathrm{d}y$
(D) $\int_0^1 \mathrm{d}x \int_0^{\sqrt{x-x^2}} f(x, y)\,\mathrm{d}y$

主要思路:将极坐标边界 $r = \cos\theta$ 转化为直角坐标偏心圆方程，确定其在第一象限的几何区域，写出直角坐标下的累次积分

>[1]极坐标边界曲线逆解为直角坐标：
>
>边界极坐标方程为 $r = \cos\theta$。
>
>两边同乘以 $r$ 得：$r^2 = r\cos\theta$。
>
>代入直角坐标：$x^2 + y^2 = x \iff \left(x - \frac{1}{2}\right)^2 + y^2 = \left(\frac{1}{2}\right)^2$。
>
>该方程表示圆心在 $(\frac{1}{2}, 0)$、半径为 $\frac{1}{2}$ 的圆。
>
>[2]确定区域与直角坐标投影：
>
>积分限中 $\theta \in [0, \frac{\pi}{2}]$，表明区域位于第一象限。
>
>因此区域为位于 $x$ 轴上方的半圆盘。
>
>解出上半圆弧的直角坐标函数：$y = \sqrt{x - x^2}$。
>
>区域在 $x$ 轴上的投影区间为 $[0, 1]$。
>
>[3]写出 X 型累次积分：
>
>采用垂直穿线法：
>
>下边界为 $x$ 轴：$y = 0$；
>
>上边界为半圆弧：$y = \sqrt{x - x^2}$。
>
>累次积分为：
>
>$$\int_0^1 \mathrm{d}x \int_0^{\sqrt{x-x^2}} f(x, y)\,\mathrm{d}y$$
>
>故正确选项为 (D)。

**习题[14.4]:分段绝对值区域直角积分化为极坐标扇形积分**

累次积分 $I = \int_{-1}^1 \mathrm{d}x \int_{|x|}^{\sqrt{2-x^2}} \sin(x^2 + y^2)\,\mathrm{d}y$ 的值为：
(A) $\frac{\pi}{4}\sin 2$
(B) $\frac{\pi}{4}(1 - \cos 2)$
(C) $\frac{\pi}{2}(1 - \cos 2)$
(D) $\frac{\pi}{2}\sin 2$

主要思路:绘制出由折线 $y = |x|$ 与圆弧 $y = \sqrt{2 - x^2}$ 围成的扇形闭区域，识别出其在极坐标下的扇形参数并计算积分

>[1]区域几何形状分析：
>
>积分区域由不等式组刻画：
>
>$$-1 \le x \le 1, \quad |x| \le y \le \sqrt{2 - x^2}$$
>
>下边界为 $y = |x|$（即第一象限角平分线 $y = x$ 与第二象限角平分线 $y = -x$）；
>
>上边界为中心在原点、半径为 $\sqrt{2}$ 的圆的上半圆弧 $x^2 + y^2 = 2$。
>
>两边界交点由 $x^2 + |x|^2 = 2 \implies 2x^2 = 2 \implies x = \pm 1$ 确定，交点为 $(-1, 1)$ 与 $(1, 1)$。
>
>[2]极坐标系下的区域表示：
>
>折线 $y = x$ ($x > 0$) 对应的射线为 $\theta = \frac{\pi}{4}$；
>
>折线 $y = -x$ ($x < 0$) 对应的射线为 $\theta = \frac{3\pi}{4}$。
>
>极径 $r$ 从原点 $r = 0$ 到外边界圆周 $r = \sqrt{2}$。
>
>因此区域在极坐标下为标准扇形：
>
>$$\frac{\pi}{4} \le \theta \le \frac{3\pi}{4}, \quad 0 \le r \le \sqrt{2}$$
>
>[3]极坐标累次积分计算：
>
>$$I = \int_{\frac{\pi}{4}}^{\frac{3\pi}{4}} \mathrm{d}\theta \int_0^{\sqrt{2}} \sin(r^2) \cdot r\,\mathrm{d}r = \left( \frac{3\pi}{4} - \frac{\pi}{4} \right) \left[ -\frac{1}{2}\cos(r^2) \right]_0^{\sqrt{2}}$$
>
>$$= \frac{\pi}{2} \cdot \left( -\frac{1}{2}\cos 2 - \left(-\frac{1}{2}\right) \right) = \frac{\pi}{4}(1 - \cos 2)$$
>
>故正确选项为 (B)。

**习题[14.5]:二维空间阶跃示性函数的卷积型二重积分**

设阶跃函数 $f(t) = \begin{cases} 1, & 0 \le t \le a \\ \\ 0, & \text{其他} \end{cases}$ ($a > 0$)，记二重积分 $I = \iint_{\mathbb{R}^2} f(x) f(y - x)\,\mathrm{d}x\mathrm{d}y$，求 $I$ 的值。

主要思路:由两乘积阶跃因子同时非零的充要条件确定有效积分区域，作仿射换元化为矩形域积分

>[1]确定被积函数的非零支撑集：
>
>被积函数 $f(x) f(y - x) \neq 0$ 当且仅当：
>
>$$0 \le x \le a \quad \text{且} \quad 0 \le y - x \le a$$
>
>即点 $(x, y)$ 必须落在以下平行四边形区域 $D$ 内：
>
>$$D = \{(x, y) \mid 0 \le x \le a, \; x \le y \le x + a\}$$
>
>在区域 $D$ 内，被积函数恒等于 $1 \times 1 = 1$；在 $D$ 之外，被积函数恒等于 $0$。
>
>[2]坐标换元与雅可比行列式：
>
>引入新变量：$u = x, \; v = y - x$。
>
>偏导数矩阵：
>
>$$\frac{\partial(u, v)}{\partial(x, y)} = \begin{vmatrix} 1 & 0 \\ \\ -1 & 1 \end{vmatrix} = 1 \implies |J| = \frac{1}{|1|} = 1$$
>
>在新平面 $uOv$ 上，积分区域 $D'$ 映射为标准矩形：
>
>$$0 \le u \le a, \quad 0 \le v \le a$$
>
>[3]计算换元积分：
>
>$$I = \iint_{D'} 1 \cdot 1\,\mathrm{d}u\mathrm{d}v = \int_0^a \mathrm{d}u \int_0^a 1\,\mathrm{d}v = a \times a = a^2$$
>
>结论：二重积分的值为 $a^2$。

**习题[14.6]:双重变上限积分的求导与 Leibniz 展开**

设函数 $f(x)$ 连续，定义 $F(t) = \int_1^t \mathrm{d}y \int_y^t f(x)\,\mathrm{d}x$ ($t > 1$)，求导数 $F'(t)$。

主要思路:通过交换积分次序将内层含有双动限的积分完全解耦为单变上限积分，运用微积分基本定理求导

>[1]交换累次积分的次序：
>
>原积分区域由不等式刻画：$1 \le y \le t, \; y \le x \le t$。
>
>该区域为由 $x = t, y = 1$ 以及对角线 $y = x$ 所围成的直角三角形。
>
>交换次序先对 $y$ 积分：$x$ 的总变化区间为 $[1, t]$，对应 $y$ 的变化范围为 $1 \le y \le x$。
>
>$$F(t) = \int_1^t \mathrm{d}x \int_1^x f(x)\,\mathrm{d}y = \int_1^t f(x) (x - 1)\,\mathrm{d}x$$
>
>[2]变上限积分直接求导：
>
>此时被积函数 $g(x) = (x - 1)f(x)$ 与外层上限参数 $t$ 无关。
>
>由于 $f(x)$ 连续，由变上限积分求导定理：
>
>$$F'(t) = \frac{\mathrm{d}}{\mathrm{d}t} \int_1^t (x - 1)f(x)\,\mathrm{d}x = (t - 1)f(t)$$
>
>[3]备选解法（含参变量积分求导公式）核对：
>
>由 Leibniz 求导公式：
>
>$$F'(t) = \left. \left( \int_y^t f(x)\,\mathrm{d}x \right) \right|_{y=t} \cdot 1 + \int_1^t \frac{\partial}{\partial t}\left( \int_y^t f(x)\,\mathrm{d}x \right)\mathrm{d}y$$
>
>第一项 $\int_t^t f(x)\,\mathrm{d}x = 0$；
>
>第二项 $\int_1^t f(t)\,\mathrm{d}y = f(t)(t - 1)$。
>
>两法完全吻合，结论为 $F'(t) = (t - 1)f(t)$。

**习题[14.7]:利用奇偶对称性计算高次多项式二重积分**

计算二重积分 $I = \iint_D (x y^5 - 1)\,\mathrm{d}\sigma$，其中闭区域 $D = \{(x, y) \mid x^2 + y^2 \le 1\}$。

主要思路:单位圆盘区域具备完全关于坐标轴的反射对称性，拆分被积函数，奇函数项积分为零，常数项乘以面积即可

>[1]拆分被积函数与分析对称性：
>
>$$I = \iint_D x y^5\,\mathrm{d}\sigma - \iint_D 1\,\mathrm{d}\sigma$$
>
>闭区域 $D$ 是单位闭圆盘，具有关于 $y$ 轴的反射对称性（若 $(x, y) \in D$，则 $(-x, y) \in D$）。
>
>[2]奇函数项积分抵消：
>
>考查第一项被积函数 $f(x, y) = x y^5$：
>
>$$f(-x, y) = (-x) y^5 = -x y^5 = -f(x, y)$$
>
>即 $f(x, y)$ 是关于变量 $x$ 的奇函数。
>
>由对称性定理：
>
>$$\iint_D x y^5\,\mathrm{d}\sigma = 0$$
>
>[3]常数项积分与结论：
>
>第二项为常数 $1$ 在区域 $D$ 上的积分，等于区域面积 $S_D$：
>
>$$\iint_D 1\,\mathrm{d}\sigma = S_D = \pi \cdot 1^2 = \pi$$
>
>因此：
>
>$$I = 0 - \pi = -\pi$$
>
>结论：二重积分的值为 $-\pi$。

**习题[14.8]:圆域上有理分式与极坐标积分计算**

计算二重积分 $I = \iint_D \frac{1 + xy}{1 + x^2 + y^2}\,\mathrm{d}\sigma$，其中闭区域 $D = \{(x, y) \mid x^2 + y^2 \le 1\}$。

主要思路:区域关于坐标轴对称，利用奇函数性质消去交叉项 $xy$，在极坐标下计算剩余的旋转不变量分式积分

>[1]拆分被积函数并应用对称性：
>
>$$I = \iint_D \frac{1}{1 + x^2 + y^2}\,\mathrm{d}\sigma + \iint_D \frac{xy}{1 + x^2 + y^2}\,\mathrm{d}\sigma$$
>
>区域 $D$ 关于 $x$ 轴与 $y$ 轴均对称。
>
>考查第二项 $g(x, y) = \frac{xy}{1 + x^2 + y^2}$：
>
>$$g(-x, y) = -g(x, y)$$
>
>关于 $x$ 是奇函数，因此其在对称区域 $D$ 上的积分为零：
>
>$$\iint_D \frac{xy}{1 + x^2 + y^2}\,\mathrm{d}\sigma = 0$$
>
>[2]极坐标系下计算第一项：
>
>$$I = \iint_D \frac{1}{1 + x^2 + y^2}\,\mathrm{d}\sigma$$
>
>在极坐标下，$0 \le \theta \le 2\pi, \; 0 \le r \le 1$。
>
>面积微元 $\mathrm{d}\sigma = r\,\mathrm{d}r\mathrm{d}\theta$。
>
>$$I = \int_0^{2\pi} \mathrm{d}\theta \int_0^1 \frac{r}{1 + r^2}\,\mathrm{d}r = 2\pi \cdot \frac{1}{2} \int_0^1 \frac{\mathrm{d}(1 + r^2)}{1 + r^2}$$
>
>[3]对数积分得出最终值：
>
>$$I = \pi \left[ \ln(1 + r^2) \right]_0^1 = \pi(\ln 2 - \ln 1) = \pi\ln 2$$
>
>结论：二重积分的值为 $\pi\ln 2$。

**习题[14.9]:最大值函数 $\max\{x^2, y^2\}$ 的正方形区域积分**

计算二重积分 $I = \iint_D \mathrm{e}^{\max\{x^2, y^2\}}\,\mathrm{d}\sigma$，其中闭区域 $D = [0, 1] \times [0, 1]$。

主要思路:利用对角线 $y = x$ 将单位正方形剖分为两个对称三角形子区域，结合轮换对称性化为一个子区域积分

>[1]剖分区域消除最大值函数：
>
>在对角线 $y = x$ 两侧：
>
>记 $D_1 = \{(x, y) \mid 0 \le x \le 1, \; 0 \le y \le x\}$；
>
>记 $D_2 = \{(x, y) \mid 0 \le y \le 1, \; 0 \le x \le y\}$。
>
>在 $D_1$ 内，$y \le x \implies y^2 \le x^2 \implies \max\{x^2, y^2\} = x^2$；
>
>在 $D_2$ 内，$x \le y \implies x^2 \le y^2 \implies \max\{x^2, y^2\} = y^2$。
>
>[2]轮换对称性合并：
>
>子区域 $D_1$ 与 $D_2$ 关于直线 $y = x$ 对称，且被积函数在两区域上形式对称：
>
>$$\iint_{D_2} \mathrm{e}^{y^2}\,\mathrm{d}\sigma = \iint_{D_1} \mathrm{e}^{x^2}\,\mathrm{d}\sigma$$
>
>因此总积分可化为一个区域的 2 倍：
>
>$$I = 2 \iint_{D_1} \mathrm{e}^{x^2}\,\mathrm{d}\sigma$$
>
>[3]累次积分求解：
>
>在 $D_1$ 上选择垂直穿线（先对 $y$ 积分）：
>
>$$I = 2 \int_0^1 \mathrm{d}x \int_0^x \mathrm{e}^{x^2}\,\mathrm{d}y = 2 \int_0^1 x\mathrm{e}^{x^2}\,\mathrm{d}x = \int_0^1 \mathrm{e}^{x^2}\,\mathrm{d}(x^2)$$
>
>$$= [\mathrm{e}^u]_0^1 = \mathrm{e}^1 - \mathrm{e}^0 = \mathrm{e} - 1$$
>
>结论：二重积分的值为 $\mathrm{e} - 1$。

**习题[14.10]:极坐标复杂无理根式积分转化为直角坐标求解**

计算极坐标累次积分 $I = \iint_D r^2 \sin\theta \sqrt{1 - r^2\cos 2\theta}\,\mathrm{d}r\mathrm{d}\theta$，其中 $D = \{(r, \theta) \mid 0 \le \theta \le \frac{\pi}{4}, 0 \le r \le \frac{1}{\cos\theta}\}$。

主要思路:将极坐标被积表达式与边界逆映射为直角坐标，识别出被积函数中含有关于 $y$ 的可凑微分因子，在三角形区域上计算

>[1]极坐标逆转为直角坐标表达式：
>
>分解被积微元：
>
>$$r^2 \sin\theta \sqrt{1 - r^2\cos 2\theta}\,\mathrm{d}r\mathrm{d}\theta = (r\sin\theta) \sqrt{1 - r^2(\cos^2\theta - \sin^2\theta)} \cdot (r\,\mathrm{d}r\mathrm{d}\theta)$$
>
>由直角与极坐标对应关系：
>
>$$x = r\cos\theta, \quad y = r\sin\theta, \quad \mathrm{d}x\mathrm{d}y = r\,\mathrm{d}r\mathrm{d}\theta$$
>
>被积表达式化为：
>
>$$y \sqrt{1 - (x^2 - y^2)}\,\mathrm{d}x\mathrm{d}y = y \sqrt{1 - x^2 + y^2}\,\mathrm{d}x\mathrm{d}y$$
>
>[2]确定直角坐标积分区域：
>
>边界射线 $\theta = 0 \implies y = 0$；
>
>边界射线 $\theta = \frac{\pi}{4} \implies y = x$；
>
>外边界 $r = \frac{1}{\cos\theta} \iff r\cos\theta = 1 \iff x = 1$。
>
>因此区域在直角坐标系下为由 $x = 1, y = 0, y = x$ 所围成的直角三角形：
>
>$$0 \le x \le 1, \quad 0 \le y \le x$$
>
>[3]累次积分求解：
>
>先对 $y$ 积分（内层凑微分）：
>
>$$I = \int_0^1 \mathrm{d}x \int_0^x y(1 - x^2 + y^2)^{1/2}\,\mathrm{d}y = \int_0^1 \mathrm{d}x \left[ \frac{1}{3}(1 - x^2 + y^2)^{3/2} \right]_0^x$$
>
>$$= \frac{1}{3} \int_0^1 \left( 1 - (1 - x^2)^{3/2} \right)\mathrm{d}x = \frac{1}{3} - \frac{1}{3} \int_0^1 (1 - x^2)^{3/2}\,\mathrm{d}x$$
>
>令 $x = \sin t$ ($t \in [0, \frac{\pi}{2}]$)：
>
>$$\int_0^1 (1 - x^2)^{3/2}\,\mathrm{d}x = \int_0^{\frac{\pi}{2}} \cos^4 t\,\mathrm{d}t = \frac{3}{4} \times \frac{1}{2} \times \frac{\pi}{2} = \frac{3\pi}{16}$$
>
>代入得：
>
>$$I = \frac{1}{3} - \frac{1}{3} \cdot \frac{3\pi}{16} = \frac{1}{3} - \frac{\pi}{16}$$
>
>结论：积分值为 $\frac{1}{3} - \frac{\pi}{16}$。

**习题[14.11]:广义无穷无界区域极坐标反常二重积分**

计算反常二重积分 $I = \int_0^{\frac{\pi}{2}} \cos\theta\,\mathrm{d}\theta \int_0^{+\infty} r^2 \mathrm{e}^{-r^2\sin^2\theta} \cdot \frac{1}{1 + r^2\cos^2\theta} r\,\mathrm{d}r$（或化简型 $I = \iint_D x \mathrm{e}^{-y^2}\,\mathrm{d}x\mathrm{d}y$，其中 $D = [0, \frac{1}{2}] \times [0, +\infty)$）。

主要思路:将极坐标形式的无界区域反常积分转化为直角坐标，识别高斯积分因子与多项式因子的乘积求解

>[1]直角坐标映射与变量识别：
>
>令 $x = r\cos\theta, y = r\sin\theta$，面积微元 $\mathrm{d}x\mathrm{d}y = r\,\mathrm{d}r\mathrm{d}\theta$。
>
>考查第一象限有界带状无界区域 $D = \{(x, y) \mid 0 \le x \le \frac{1}{2}, \; 0 \le y < +\infty\}$。
>
>被积函数为 $f(x, y) = x \mathrm{e}^{-y^2}$。
>
>[2]计算直角坐标下的反常二重积分：
>
>由于变量完全分离，化为两个一元积分的乘积：
>
>$$I = \left( \int_0^{\frac{1}{2}} x\,\mathrm{d}x \right) \left( \int_0^{+\infty} \mathrm{e}^{-y^2}\,\mathrm{d}y \right)$$
>
>[3]代入高斯积分得出结果：
>
>第一项定积分：
>
>$$\int_0^{\frac{1}{2}} x\,\mathrm{d}x = \left[ \frac{x^2}{2} \right]_0^{\frac{1}{2}} = \frac{1}{8}$$
>
>第二项为标准半轴高斯积分：
>
>$$\int_0^{+\infty} \mathrm{e}^{-y^2}\,\mathrm{d}y = \frac{\sqrt{\pi}}{2}$$
>
>两者相乘：
>
>$$I = \frac{1}{8} \cdot \frac{\sqrt{\pi}}{2} = \frac{\sqrt{\pi}}{16}$$
>
>若带状区域宽度为 $0 \le x \le \frac{\sqrt{2}}{2}$，则积分为 $\frac{\sqrt{\pi}}{8}$。

**习题[14.12]:积分值极大化闭区域反求与椭圆广义极坐标积分**

设二元连续函数 $f(x, y) = 1 - 2x^2 - y^2$，求使二重积分 $I(D) = \iint_D (1 - 2x^2 - y^2)\,\mathrm{d}\sigma$ 达到最大值的闭区域 $D$，并求出此最大值。

主要思路:根据二重积分保号性，极大化闭区域由非负点集 $1 - 2x^2 - y^2 \ge 0$ 确定；引入广义极坐标变换求解椭圆闭域上的积分

>[1]确定使积分达到最大值的闭区域：
>
>由二重积分的严格保号性：
>
>当 $1 - 2x^2 - y^2 > 0$ 时，被积函数贡献正值；
>
>当 $1 - 2x^2 - y^2 < 0$ 时，被积函数贡献负值。
>
>若区域 $D$ 包含任何使被积函数为负的点，积分值会减小；若遗漏任何使被积函数为正的点，积分值亦会减小。
>
>因此，使积分达到极大值的闭区域为椭圆盘：
>
>$$D = \left\{(x, y) \;\middle|\; 2x^2 + y^2 \le 1\right\} = \left\{(x, y) \;\middle|\; \frac{x^2}{1/2} + \frac{y^2}{1} \le 1\right\}$$
>
>[2]引入广义极坐标变换：
>
>作坐标变换：
>
>$$x = \frac{1}{\sqrt{2}}r\cos\theta, \quad y = r\sin\theta \quad (0 \le \theta \le 2\pi, \; 0 \le r \le 1)$$
>
>计算雅可比行列式：
>
>$$J = \frac{\partial(x, y)}{\partial(r, \theta)} = \begin{vmatrix} \frac{1}{\sqrt{2}}\cos\theta & -\frac{1}{\sqrt{2}}r\sin\theta \\ \\ \sin\theta & r\cos\theta \end{vmatrix} = \frac{1}{\sqrt{2}}r\cos^2\theta - \left(-\frac{1}{\sqrt{2}}r\sin^2\theta\right) = \frac{1}{\sqrt{2}}r$$
>
>面积微元关系：$\mathrm{d}\sigma = |J|\,\mathrm{d}r\mathrm{d}\theta = \frac{1}{\sqrt{2}}r\,\mathrm{d}r\mathrm{d}\theta$。
>
>被积函数代入：$1 - 2x^2 - y^2 = 1 - r^2$。
>
>[3]累次积分求解：
>
>$$I_{\max} = \int_0^{2\pi} \mathrm{d}\theta \int_0^1 (1 - r^2) \cdot \frac{1}{\sqrt{2}}r\,\mathrm{d}r = \frac{2\pi}{\sqrt{2}} \int_0^1 (r - r^3)\,\mathrm{d}r$$
>
>$$= \sqrt{2}\pi \left[ \frac{r^2}{2} - \frac{r^4}{4} \right]_0^1 = \sqrt{2}\pi \left( \frac{1}{2} - \frac{1}{4} \right) = \frac{\sqrt{2}\pi}{4}$$
>
>结论：极大化区域为闭椭圆域 $2x^2 + y^2 \le 1$，积分最大值为 $\frac{\sqrt{2}\pi}{4}$。
