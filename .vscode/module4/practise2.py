'''
* Ask the student information as input and store them in csv file
add age to the student
make sure the student information input consist a function to handle job 
list all the students whose age is greater than 15
'''
import csv

student = [
    {"name": "Kushal", "age": 14 ,"roll_no":19},
    {"name": "Shaishab", "age": 16,"roll_no":19},
    {"name": "Tanisha", "age": 15,"roll_no":19},
    {"name": "dipti", "age": 17,"roll_no":19},
    {"name": "Eva", "age": 18,"roll_no":19}
]

def student_info():
    with open('collection.csv','a') as file:
        Head =["name","age","roll_no"]
        writer=csv.DictWriter(file,fieldnames=Head)
        # writer.writeheader()
        writer.writerows(student)
student_info()

def get_function():
    with open('collection.csv','r') as file:
        reader=csv.DictReader(file,delimiter=',')
        for row in reader:
            print(row)
            # if int(row[(age)]) > 15:
            #     print(row)
get_function()

# for i in range(1,10):
#     if age>15:
#         print("list the collection of student ")
#     elif age>=15:
#         print("doesnt contain the list")
#     else:
#         print("not contain in the list")
names_above_15 = [student["name"] for student in student if student["age"] > 15]
print(names_above_15 )

         

    
    