#when the user defines the class that inherits all the properties of other class called inheritance
#syntax :class father:
#properties of father
        # class son(father) it includes the properties of all father as a parent class
        # 

class father:
    def details(self) :
        name = "hero"
        age = 42
        sex = 'male'
        print(f"The father name is {name} and his age is {age} with the gender {sex}")
class son(father):
    def details1(self):
        name = 'mero'
        age = 24
        sex = "male"
        print(f"The son name is{name} and his age is{age} with the gender of{sex}")

son = son()
son.details()
son.details1()