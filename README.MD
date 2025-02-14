###FUNDAMENTALS OF PROGRAMMING
1. variables:storage reference for data info
2. data Types
            -String 
            -number: integer : 42, 50 ,1000000
                     float 3.14,0.1
                     complex:when number is large >1000000000
            -boolean: evaluates to True or False
 NON PRIMITIVES (SEQUENCES IN PYTHON)
1. List : ordered mutable collection
 variablename=["Apple","Banana", "Orange"]
2. Tuple : ordered , immutable collection
 variablename=(10.04,30.50)
3. Range : sequence of numbers
  variablename=(5)
4. Set: collection of unique items 
 variablenames={1,2,3,4,5}
5. dictionary ; key and value pairs
variablename={
                key:value
            }
      THE NON DATATYPE
  variablename=None


### PYTHON OPERATORS
special symbols that perform operations on our variables
 
-Arithmetic Operators
(+,-,*,/,%)
 Comparison Operators : usually evaluate to true or false
- a. == Equal to e.g a==b
- b. != not equal to a !=b
- c. >greater than a>b
- d <less than
- e. grater than or equal to a>=b
- e. less than or equal to a<=b

Logical Operators : combine conditional statements
- a. and :: $ :: returns true if both conditions are true
- b. or :: || ::  returns true if one condition is met
- c. not  :: ! :: reverses the result e.g a !=b
 
  Assignment Operators : used to assign values to variables
- a.= : x=4, y="Jose"
- b. += : add and assign , x +=2 (x=x+2)
- b. += : subtracts and assign , x -=2 (x=x-2)
- b. += : multiply and assign , x *=2 (x=x*2)
- b. += :  divide and assign , x /=2 (x=x/2)
- b. += :  modulus and assign , x %=2 (x=x%2)
- b. += :  divide and assign , x /=2 (x=x/2)
 
Identity Operators
a. is : returns true if both comparisons refer to the same object 
b. is not : returns true if they refer to different object.


### CONDITIONAL STATEMENTS
Make decisions in code based off conditions

1. if statement
 

### TYPE CASTING
This is the process of converting one data type to another
Explicit Type Casting (Manually)

Toconvert to 
Integer = int(input(value))
float = float(value)
string = str(value to be converted)
list = (value)
tuple = tuple(value)
set = set(value)

2. Ternary Operator/ Conditional
    short way of writing an if, else statement
    age=18
    variabletostoreresult = (what to be evaluated if true) if (condition) else (result if false)

3. Nested IF
    an if statement with an if statement inside
    if condition:
        code to execute
    if condition:

4. match-case (python3.10+)
    matches a code logic as per selection
   variable = ""
   match variable :
     case selection:
         code to execute


### LOOPS
Are used for repeating an executing a block of code X times
1. for loop : iterates (loop) over seguences \; list , dictionary , tuple, string and range
2. while loop : repeats the block code as long as the condition is true


### VARIABLE SCOPING
Reference to where a variable can be accessed in a program
1. LOCAL SCOPE
2. variables declared in a local scope will only be accessible within that function
3. GLOBAL SCOPE
4. variables defined in this scope can be accessed anywhere within the file
5. ENCLOSING SCOPE
6. when a function is defined within another function, the inner function can be access variables of the outer function