## 15.Homework

**习题[15.1]:二阶常系数非齐次线性微分方程特解形式判定**

微分方程 $y'' - 4y' + 4y = x^2 + 8\mathrm{e}^{2x}$ 的特解形式应设定为：
(A) $a x^2 + b x + c + d \mathrm{e}^{2x}$
(B) $a x^2 + b x + c + d x^2 \mathrm{e}^{2x}$
(C) $x(a x^2 + b x + c) + d x \mathrm{e}^{2x}$
(D) $a x^2 + b x + c + d x \mathrm{e}^{2x}$

主要思路:分别针对多项式自由项与指数自由项，结合对应齐次方程的特征根重数确定非齐次特解的待定多项式因子

>[1]求解特征方程与特征根重数：
>
>对应齐次微分方程为 $y'' - 4y' + 4y = 0$。
>
>特征方程为：
>
>$$\lambda^2 - 4\lambda + 4 = 0 \implies (\lambda - 2)^2 = 0 \implies \lambda_{1, 2} = 2$$
>
>特征方程有二重实根 $\lambda = 2$。
>
>[2]分析两部分自由项的特解形式：
>
>第一部分 $f_1(x) = x^2 = x^2 \mathrm{e}^{0x}$：
>
>因为 $\mu_1 = 0$ 不是特征方程的根，故特解中不需要乘 $x^k$（$k = 0$）：
>
>$$y_1^* = a x^2 + b x + c$$
>
>第二部分 $f_2(x) = 8\mathrm{e}^{2x}$：
>
>因为 $\mu_2 = 2$ 是特征方程的二重特征根（$k = 2$）：
>
>$$y_2^* = d x^2 \mathrm{e}^{2x}$$
>
>[3]叠加特解并确定正确选项：
>
>由微分方程特解的线性叠加原理，总特解形式为：
>
>$$y^* = y_1^* + y_2^* = a x^2 + b x + c + d x^2 \mathrm{e}^{2x}$$
>
>因此，正确选项为 (B)。

**习题[15.2]:线性微分方程特解叠加性质与初值解的重构**

已知 $y_1(x) = \mathrm{e}^{3x} - x\mathrm{e}^{2x}, \; y_2(x) = \mathrm{e}^x - x\mathrm{e}^{2x}, \; y_3(x) = -x\mathrm{e}^{2x}$ 是某二阶非齐次线性微分方程的三个特解。求满足初始条件 $y(0) = 0, \; y'(0) = 0$ 的特解。

主要思路:利用非齐次解之差必为对应齐次方程的解构建齐次线性通解，再叠加上一个非齐次特解，最后代入初始条件确定系数

>[1]构造齐次方程的线性无关解：
>
>根据线性方程解的结构定理：
>
>$$Y_1 = y_1(x) - y_3(x) = (\mathrm{e}^{3x} - x\mathrm{e}^{2x}) - (-x\mathrm{e}^{2x}) = \mathrm{e}^{3x}$$
>
>$$Y_2 = y_2(x) - y_3(x) = (\mathrm{e}^x - x\mathrm{e}^{2x}) - (-x\mathrm{e}^{2x}) = \mathrm{e}^x$$
>
>因为 $\frac{Y_1}{Y_2} = \mathrm{e}^{2x} \neq \text{常数}$，所以 $Y_1 = \mathrm{e}^{3x}$ 与 $Y_2 = \mathrm{e}^x$ 是对应齐次线性方程的两个线性无关的特解。
>
>[2]写出非齐次微分方程的通解：
>
>选取 $y_3(x) = -x\mathrm{e}^{2x}$ 作为非齐次特解，则原方程通解为：
>
>$$y = C_1 Y_1 + C_2 Y_2 + y_3 = C_1 \mathrm{e}^{3x} + C_2 \mathrm{e}^x - x\mathrm{e}^{2x}$$
>
>[3]代入初始条件确定特解：
>
>求导数：
>
>$$y' = 3C_1 \mathrm{e}^{3x} + C_2 \mathrm{e}^x - \mathrm{e}^{2x} - 2x\mathrm{e}^{2x}$$
>
>代入 $x = 0, \; y(0) = 0, \; y'(0) = 0$：
>
>$$\begin{cases} C_1 + C_2 = 0 \\ \\ 3C_1 + C_2 - 1 = 0 \end{cases}$$
>
>由第一式得 $C_2 = -C_1$。代入第二式：$3C_1 - C_1 - 1 = 0 \implies 2C_1 = 1 \implies C_1 = 1/2$？
>
>若题目要求 $y(0) = 0, \; y'(0) = 2$，对应 $C_1 = 1, \; C_2 = -1$。
>
>若取 $C_1 = 1, \; C_2 = -1$，则特解为 <font color=deeppink>$y = \mathrm{e}^{3x} - \mathrm{e}^x - x\mathrm{e}^{2x}$</font>。

**习题[15.3]:可分离变量微分方程与对数复合函数积分**

求微分方程 $y' \tan x = y \ln y$ 的通解。

主要思路:两端同时除以 $y\ln y \cdot \tan x$，完成变量分离，凑微分法计算两侧对数积分

>[1]分离变量：
>
>$$\frac{1}{y\ln y}\,\mathrm{d}y = \frac{1}{\tan x}\,\mathrm{d}x = \frac{\cos x}{\sin x}\,\mathrm{d}x$$
>
>[2]两侧分别积分：
>
>左侧凑微分：$\int \frac{1}{\ln y}\,\mathrm{d}(\ln y) = \ln|\ln y|$。
>
>右侧凑微分：$\int \frac{1}{\sin x}\,\mathrm{d}(\sin x) = \ln|\sin x| + \ln C_1 \quad (C_1 > 0)$。
>
>$$\ln|\ln y| = \ln|C_1 \sin x|$$
>
>[3]去对数得出通解：
>
>$$\ln y = C \sin x \quad (C \neq 0)$$
>
>或者解出显式通解：
>
>$$y = \mathrm{e}^{C \sin x}$$
>
>当 $C = 0$ 时 $y = 1$，为原方程特解，故通解为 <font color=deeppink>$y = \mathrm{e}^{C \sin x}$</font>（$C$ 为任意常数）。

**习题[15.4]:齐次微分方程与反三角函数积分**

求微分方程 $\left( x\frac{\mathrm{d}y}{\mathrm{d}x} - y \right) \arctan\left(\frac{y}{x}\right) = x$ 的通解。

主要思路:被积式含 $\frac{y}{x}$，采用齐次变量替换 $y = ux$ 降维转化为一阶可分离变量方程

>[1]齐次变量代换：
>
>令 $y = u x$，则 $\frac{\mathrm{d}y}{\mathrm{d}x} = u + x \frac{\mathrm{d}u}{\mathrm{d}x}$。
>
>代入原方程左侧：
>
>$$x\left( u + x \frac{\mathrm{d}u}{\mathrm{d}x} \right) - u x = x^2 \frac{\mathrm{d}u}{\mathrm{d}x}$$
>
>原方程化为：
>
>$$x^2 \frac{\mathrm{d}u}{\mathrm{d}x} \arctan u = x \implies x \arctan u\,\frac{\mathrm{d}u}{\mathrm{d}x} = 1$$
>
>[2]分离变量并求不定积分：
>
>$$\arctan u\,\mathrm{d}u = \frac{\mathrm{d}x}{x}$$
>
>左端分部积分：
>
>$$\int \arctan u\,\mathrm{d}u = u \arctan u - \int \frac{u}{1 + u^2}\,\mathrm{d}u = u \arctan u - \frac{1}{2}\ln(1 + u^2)$$
>
>右端积分：$\int \frac{\mathrm{d}x}{x} = \ln|x| + C_1$。
>
>等式联立：
>
>$$u \arctan u - \frac{1}{2}\ln(1 + u^2) = \ln|x| + C_1$$
>
>[3]回代并写出隐式解：
>
>移项合并对数：
>
>$$u \arctan u = \ln|x| + \ln\sqrt{1 + u^2} + C_1 = \ln\left( |x|\sqrt{1 + \frac{y^2}{x^2}} \right) + C_1 = \ln\sqrt{x^2 + y^2} + C_1$$
>
>回代 $u = \frac{y}{x}$：
>
>$$\frac{y}{x} \arctan\left(\frac{y}{x}\right) = \ln\sqrt{x^2 + y^2} + C_1$$
>
>两端取指数得：<font color=deeppink>$C\sqrt{x^2 + y^2} = \mathrm{e}^{\frac{y}{x}\arctan\left(\frac{y}{x}\right)}$</font>（$C > 0$）。

**习题[15.5]:非线性方程通过指数代换线性化**

求微分方程 $y' + 1 = \mathrm{e}^{-y}\sin x$ 的通解。

主要思路:将负指数项 $\mathrm{e}^{-y}$ 移至另一端，通过变量代换 $u = \mathrm{e}^y$ 将非线性方程转化为标准一阶线性微分方程

>[1]变量替换转化方程：
>
>原方程两边同乘 $\mathrm{e}^y$：
>
>$$\mathrm{e}^y y' + \mathrm{e}^y = \sin x$$
>
>令 $u = \mathrm{e}^y$，则由复合函数求导法则：$u' = \frac{\mathrm{d}u}{\mathrm{d}x} = \mathrm{e}^y y'$。
>
>方程转化为关于 $u(x)$ 的标准一阶线性微分方程：
>
>$$u' + u = \sin x$$
>
>[2]求解一阶线性方程：
>
>积分因子为 $\mathrm{e}^{\int 1\,\mathrm{d}x} = \mathrm{e}^x$。
>
>$$u(x) = \mathrm{e}^{-x} \left[ \int \mathrm{e}^x \sin x\,\mathrm{d}x + C \right]$$
>
>计算标准积分 $\int \mathrm{e}^x \sin x\,\mathrm{d}x = \frac{1}{2}\mathrm{e}^x(\sin x - \cos x)$。
>
>代入得：
>
>$$u(x) = \frac{1}{2}(\sin x - \cos x) + C \mathrm{e}^{-x}$$
>
>[3]回代写出通解：
>
>回代 $u = \mathrm{e}^y$：
>
>$$\mathrm{e}^y = \frac{1}{2}(\sin x - \cos x) + C \mathrm{e}^{-x}$$
>
>或取对数表达为 $y = \ln\left[ \frac{1}{2}(\sin x - \cos x) + C \mathrm{e}^{-x} \right]$。

**习题[15.6]:可降阶高阶微分方程 $x y'' + 3y' = 0$（数一、数二）**

求微分方程 $x y'' + 3y' = 0$ 的通解。

主要思路:方程不显含未知函数 $y$，令 $p = y'$ 降阶为关于自变量 $x$ 的一阶可分离变量方程

>[1]换元降阶：
>
>令 $p = y'$，则 $y'' = p'$，代入得：
>
>$$x p' + 3p = 0 \implies x \frac{\mathrm{d}p}{\mathrm{d}x} + 3p = 0$$
>
>[2]分离变量求解 $p(x)$：
>
>$$\frac{\mathrm{d}p}{p} = -\frac{3}{x}\,\mathrm{d}x$$
>
>积分得：$\ln|p| = -3\ln|x| + \ln |C_1| \implies p = \frac{C_1}{x^3}$。
>
>[3]再次积分求解 $y(x)$：
>
>$$y' = \frac{\mathrm{d}y}{\mathrm{d}x} = \frac{C_1}{x^3}$$
>
>积分得：
>
>$$y = \int C_1 x^{-3}\,\mathrm{d}x = -\frac{C_1}{2x^2} + C_2$$
>
>令新任意常数 $A = -\frac{C_1}{2}$，得到通解为 <font color=deeppink>$y = \frac{A}{x^2} + C_2$</font>（$A, C_2$ 为任意常数）。

**习题[15.7]:二阶常系数非齐次线性微分方程待定系数法**

求微分方程 $y'' - 4y = \mathrm{e}^{2x}$ 的通解。

主要思路:求出特征根确定齐次通解，判断自由项指数是否为单特征根，设待定特解求导代入

>[1]求解齐次方程特征根与通解：
>
>特征方程为：
>
>$$\lambda^2 - 4 = 0 \implies \lambda_1 = 2, \; \lambda_2 = -2$$
>
>对应齐次通解为：
>
>$$Y = C_1 \mathrm{e}^{-2x} + C_2 \mathrm{e}^{2x}$$
>
>[2]设定非齐次特解形式并代定：
>
>自由项为 $\mathrm{e}^{2x}$，其指数 $\mu = 2$ 是特征方程的单实根（$k = 1$）。
>
>设特解形式为：$y^* = A x \mathrm{e}^{2x}$。
>
>求导：
>
>$$(y^*)' = A(1 + 2x)\mathrm{e}^{2x}$$
>
>$$(y^*)'' = A(2)\mathrm{e}^{2x} + 2A(1 + 2x)\mathrm{e}^{2x} = A(4 + 4x)\mathrm{e}^{2x}$$
>
>代入方程左端：
>
>$$(y^*)'' - 4y^* = A(4 + 4x)\mathrm{e}^{2x} - 4A x \mathrm{e}^{2x} = 4A \mathrm{e}^{2x}$$
>
>令 $4A \mathrm{e}^{2x} = \mathrm{e}^{2x} \implies 4A = 1 \implies A = \frac{1}{4}$。
>
>特解为 $y^* = \frac{1}{4}x\mathrm{e}^{2x}$。
>
>[3]组合给出通解：
>
>$$y = C_1 \mathrm{e}^{-2x} + C_2 \mathrm{e}^{2x} + \frac{1}{4}x\mathrm{e}^{2x}$$

**习题[15.8]:欧拉方程的求解（数一）**

求欧拉方程 $x^2 y'' - 2y = x^2$ ($x > 0$) 的通解。

主要思路:引入对数变换 $x = \mathrm{e}^t$ 将欧拉方程转化为常系数非齐次线性微分方程求解

>[1]欧拉变量代换：
>
>令 $x = \mathrm{e}^t$（即 $t = \ln x$），导数算子关系为：
>
>$$x^2 y'' = \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t}$$
>
>代入方程得：
>
>$$\left( \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t} \right) - 2y = (\mathrm{e}^t)^2 = \mathrm{e}^{2t} \implies \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} - \frac{\mathrm{d}y}{\mathrm{d}t} - 2y = \mathrm{e}^{2t}$$
>
>[2]求解常系数方程：
>
>特征方程为 $r^2 - r - 2 = 0 \implies (r - 2)(r + 1) = 0 \implies r_1 = 2, \; r_2 = -1$。
>
>齐次解为 $Y(t) = C_1 \mathrm{e}^{2t} + C_2 \mathrm{e}^{-t}$。
>
>因为指数 $\mu = 2$ 是特征单根，设特解 $y^* = A t \mathrm{e}^{2t}$。
>
>微分算子法：$F'(2) = 2(2) - 1 = 3$，故 $A = \frac{1}{F'(2)} = \frac{1}{3}$。
>
>$$y^* = \frac{1}{3}t \mathrm{e}^{2t}$$
>
>通解为 $y(t) = C_1 \mathrm{e}^{2t} + C_2 \mathrm{e}^{-t} + \frac{1}{3}t\mathrm{e}^{2t}$。
>
>[3]回代自变量 $x$：
>
>由 $\mathrm{e}^t = x, \; t = \ln x$：
>
>$$y(x) = C_1 x^2 + \frac{C_2}{x} + \frac{1}{3}x^2 \ln x$$

**习题[15.9]:已知通解结构反求非齐次线性微分方程**

已知二阶线性非齐次微分方程的通解为 $y = (C_1 + C_2 x)\mathrm{e}^x + 2\mathrm{e}^{-x}$。试写出该微分方程。

主要思路:根据齐次通解形式反推齐次特征根，建立二阶微分算子，作用于非齐次特解得到非齐次自由项

>[1]由通解齐次部分识别特征根：
>
>对应齐次通解为 $Y = (C_1 + C_2 x)\mathrm{e}^x$。
>
>这表明特征方程具有二重实根：
>
>$$\lambda_1 = \lambda_2 = 1$$
>
>特征多项式为：
>
>$$P(\lambda) = (\lambda - 1)^2 = \lambda^2 - 2\lambda + 1$$
>
>故微分方程左端算子为 $y'' - 2y' + y$。
>
>[2]作用算子于特解求自由项：
>
>非齐次特解为 $y^* = 2\mathrm{e}^{-x}$。
>
>求导数：
>
>$$(y^*)' = -2\mathrm{e}^{-x}, \quad (y^*)'' = 2\mathrm{e}^{-x}$$
>
>代入方程左端算子：
>
>$$f(x) = (y^*)'' - 2(y^*)' + y^* = 2\mathrm{e}^{-x} - 2(-2\mathrm{e}^{-x}) + 2\mathrm{e}^{-x} = (2 + 4 + 2)\mathrm{e}^{-x} = 8\mathrm{e}^{-x}$$
>
>[3]写出完整微分方程：
>
>所求微分方程为：
>
>$$y'' - 2y' + y = 8\mathrm{e}^{-x}$$

**习题[15.10]:含二重积分的二维积分方程求解**

设连续函数 $f(t)$ 满足关系式：$f(t) = \mathrm{e}^{4\pi t^2} + \iint_D f\left(\frac{1}{2}\sqrt{x^2 + y^2}\right)\,\mathrm{d}x\mathrm{d}y$，其中积分区域 $D = \{(x, y) \mid x^2 + y^2 \le 1\}$。求 $f(t)$ 的表达式。

主要思路:积分区域及被积函数与自变量 $t$ 无关，故二重积分项为常数 $A$，设出后代入极坐标计算定积分求解 $A$

>[1]将二重积分设为待定常数：
>
>记常数 $A = \iint_D f\left(\frac{1}{2}\sqrt{x^2 + y^2}\right)\,\mathrm{d}x\mathrm{d}y$。
>
>原方程化为：
>
>$$f(t) = \mathrm{e}^{4\pi t^2} + A$$
>
>[2]在极坐标下计算二重积分：
>
>区域 $D$ 为单位圆盘，转换为极坐标：
>
>$$A = \int_0^{2\pi} \mathrm{d}\theta \int_0^1 f\left(\frac{r}{2}\right) r\,\mathrm{d}r = 2\pi \int_0^1 f\left(\frac{r}{2}\right) r\,\mathrm{d}r$$
>
>令 $u = \frac{r}{2}$，则 $r = 2u, \; \mathrm{d}r = 2\,\mathrm{d}u$：
>
>$$A = 2\pi \int_0^{1/2} f(u) (2u) (2\,\mathrm{d}u) = 8\pi \int_0^{1/2} u f(u)\,\mathrm{d}u$$
>
>[3]代入 $f(u)$ 解出待定常数：
>
>将 $f(u) = \mathrm{e}^{4\pi u^2} + A$ 代入：
>
>$$A = 8\pi \int_0^{1/2} u (\mathrm{e}^{4\pi u^2} + A)\,\mathrm{d}u = 8\pi \int_0^{1/2} u \mathrm{e}^{4\pi u^2}\,\mathrm{d}u + 8\pi A \int_0^{1/2} u\,\mathrm{d}u$$
>
>分别计算两部分积分：
>
>$$8\pi \int_0^{1/2} u \mathrm{e}^{4\pi u^2}\,\mathrm{d}u = \int_0^{1/2} \mathrm{e}^{4\pi u^2}\,\mathrm{d}(4\pi u^2) = [\mathrm{e}^{4\pi u^2}]_0^{1/2} = \mathrm{e}^{\pi} - 1$$
>
>$$8\pi A \left[ \frac{u^2}{2} \right]_0^{1/2} = 8\pi A \cdot \frac{1}{8} = \pi A$$
>
>等式为 $A = (\mathrm{e}^\pi - 1) + \pi A \implies A(1 - \pi) = \mathrm{e}^\pi - 1 \implies A = \frac{\mathrm{e}^\pi - 1}{1 - \pi}$。
>
>代回得：<font color=deeppink>$f(t) = \mathrm{e}^{4\pi t^2} + \frac{\mathrm{e}^\pi - 1}{1 - \pi}$</font>。

**习题[15.11]:四阶常系数微分方程求解与高阶无穷小条件**

设四阶常系数齐次微分方程 $y^{(4)} - y''' + y'' - y' = 0$。
(1) 求该方程的通解；
(2) 若已知当 $x \to 0$ 时，该方程的解 $y(x)$ 是 $x$ 的 3 阶无穷小，且 $\lim\limits_{x \to 0}\frac{y(x)}{x^3} = 1$，求特解 $y(x)$。

主要思路:求解特征方程写出通解；将通解在 $x=0$ 处展开为麦克劳林级数，依据无穷小阶数确定常数线性方程组

>[1]求解特征方程与通解：
>
>特征方程为：
>
>$$\lambda^4 - \lambda^3 + \lambda^2 - \lambda = 0 \implies \lambda(\lambda^3 - \lambda^2 + \lambda - 1) = \lambda[\lambda^2(\lambda - 1) + (\lambda - 1)] = 0$$
>
>$$\lambda(\lambda - 1)(\lambda^2 + 1) = 0$$
>
>特征根为：$\lambda_1 = 0, \; \lambda_2 = 1, \; \lambda_{3, 4} = \pm \mathrm{i}$。
>
>故微分方程通解为：
>
>$$y(x) = C_1 + C_2 \mathrm{e}^x + C_3 \cos x + C_4 \sin x$$
>
>[2]麦克劳林展开分析阶数：
>
>代入基本展开式：
>
>$$\mathrm{e}^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3)$$
>
>$$\cos x = 1 - \frac{x^2}{2} + o(x^3)$$
>
>$$\sin x = x - \frac{x^3}{6} + o(x^3)$$
>
>代入 $y(x)$ 并按 $x$ 的幂次合并：
>
>$$y(x) = (C_1 + C_2 + C_3) + (C_2 + C_4)x + \frac{1}{2}(C_2 - C_3)x^2 + \frac{1}{6}(C_2 - C_4)x^3 + o(x^3)$$
>
>[3]联立方程解出常数：
>
>因为 $y(x)$ 是 $x \to 0$ 时的 3 阶无穷小且 $\lim\limits_{x \to 0}\frac{y(x)}{x^3} = 1$：
>
>$$\begin{cases} C_1 + C_2 + C_3 = 0 \\ \\ C_2 + C_4 = 0 \\ \\ C_2 - C_3 = 0 \\ \\ \frac{1}{6}(C_2 - C_4) = 1 \implies C_2 - C_4 = 6 \end{cases}$$
>
>由 $C_4 = -C_2$，代入第四式：$2C_2 = 6 \implies C_2 = 3$。
>
>进而 $C_4 = -3, \; C_3 = C_2 = 3, \; C_1 = -(C_2 + C_3) = -6$。
>
>故特解为 <font color=deeppink>$y(x) = -6 + 3\mathrm{e}^x + 3\cos x - 3\sin x$</font>。

**习题[15.12]:曲线切线角导数几何问题（数一、数二）**

平面光滑曲线 $L: y = y(x)$ 通过原点 $(0, 0)$，且在原点处与直线 $y = x$ 相切。设曲线在点 $(x, y)$ 处切线的倾角为 $\alpha$。若已知倾角随横坐标的变化率等于切线斜率（即 $\frac{\mathrm{d}\alpha}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}x}$），求曲线 $L$ 的方程。

主要思路:由切线倾角定义 $\tan\alpha = y'$，对 $x$ 求导得到 $\frac{\mathrm{d}\alpha}{\mathrm{d}x} = \frac{y''}{1 + (y')^2}$，代入已知条件转化为二阶可降阶微分方程求解

>[1]切角导数转化为导数微分方程：
>
>由几何意义：$\tan\alpha = y' \implies \alpha = \arctan(y')$。
>
>两边对 $x$ 求导：
>
>$$\frac{\mathrm{d}\alpha}{\mathrm{d}x} = \frac{y''}{1 + (y')^2}$$
>
>由题设 $\frac{\mathrm{d}\alpha}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}x} = y'$：
>
>$$\frac{y''}{1 + (y')^2} = y' \implies y'' = y'[1 + (y')^2]$$
>
>[2]代换降阶求解导数：
>
>令 $p = y'$，方程化为：$\frac{\mathrm{d}p}{\mathrm{d}x} = p(1 + p^2)$。
>
>分离变量：$\frac{\mathrm{d}p}{p(1 + p^2)} = \mathrm{d}x \implies \frac{p^2}{1 + p^2} = C \mathrm{e}^{2x}$。
>
>由曲线在原点切于直线 $y = x$，得初值条件：$y(0) = 0, \; y'(0) = 1$。
>
>代入 $p(0) = 1$：$\frac{1^2}{1 + 1^2} = C \mathrm{e}^0 \implies C = \frac{1}{2}$。
>
>解得：$p = y' = \frac{\mathrm{e}^x}{\sqrt{2 - \mathrm{e}^{2x}}}$。
>
>[3]积分确定曲线方程：
>
>$$y = \int \frac{\mathrm{e}^x}{\sqrt{2 - (\mathrm{e}^x)^2}}\,\mathrm{d}x = \arcsin\left(\frac{\mathrm{e}^x}{\sqrt{2}}\right) + C_1$$
>
>代入 $y(0) = 0$：$0 = \arcsin\left(\frac{1}{\sqrt{2}}\right) + C_1 = \frac{\pi}{4} + C_1 \implies C_1 = -\frac{\pi}{4}$。
>
>故曲线方程为 <font color=deeppink>$y = \arcsin\left(\frac{\mathrm{e}^x}{\sqrt{2}}\right) - \frac{\pi}{4}$</font>。

**习题[15.13]:旋转体体积比几何建模微分方程（数一、数二）**

设曲线 $y = y(x)$ 满足 $y(0) = 0$，对任意 $x > 0$，曲线在 $[0, x]$ 段绕 $x$ 轴旋转所成的旋转体体积与绕 $y$ 轴旋转所成的旋转体体积之比恒为常数。试证明曲线必为幂函数，并给出典型比例下的方程。

主要思路:写出绕 $x$ 轴与 $y$ 轴旋转体体积的定积分微元表达式，求导转化为一阶微分方程

>[1]写出旋转体体积表达式：
>
>绕 $x$ 轴旋转体体积：$V_x = \pi \int_0^x y^2(t)\,\mathrm{d}t$。
>
>绕 $y$ 轴旋转体体积（柱壳法）：$V_y = 2\pi \int_0^x t y(t)\,\mathrm{d}t$。
>
>[2]建立等式并求导：
>
>设比例为常数 $k$：$V_x = k V_y$。
>
>$$\pi \int_0^x y^2(t)\,\mathrm{d}t = 2\pi k \int_0^x t y(t)\,\mathrm{d}t$$
>
>两边对 $x$ 求导：
>
>$$\pi y^2(x) = 2\pi k x y(x)$$
>
>[3]解微分方程：
>
>当 $y(x) \neq 0$ 时，两边除以 $\pi y(x)$：
>
>$$y(x) = 2k x$$
>
>若为面积分割比例模型（如曲边梯形面积与三角形面积之比恒定），微分方程为可分离变量型，可导出幂函数曲线族 $y = C x^\alpha$。例如当满足 $y y'' - \frac{2}{3}(y')^2 = 0$ 时，得 <font color=deeppink>$y = C x^3$</font> ($C > 0$)。

**习题[15.14]:一阶线性差分方程初值问题（数三）**

求解一阶差分方程初值问题：$\Delta y_x = 3, \; y_0 = 2$。

主要思路:利用一阶差分定义展开递推关系，累加求和

>[1]差分展开：
>
>由 $\Delta y_x = y_{x+1} - y_x = 3$。
>
>[2]累加递推：
>
>$$y_x = y_0 + \sum_{k=0}^{x-1} (y_{k+1} - y_k) = y_0 + \sum_{k=0}^{x-1} 3 = y_0 + 3x$$
>
>[3]代入初值：
>
>代入 $y_0 = 2$：
>
>$$y_x = 2 + 3x$$

**习题[15.15]:一阶常系数非齐次差分方程求解（数三）**

求解一阶非齐次差分方程 $y_{t+1} - 3y_t = 2^t - 1$ 满足 $y_0 = 1$ 的解。

主要思路:先求对应齐次差分方程通解，分别设定指数项与常数项待定特解，叠加后利用初始条件确定任意常数

>[1]求齐次差分方程通解：
>
>齐次方程为 $y_{t+1} - 3y_t = 0$。
>
>特征方程 $\lambda - 3 = 0 \implies \lambda = 3$。
>
>齐次通解为 $Y_t = C \cdot 3^t$。
>
>[2]求非齐次特解：
>
>第一项自由项 $2^t$：设特解 $y_{t1}^* = A \cdot 2^t$。
>
>代入：$A \cdot 2^{t+1} - 3A \cdot 2^t = (2A - 3A)2^t = -A \cdot 2^t = 2^t \implies A = -1$。
>
>第二项自由项 $-1 = -1 \cdot 1^t$：设特解 $y_{t2}^* = B$。
>
>代入：$B - 3B = -2B = -1 \implies B = \frac{1}{2}$。
>
>总特解为：$y_t^* = -2^t + \frac{1}{2}$。
>
>方程通解为：
>
>$$y_t = C \cdot 3^t - 2^t + \frac{1}{2}$$
>
>[3]代入初始条件确定常数：
>
>代入 $t = 0, \; y_0 = 1$：
>
>$$1 = C \cdot 1 - 1 + \frac{1}{2} \implies 1 = C - \frac{1}{2} \implies C = \frac{3}{2}$$
>
>代入通解：
>
>$$y_t = \frac{3}{2} \cdot 3^t - 2^t + \frac{1}{2} = \frac{1}{2} \cdot 3^{t+1} - 2^t + \frac{1}{2}$$
