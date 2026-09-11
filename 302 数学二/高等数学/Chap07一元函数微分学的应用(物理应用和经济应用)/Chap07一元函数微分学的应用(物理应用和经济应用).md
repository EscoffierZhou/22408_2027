# chap7一元函数微分学的应用(物理应用和经济应用)

目的[1]:掌握导数的物理本质——变化率模型与相关变化率(数一/数二高频考点)

目的[2]:掌握质点直线运动中的位移、速度、加速度与高阶导数链式微分关系

目的[3]:掌握平面曲线运动中的速度分解、法向/切向加速度与曲率动力学模型

目的[4]:熟练建立物理量之间的几何/代数约束方程，并结合隐函数求导法与链式法则求解变化率

目的[5]:掌握导数在经济学中的边际分析(边际成本、边际收益、边际利润及利润最大化准则)

目的[6]:掌握需求价格弹性公式、弹性与收益的关系，熟练运用导数分析经济决策

## 1.导数的物理本质:变化率与相关变化率

###### **原理[1]:变化率的物理定义**

若物理量$y$依赖于时间参数$t$，则$y$对$t$的导数即为$y$随时间$t$变化的**瞬时变化率**：

$$\frac{\mathrm{d}y}{\mathrm{d}t} = \lim_{\Delta t \to 0} \frac{\Delta y}{\Delta t}$$

(1) 若$\frac{\mathrm{d}y}{\mathrm{d}t} > 0$，表示物理量随时间增加(如膨胀、上升、升温、加速)；

(2) 若$\frac{\mathrm{d}y}{\mathrm{d}t} < 0$，表示物理量随时间减少(如收缩、下降、降温、减速)。

###### **原理[2]:相关变化率模型与标准SOP流程**

设两个或多个物理量$x, y, \theta$都是时间$t$的可导函数，它们之间通过某种几何约束关系或物理规律满足关联方程：

$$F(x, y, \dots) = 0$$

若已知其中某些量的变化率(如$\frac{\mathrm{d}x}{\mathrm{d}t}$)，求另一物理量对时间的变化率$\frac{\mathrm{d}y}{\mathrm{d}t}$。

>[相关变化率标准解题SOP(步控流程)]
>
>操作[1]:选元定标：设出所有随时间变化的变量(记为$x(t), y(t), \theta(t)$等)。
>
>注意:变化过程中的动量严禁在求导前代入固定数值！
>
>操作[2]:几何/物理建模：利用勾股定理、相似三角形、三角函数定义或体积公式建立几何约束方程$F(x, y) = 0$。
>
>操作[3]:对时间$t$全求导：方程两边关于时间$t$求导(视各变量为$t$的复合函数，严格应用链式法则)。
>
>操作[4]:代入特定瞬时值：仅在求导完成后，将题设中“特定瞬间”的几何位置参数和已知变化率代入，解出目标变化率。

## 2.质点直线运动与微分关系

###### **原理[1]:质点直线运动中的高阶导数链**

设质点沿直线运动的位置坐标随时间的变化规律为位移函数$s = s(t)$：

(1) **瞬时速度(一阶导数):** $v(t) = \frac{\mathrm{d}s}{\mathrm{d}t} = s'(t)$

(2) **瞬时加速度(二阶导数):** $a(t) = \frac{\mathrm{d}v}{\mathrm{d}t} = \frac{\mathrm{d}^2s}{\mathrm{d}t^2} = s''(t)$

(3) **加加速度/变加速度(三阶导数Jerk):** $j(t) = \frac{\mathrm{d}a}{\mathrm{d}t} = \frac{\mathrm{d}^3s}{\mathrm{d}t^3} = s'''(t)$

###### **原理[2]:以位移为自变量的链式法则变换**

在动力学问题中，加速度或外力常由位置决定(如弹簧弹力、万有引力$a = a(s)$)。此时时间参数$t$被消去，利用复合求导链式法则进行转化：

$$a = \frac{\mathrm{d}v}{\mathrm{d}t} = \frac{\mathrm{d}v}{\mathrm{d}s} \cdot \frac{\mathrm{d}s}{\mathrm{d}t} = v \frac{\mathrm{d}v}{\mathrm{d}s} = \frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{1}{2}v^2\right)$$

>本质作用:此关系是建立牛顿第二定律微分方程的桥梁：$F = ma \implies F(s) = mv \frac{\mathrm{d}v}{\mathrm{d}s}$，分离变量即可直接积分求解速度与位移的关系。

## 3.平面曲线运动与切向/法向加速度(结合曲率)

###### **原理[1]:切向加速度与法向加速度的正交分解**

当质点沿平面曲线$y = f(x)$运动，弧长参数为$s$，瞬时速率为$v = \frac{\mathrm{d}s}{\mathrm{d}t}$时，其加速度向量$\vec{a}$可正交分解为切向分量$\vec{a}_\tau$与法向分量$\vec{a}_n$：

$$\vec{a} = a_\tau \vec{\tau} + a_n \vec{n}$$

(1) **切向加速度$a_\tau$:** 反映**速率大小改变的快慢**：

$$a_\tau = \frac{\mathrm{d}v}{\mathrm{d}t} = \frac{\mathrm{d}^2s}{\mathrm{d}t^2}$$

(2) **法向加速度$a_n$:** 反映**运动速度方向改变的快慢**，与轨迹在当前点的曲率$K$及曲率半径$R$直接绑定：

$$a_n = \frac{v^2}{R} = K v^2$$

(3) **全加速度大小:** 

$$a = \vert{}\vec{a}\vert{} = \sqrt{a_\tau^2 + a_n^2} = \sqrt{\left(\frac{\mathrm{d}v}{\mathrm{d}t}\right)^2 + (K v^2)^2}$$

###### **原理[2]:平面直角坐标下的曲率计算**

若曲线方程为$y = f(x)$，在点$(x, y)$处的曲率$K$为：

$$K = \frac{\vert{}y''\vert{}}{[1 + (y')^2]^{\frac{3}{2}}}$$

曲率半径为$R = \frac{1}{K}$。

## 5.经典强化例题精解

**例题[1]:相关变化率(仰角与高度模型)**

观测站位于离火箭发射台水平距离为$3\text{ km}$的平地上。若火箭垂直向上发射，当火箭高度达到$4\text{ km}$时，其瞬时上升速度为$800\text{ km/h}$。求此时观测站仪器对火箭观测仰角的变化率。

主要思路:利用直角三角形建立正切函数几何约束方程$y = 3\tan\theta$，两端对时间$t$求导应用链式法则，代入特定瞬间的几何量解出仰角变化率

>[1]选元与几何建模：
>
>设在时刻$t$，火箭垂直高度为$y(t)$，观测站仪器的仰角为$\theta(t)$。
>
>由直角三角形三角函数关系：
>
>$$\tan\theta = \frac{y}{3} \implies y = 3\tan\theta$$
>
>[2]两端关于时间$t$求导：
>
>方程两端关于时间$t$求导(视$y$与$\theta$为$t$的复合函数)：
>
>$$\frac{\mathrm{d}y}{\mathrm{d}t} = 3\sec^2\theta \cdot \frac{\mathrm{d}\theta}{\mathrm{d}t}$$
>
>[3]确定特定瞬间的几何量：
>
>当火箭高度$y = 4\text{ km}$时：
>
>(1) 水平距离为$3\text{ km}$，斜边视线距离为$\sqrt{3^2 + 4^2} = 5\text{ km}$；
>
>(2) 此时$\cos\theta = \frac{3}{5} \implies \sec\theta = \frac{5}{3}$；
>
>(3) 瞬时上升速度已知：$\frac{\mathrm{d}y}{\mathrm{d}t} = 800\text{ km/h}$。
>
>[4]代入计算仰角变化率：
>
>$$800 = 3 \cdot \left(\frac{5}{3}\right)^2 \cdot \frac{\mathrm{d}\theta}{\mathrm{d}t} = \frac{25}{3} \cdot \frac{\mathrm{d}\theta}{\mathrm{d}t}$$
>
>解得：
>
>$$\frac{\mathrm{d}\theta}{\mathrm{d}t} = \frac{800 \times 3}{25} = 96\text{ rad/h}$$

**例题[2]:相关变化率(倒圆锥漏水模型)**

一倒置圆锥形水漏斗，其底面圆半径为$R = 6\text{ cm}$，高为$H = 12\text{ cm}$。水以$2\text{ cm}^3\text{/s}$的恒定速率从底部小孔漏出。当水深为$4\text{ cm}$时，求漏斗中水面下降的速率。

主要思路:利用相似三角形将半径$r$用高$h$表示以消元，建立单一变量体积公式$V(h)$，两边对$t$求导后代入瞬时水深求解

>[1]选元与几何相似消元：
>
>设在时刻$t$，水深为$h(t)$，对应水面半径为$r(t)$，水的体积为$V(t)$。
>
>由圆锥截面的相似三角形性质：
>
>$$\frac{r}{h} = \frac{R}{H} = \frac{6}{12} = \frac{1}{2} \implies r = \frac{1}{2}h$$
>
>[2]建立单变量体积函数：
>
>$$V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \left(\frac{1}{2}h\right)^2 h = \frac{1}{12}\pi h^3$$
>
>[3]两端对时间$t$求导：
>
>$$\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{1}{12}\pi \cdot 3h^2 \frac{\mathrm{d}h}{\mathrm{d}t} = \frac{1}{4}\pi h^2 \frac{\mathrm{d}h}{\mathrm{d}t}$$
>
>[4]代入已知瞬时值计算：
>
>漏水说明体积随时间减少，$\frac{\mathrm{d}V}{\mathrm{d}t} = -2\text{ cm}^3\text{/s}$，水深$h = 4\text{ cm}$：
>
>$$-2 = \frac{1}{4}\pi (4)^2 \frac{\mathrm{d}h}{\mathrm{d}t} = 4\pi \frac{\mathrm{d}h}{\mathrm{d}t} \implies \frac{\mathrm{d}h}{\mathrm{d}t} = -\frac{1}{2\pi}\text{ cm/s}$$
>
>故水面下降的速率为$\frac{1}{2\pi}\text{ cm/s}$。

**例题[3]:相关变化率(滑梯靠墙下滑模型)**

长为$5\text{ m}$的梯子靠在垂直的墙上。底端以$2\text{ m/s}$的匀速沿水平地面向远离墙面方向滑动。当底端离墙面$3\text{ m}$时，求顶端沿墙面下滑的速度，以及梯子与地面夹角$\theta$的变化率。

主要思路:建立勾股定理约束方程$x^2 + y^2 = 25$对时间求导求解顶端下滑速度；通过余弦定义$\cos\theta = \frac{x}{5}$对时间求导求解角速度

>[1]勾股定理建模与求导：
>
>设底端离墙距离为$x(t)$，顶端离地高度为$y(t)$。满足几何约束：
>
>$$x^2 + y^2 = 5^2 = 25$$
>
>两端对时间$t$求导：
>
>$$2x\frac{\mathrm{d}x}{\mathrm{d}t} + 2y\frac{\mathrm{d}y}{\mathrm{d}t} = 0 \implies x\frac{\mathrm{d}x}{\mathrm{d}t} + y\frac{\mathrm{d}y}{\mathrm{d}t} = 0$$
>
>[2]计算特定瞬时的顶端速度：
>
>当$x = 3\text{ m}$时，代入勾股方程得$y = \sqrt{25 - 3^2} = 4\text{ m}$。
>
>已知$\frac{\mathrm{d}x}{\mathrm{d}t} = 2\text{ m/s}$，代入得：
>
>$$3(2) + 4\frac{\mathrm{d}y}{\mathrm{d}t} = 0 \implies \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{3}{2}\text{ m/s}$$
>
>说明顶端沿墙面下滑的速度大小为$1.5\text{ m/s}$。
>
>[3]求夹角$\theta$的变化率：
>
>由几何关系$\cos\theta = \frac{x}{5}$，两端对$t$求导：
>
>$$-\sin\theta \frac{\mathrm{d}\theta}{\mathrm{d}t} = \frac{1}{5}\frac{\mathrm{d}x}{\mathrm{d}t}$$
>
>此时$\sin\theta = \frac{y}{5} = \frac{4}{5}$，代入得：
>
>$$-\frac{4}{5} \frac{\mathrm{d}\theta}{\mathrm{d}t} = \frac{1}{5} \times 2 \implies \frac{\mathrm{d}\theta}{\mathrm{d}t} = -\frac{1}{2}\text{ rad/s}$$

**例题[4]:曲线运动(法向加速度与曲率结合)**

质点沿抛物线轨道$y = \frac{1}{2}x^2$运动。当质点到达点$(1, \frac{1}{2})$时，已知质点在该点的瞬时速率为$v = 2\sqrt{5}\text{ m/s}$，且速率随时间的增加率为$\frac{\mathrm{d}v}{\mathrm{d}t} = 3\text{ m/s}^2$。求质点在该瞬时的全加速度大小。

主要思路:切向加速度直接由速率导数给出；法向加速度通过轨迹曲率公式$K$及$a_n = Kv^2$计算；最后合成全加速度

>[1]切向加速度计算：
>
>切向加速度反映速率大小改变的快慢，直接由已知条件给出：
>
>$$a_\tau = \frac{\mathrm{d}v}{\mathrm{d}t} = 3\text{ m/s}^2$$
>
>[2]计算轨迹在点$x = 1$处的曲率$K$：
>
>(1) $y' = x \implies y'(1) = 1$；
>
>(2) $y'' = 1 \implies y''(1) = 1$；
>
>(3) 代入平面曲线曲率公式：
>
>  $$K = \frac{\vert{}y''\vert{}}{[1 + (y')^2]^{\frac{3}{2}}} = \frac{1}{[1 + 1^2]^{\frac{3}{2}}} = \frac{1}{2^{\frac{3}{2}}} = \frac{1}{2\sqrt{2}}$$
>
>[3]计算法向加速度$a_n$：
>
>$$a_n = K v^2 = \frac{1}{2\sqrt{2}} \times (2\sqrt{5})^2 = \frac{20}{2\sqrt{2}} = 5\sqrt{2}\text{ m/s}^2$$
>
>[4]合成全加速度大小：
>
>$$a = \sqrt{a_\tau^2 + a_n^2} = \sqrt{3^2 + (5\sqrt{2})^2} = \sqrt{9 + 50} = \sqrt{59}\text{ m/s}^2$$
