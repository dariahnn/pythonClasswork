"""
for loop : loops over sequences
syntax
for item in variablerefforsequence;
    code executed repeatedly

"""
fruits = ["Mango", "Banana", "Apple"]
for fruit in fruits:
    print(f"My favourite fruit is {fruit}")

# looping using range
#the loop will execute the code logic acording to the stipulated range size
#i.e. range(5) = equal to five loops
# print the number 0 to 4
for item in range(5):
    print(item)
for item in range(1,5):
    print(item)
for item in range(1,10,2):
    print(item)

"""
range(x) :start from and excludes x
range(start,stop) : start fom start and stop
range(start,stop,step) : start from start and exclude step but skip using step
"""

# sample program to print 0 to 4 using while
x=0
while x < 5:
    print(x)
    x += 1

"""
LOOP CONTROL STATEMENTS
1. Break: EXITS A LOOP EARLY 
2. CONTINUE : SKIP THE CURRENT ITERATION(LOOP) AND MOVE TO NEXT
3. PASS : SIMPLY A PLACEHOLDER
"""

for i in fruits:
pass

#break
for i in fruits:
    if i== "Apple":
        break
    print(i)
#continue
for i in fruits:
    if i== "Banana":
        continue
        print(i)