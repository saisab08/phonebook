class calculator:
    def calculate(self,x,y):
        return x,y
class multiply(calculator):

    def calculate(self,x):
        return x*10
    
class addition(calculator):
    def calculate(self, x, y):
        return x +y

m = multiply()
x =m.calculate(10)
print(x)

A = addition()
y = A.calculate(10,20)
print(y)    
    
