# Chap10 一元积分学的应用(几何)

目的[1]:深刻理解微元分析法（“度量 vs 本质”与 $o(\Delta x)$ 高阶无穷小忽略准则），熟练掌握平面直角坐标、极坐标、参数方程三种体系下的平面图形面积微元构建与计算

目的[2]:彻底掌握旋转体体积两大经典微元（切片圆盘法/圆环法 Disc/Washer Method 与柱壳法 Cylindrical Shells Method），做到根据图形特征自由秒切

目的[3]:深刻掌握平面曲线弧长微元 $\mathrm{d}s$ 在直角坐标、参数方程、极坐标三种体系下的统一定义与精准计算

目的[4]:掌握旋转曲面的侧面积微元 $\mathrm{d}S = 2\pi r\,\mathrm{d}s$ 的本质机理与易错陷阱（绝对不可用 $\mathrm{d}x$ 替代弧长微元 $\mathrm{d}s$）

目的[5]:全面掌握由已知平行截面面积求立体体积的截面积分法，以及函数平均值定理及其变限微分方程逆问题

目的[6]:系统掌握平面均质薄板形心坐标公式、平面曲线质心公式及其与二重积分重心的微积分同构关系

## 1.微元分析法核心思想与平面图形的面积

###### **方法[1]:微元法（元素法）的本质与“度量 vs 本质”辨析**

在高等数学与考研数学中，定积分的最核心应用在于“微元法”（又称元素法）。微元法是将所求几何量或物理量 $U$ 表达为定积分的有效工具。

[1]微元法的标准实施三部曲：
>(1) **分割与近似（求微元 $\mathrm{d}U$）**：
>
>在自变量变化区间 $[a, b]$ 上任取一个微小区间 $[x, x + \mathrm{d}x]$。设在这一小区间上，量 $U$ 的微小增量为 $\Delta U$。若能找到一个形如 $f(x)\,\mathrm{d}x$ 的连续微分表达式，使得：
>
>$$\Delta U = f(x)\,\mathrm{d}x + o(\mathrm{d}x)$$
>
>其中 $o(\mathrm{d}x)$ 是当 $\mathrm{d}x \to 0$ 时比 $\mathrm{d}x$ 更高阶的无穷小量，则称 $\mathrm{d}U = f(x)\,\mathrm{d}x$ 为所求量 $U$ 的**微元**（或微分元素）。
>
>(2) **求和与取极限（积分离散化为整体）**：
>
>对区间 $[a, b]$ 上的全部微元进行连续累加，即取定积分：
>
>$$U = \int_a^b \mathrm{d}U = \int_a^b f(x)\,\mathrm{d}x$$

[2]“度量 vs 本质”的哲学辨析与高阶无穷小舍弃原则：
>(1) **曲边梯形面积中的高阶误差**：
>
>以曲边梯形为例，底边为 $\Delta x$，高为曲线高度。若用矩形面积 $f(x)\Delta x$ 近似梯形面积 $\Delta U$，误差为一个小三角形或小弯曲区域。由于曲线连续可导，该弯折区域的面积不超过 $\frac{1}{2}|\Delta f|\Delta x = \frac{1}{2}|f'(\xi)|(\Delta x)^2 = o(\Delta x)$。因此在极限求和 $\sum \Delta U$ 中，全部误差之和 $\sum o(\Delta x) \to 0$。用矩形微元 $f(x)\,\mathrm{d}x$ 完全精确。
>
>(2) **弧长与侧面积中的致命陷阱**：
>
>在计算曲线弧长或旋转曲面侧面积时，若误以为倾斜曲线微元可以近似为水平线段 $\Delta x$，其误差为：
>
>$$\Delta s - \Delta x = \sqrt{(\Delta x)^2 + (\Delta y)^2} - \Delta x = \Delta x \left(\sqrt{1 + \left(\frac{\Delta y}{\Delta x}\right)^2} - 1\right)$$
>
>此时当 $y' \neq 0$ 时，括号内为非零常数，误差是与 $\Delta x$ 同阶的**同阶无穷小**，而绝非高阶无穷小 $o(\Delta x)$！若直接忽略该误差，求和结果将彻底错误。因此，弧长必须采用斜边弦长 $\mathrm{d}s = \sqrt{\mathrm{d}x^2 + \mathrm{d}y^2}$ 作为微元。

###### **公式[1]:直角坐标系下的平面图形面积**

设平面图形由连续曲线所围成，按投影方向划分为 $X$ 型与 $Y$ 型区域：

[1]$X$ 型区域（垂直条微元法）：
>若平面区域 $D$ 由上边界 $y = y_2(x)$、下边界 $y = y_1(x)$ 以及两条垂直直线 $x = a, x = b$ ($a < b$) 围成，且 $y_2(x) \geqslant y_1(x)$：
>
>取宽为 $\mathrm{d}x$ 的垂直狭长矩形微元，面积微元为：
>
>$$\mathrm{d}S = [y_2(x) - y_1(x)]\,\mathrm{d}x$$
>
>平面图形总面积为：
>
>$$S = \int_a^b [y_2(x) - y_1(x)]\,\mathrm{d}x$$

[2]$Y$ 型区域（水平条微元法）：
>若平面区域 $D$ 由右边界 $x = x_2(y)$、左边界 $x = x_1(y)$ 以及两条水平直线 $y = c, y = d$ ($c < d$) 围成，且 $x_2(y) \geqslant x_1(y)$：
>
>取高为 $\mathrm{d}y$ 的水平狭长矩形微元，面积微元为：
>
>$$\mathrm{d}S = [x_2(y) - x_1(y)]\,\mathrm{d}y$$
>
>平面图形总面积为：
>
>$$S = \int_c^d [x_2(y) - x_1(y)]\,\mathrm{d}y$$

###### **公式[2]:参数方程下的平面图形面积**

若平面曲线由参数方程给出：

$$\begin{cases} x = x(t) \\ \\ y = y(t) \end{cases} \quad (\alpha \leqslant t \leqslant \beta)$$

[1]常规积分公式：
>若参数 $t$ 从 $\alpha$ 增加到 $\beta$ 时，$x(t)$ 单调增加，且曲线在 $x$ 轴上方，面积微元为：
>
>$$\mathrm{d}S = y(x)\,\mathrm{d}x = y(t)x'(t)\,\mathrm{d}t$$
>
>故平面图形面积为：
>
>$$S = \int_\alpha^\beta y(t)x'(t)\,\mathrm{d}t$$
>
>若随着 $t$ 增大 $x(t)$ 递减，则加负号或取绝对值 $|x'(t)|$ 保持非负。

[2]闭合曲线面积的对称式（格林公式导出）：
>对于无自交的正向闭合光滑曲线 $L$（逆时针方向），围成区域 $D$ 的面积可表示为第二类曲线积分，根据格林公式：
>
>$$S = \iint_D \mathrm{d}x\mathrm{d}y = \frac{1}{2}\oint_L (x\,\mathrm{d}y - y\,\mathrm{d}x)$$
>
>代入参数方程得高度对称的形式：
>
>$$S = \frac{1}{2}\int_\alpha^\beta [x(t)y'(t) - y(t)x'(t)]\,\mathrm{d}t$$
>
>该公式在处理摆线拱、星形线、椭圆等参数曲线时极为优雅且不易混淆符号。

###### **公式[3]:极坐标系下的平面图形面积**

在极坐标系 $(r, \theta)$ 下，平面图形由射线及极径曲线界定：

[1]单曲线扇形微元：
>由曲线 $r = r(\theta)$ 以及两条极角射线 $\theta = \alpha, \theta = \beta$ ($\alpha < \beta$) 所围成的曲边扇形：
>
>取夹角为 $\mathrm{d}\theta$ 的微小扇形，由于半径为 $r(\theta)$，弧长为 $r(\theta)\,\mathrm{d}\theta$，小扇形面积近似为以 $r$ 为底、弧长为高的三角形面积：
>
>$$\mathrm{d}S = \frac{1}{2}r^2(\theta)\,\mathrm{d}\theta$$
>
>图形总面积为：
>
>$$S = \frac{1}{2}\int_\alpha^\beta r^2(\theta)\,\mathrm{d}\theta$$

[2]双曲线同向夹层面积：
>若区域介于外边界 $r_2(\theta)$ 与内边界 $r_1(\theta)$ 之间 ($r_2(\theta) \geqslant r_1(\theta) \geqslant 0$)：
>
>$$\mathrm{d}S = \frac{1}{2}[r_2^2(\theta) - r_1^2(\theta)]\,\mathrm{d}\theta \implies S = \frac{1}{2}\int_\alpha^\beta [r_2^2(\theta) - r_1^2(\theta)]\,\mathrm{d}\theta$$

## 2.旋转体体积与已知平行截面面积的立体体积

###### **公式[4]:绕坐标轴旋转的旋转体体积**

平面区域绕定直线旋转一周所形成的几何体称为旋转体。考研中根据切片方向分为“圆盘/圆环法”与“圆柱壳法”：

[1]圆盘法与圆环法 (Disk / Washer Method，垂直切片)：
>(1) **绕 $x$ 轴旋转**：
>
>由连续曲线 $y = f(x)$、$x$ 轴及垂线 $x = a, x = b$ ($a < b$) 围成的曲边梯形绕 $x$ 轴旋转：
>
>垂直于 $x$ 轴切出的薄片为底半径为 $|y(x)|$、厚度为 $\mathrm{d}x$ 的圆盘，体积微元为：
>
>$$\mathrm{d}V_x = \pi y^2(x)\,\mathrm{d}x$$
>
>总体积为：
>
>$$V_x = \pi \int_a^b y^2(x)\,\mathrm{d}x$$
>
>若区域由两曲线 $y_2(x) \geqslant y_1(x) \geqslant 0$ 界定，则切片为圆环（Washer），体积为：
>
>$$V_x = \pi \int_a^b [y_2^2(x) - y_1^2(x)]\,\mathrm{d}x$$
>
>(2) **绕 $y$ 轴旋转（$Y$ 型截面）**：
>
>若区域由 $x = g(y)$ 及水平线 $y = c, y = d$ 界定，绕 $y$ 轴旋转时垂直于 $y$ 轴切片：
>
>$$V_y = \pi \int_c^d x^2(y)\,\mathrm{d}y$$

[2]圆柱壳法 (Cylindrical Shells Method，平行切片/套筒法)：
>(1) **绕 $y$ 轴旋转（自变量为 $x$）**：
>
>曲边梯形 $0 \leqslant y \leqslant f(x), a \leqslant x \leqslant b$ ($0 \leqslant a < b$) 绕 $y$ 轴旋转：
>
>在 $x$ 处取厚度为 $\mathrm{d}x$ 的竖向狭长条，绕 $y$ 轴旋转一周展开后为一个薄壁圆柱薄壳：
>
>- 薄壳旋转半径为 $x$；
>- 薄壳高度为 $f(x)$；
>- 薄壳周长为 $2\pi x$；
>- 薄壳壁厚为 $\mathrm{d}x$。
>
>体积微元为薄壳侧面积乘壁厚：
>
>$$\mathrm{d}V_y = 2\pi x f(x)\,\mathrm{d}x$$
>
>总体积为：
>
>$$V_y = 2\pi \int_a^b x f(x)\,\mathrm{d}x$$
>
>(2) **绕 $x$ 轴旋转（自变量为 $y$）**：
>
>同理，由 $x = g(y), c \leqslant y \leqslant d$ ($0 \leqslant c < d$) 绕 $x$ 轴旋转：
>
>$$V_x = 2\pi \int_c^d y g(y)\,\mathrm{d}y$$

[3]绕平行于坐标轴的直线旋转：
>若旋转轴为水平线 $y = y_0$ 或垂直线 $x = x_0$：
>
>- 圆盘法只需将回转半径修正为点到轴的垂直距离，如绕 $y = y_0$ 旋转：$\mathrm{d}V = \pi |y(x) - y_0|^2\,\mathrm{d}x$；
>- 圆柱壳法只需将圆柱半径修正为 $|x - x_0|$ 或 $|y - y_0|$，如绕 $x = x_0$ 旋转：$\mathrm{d}V = 2\pi |x - x_0| y(x)\,\mathrm{d}x$。

###### **公式[5]:已知平行截面面积的立体体积**

若一个立体介于垂直于 $x$ 轴的两平面 $x = a$ 与 $x = b$ ($a < b$) 之间：

[1]截面积分原理：
>过点 $x \in [a, b]$ 作垂直于 $x$ 轴的平行截面，若该截面的面积为已知连续函数 $A(x)$：
>
>取厚度为 $\mathrm{d}x$ 的立体薄片，薄片体积微元为：
>
>$$\mathrm{d}V = A(x)\,\mathrm{d}x$$
>
>立体的总体积为：
>
>$$V = \int_a^b A(x)\,\mathrm{d}x$$

[2]考研典型截面几何形状：
>(1) 截面为圆或半圆：$A(x) = \pi R^2(x)$ 或 $\frac{1}{2}\pi R^2(x)$；
>
>(2) 截面为正方形：边长为 $l(x)$，则 $A(x) = l^2(x)$；
>
>(3) 截面为等边三角形：边长为 $l(x)$，则 $A(x) = \frac{\sqrt{3}}{4}l^2(x)$；
>
>(4) 截面为等腰直角三角形：直角边为 $l(x)$，则 $A(x) = \frac{1}{2}l^2(x)$。

## 3.平面曲线的弧长

###### **公式[6]:三大坐标系下的弧长微元与积分公式**

弧长微元 $\mathrm{d}s$ 是曲线切向位移的欧氏长度度量，满足勾股定理：$(\mathrm{d}s)^2 = (\mathrm{d}x)^2 + (\mathrm{d}y)^2$。

[1]直角坐标系形式：
>(1) **显式函数 $y = f(x) \quad (a \leqslant x \leqslant b)$**：
>
>$$\mathrm{d}s = \sqrt{(\mathrm{d}x)^2 + (\mathrm{d}y)^2} = \sqrt{1 + [f'(x)]^2}\,\mathrm{d}x$$
>
>弧长为：
>
>$$s = \int_a^b \sqrt{1 + [f'(x)]^2}\,\mathrm{d}x$$
>
>(2) **反函数形式 $x = g(y) \quad (c \leqslant y \leqslant d)$**：
>
>$$\mathrm{d}s = \sqrt{1 + [g'(y)]^2}\,\mathrm{d}y \implies s = \int_c^d \sqrt{1 + [g'(y)]^2}\,\mathrm{d}y$$

[2]参数方程形式：
>曲线由 $\begin{cases} x = x(t) \\ \\ y = y(t) \end{cases} \quad (\alpha \leqslant t \leqslant \beta)$ 给出，其中 $x'(t), y'(t)$ 连续且不同时为 0：
>
>$$\mathrm{d}s = \sqrt{[x'(t)\,\mathrm{d}t]^2 + [y'(t)\,\mathrm{d}t]^2} = \sqrt{[x'(t)]^2 + [y'(t)]^2}\,\mathrm{d}t$$
>
>弧长为：
>
>$$s = \int_\alpha^\beta \sqrt{[x'(t)]^2 + [y'(t)]^2}\,\mathrm{d}t$$

[3]极坐标形式：
>曲线由 $r = r(\theta) \quad (\alpha \leqslant \theta \leqslant \beta)$ 给出：
>
>由直角坐标与极坐标转换关系：$x = r(\theta)\cos\theta, y = r(\theta)\sin\theta$。
>
>两边微分：
>
>$$\mathrm{d}x = r'\cos\theta\,\mathrm{d}\theta - r\sin\theta\,\mathrm{d}\theta, \quad \mathrm{d}y = r'\sin\theta\,\mathrm{d}\theta + r\cos\theta\,\mathrm{d}\theta$$
>
>平方求和：
>
>$$(\mathrm{d}x)^2 + (\mathrm{d}y)^2 = [r^2(\theta) + (r'(\theta))^2]\,(\mathrm{d}\theta)^2$$
>
>故极坐标下的弧长微元为：
>
>$$\mathrm{d}s = \sqrt{r^2(\theta) + [r'(\theta)]^2}\,\mathrm{d}\theta$$
>
>弧长为：
>
>$$s = \int_\alpha^\beta \sqrt{r^2(\theta) + [r'(\theta)]^2}\,\mathrm{d}\theta$$

## 4.旋转曲面的侧面积

###### **公式[7]:旋转曲面侧面积微元与计算公式**

平面光滑弧段绕定轴旋转所生成的曲面称为旋转曲面。

[1]微元原理与几何剖析：
>在曲线上取微元弧段 $\mathrm{d}s$。该小段绕轴旋转一周展开后为一个高（母线长）为 $\mathrm{d}s$、上下底周长近似为 $2\pi r$ 的圆台侧面：
>
>$$\mathrm{d}S = 2\pi r\,\mathrm{d}s$$
>
>其中 $r$ 为曲线点到旋转轴的垂直距离。
>
>**核心红线**：微元是弧长 $\mathrm{d}s$，而不是水平投影 $\mathrm{d}x$。用圆柱面积 $2\pi y\,\mathrm{d}x$ 替代会导致系统性误差，因为斜率 $y' \neq 0$ 时 $\mathrm{d}s = \sqrt{1+y'^2}\,\mathrm{d}x > \mathrm{d}x$。

[2]直角坐标系下的旋转侧面积：
>(1) **绕 $x$ 轴旋转**：
>
>回转半径为 $r = |y(x)|$：
>
>$$S_x = 2\pi \int_a^b |y(x)|\,\mathrm{d}s = 2\pi \int_a^b |y(x)|\sqrt{1 + [y'(x)]^2}\,\mathrm{d}x$$
>
>(2) **绕 $y$ 轴旋转**：
>
>回转半径为 $r = |x|$：
>
>$$S_y = 2\pi \int_a^b |x|\,\mathrm{d}s = 2\pi \int_a^b |x|\sqrt{1 + [y'(x)]^2}\,\mathrm{d}x$$

[3]参数方程下的旋转侧面积：
>曲线由 $\begin{cases} x = x(t) \\ \\ y = y(t) \end{cases} \quad (\alpha \leqslant t \leqslant \beta)$ 给出：
>
>(1) **绕 $x$ 轴**：
>
>$$S_x = 2\pi \int_\alpha^\beta |y(t)|\sqrt{[x'(t)]^2 + [y'(t)]^2}\,\mathrm{d}t$$
>
>(2) **绕 $y$ 轴**：
>
>$$S_y = 2\pi \int_\alpha^\beta |x(t)|\sqrt{[x'(t)]^2 + [y'(t)]^2}\,\mathrm{d}t$$

[4]极坐标下的旋转侧面积：
>曲线 $r = r(\theta) \quad (\alpha \leqslant \theta \leqslant \beta)$ 绕极轴（$x$ 轴，此时纵坐标 $y = r\sin\theta \geqslant 0$）旋转：
>
>$$S_x = 2\pi \int_\alpha^\beta r(\theta)\sin\theta \sqrt{r^2(\theta) + [r'(\theta)]^2}\,\mathrm{d}\theta$$

## 5.函数平均值与平面图形形心坐标

###### **公式[8]:连续函数在区间上的平均值**

[1]定义与几何意义：
>设 $f(x)$ 在闭区间 $[a, b]$ 上连续，称数值：
>
>$$\overline{f} = \frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x$$
>
>为函数 $f(x)$ 在区间 $[a, b]$ 上的**算术平均值**（平均值）。
>
>几何意义：由积分第一中值定理，在 $(a, b)$ 内至少存在一点 $\xi$，使得 $\int_a^b f(x)\,\mathrm{d}x = f(\xi)(b-a)$，即 $f(\xi) = \overline{f}$。以区间长 $b-a$ 为底、以平均值 $\overline{f}$ 为高的矩形面积，恰好等于曲边梯形的真实面积。

[2]离散平均到连续积分的极限过渡：
>将区间 $[a, b]$ 进行 $n$ 等分，分点为 $x_i = a + i\frac{b-a}{n}$。采样点函数值的算术平均为：
>
>$$\frac{1}{n}\sum_{i=1}^n f(x_i) = \frac{1}{b-a}\sum_{i=1}^n f(x_i)\frac{b-a}{n} = \frac{1}{b-a}\sum_{i=1}^n f(x_i)\Delta x$$
>
>当 $n \to \infty$ 时，黎曼和极限即给出连续平均值 $\frac{1}{b-a}\int_a^b f(x)\,\mathrm{d}x$。

###### **公式[9]:平面图形与曲线的形心坐标**

形心（几何中心）即假定面密度或线密度均匀恒定（$\rho = 1$）时的质心坐标。

[1]平面均质薄板的形心 $(\overline{x}, \overline{y})$：
>设平面均质区域 $D$ 由 $0 \leqslant y \leqslant f(x), a \leqslant x \leqslant b$ 确定：
>
>(1) **总面积 $A$**：
>
>$$A = \int_a^b f(x)\,\mathrm{d}x$$
>
>(2) **对 $y$ 轴的静矩 $M_y$（决定横坐标 $\overline{x}$）**：
>
>取宽为 $\mathrm{d}x$ 的竖条，其横坐标为 $x$，微元面积为 $f(x)\,\mathrm{d}x$，静矩微元为 $\mathrm{d}M_y = x\,\mathrm{d}A = x f(x)\,\mathrm{d}x$：
>
>$$\overline{x} = \frac{M_y}{A} = \frac{\int_a^b x f(x)\,\mathrm{d}x}{\int_a^b f(x)\,\mathrm{d}x}$$
>
>(3) **对 $x$ 轴的静矩 $M_x$（决定纵坐标 $\overline{y}$）**：
>
>竖条的高度为 $f(x)$，由于竖条质量均匀，其形心高度处于中点 $\frac{f(x)}{2}$，静矩微元为 $\mathrm{d}M_x = \frac{f(x)}{2}\,\mathrm{d}A = \frac{1}{2}f^2(x)\,\mathrm{d}x$：
>
>$$\overline{y} = \frac{M_x}{A} = \frac{\frac{1}{2}\int_a^b f^2(x)\,\mathrm{d}x}{\int_a^b f(x)\,\mathrm{d}x}$$
>
>(4) **两曲线夹层区域通式**：
>
>若区域界于 $f_1(x) \leqslant y \leqslant f_2(x)$ 之间：
>
>$$\overline{x} = \frac{\int_a^b x [f_2(x) - f_1(x)]\,\mathrm{d}x}{\int_a^b [f_2(x) - f_1(x)]\,\mathrm{d}x}, \quad \overline{y} = \frac{\frac{1}{2}\int_a^b [f_2^2(x) - f_1^2(x)]\,\mathrm{d}x}{\int_a^b [f_2(x) - f_1(x)]\,\mathrm{d}x}$$

[2]平面均质细曲线的质心 $(\overline{x}, \overline{y})$：
>设平面连续曲线段为 $L$，总弧长为 $s = \int_L \mathrm{d}s$：
>
>$$\overline{x} = \frac{\int_L x\,\mathrm{d}s}{\int_L \mathrm{d}s} = \frac{1}{s}\int_L x\,\mathrm{d}s, \quad \overline{y} = \frac{\int_L y\,\mathrm{d}s}{\int_L \mathrm{d}s} = \frac{1}{s}\int_L y\,\mathrm{d}s$$
>
>计算时将 $\mathrm{d}s$ 根据直角坐标、参数方程或极坐标代入对应的微分形式。
