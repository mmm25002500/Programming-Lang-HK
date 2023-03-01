# 1
class Window:
    def __init__(self,w=10,h=5):
        self.width=w
        self.height=h

# 1-1
w0 = Window()
# 1-2
w1 = Window(12, 18)
# 1-3
setattr(w1, 'width', 16)
setattr(w1, 'height', 7)
# 1-4
area_w0 = w0.width * w0.height
area_w1 = w1.width * w1.height

if area_w0 > area_w1:
    print("w0 的面積較大")
else:
    print("w1 的面積較大")

# 2
class Pen():
    price=30

# 2-a
p0 = Pen()
print(hasattr(p0, 'price'))
print(getattr(p0, 'price'))

# 2-b
p0.price = 45

# 2-c
print(Pen.price)

# 2-d
p1 = Pen()
print(p1.price)

# 2-e
Pen.price = 50
print(p0.price)
print(p1.price)

# 因為 p0 已經賦值了，所以 p0.price = 45。而 p1 沒有賦值，所以 p1.price = 50。

# 3
class Factor:
    factor_list=[2,3,6,8]
    def __init__(self,num):
        print('initial factor_list:',Factor.factor_list)
        self.num=num

    # 3-a
    def find_factors(self):
        factors = []
        for factor in Factor.factor_list:
            if self.num % factor == 0:
                factors.append(factor)
        return factors
    
    # 3-b
    @classmethod
    def add_factors(cls, lst):
        for num in lst:
            if num not in cls.factor_list:
                cls.factor_list.append(num)

    # 3-c
    @classmethod
    def remove_factors(cls, lst):
        for num in lst:
            if num in cls.factor_list:
                cls.factor_list.remove(num)
    
    # 3-d      
    @classmethod
    def show_factor_list(cls):
        print('factor_list:', cls.factor_list)

    # 3-e    
    @staticmethod
    def isfactor(num, n):
        return num % n == 0
    
# 4
class Person:
    def __init__(self, na):
        self.name = na
    
    # 4-a
    def print_name(self):
        print('name=', self.name)

# 4-b
class Student(Person):
    def __init__(self, na, ge):
        super().__init__(na)
        self.gender = ge
        
    def print_info(self):
        print('name=', self.name, ', gender=', self.gender)

# 5
class Year:
    def __init__(self,y):
        self.__year=y

    # 5-a
    def isleap(self):
        if self.__year % 4 == 0:
            if self.__year % 100 == 0:
                if self.__year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    
    # 5-b
    # getter
    @property
    def year(self):
        return self.__year
    
    # setter
    @year.setter
    def year(self, y):
        self.__year = y