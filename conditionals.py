## if statement
"""
if condition :
    #code to be executed only if condition is met
elif condition :
    #code to be executrd if the condition in initial if statement is not met
else:
    #if condition above is not met



"""



age= int(input("enter age: "))
is_vip = False
if is_vip:
    print("Welcome VIP! Enjoy exclusive access and free drinks")
elif age>=25:
    print("Entry granted, get a free drink")
elif age >=18 and age< 25:
    print("Entry granted, but no free drink")
else
    print("This event is not for you, no entry!!")


# sample program using ternary
result ="Entry granted" if age >= 25 else "Not enough free drinks"
print(result)

# sample program using a nested if
age= int(input("enter age: "))
is_vip = False

if age>= 18:
    print("Entry Granted")
#   we check if user is VIP
    if is_vip:
        print("Welcome VIP! You get free drinks")
    else:
        print("No free drinks")
else:
    print("You are too young to enter")

### MATCH CASE EXAMPLE
day= "Monday"
match day:
    case "Monday":
        print("Start of the workweek.")
    case "Friday":
        print("Weekend is here")
    case "Sunday":
        print("Time to relax")
    case _:
        print("Just another day")


