# -*- coding: utf-8 -*
#==========================类的引用==================================
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
