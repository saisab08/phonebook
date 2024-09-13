def get_info():
    name = input("enter the name ")
    age = int(input("enter the age"))
    with open("stdfile.txt",'w') as file:
        file.write(name)
        file.write(str(age))
    print("writing success") 
get_info()

print()


###
   




