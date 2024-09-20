# Write a program on the basis of following scenarios . (10)
# a. Create a Class Called Library
# b. Create add_book and show_books method in the class
# c. The properties of Library are , book_name, author , publication
# d. Create object of class to perform add_book and show_books operation

class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book_name, author, publication):
        book = {
            'book_name': book_name,
            'author': author,
            'publication': publication
        }
        self.books.append(book)
        print(f"Book '{book_name}' book stored.")


    def show_books(self):

        if i in range== 0:
            book = i+1

            
            print("No books in the library.")
        else:
            print("Books in the library:")
            for i in book(self.books, 1):
                print(f"{i}. {book['book_name']} by {book['author']} (Publication: {book['publication']})")

tech_library = Library()
tech_library.add_book("The book from nepal tech pal:,python class")
tech_library.add_book("the book from nepal tech pal:, python exams")
tech_library.add_book("The book from nepal tech pal :, django class")

tech_library.show_books()
tech_library.add_book()



# 2 What are list,sets and dictionary how can we create them in python give example and use
# case of each (5)

#Ans:lists is an order sequnce of mutable data typesitems and its denotated by []
my_lists=['apple','bananana','cat','dog']
print(my_lists,type(my_lists))
my_lists[2]=5
print(my_lists)

#Sets:
# Ans: A set is an unordered collection of unordered items and it is immutable in nature.
s = {1,2,3,'apple'}
print(s)
print(s,type(s))
s.remove(1)
print(s)

#Dictionary:
#Ans: dictionary are the mutable data types where the key pair of the values are stored.
d={
   'name':"saisab",
   'age': 24
}
print(d,type(d))
print(d)



#Q3. Write a program that perform Division operation between 2 numbers , use Exception
# handling to handel runtime errors (5)
# E.g user can enter 2 numbers in a,b variables and the program will perform division ans=a/b handel division by 0
# exception
a = int(input("enter the firstg number"))
b = int(input("enter the second number"))

try:
    c = a/b
    print("ans",c)
except:
    print("cant divide by jero")


#4 complete the  following code :
def age_check(func):
    def wrapper(age):
        if age<18:
            raise ValueError("age must be greater or equal than 18")
        return func(age)
    return wrapper
@age_check
def can_vote(age):
    print("yes, you can vote")

age = int(input("enter the age"))
try:
    can_vote(age)
except Exception as e:
    print (e)



#5 write a program that will write your name , age into a text file (5)

import csv 

data =[
    {"name": "Shaishab", "age": 16,"roll_no":19},
    
]
def my_info():
    with open('txtfile.csv','a') as file:
        Head =["name","age"]
        writer=csv.DictWriter(file,fieldnames=Head)
        writer.writerows(data)
my_info()

def get_function():
    with open('txtfile.csv','r') as file:
        reader=csv.DictReader(file,delimiter=',')
        for row in reader:
            print(row)
get_function()





