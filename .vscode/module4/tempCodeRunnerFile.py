'''
Ask student information as input and store the in CSV file.
Add age to student.
Make sure the student information input consist of a fucntion to handle job.
List all the students whose age is greater than 15.
'''

import csv
data=[]

name = input("enter the name of the students")
age = int(input("enter the age of the student"))
roll = ("enter the roll of the student")

def get_info():
    with open('collection.csv','w') as file:
        Head =["name","class","roll"]
        writer=csv.DictWriter(file,fieldnames=Head)
        writer.writeheader()
        writer.writerows(data)
get_info()

def get_function():
    with open('collection.csv','r') as file:
        reader=csv.DictReader(file,delimiter=',')
        for row in reader:
            print(row)
get_function()

for i in range(1,10):
    if age>15:
        print("list the collection of student ")
    elif age>=15:
        print("doesnt contain the list")
    else:
        print("not contain in the list")


         

    
    