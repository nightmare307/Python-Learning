# -*- coding: utf-8 -*

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

