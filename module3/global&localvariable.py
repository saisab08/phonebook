#local variable
def function(name):
    name= "my name is saisab"
    print(name)
function("saisab")   


#if outside the function
def function(name):
    d = 'my name is ',name
    print(d)
function("saisab")

print()

#####global variable
def function(name):
    print("inside function",d)
d="its me saisab"
print(d)
function("saisab")
print("outside function",d)                                                                                                 




  


