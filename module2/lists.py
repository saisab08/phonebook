#lists is an order sequnce of items and its denotated by []
#it is the mutable datatypes

my_lists=['apple','bananana','cat','dog']
print(my_lists,type(my_lists))
my_lists[2]=5
print(my_lists)

#######

fruits = ['apple','orange','lichhi','banana']
fruits[0],fruits[1]=fruits[1],fruits[0]
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
fruits.append("mango")
print(fruits)
fruits.insert(1,"strawberry")
print(fruits)
fruits.remove("lichhi")
print(fruits)