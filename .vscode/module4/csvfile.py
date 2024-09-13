import csv

student=[{
"name":"saisab",
"class":12,
"roll_no":17
}]
with open('data.csv','w') as file:
    Head=["name","class","roll_no"]
    writer=csv.DictWriter(file,fieldnames=Head)
    writer.writeheader()
    writer.writerows(student)


with open('data.csv','r') as file:
    reader=csv.DictReader(file,delimiter=',')
    for row in reader:
        print(row)

##############################################
'''
* Ask the student information as input and store them in csv file
add age to the student
make sure the student information input consist a function to handle job 
list all the students whose age is greater than 15
'''
    
