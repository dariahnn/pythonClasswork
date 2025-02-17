"""
Creating a class :  we use the keyword class i.e.
class classname:
"""

class User:
    # here I can now define my class properties
    fullname = "Draco Anandz"
    role_id = "Lecturer"
    Staff_id= 348673436
    is_verified = True

"""
to create and object we use the name of the class followed by the paentheses () i.e. variable = user()

"""
person1 = User() #this creates an object of the user class
print(person1)
print(person1.fullname)#to access a property use the dot notation
"""
1.the __init__() method : this method is always executed on an object creation
2. __str__() method : this method returns the string representation of an object
"""
class Person:
    def __init__(self,fullname,role_id, staff_id, is_verified):
        self.fullname = fullname
        self.role_id = role_id
        self.staff_id = staff_id
        self.is_verified = is_verified
    def __str__(self):
        return f"{self.fullname}, {self.role_id}, {self.staff_id}, {self.is_verified}"
#create object
p1 = Person("darian","lecturer",63484674,True)
p2 = Person("alice","student",0,True)
print(p1)
print(p1.fullname)
print(p2.fullname)

