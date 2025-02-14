from variable import myName

myName=input("Enter your name:")
print(f"{myName} Welcome to the console calculator")
# let the user pick operation to work on
while True:
    print("\nAvailable Operations:")
    print("1. Addition")
    print("2. Sutraction")
    print("3. Multiplication(*)")
    print("4. Divition(/)")
    print("5. Modulus(%)")
    print("6. Exit")

    my_choice = input("enter your operation: 1-6")
    #prompt them for the numbers to be used
    num1=float(input("Enter the first number"))
    num2=float(input("Enter the second number"))

    if my_choice == "6":
        print("Thank You for using my app")
        break  # stops the loop
    elif my_choice=="1":
        print("Adding numbers")
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif my_choice=="2":
        print("Subtracting numbers")
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif my_choice=="3":
        print("Multiplying numbers")
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif my_choice=="4":
        print("Dividing numbers")
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    elif my_choice=="5":
        print("Modulating numbers")
        result = num1 % num2
        print(f"{num1} + {num2} = {result}")
    else:
        print(f"{myName}, This is an Invalid choice")


