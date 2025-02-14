"""
CUSTOM FUNCTIONS IN PYTHON ARE OF TWO MAIN TYPES
-Simple functions : fun with no parameters
-Functions with parameters :information that a function is supposed to use
"""

def greet():
    #function body
    #print("Hello World")
    return "Hello World"
#CALLING A FUNCTION OR INVOKING A FUNCTION
print(greet())

#functions with parameters
name= "Joseph"
def welcomeFunction(name):
    #print("Welcome" + name)
    return "Welcome" + name
    print(welcomeFunction(name))
name="Joseph"
school="EMOBILIS"
def WelcomeFunction(SCH):
    #print("Welcome" + SCH)
    return"Welcome" + SCH
print(WelcomeFunction(SCH))