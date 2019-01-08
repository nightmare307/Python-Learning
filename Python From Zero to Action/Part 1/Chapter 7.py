# -*- coding: utf-8 -*

from Class_Module import *
#颜色类
class ColorBox():
    def __init__(self,index=0):
        self.set_color=['black','white','blue','green']
        self.index=index
    def setColor(self):
        return self.set_color[self.index]
#立方体类
class BoxClass():
    def __init__(self, Boxlength, Boxwidth, Boxheight,BoxColor=0):
        self.length = Boxlength
        self.width = Boxwidth
        self.height = Boxheight
        self.color=ColorBox(BoxColor).setColor
    def volume(self):
        return self.length*self.width*self.height

myBox = BoxClass(10, 10, 10,1)
print('立方体体积是%d,颜色是%s'%(myBox.volume(),myBox.color()))
myBox2 = BoxClass(3, 8, 2)
print('立方体体积是%d' % (myBox2.volume()))

bl=myBox.length
print(bl)
#==========================类的继承==================================
'''
class BoxClassN():
    def __init__(self, Boxlength, Boxwidth, Boxheight):
        self.length = Boxlength
        self.width = Boxwidth
        self.height = Boxheight
    def volume(self):
        return self.length*self.width*self.height
#=========================以下是继承类===============================
class BoxClassIn(BoxClassN):
    def __init__(self, Boxlength, Boxwidth, Boxheight):
        super().__init__(Boxlength, Boxwidth, Boxheight)
        self.color='white'
        self.material='paper'
        self.type='fish'
    def area(self):
        superficial=self.length*self.height+self.width*self.height+self.length*self.width
        return superficial*2
'''
#主程序调用
myBox3=BoxClassIn(10,8,3)
print('立方体体积是%d，表面积是%d，颜色是%s，材质是%s，类型是%s'%(myBox3.volume(),myBox3.area(),myBox3.color,myBox3.material,myBox3.type))

#==========================================重写方法=========================================
class BoxClassRe(BoxClassN):
    def __init__(self, Boxlength, Boxwidth, Boxheight):
        super().__init__(Boxlength, Boxwidth, Boxheight)
    def volume(self,num=1):
        return self.length*self.width*self.height*num
myBox2 = BoxClassRe(8, 8, 2)
print('10个立方体体积是%d' % (myBox2.volume(10)))
#=========================================私有化===========================================
class TeatPrivate():
    def __init__(self):
        self.__say='ok'
    def p(self):
        print(self.__say)
    def __p1(self):
        print(self.__say)
#======================私有类调用=======================
show=TeatPrivate()
show.p()