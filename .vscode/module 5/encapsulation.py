#By using encapsulation,we can restrict the vaiables and method acess globally by making it private or protected.
#Note : single underscore (protected)
    # : double underscore (privated)

# _a = 10#protected:it can be print even outside the class
# __b = 20#private:it can be prinnt only inside the class

class number:
    _a = 10
    __b = 20
    def value(self):
        print("a=" ,self._a)
        print("b =",self.__b)
object = number()
object.value()