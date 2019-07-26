print("hello world")
print("Bye world")

"""
num1 = int(raw_input("Enter number #1: "))
num2 = int(raw_input("Enter number #2: "))
total = (num1) + (num2)
print("The sum is " + str(total ))
"""
"""
int(x) converts x (the value inside) to an integer (whole number)
float(x) converts x (the value inside) to a float (decimal number)
Strings cannot be mixed with integers, so we have to convert the
number (integer) back to a String to print it by using the str()
"""
"""
num = int(raw_input("Enter a number: "))
if num > 0:
    print ("That's a positive number!")
    print("wow")
elif num < 0:
    print("That's a negative number!")
else:
    print("Zero is neither positive nor negative")
"""
"""
for i in range(5, 2, -1):
    print(i)
x = 1

while x <= 5:
    print(x)
    x = x + 1

my_name = "Bob"
friend1 = "Alice"
friend2 = " John"
friend3 = "Mallory"

print(
    "My name is %s and my friends are %s, %s, and %s" %
    (my_name, friend1, friend2, friend3)
)

def greetAgent(first_name, last_name):
    print("%s, %s, %s." % (last_name, first_name, last_name))

greetAgent("James", "Bond")
"""


def findSum(x):
    sum = 0
    for i in range(1,x+1):
        sum = sum + i
    
    print(sum)

findSum(10)
