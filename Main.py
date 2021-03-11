from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import math

class Main_UI(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.initUI()

    def initUI(self):
        #设置窗口标题以及大小
        self.setWindowTitle('基本函数教学辅助')
        self.resize(1100,600)

        #窗口居中
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2

        self.figure = plt.figure()
        self.btn1 = QPushButton('绘制')
        self.edit = QLineEdit()
        self.cb = QComboBox()  #下拉列表
        self.textEdit = QTextEdit()
        self.label1 = QLabel('f(x)=')
        self.label2 = QLabel('函数性质')
        self.canvas = FigureCanvas(self.figure)
        self.btn1.clicked.connect(self._plot)

        self.cb.addItem('请选择')
        self.cb.addItem('一次函数')
        self.cb.addItem('二次函数')
        self.cb.addItem('反比例函数')
        self.cb.addItem('幂函数')
        self.cb.addItem('指数函数')
        self.cb.addItem('对数函数')
        self.cb.addItem('三角函数')
        self.cb.currentIndexChanged.connect(self.function)

        #设置布局
        self.layout1 = QGridLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QGridLayout()
        self.layout1.addWidget(self.cb,0,0,1,1)
        self.layout1.addWidget(self.label1,0,1,1,1)
        self.layout1.addWidget(self.edit,0,2,1,4)
        self.layout1.addWidget(self.btn1,0,6,1,1)
        self.layout2.addLayout(self.layout1)
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.textEdit)
        self.layout3.addLayout(self.layout2,0,0,1,1)
        self.layout3.addWidget(self.canvas,0,1,1,1)


        self.setLayout(self.layout1)
        self.setLayout(self.layout2)
        self.setLayout(self.layout3)

    def function(self):
        fun = self.cb.currentIndex()
        if fun == 1:
            self.textEdit.setText("""一般形式：y=kx+b（k,b为常数，k≠0）
性质：
1、k叫做比例系数，也叫斜率。b叫做在y轴上的截距。特殊的b=0称为正比例函数。
2、若k>0，y随x的增加而增加；若k<0，y随x的增加而减少。
3、直线y=k1x+b1（k1≠0）与直线y=k2x+b2（k2≠0）的位置关系:
① 两直线平行k1=k2，且b1≠b2；
② 两直线相交k1≠k2；
③ 两直线重合k1=k2，且b1=b2；
④ 两直线相互垂直k1k2=-1。
4、直线y=kx+b与坐标轴的交点坐标及围成的三角形面积:
① 与x轴的交点A坐标为（-b/k，0）；
② 与y轴的交点B坐标为（0，b）；
③ 与坐标轴围成的三角形面积为：S△AOB=b²/2丨k丨。
5、直线y=kx+b的对称:
① 关于x轴的对称得到直线y=-kx-b；
② 关于y轴的对称得到直线y=-kx+b；
③ 关于原点的对称得到直线y=kx-b。""")
        elif fun == 2:
            self.textEdit.setText("""输入注意：x²输入方式为x**2
一般形式：y=ax²+bx+c（a,b,c为常数，a≠0）
性质：
1、若a>0，二次函数开口方向向上，若a<0，二次函数开口方向向下。
2、对称轴为x=-b/2a，最值为(4ac-b²)/4a
3、若a>0，函数在(-∞,-b/2a)递减，(-b/2a,∞)递增；若a<0，函数在(-∞,-b/2a)递增，(-b/2a,∞)递减。
4、△=b²-4ac，若△>0，函数与x轴有两个交点；若△=0，函数与x轴有且仅有一个交点；若△<0，函数与x轴没有交点。
5、顶点式：y=a(x+b/2a)²+k
   零点式：a(x-x1)(x-x2) （其中x1，x2为二次函数与坐标轴的交点）
6、平移遵守的规律：左加右减，上加下减。
7、找对称的五点来画图像。（一般为顶点，与y轴交点于关于对称轴对称的对应点，与x轴的两个交点）""")        
        elif fun == 3:
            self.textEdit.setText("""一般形式：y=a/x（x≠0）
性质：
1、当a>0，图像位于第一、三象限，同一个象限内，y随x的增大而减小；当a<0，图像位于第二、四象限，同一象限内，y随x的增大而增大。
2、定义域为x≠0，值域为y≠0。即与坐标轴无限靠近，但不相交。
3、反比例函数是轴对称图形，对称轴为y=x或y=-x；也是中心对称图形，对称中心为原点。
4、反比例上一点m向x、y分别做垂线，交于q、w，则矩形mwqo（o为原点）的面积为|k|""")
        elif fun == 4:
            self.textEdit.setText("""（幂函数包括一次函数，二次函数以及反比例函数）
输入提醒：x的a次方输入方式为x**a
一般形式：y=x**a
正值性质：
当α>0时，幂函数有下列性质：
1、图像都经过点（1,1）（0,0）；
2、函数的图像在区间[0,+∞）上是增函数；
3、在第一象限内，α>1时，导数值逐渐增大；α=1时，导数为常数；0<α<1时，导数值逐渐减小，趋近于0；
负值性质：
当α<0时，幂函数有下列性质：
1、图像都通过点（1,1）；
2、图像在区间（0，+∞）上是减函数；（内容补充：若为X-2，易得到其为偶函数。利用对称性，对称轴是y轴，可得其图像在区间（-∞，0）上单调递增。其余偶函数亦是如此）。
3、在第一象限内，有两条渐近线（即坐标轴），自变量趋近0，函数值趋近+∞，自变量趋近+∞，函数值趋近0。
零值性质：
当α=0时，幂函数有下列性质：
图像是直线y=1去掉一点（0,1）。它的图像不是直线。""")
        elif fun == 5:
            self.textEdit.setText("""输入提醒：a的x次方输入方式为a**x
一般形式：y=a**x
性质：
1、指数函数的定义域为R，这里的前提是a大于0且不等于1。对于a不大于0的情况，则必然使得函数的定义域不连续，因此我们不予考虑，同时a等于0函数无意义一般也不考虑。
2、指数函数的值域为(0， +∞)。
3、函数图形都是上凹的。
4、a>1时，则指数函数单调递增；若0<a<1，则为单调递减的
5、当a从0趋向于无穷大的过程中（不等于0）函数的曲线从分别接近于Y轴与X轴的正半轴的单调递减函数的位置，趋向分别接近于Y轴的正半轴与X轴的负半轴的单调递增函数的位置。其中水平直线y=1是从递减到递增的一个过渡位置。
6、函数总是在某一个方向上无限趋向于X轴,并且永不相交。
7、函数总是通过（0，1）这点,(若有常数项，且常数项为b，函数定过点(0,1+b))
8、指数函数无界。
9、指数函数是非奇非偶函数。""")
        elif fun == 6:
            self.textEdit.setText("""输入提醒：底数为a的对数函数输入方式为log(x)/log(a)
一般形式：y=loga(x) （a为对数函数的底数，a≠0或1）
性质：
1、对数函数是指数函数的反函数，二者关于y=x对称。
2、定义域为x>0，值域为R。且零点为x=1。
3、对数函数无界。
4、对数函数是非奇非偶函数。
5、对数函数的函数图像恒过定点（1，0）；
6、a>1时，在定义域上为单调增函数；0<a<1时，在定义域上为单调减函数。""")
        elif fun == 7:
            self.textEdit.setText("""一般形式：y=Asin(wx+φ)或者y=Acos(wx+φ)
性质：
1、三角函数都具有周期性，且T=2π/w
2、画图都采取五点画图，找五个点确定一个周期内的函数图像。
3、正弦函数为奇函数，余弦函数为偶函数。""")
        elif fun == 0:
            self.textEdit.clear()

    def _plot(self):
        ax = self.figure.add_axes([0.1,0.1,0.8,0.8])
        ax.clear() 
        x = linspace(-100,100,10000)
        y = eval(self.edit.text()) 
        ax.plot(x,y)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main_UI()
    main.show()
    sys.exit(app.exec_())