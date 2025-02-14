"""
THIS PROGRAM FILE
"""


def calculate_birth_year(name,age):
    from datetime import datetime
    current_year = datetime.now().year
    birth_year =  current_year-age
    return f"Hello {name} , you were born in this {birth_year}"

user_name= input("Enter name ")
user_age = int(input("Enter your age"))
result = calculate_birth_year(user_name,user_age)
print(result)