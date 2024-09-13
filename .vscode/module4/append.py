#new_message = "hellow world how are you"
#with open("myfile.txt",'a') as file:
   # file.write(new_message)
#print("success")



#write a program to get the student informtion and placed it in a file........ 
def get_info():
    name = ("enter the name ")
    age = int(input("enter the age"))
    with open("myfile.txt", '+w') as file:
        file.write(name,age)
    print("writing successs")

  

