#Create a variable x and assign the value 5 to it. Print the value of x.
x = 5
print(x,type(x))

#Write a program that assigns a string value to a variable and then prints it.
name = "shaishab"
print(name,type(name))

#What is the difference between int, float, and str? Create examples of each.
x = 12
y = 12.5
a= "don"
print(x,type(x))
print(y,type(y))
print(a,type(a))



##



##create a dictionary consisting of persons name,sex,address,hobbies,age, also use proper data types for each item
##try to change his/her any one hobbies
#and try to add another field called phone_number and assign some value to it

d ={

    "name":"saisab",
    "sex": "male",
    "address":"pokhara",
    "hobbies":("flowering","riding" ),
    "age":24

}
print(d)
print(d,type(d))
d.update({"hobbies":"flowering ,cycling"})
print(d)
d['phone_nu']=986972
print(d) 


####Write a program using nestedif to printwether the day is among[sunday,mon,tue......saturday]
day = int(input("enter the days number"))
if day==1:
    print("sunday")
elif day ==2:
    print("monday")
elif day==3:
    print("tuesday")
elif day==4:
    print('wednesday')
elif day ==5:
    print("Thursday")
elif day ==6:
    print("friday")
elif day==7:
    print("saturday")
else:
    print("no day")
   
#############################

#######
number = []
def get_multiply(n):
    for i in range(1,11):
        value = ("the multiplication of a number ",number)
        result = (f"5*i={number}")
        print(result)
    get_multiply(5)
    