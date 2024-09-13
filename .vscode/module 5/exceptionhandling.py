# Exception is nothing but a run time error due & it happens during the implemenation of wrong logic.

#& exception handling is the mechanism of handling run time error

a = int(input("enter the firstg number"))
b = int(input("enter the second number"))

try:
    c = a/b
    print("ans",c)
except:
    print("cant divide by jero")
finally:
    print("wecome to simalchaur")
