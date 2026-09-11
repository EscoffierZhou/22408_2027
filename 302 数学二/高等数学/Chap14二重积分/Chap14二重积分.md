# Chap14 二重积分

目的[1]:深刻理解二重积分的定义与空间曲顶柱体体积几何意义，掌握二元黎曼和的极限本质与网格直径趋于零的充要条件

目的[2]:融会贯通二重积分的基本性质（线性性、区域可加性、保号性、估值不等式、积分中值定理与对偶平均值）

目的[3]:熟练掌握普通对称性（奇偶性化简积分）与轮换对称性（坐标对调化简积分）在二重积分计算中的核心秒杀策略

目的[4]:精通直角坐标系下X型与Y型积分区域的确定、穿线法以及化二重积分为二次累次积分与交换积分次序技巧

目的[5]:精通极坐标系下二重积分的计算准则、极点在不同位置（区域内部、边界上、区域外部）时的穿线与边界角确定方法

目的[6]:系统掌握考研高频平面曲线（直线族、偏心圆、心形线、伯努利双纽线、玫瑰线、旋转椭圆等）及其积分区域图鉴

目的[7]:掌握二重积分的换元法与雅可比行列式（Jacobian）理论，熟练处理一般仿射变换、广义极坐标与斜坐标系变换

目的[8]:掌握平面薄板质心坐标公式、转动惯量以及古鲁金第二定理（Pappus-Guldinus 定理）在旋转体体积计算与质心反求中的应用

## 1.二重积分的概念与几何意义

###### **概念[1]:二重积分的定义与黎曼和**

[1]定义背景与曲顶柱体体积问题：
>设平面上有界闭区域为 $D$，曲顶柱体的底面为 $D$，顶面由连续曲面 $z = f(x, y) \ge 0$ 给出，侧面是以 $D$ 的边界为准线、母线平行于 $z$ 轴的柱面。
>
>求该曲顶柱体的体积 $V$ 需经历经典的“四步法”：
>
>(1) **分割**：用任意一组光滑曲线网将区域 $D$ 任意分割成 $n$ 个小闭区域 $\Delta\sigma_1, \Delta\sigma_2, \dots, \Delta\sigma_n$，其面积分别记作 $\Delta\sigma_i$ ($i = 1, 2, \dots, n$)。
>
>记 $\lambda = \max\limits_{1 \le i \le n} \{\mathrm{diam}(\Delta\sigma_i)\}$ 为这 $n$ 个小区域直径的最大值（网格直径）。
>
>(2) **近似**：在每个小区域 $\Delta\sigma_i$ 上任取一点 $(\xi_i, \eta_i)$，以底面积为 $\Delta\sigma_i$、高为 $f(\xi_i, \eta_i)$ 的平顶平柱体体积近似代替第 $i$ 个小曲顶柱体的体积：
>
>$$\Delta V_i \approx f(\xi_i, \eta_i)\,\Delta\sigma_i$$
>
>(3) **求和**：曲顶柱体体积的近似值为全部小平柱体体积之和：
>
>$$V \approx \sum_{i=1}^n f(\xi_i, \eta_i)\,\Delta\sigma_i$$
>
>(4) **取极限**：当网格直径 $\lambda \to 0$ 时，如果上述黎曼和式的极限存在，则该极限值即为曲顶柱体的真实体积：
>
>$$V = \lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i, \eta_i)\,\Delta\sigma_i$$

[2]二重积分的分析定义：
>设 $f(x, y)$ 是有界闭区域 $D$ 上的有界函数。将 $D$ 任意划分为 $n$ 个小区域 $\Delta\sigma_i$，在每个 $\Delta\sigma_i$ 上任取一点 $(\xi_i, \eta_i)$。
>
>若极限：
>
>$$\lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i, \eta_i)\,\Delta\sigma_i = I$$
>
>存在，且极限值 $I$ 与区域 $D$ 的分割方法以及点 $(\xi_i, \eta_i)$ 的选取方法完全无关，则称函数 $f(x, y)$ 在区域 $D$ 上<font color=deeppink>可积</font>。
>
>数 $I$ 称为函数 $f(x, y)$ 在区域 $D$ 上的<font color=deeppink>二重积分</font>，记作：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma \quad \text{或} \quad \iint_D f(x, y)\,\mathrm{d}x\mathrm{d}y$$
>
>其中 $f(x, y)$ 称为<font color=deeppink>被积函数</font>，$f(x, y)\,\mathrm{d}\sigma$ 称为<font color=deeppink>被积表达式</font>，$\mathrm{d}\sigma$（或 $\mathrm{d}x\mathrm{d}y$）称为<font color=deeppink>面积微元</font>，$x, y$ 称为<font color=deeppink>积分变量</font>，$D$ 称为<font color=deeppink>积分区域</font>。

###### **概念[2]:二重积分的可积性准则**

[1]充分条件：
>(1) **连续函数必可积**：若二元函数 $f(x, y)$ 在有界闭区域 $D$ 上连续，则 $f(x, y)$ 在 $D$ 上必然可积。
>
>(2) **间断点分布在有限条光滑曲线上**：若有界函数 $f(x, y)$ 在有界闭区域 $D$ 上的间断点全部分布在有限条光滑（或分段光滑）曲线上，则 $f(x, y)$ 在 $D$ 上依然可积。

[2]几何与物理意义：
>(1) **几何意义**：
>
>当 $f(x, y) \ge 0$ 时，$\iint_D f(x, y)\,\mathrm{d}\sigma$ 表示以 $D$ 为底、顶面为曲面 $z = f(x, y)$ 的曲顶柱体的体积；
>
>当 $f(x, y) \le 0$ 时，$\iint_D f(x, y)\,\mathrm{d}\sigma = -V$，表示位于 $xOy$ 平面下方的曲顶柱体体积的负值；
>
>一般情况下，$\iint_D f(x, y)\,\mathrm{d}\sigma$ 表示位于 $xOy$ 平面上方体积减去位于下方体积的<font color=deeppink>代数和</font>。
>
>(2) **物理意义**：
>
>当平面薄板占有的闭区域为 $D$，面密度分布函数为连续函数 $\rho(x, y)$ 时，薄板的总质量 $M$ 为：
>
>$$M = \iint_D \rho(x, y)\,\mathrm{d}\sigma$$

## 2.二重积分的基本性质

###### **定理[1]:线性性质与区域可加性**

[1]线性运算法则：
>设 $\alpha, \beta$ 为任意常数，若 $f(x, y)$ 与 $g(x, y)$ 在闭区域 $D$ 上均可积，则 $\alpha f(x, y) + \beta g(x, y)$ 在 $D$ 上亦可积，且：
>
>$$\iint_D [\alpha f(x, y) + \beta g(x, y)]\,\mathrm{d}\sigma = \alpha \iint_D f(x, y)\,\mathrm{d}\sigma + \beta \iint_D g(x, y)\,\mathrm{d}\sigma$$

[2]积分区域的代数可加性：
>若有界闭区域 $D$ 被分成两个无内部重叠子区域 $D_1$ 与 $D_2$（即 $D = D_1 \cup D_2$ 且 $D_1$ 与 $D_2$ 仅可能在边界曲线相交），则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = \iint_{D_1} f(x, y)\,\mathrm{d}\sigma + \iint_{D_2} f(x, y)\,\mathrm{d}\sigma$$

###### **定理[2]:规范性与面积计算**

[1]常数函数的二重积分：
>当被积函数恒等于常数 $1$ 时，二重积分在数值上等于积分区域 $D$ 的平面几何面积，记作 $S_D$（或 $A_D$）：
>
>$$\iint_D 1\,\mathrm{d}\sigma = \iint_D \mathrm{d}\sigma = S_D$$

###### **定理[3]:单调性、保号性与估值不等式**

[1]单调不等式性：
>若在有界闭区域 $D$ 上恒有 $f(x, y) \le g(x, y)$，则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma \le \iint_D g(x, y)\,\mathrm{d}\sigma$$

[2]严格保号性：
>若在闭区域 $D$ 上 $f(x, y) \ge 0$ 且 $f(x, y)$ 连续不恒为零，则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma > 0$$
>
><font color=red>核心推论（最值区域判定法）</font>：要使二重积分 $\iint_D f(x, y)\,\mathrm{d}\sigma$ 取得绝对最大值，闭区域 $D$ 应当包含且仅包含所有满足 $f(x, y) \ge 0$ 的点集构成的闭区域。

[3]绝对值不等式：
>若 $f(x, y)$ 在闭区域 $D$ 上可积，则 $|f(x, y)|$ 亦可积，且满足三角不等式：
>
>$$\left| \iint_D f(x, y)\,\mathrm{d}\sigma \right| \le \iint_D |f(x, y)|\,\mathrm{d}\sigma$$

[4]估值定理：
>设 $M$ 与 $m$ 分别为连续函数 $f(x, y)$ 在有界闭区域 $D$ 上的最大值与最小值，$S_D$ 为 $D$ 的面积，则恒有：
>
>$$m \cdot S_D \le \iint_D f(x, y)\,\mathrm{d}\sigma \le M \cdot S_D$$

###### **定理[4]:二重积分中值定理与积分平均值**

[1]积分第一中值定理：
>设函数 $f(x, y)$ 在有界闭区域 $D$ 上连续，$D$ 是连通闭区域，$S_D$ 为 $D$ 的面积，则在 $D$ 上至少存在一点 $(\xi, \eta) \in D$，使得：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = f(\xi, \eta) \cdot S_D$$
>
>几何直观：曲顶柱体的体积等于以 $D$ 为底、以某处高度 $f(\xi, \eta)$ 为高的小平顶柱体的体积。

[2]广义积分中值定理：
>设 $f(x, y), g(x, y)$ 在有界闭区域 $D$ 上连续，且 $g(x, y)$ 在 $D$ 上不变号（恒非负或恒非正），则在 $D$ 内至少存在一点 $(\xi, \eta) \in D$，使得：
>
>$$\iint_D f(x, y) g(x, y)\,\mathrm{d}\sigma = f(\xi, \eta) \iint_D g(x, y)\,\mathrm{d}\sigma$$

[3]连续函数的区域平均值：
>二元函数 $f(x, y)$ 在平面区域 $D$ 上的平均值定义为：
>
>$$\bar{f} = \frac{1}{S_D} \iint_D f(x, y)\,\mathrm{d}\sigma$$

## 3.对称性与奇偶性定理

###### **定理[1]:关于坐标轴的普通对称性（奇偶性化简）**

[1]关于 $y$ 轴对称（即 $x \leftrightarrow -x$ 区域不变）：
>设区域 $D$ 关于 $y$ 轴对称，记 $D_1$ 为 $D$ 在右半平面（$x \ge 0$）的部分：
>
>(1) 若 $f(-x, y) = -f(x, y)$（关于 $x$ 为奇函数），则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = 0$$
>
>(2) 若 $f(-x, y) = f(x, y)$（关于 $x$ 为偶函数），则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = 2 \iint_{D_1} f(x, y)\,\mathrm{d}\sigma$$

[2]关于 $x$ 轴对称（即 $y \leftrightarrow -y$ 区域不变）：
>设区域 $D$ 关于 $x$ 轴对称，记 $D_1$ 为 $D$ 在上半平面（$y \ge 0$）的部分：
>
>(1) 若 $f(x, -y) = -f(x, y)$（关于 $y$ 为奇函数），则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = 0$$
>
>(2) 若 $f(x, -y) = f(x, y)$（关于 $y$ 为偶函数），则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = 2 \iint_{D_1} f(x, y)\,\mathrm{d}\sigma$$

[3]关于原点对称（即 $(x, y) \leftrightarrow (-x, -y)$ 区域不变）：
>设区域 $D$ 关于原点对称：
>
>(1) 若 $f(-x, -y) = -f(x, y)$，则 $\iint_D f(x, y)\,\mathrm{d}\sigma = 0$。
>
>(2) 若 $f(-x, -y) = f(x, y)$，则 $\iint_D f(x, y)\,\mathrm{d}\sigma = 2 \iint_{D_1} f(x, y)\,\mathrm{d}\sigma$（$D_1$ 为任意半区）。

###### **定理[2]:关于直线 $y = x$ 的轮换对称性**

[1]轮换对称性定义与基本定理：
>设闭区域 $D$ 关于直线 $y = x$ 对称（即若 $(x, y) \in D$，则 $(y, x) \in D$）。
>
>则对调积分变量 $x$ 与 $y$ 时积分值保持不变：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = \iint_D f(y, x)\,\mathrm{d}\sigma$$
>
>由此可得核心配对求和公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = \frac{1}{2} \iint_D [f(x, y) + f(y, x)]\,\mathrm{d}\sigma$$

[2]常见轮换对称秒杀模型：
>(1) **齐次幂和模型**：若 $D$ 关于 $y = x$ 对称，则：
>
>$$\iint_D x^k\,\mathrm{d}\sigma = \iint_D y^k\,\mathrm{d}\sigma = \frac{1}{2} \iint_D (x^k + y^k)\,\mathrm{d}\sigma$$
>
>(2) **分母对称有理化模型**：
>
>$$\iint_D \frac{x}{x + y}\,\mathrm{d}\sigma = \frac{1}{2} \iint_D \frac{x + y}{x + y}\,\mathrm{d}\sigma = \frac{1}{2} S_D$$
>
>(3) **奇偶差项化简模型**：若 $f(x, y) = -f(y, x)$（反对称），则：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = 0$$

## 4.直角坐标系下的计算方法与交换积分次序

###### **方法[1]:X型与Y型积分区域的确定与穿线法**

[1]X型区域（垂直穿线法，后积 $x$，先积 $y$）：
>如果区域 $D$ 可以表示为：
>
>$$D = \{(x, y) \mid a \le x \le b, \; g_1(x) \le y \le g_2(x)\}$$
>
>其中 $g_1(x), g_2(x)$ 在 $[a, b]$ 上连续，且 $g_1(x) \le g_2(x)$。
>
>穿线法则：在区间 $[a, b]$ 内任取一点 $x$ 作一条平行于 $y$ 轴并朝向正方向的射线，射线从下边界曲线 $y = g_1(x)$ 穿入，从上边界曲线 $y = g_2(x)$ 穿出。
>
>二重积分化为直角坐标下的二次累次积分公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}x\mathrm{d}y = \int_a^b \mathrm{d}x \int_{g_1(x)}^{g_2(x)} f(x, y)\,\mathrm{d}y$$

[2]Y型区域（水平穿线法，后积 $y$，先积 $x$）：
>如果区域 $D$ 可以表示为：
>
>$$D = \{(x, y) \mid c \le y \le d, \; h_1(y) \le x \le h_2(y)\}$$
>
>其中 $h_1(y), h_2(y)$ 在 $[c, d]$ 上连续，且 $h_1(y) \le h_2(y)$。
>
>穿线法则：在区间 $[c, d]$ 内任取一点 $y$ 作一条平行于 $x$ 轴并朝向正方向的射线，射线从左边界曲线 $x = h_1(y)$ 穿入，从右边界曲线 $x = h_2(y)$ 穿出。
>
>二重积分化为累次积分公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}x\mathrm{d}y = \int_c^d \mathrm{d}y \int_{h_1(y)}^{h_2(y)} f(x, y)\,\mathrm{d}x$$

###### **方法[2]:交换积分次序的三步准则**

[1]交换积分次序的标准化解题步骤：
>(1) **根据原累次积分提炼不等式组**：
>
>例如由 $\int_a^b \mathrm{d}x \int_{g_1(x)}^{g_2(x)} f(x, y)\,\mathrm{d}y$ 写出 $D = \{(x, y) \mid a \le x \le b, g_1(x) \le y \le g_2(x)\}$。
>
>(2) **精准绘制平面积分区域 $D$**：
>
>画出边界曲线 $x = a, x = b, y = g_1(x), y = g_2(x)$ 及所有交点，标注阴影连通域。
>
>(3) **反解边界曲线并按另一方向穿线**：
>
>将 $y = g_1(x), y = g_2(x)$ 反解为 $x = h(y)$。若区域在水平方向投影由不同单调分支或折角线界定，则需将其分割为若干个简单的子Y型区域，写出新的外层与内层积分限。

[2]必须交换积分次序的两大经典场景：
>(1) **被积函数的原函数非初等函数**：
>
>如 $\frac{\sin x}{x}, \mathrm{e}^{-x^2}, \mathrm{e}^{y^2}, \cos(y^2), \frac{1}{\ln x}$ 等，在原次序下内层积分无法用初等函数显式积出，必须交换次序先对另一变量求积。
>
>(2) **复杂反函数与动边界组合**：
>
>内层含有复杂的反三角函数如 $\arcsin\sqrt{x}$、多层嵌套函数等，交换次序后先对另一变量积分可衍生出多项式因子，从而利用分部积分法化繁为简。

## 5.极坐标系下的计算方法

###### **概念[1]:极坐标面积微元的几何推导**

[1]极坐标网格与扇形微元：
>设平面点 $P$ 的极坐标为 $(r, \theta)$，直角坐标与极坐标的转换关系为：
>
>$$x = r\cos\theta, \quad y = r\sin\theta \quad (r \ge 0, \; 0 \le \theta < 2\pi)$$
>
>用极径射线簇 $\theta = \text{常数}$ 与同心圆族 $r = \text{常数}$ 将区域分割为小曲边四边形。
>
>对于由 $\theta$ 到 $\theta + \Delta\theta$、由 $r$ 到 $r + \Delta r$ 所围成的小扇形环域，其面积微元为内外两个圆扇形面积之差：
>
>$$\Delta\sigma = \frac{1}{2}(r + \Delta r)^2 \Delta\theta - \frac{1}{2}r^2 \Delta\theta = r\,\Delta r\Delta\theta + \frac{1}{2}(\Delta r)^2 \Delta\theta$$
>
>略去高阶无穷小，得到极坐标系下的面积微元标准公式：
>
>$$\mathrm{d}\sigma = r\,\mathrm{d}r\,\mathrm{d}\theta$$
>
><font color=red>核心避坑警示</font>：由直角坐标转化为极坐标时，面积微元 $\mathrm{d}x\mathrm{d}y$ 必须替换为 $r\,\mathrm{d}r\mathrm{d}\theta$，严禁遗漏因子 $r$！

###### **方法[1]:极点在不同相对位置时的穿线定限法则**

[1]极点 $O(0, 0)$ 位于区域 $D$ 的内部：
>射线绕极点逆时针旋转一周扫过整个区域：
>
>(1) 角度范围：$\alpha = 0, \beta = 2\pi$。
>
>(2) 径向范围：对任意固定的 $\theta$，射线从原点 $r = 0$ 穿入，穿出外边界曲线 $r = R(\theta)$。
>
>累次积分公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = \int_0^{2\pi} \mathrm{d}\theta \int_0^{R(\theta)} f(r\cos\theta, r\sin\theta)\,r\,\mathrm{d}r$$

[2]极点 $O(0, 0)$ 位于区域 $D$ 的边界上：
>过极点向区域引两条切线（或边界渐近线），夹角记为 $[\alpha, \beta]$（跨度通常 $\le \pi$）：
>
>(1) 角度范围：$\theta \in [\alpha, \beta]$。
>
>(2) 径向范围：从极点 $r = 0$ 穿入，穿出对侧边界曲线 $r = R(\theta)$。
>
>累次积分公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = \int_\alpha^\beta \mathrm{d}\theta \int_0^{R(\theta)} f(r\cos\theta, r\sin\theta)\,r\,\mathrm{d}r$$

[3]极点 $O(0, 0)$ 位于区域 $D$ 的外部：
>过极点引区域的两条切线，夹角为 $[\alpha, \beta]$：
>
>(1) 角度范围：$\theta \in [\alpha, \beta]$。
>
>(2) 径向范围：从内边界曲线 $r = r_1(\theta)$ 穿入，穿出外边界曲线 $r = r_2(\theta)$。
>
>累次积分公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}\sigma = \int_\alpha^\beta \mathrm{d}\theta \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,\mathrm{d}r$$

###### **模型[1]:直角坐标与极坐标的选择判据**

[1]优先选用极坐标系的情形：
>(1) **被积函数特征**：被积函数中含有 $x^2 + y^2$、$\sqrt{x^2 + y^2}$、$\frac{y}{x}$、$\frac{x}{y}$ 等旋转不变量结构。
>
>(2) **积分区域特征**：区域边界含有圆、圆弧、圆环、扇形，或含有心形线、双纽线等极坐标初等函数。

[2]优先选用直角坐标系的情形：
>(1) 区域边界主要由平行于坐标轴的直线（如矩形、直角三角形）界定。
>
>(2) 被积函数变量可完全分离为 $f(x) \cdot g(y)$ 且区域为矩形域 $[a, b] \times [c, d]$。

## 6.考研常用曲线与积分区域图鉴

###### **图鉴[1]:常见圆族与偏心圆的极坐标方程**

[1]中心在原点的同心圆族：
>直角坐标方程：$x^2 + y^2 = R^2 \iff$ 极坐标方程：$r = R$。

[2]与坐标轴相切的偏心圆族：
>(1) **中心在 $(a, 0)$、半径为 $a$ 的圆**：
>
>直角坐标：$(x - a)^2 + y^2 = a^2 \iff x^2 + y^2 = 2ax$
>
>极坐标：$r^2 = 2ar\cos\theta \implies r = 2a\cos\theta \quad \left(-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}\right)$
>
>(2) **中心在 $(0, a)$、半径为 $a$ 的圆**：
>
>直角坐标：$x^2 + (y - a)^2 = a^2 \iff x^2 + y^2 = 2ay$
>
>极坐标：$r^2 = 2ar\sin\theta \implies r = 2a\sin\theta \quad (0 \le \theta \le \pi)$

###### **图鉴[2]:高频超越曲线与几何区域**

[1]心形线（Cardioid）：
>(1) 极坐标方程：$r = a(1 + \cos\theta)$ ($a > 0, 0 \le \theta \le 2\pi$)，图形关于极轴对称，尖点在极点处向左凹入。
>
>(2) 围成区域的面积计算：
>
>$$S = \int_0^{2\pi} \mathrm{d}\theta \int_0^{a(1+\cos\theta)} r\,\mathrm{d}r = \frac{1}{2} a^2 \int_0^{2\pi} (1 + \cos\theta)^2\,\mathrm{d}\theta = \frac{3}{2}\pi a^2$$

[2]伯努利双纽线（Lemniscate of Bernoulli）：
>(1) 直角坐标方程：$(x^2 + y^2)^2 = 2a^2(x^2 - y^2)$
>
>(2) 极坐标方程：$r^2 = 2a^2\cos 2\theta$
>
>定义域满足 $\cos 2\theta \ge 0$，即 $-\frac{\pi}{4} \le \theta \le \frac{\pi}{4}$（右瓣）与 $\frac{3\pi}{4} \le \theta \le \frac{5\pi}{4}$（左瓣）。
>
>(3) 全区域总面积：
>
>$$S = 4 \times \frac{1}{2} \int_0^{\frac{\pi}{4}} 2a^2\cos 2\theta\,\mathrm{d}\theta = 2a^2$$

[3]多叶玫瑰线（Rose Curves）：
>(1) $r = a\sin 2\theta$ 或 $r = a\cos 2\theta$（四叶玫瑰线，单叶角宽 $\frac{\pi}{4}$）。
>
>(2) $r = a\cos 3\theta$（三叶玫瑰线，单叶角宽 $\frac{\pi}{3}$）。

[4]椭圆与广义极坐标：
>椭圆域 $\frac{x^2}{a^2} + \frac{y^2}{b^2} \le 1$。
>
>令广义极坐标：$x = ar\cos\theta, y = br\sin\theta$ ($0 \le \theta \le 2\pi, 0 \le r \le 1$)。
>
>面积微元关系：$\mathrm{d}\sigma = ab\,r\,\mathrm{d}r\mathrm{d}\theta$。

## 7.换元法与雅可比行列式

###### **定理[1]:二重积分的一般变量代换定理**

[1]坐标变换映射与可积条件：
>设平面变换 $T: x = x(u, v), y = y(u, v)$ 将 $uOv$ 平面上的有界闭区域 $D'$ 一对一地连续可微映射为 $xOy$ 平面上的有界闭区域 $D$。
>
>假设偏导数连续，且在 $D'$ 内部其雅可比行列式（Jacobian）$J(u, v) \neq 0$：
>
>$$J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}$$
>
>则对 $D$ 上的连续函数 $f(x, y)$，有二重积分换元公式：
>
>$$\iint_D f(x, y)\,\mathrm{d}x\mathrm{d}y = \iint_{D'} f(x(u, v), y(u, v)) \cdot |J(u, v)|\,\mathrm{d}u\mathrm{d}v$$

[2]雅可比行列式的几何微元放大率：
>微元面积变形率的绝对值即为雅可比行列式的绝对值：
>
>$$\mathrm{d}\sigma_{xy} = |J(u, v)|\,\mathrm{d}u\mathrm{d}v$$
>
>重要倒数定理：若映射可逆，则有：
>
>$$\frac{\partial(x, y)}{\partial(u, v)} = \frac{1}{\frac{\partial(u, v)}{\partial(x, y)}}$$
>
>当给出的是反向关系式 $u = u(x, y), v = v(x, y)$ 时，直接求 $\frac{\partial(u, v)}{\partial(x, y)}$ 并取倒数，无需繁琐反解 $x, y$。

###### **模型[1]:高频换元模型与雅可比行列式速查**

[1]线性仿射变换模型（平行四边形区域）：
>设区域边界由平行线族 $a_1 x + b_1 y = c_1, a_1 x + b_1 y = d_1$ 与 $a_2 x + b_2 y = c_2, a_2 x + b_2 y = d_2$ 界定。
>
>令 $u = a_1 x + b_1 y, v = a_2 x + b_2 y$。
>
>雅可比行列式为：
>
>$$\frac{\partial(u, v)}{\partial(x, y)} = \begin{vmatrix} a_1 & b_1 \\ \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1 \implies |J| = \frac{1}{|a_1 b_2 - a_2 b_1|}$$
>
>变换后新区域 $D'$ 成为平行于坐标轴的矩形区域 $[c_1, d_1] \times [c_2, d_2]$，实现变量完全解耦。

[2]双曲带状区域模型：
>设边界由双曲线族 $xy = p_1, xy = p_2$ 与 $y = q_1 x, y = q_2 x$ 界定。
>
>令 $u = xy, v = \frac{y}{x}$。
>
>则 $\frac{\partial(u, v)}{\partial(x, y)} = \begin{vmatrix} y & x \\ \\ -\frac{y}{x^2} & \frac{1}{x} \end{vmatrix} = \frac{y}{x} - \left(-\frac{y}{x}\right) = \frac{2y}{x} = 2v$。
>
>从而面积微元代换为：
>
>$$\mathrm{d}x\mathrm{d}y = \frac{1}{2v}\,\mathrm{d}u\mathrm{d}v$$

## 8.平面几何物理应用与古鲁金第二定理

###### **公式[1]:薄板质量、质心与转动惯量**

[1]平面薄板的质量：
>设面密度分布函数为 $\rho(x, y)$，则总质量为：
>
>$$M = \iint_D \rho(x, y)\,\mathrm{d}\sigma$$

[2]平面薄板的质心坐标 $(\bar{x}, \bar{y})$：
>静态矩定义：
>
>$$M_y = \iint_D x\,\rho(x, y)\,\mathrm{d}\sigma, \quad M_x = \iint_D y\,\rho(x, y)\,\mathrm{d}\sigma$$
>
>质心坐标公式：
>
>$$\bar{x} = \frac{M_y}{M} = \frac{\iint_D x\,\rho(x, y)\,\mathrm{d}\sigma}{\iint_D \rho(x, y)\,\mathrm{d}\sigma}, \quad \bar{y} = \frac{M_x}{M} = \frac{\iint_D y\,\rho(x, y)\,\mathrm{d}\sigma}{\iint_D \rho(x, y)\,\mathrm{d}\sigma}$$
>
>若薄板质地均匀，面密度 $\rho(x, y) = \text{常数}$，则质心即为几何形心：
>
>$$\bar{x} = \frac{1}{S_D} \iint_D x\,\mathrm{d}\sigma, \quad \bar{y} = \frac{1}{S_D} \iint_D y\,\mathrm{d}\sigma$$

[3]转动惯量公式：
>(1) 薄板对 $x$ 轴的转动惯量：$I_x = \iint_D y^2 \rho(x, y)\,\mathrm{d}\sigma$
>
>(2) 薄板对 $y$ 轴的转动惯量：$I_y = \iint_D x^2 \rho(x, y)\,\mathrm{d}\sigma$
>
>(3) 薄板对原点（垂直轴）的极转动惯量：
>
>$$I_0 = I_x + I_y = \iint_D (x^2 + y^2) \rho(x, y)\,\mathrm{d}\sigma$$

###### **定理[1]:古鲁金第二定理（Pappus-Guldinus 定理）**

[1]定理表述：
>设平面连通闭区域 $D$ 位于某定直线 $L$ 的一侧（即直线 $L$ 不穿过区域 $D$ 的内部）。
>
>当闭区域 $D$ 绕直线 $L$ 旋转一周所形成的旋转体体积记为 $V$，则体积严格等于区域的面积 $S_D$ 与该区域形心绕旋转轴运动一周所扫过的圆周长度的乘积：
>
>$$V = 2\pi d \cdot S_D$$
>
>其中 $d = \mathrm{dist}((\bar{x}, \bar{y}), L)$ 是区域 $D$ 的几何形心到旋转轴 $L$ 的垂直欧氏距离。

[2]倾斜任意轴的体积解析计算公式：
>设直线方程为一般式 $L: Ax + By + C = 0$。区域内任意点 $(x, y)$ 到直线的垂直距离为：
>
>$$d(x, y) = \frac{|Ax + By + C|}{\sqrt{A^2 + B^2}}$$
>
>若 $L$ 不穿过区域内部（即 $Ax+By+C$ 在 $D$ 上恒不变号），则绕轴 $L$ 旋转体的体积可由二重积分直接积分给出：
>
>$$V = 2\pi \iint_D d(x, y)\,\mathrm{d}\sigma = \frac{2\pi}{\sqrt{A^2 + B^2}} \left| \iint_D (Ax + By + C)\,\mathrm{d}\sigma \right|$$

[3]古鲁金定理的逆用秒杀法（反求形心坐标）：
>利用柱壳法或截面法求出绕 $x$ 轴与 $y$ 轴的旋转体体积 $V_x$ 与 $V_y$，由古鲁金定理可直接反解形心坐标：
>
>$$\bar{y} = \frac{V_x}{2\pi S_D}, \quad \bar{x} = \frac{V_y}{2\pi S_D}$$
>
>免去了计算高难度二重积分静态矩 $M_x = \iint_D y\,\mathrm{d}\sigma$ 的积分运算。
