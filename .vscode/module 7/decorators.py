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