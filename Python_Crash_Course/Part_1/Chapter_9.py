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

#*9.3用户
class User():
    '''用户类'''
    def __init__(self, first_name, last_name,age,gender,hobby):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.hobby=hobby
    def describe_user(self):
        return self.first_name.title()+' '+self.last_name.title()+' is a '+str(self.age) +' years old '+self.gender + ' , he/she\'s hobby is '+self.hobby
lee = User('chris', 'lee', 18, 'man', 'sleep')
print(lee.describe_user())

#*9.4就餐人数
class RestaurantCount():
    '''餐厅类'''
    def __init__(self, restaurant_name, cuisine_type):
        '''初始化餐厅信息'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_reserved = 0
    def describe_restaurant(self):
        '''打印餐厅信息'''
        return self.restaurant_name, self.cuisine_type
    def open_restaurant(self):
        '''餐厅正在营业'''
        return self.restaurant_name
    def set_number_reserved(self, numbers):
        self.number_reserved=numbers
        return self.number_reserved
    def increment_number_server(self,numbers):
        self.number_reserved += numbers
        return self.number_reserved

#*9.5尝试登录次数
