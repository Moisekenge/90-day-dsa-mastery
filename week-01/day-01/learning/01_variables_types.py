"""
Day 1 - Section 1: Variables and Types
Practice: Create variables of each type, convert between types, use type().
"""

# --- Integers ---
# TODO: Create integer variables, practice arithmetic
x = 10
y = -5
z = 0 

print(x, y, z)    # 10 -3 0 
print(type(x))    # <class 'int'>

# arithmetic with integers 
print(x + y)    # 7 addition 
print(x - y)    # 13 subtraction
print(x * y)    # -3- multiplication
print(x ** 2)   # 100 power 
print(x // y)   # -2 modulor(remainder)

#key distinction: 
print(x / y)    #  -3.333 regular division always returns float 
print(x // y)   # -4 floor division returns int 


# --- Floats ---
# TODO: Create float variables, practice float division vs integer division
a = 3.14 
b = -0.5 
c = 2.0      # still a float even though its a whole number 

print (a, b, c)
print(type(a))  # <class 'float'>

#warning: floating point precision
print(0.1 + 0.2)          #0.30000000000000004 (NOT 0.3) 
print(0.1 + 0.2 == 0.3)  # False( this WILL bite you)

# How to handle it: 
print(round(0.1 + 0.2, 1) == 0.3) # True 
print(abs(0.1 + 0.2 - 0.3) < 1e-9) # True (epsilon comparison)

#useful functions 
print(abs(-3.7))  # 3.7 absolute 
print(round(3.14159, 2)) # 3.14 

# infinity 
print(float('inf')) # inf - you'll use this in DSA for comparisons 
print(float('-inf')) # -inf
print(float('inf') > 999999999) # True

# --- Strings ---
# TODO: Create strings, practice f-strings, string methods
name = "Moise"
greeting = 'Hello'  # single or double quotes work for strings 
multiline = """This is a multiline string"""
print(type(name)) # <class 'str'>

#Strings are IMMUTABLE - you can change them in place 
#name[0] = 'm' <- this would crash, you have to create a new string instead

#f-string (your best friend for formatting)
age = 22 

print(f"My name is {name} and I am {age} years old.")
print(f"Next year I'll be {age + 1}")  # expressions inside {}
print(f"Pi is {3.14159:2f}")  # format to 2 decimials -> 3.14

#string methods (these return New Strings, original unchanged)
msg = " Hello, World!"

print(msg.upper())   # " HELLO, WORLD!"
print(msg.lower())  # " hello, world"
print(msg.strip())  # "Hello, world!"
print(msg.replace("World", "Python")) # " Hello, Python!"
print(msg.split())   # ['Hello,', 'World!'] - split into list 

# indexing and slicing 
word = "Python"
print(word[0])    # 'P' - first character
print(word[-1])  # 'n' - last character
print(word[0:3]) # 'Pyt' - slice from index 0 to 2
print(word[::-1]) # 'nohtyP' - reverse string


# useful check 
print("Py" in "Python")  # True - membership check 
print(word.startswith("Py")) # True 
print(word.endswith("on")) # True 
print("123".isdigit())     #True
print("abc".isalpha())    # True

#length 
print(len(word)) # 6

#concanatenation
print("Hello" + "" "World") # Hellow World 

# ord and chr - character to number and back 
print(ord('a')) #97 
print(ord('A')) # 65 
print(chr(97)) # a
# this is useful for leetcode problems involving characters and their positions in the alphabet

# --- Booleans ---
# TODO: Practice truthy/falsy values
# What evaluates to False? 0, 0.0, "", None, [], {}, set(), False

# Boooleans
is_active  = True 
is_deleted = False 

print(type(is_active))   # <class 'bool'>

#Boolean are integers: True == 1, False == 0 
print(True + True)  # 2
print(True * 10) # 10
print(False + 5) # 5

# Truthy and Falsy values - memorize what evaluates to False: 
#False, 0, 0.0 "", None, {}, set(), ()
#EVERYTHING ELSE is True 
print(bool(0)) # False 
print(bool("")) # False 
print(bool(None)) # False
print(bool([])) # False 
print(bool({})) # False

print(bool(1)) # True
print(bool("hi")) # True
print(bool([1,2])) # True
print(bool(-1)) # True - negative numbers are also truthy !

# Why this matters - you'll write this pattern constantly: 
my_list = []
if not my_list:
    print("List is empty")  # this works because [] is falsy 

#Logical operators
print(True and False) # False
print(True or False)  # True
print(not True)       # False

#Short-circuit evaluation 
# and -> returns first falsy value (or last value if all truthy)
# or -> returns first truthy value (or last value if all falsy)
print(0 and "hello") # 0  (Stopped at first falsy)
print(1 and "hello") # hello (all truthy, returns last)
print(0 or "hello")  # hello (skipped falsy, found truthy)
print("" or "default") # default -- useful for default values ! 

# --- Type Conversion ---
# TODO: int(), float(), str(), bool() conversions

#type conversion 

#string to int/float 
print(int("42")) # 42
print(float("3.14"))
#print(int("abc")) # ValueError - can't convert string float -> int directly 
print(int(float("3.14")))  # 3 -- string -> float -> int works 

#float to int (TRUNCATES, does not round)
print(int(3.9))  # 3 (not 4!)
print(int(-3.9)) # -3 (not -4!) 

#int to string 
print(str(42)) # "42"
print(str(3.14)) # "3.14"

#useful pattern: digit manipulation
num = 12345
digits = str(num) 
print(digits[0])   # '1' - first digit as string
print(len(digits)) # 5 - counts digits 
print(int(digits[::-1])) # 54321 - reverses a number 

#bool conversion 
print(int(True))   # 1 
print(int(False))  # 0
print(str(True))  # "True"

#input() always returns a string - must convert 
#age = int(input("Enter age: ")) # common pattern 



if __name__ == "__main__":
    # Run your experiments here
    pass
