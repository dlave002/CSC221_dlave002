import math
import random

""" file1 = open('small_file.txt', 'r')
# FIX THE TWO LINES BELOW
line = file1.readline()
while line:
    print(line)
file1.close() """

# 2.3 Standard Operators
# Experiment with pow(x, y, modulo). What does modulo do?
# INSERT YOUR CODE HERE

# Experiment with round(x, n). What does n do? What about n=2 vs n=-2?
# INSERT YOUR CODE HERE

def pow(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y if y < x else y - x
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y if y != 0 else "Division by zero is undefined"
    
def rounds(x,n):
    x = round(x, n)
    return x

print(pow(1,2,'/'))



# 2.4 In-Place Assignment
# What should a = [1, 2, 3] followed by a += [7, 6, 5] do? Show me!
# INSERT YOUR CODE HERE
# return [1, 2, 3, 7, 6, 5]

# What should a = [1, 2, 3] followed by a *= 4 do? Show me!
# INSERT YOUR CODE HERE

""" SyntaxError: invalid syntax
 """


# 2.5 Object Comparison
# Make an exanmple showing the difference between == and is.
# INSERT YOUR CODE HERE


# Using ==
x = [1, 2, 3]
y = [1, 2, 3]

# == checks for the equality of values
print("Using ==:")
print(x == y)  # Output: True, because the values are the same
print(x is y)  # Output: False, because they are different objects in memory

# Using is
a = [1, 2, 3]
b = a  # b now references the same object as a

# is checks for the identity of the objects (whether they are the same object in memory)
print("\nUsing is:")
print(a == b)  # Output: True, because the values are the same
print(a is b)  # Output: True, because they reference the same object in memory


# 2.7 Boolean Expressions and Truth
# Why does the code below only output 'Ned'?
def ned():
    print('Ned')
    return False
def lecky():
    print("lecky")
    return False
if ned() and lecky():
    print('wrote this')

""" The reason why it only print out Ned because after the line print('Ned') you return false immediately which lead to the function stop and the rest of the code inside the function would never be call """


# 2.8 Conditional Expressions
# Convert the code called out into a one-line conditional expression...
# And what does that format do?
import random
random.seed(42)

def above_or_below():
    x = random.randint(1,100)
    # MAKE THE FOLLOWING 4 LINES INTO ONE CONDITIONAL EXPRESSION
    y = -1 if x < 50 else 1
    return y


for i in range(10):
    # WHAT DOES THIS LINE DO?
    """ format(...): This is a method used for formatting strings in Python. In this context, it's used to format the result of above_or_below().

    " +d": This is the format specification. Here, it's saying to format the value as a signed decimal integer (d), and the + sign indicates that positive numbers should be prefixed with a plus sign. """
    print(format(above_or_below(),"+d"))

# 2.9 Iterables
# Show an example of every iterable in Table 2.5

# INSERT YOUR CODE HERE

print(1 < 2)
print(2 > 1)
print(2 >= 2)
print(1 <= 1)



# 2.10 Operations on Sequences
# Show that the exam ple at the end pof section 2.10 are correct
# The code starts with
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:5])
print(a+ [1,2,3,4,5])
z = [3,4,5]
b = [z]
c = 4* b

print(c)



# 2.11 Operations on Mutable Sequences
# Create a list with the first 2 million positive integers in it ([1, 2, 3, ... , 2,000,000])
# Replace the centermost 1,000,000 integers with the string 'MiddleStuff'
# Figure out some way to print this and look at len(this) to demonstrate that it works

# INSERT YOUR CODE HERE

# Create a list with the first 2 million positive integers
numbers = list(range(1, 2000001))

# Find the midpoint
midpoint = len(numbers) // 2

# Replace the centermost 1,000,000 integers with the string 'MiddleStuff'
numbers[midpoint - 500000:midpoint + 500000] = ['MiddleStuff'] * 1000000

# Print a portion of the list and its length to demonstrate
print(numbers[:10])  # Print the first 10 elements
print(len(numbers))   # Print the length of the list



# 2.12 Operations on Sets
# rand1 and rand2 are two independent lists of 1000 numbers between 1 and 1000 inclusive
# What are set1 - set4?
# How many numbers between 1 and 1000 appear in neither list?
import random
random.seed(42)

rand1 = [random.randint(1,1000) for i in range(1000)]
rand2 = [random.randint(1,1000) for i in range(1000)]
set1 = set(rand1)
set2 = set(rand2)
set3 = set1 | set2
set4 = set1 & set2
print(len(set1), len(set2), len(set3), len(set4))

random.seed(42)

rand1 = [random.randint(1, 1000) for i in range(1000)]
rand2 = [random.randint(1, 1000) for i in range(1000)]

set1 = set(rand1)
set2 = set(rand2)

# Union of the sets
set3 = set1 | set2

# Intersection of the sets
set4 = set1 & set2

# Set difference gives the elements in set1 but not in set4
difference_set = set1 - set4

print("set1 - set4:", difference_set)
print("Number of unique numbers between 1 and 1000 that appear in neither list:", len(set3) - len(set4))




# 2.14 List, Set, and Dictionary Comprehensions
# Use a dictionary comprehension to create a dictionary that contains the square
# and square root of the factorials from 0 to 100
import math

# Hint: Make a list of the first 100 factorials
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
fact_100 = [factorial(x) for x in range(1, 101)]
print(fact_100)

#dict1 = { YOUR CODE HERE }
#print(dict1)


# Function to calculate factorial
def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# List of the first 100 factorials
fact_100 = [factorials(x) for x in range(101)]

# Dictionary comprehension to create a dictionary with squares and square roots of factorials
dict1 = {n: (n**2, math.sqrt(n)) for n in fact_100}

print(dict1)