import string # To use string methods like upper(), casefold() etc

def opening():
    print("********************")

print("Hello World")
slices = input("Pick a number\n") # Creating variable
print("Great! You'll get " + str(slices) + " slices of pizza.\n")

opening() # Creating function
def multiply(x, y):
    return x * y

x = int(input("Pick a number for x\n"))
y = int(input("Pick a number for y\n"))
total = multiply(x, y)
print(f"The total of x * y with multiply() function is {total}.\n")

# Python has no command for declaring a variable.
# A variable is created when some value is assigned to it.
# The value assigned to a variable determines the data type of that variable.
# In Python, void functions are not exactly the same as functions in C/C++
# If the function body does not have any return statement then a special value None returns when the function terminates

opening()
def power(base, exponent):                                              # Creating pow function
    result = 1
    for x in range(exponent):
        result = result * base
    return result

def print_pow(base, exponent):
    my_power = power(base, exponent)
    print(f"{base} raised to {exponent}, the power is {my_power}.")
    # f-strings (formatted string literals) is a concise and readable way to embed variables directly into strings
    # The f before the string indicates that it is an f-string, and within the curly braces {}, can insert variables or expressions that will be evaluated and formatted into the string
    # Why Use f-strings?
        # Readability: F-strings make the code more readable compared to other methods of string formatting (like using + concatenation or .format()), especially when there are many variables to include in a string.
        # Performance: F-strings are faster than alternatives like % formatting or .format(), because they are evaluated at runtime and directly inserted into the string.

    #Comparison:

    # print("{} raised to {}, the power is {}.".format(base, exponent, my_power))

    # Or using string concatenation (less efficient and harder to read):

    # print(str(base) + " raised to " + str(exponent) + ", the power is " + str(my_power) + ".")

base = int(input("What is the base?\n"))
exponent = int(input("What is the exponent?\n"))
print_pow(base, exponent)
print("\n")

# Python is an interpreted language
# Unlike C++, python does not need datatype when declaring variables
# Python data types are numeric(int, float), dictionary{}, bool, set{}, sequence types(string, list, tuple) 

opening() # Integral types in C++, numeric in Python
# int = integers, contains positive and negative whole numbers. No fractions or decimals
# float = floating numbers = decimal point numbers
# complex = complex numbers

a = 1
print(f"Type of a is {type(a)}.")

b = 1.0
print(f"The type of b is {type(b)}.")

c = 1 + 1j
print(f"The type of c is {type(c)}.")

# Compared to C/C++, Python DOES NOT have signed and unsigned integers as data types
# There is no need to specify the data types of variables as the interpreter itself predicts the variable data type based on the value assigned to it
# But can still convert signed integer to unsigned integer with the following example
signed_integer = -100

# Adding 2^32 to convert signed to unsigned integer
unsigned_integer = signed_integer + 2**32
print(unsigned_integer)
print(type(unsigned_integer))

opening()
print(f"Python3 use Unicode by default and it allows for the representation of a much wider range of characters. Thus Python does not have a character data type like C++ does.\n")

opening() # In Python it is known as Escape Characters(Escape sequences in C++)
text1 = "Hello"
text2 = "There"
print("Python and C++ are \"super\" awesome!")       # \" for strings
print("\\\' is used for single \'1\' character.")    # \' for chars and \\ for one backlash
print(f"{text1}\r {text2}.")                         # \r similar to \n? carriage return?
print(f"{text1}\t {text2}.")                         # \t tab between strings
print(f"{text1}\b {text2}.")                         # \b delete a char
print(f"{text1}\f{text2}.")                          # \f == \v(C++)
print("\n")

opening() # BOOL FUNCTION
not_found = 0
found = True
num = 5
print(bool(num))
print(bool(found))
print(bool(not_found))
print("\n")

# Any strings, list, tuple, set and dictionary are True, except empty ones
# Any number is True, except 0

opening() # Floating num
a_ = 10.0
print(type(a_))
print(float(50.77))

b_ = float('-123.12')  # Convert it to strings
print(b_)

# Special characters cannot be floating numbers
# Example
 #print(float('uba'))  Output = ValueError: could not convert string to float: 'uba'
 
c_ = float(3)
print(type(c_))   # Because specified it will be floating num even without decimal points
print("\n")

opening()  # Constant
# Constants are usually defined on a module level and written in all capital letters with underscores separating words
MAX_OVERFLOW = 100
TOTAL = 5
print(f"These examples {MAX_OVERFLOW} and {TOTAL}, will be an examples of const variables in Python.\n")

opening()  # Numeric function
# More often used = standard operators such as +, -, *, /
# pow for getting power value
# Import math library for advanced mathematical operations
# Functions such as min, max to get minimum and maximum of the numbers passed
# Can also perform arithmetic operations using operator like, add, sub, mul, trudiv
import operator
from operator import add, sub, mul, truediv
print(add(5, 2))
print(truediv(3,4))
print(pow(2, 3))  # Also available in math library

# like C++, Python library consist of ceil, floor, round
# ceil = get next integer to the passed decimal value
# floor = get prior integer to the passed decimal value
# round
print(round(4.7))
print(round(4.4))
print(round(4.66687, 3)) # Can round the decimal to desired decimal places
print(min(8, 4, 5, 1))
print(max(8, 4, 5, 1))
print("\n")

opening() # Strings
# Strings surrounded by either single or double quotation marks are the same
print(f"\"Hello\" is the same as \'Hello\'.")

# Assigning a variable followed by an equal and the string
a = "hello"
print(a)

# Multiline string to a variable using three quotes -> """
a_ = """In C++ to get more words insted of using std::cin,
use getline(std::cin, a), and it will print out the whole sentence."""
print(a_)

# Like C++, strings in Python are also an arrays of bytes representing the unicode characters
# Python does not have a char data type, a single char is simply a string with a length of 1
# Square bracket can be used to access elements of the string

a__ = "Hello, There!"
print(a__[0])

# Strings are arrays, can loop through the characters in a string with for loop
for x in "Hello":
    print(x)
    
# In C++ get the length with "length()", and in Python its "len()"
print(len(a__))

# Checking certain phrase or char prsent in a string, use keyword "in"
print("whole" in a_)

# If statement
if "!" in a__:
    print("'!' is present.")
    
# "not" for phrase or char that does not appear in string
print("whole" not in a__)

# If statement for "not"
if "whole" not in a__:
    print("'whole' is NOT present.\n")

opening() # String methods
b_ = "c++ string methods does have similarities with Python ones."
print(f".capitalize() converts the first char to upper case, for example \"{b_.capitalize()}\". .upper() converts the original string to an uppercase string. For example, \"{b_.upper()}\"\n")

upper_b = b_.upper()
print(upper_b)
print(f".casefold() convert strings into lower case, for example \"{upper_b.casefold()}\"\n")
print(f".lower() also work in a similar way, for example \"{upper_b.lower()}\"\n")

a = {"Hello", "there", "Nikki"}
string = " ".join(a)
print(f".join() converts the elements into a string, for example, \"{string}\".\n")

b = "   something   "
print(f".lstrip() returns a removed spaces left side of the string, for example, \"{b.lstrip()}\".\n The rstrip() will returns a removed right spaces of the string, for example, \"{b.rstrip()}\".\n")

c = "Hello there Nikki"
print(f".replace() in C++ is similar to python. It returns a string where a specified value is replaced with a specified value. For example, \"Hello\" will be replaced with \"Hi\", ({c}) to ({c.replace("Hello", "Hi")}).")