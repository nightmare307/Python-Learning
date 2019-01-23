# -*- coding: utf-8 -*
#*9.1餐馆
class Restaurant():
    '''餐厅类'''
    def __init__(self, restaurant_name, cuisine_type):
        '''初始化餐厅信息'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        '''打印餐厅信息'''
        return self.restaurant_name,self.cuisine_type
    
    def open_restaurant(self):
        '''餐厅正在营业'''
        return self.restaurant_name

restaurant=Restaurant('京味斋','北京菜')
print('This %s is sell %s'%(restaurant.restaurant_name,restaurant.cuisine_type))
print('%s is opening' % (restaurant.restaurant_name))

#*9.2三家餐馆
