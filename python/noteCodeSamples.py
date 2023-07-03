# Python study practice code
# Hamid S.
############################


# variable name
message = "Hello Python Crash Course reader!"
print(message)

# this gives error cuz of spelling
''' message = "Hello Python Crash Course reader!"
print(mesage) '''

# changing case in string with methods. The dot tells title() to act on variable name
name = "ada lovelace"
print(name.title())

# change case to uppercase or lowercase
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# using variables in strings
# These strings are called f-strings. The f is for format, 
# because Python formats the string by replacing the name of any variable in braces with its value.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# You can also use f-strings to compose a message, and then assign the entire message to a variable:
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# You can use whitespace to organize your output so it’s easier for users to read.
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitespaces
# To programmers, 'python' and 'python ' look pretty much the same. 
# But to a program, they are two different strings. For right side of a string, use the rstrip(). 
# It is only removed temporarily
favorite_language = 'python '
favorite_language
#'python '
favorite_language.rstrip()
#'python'
favorite_language
#'python '

# To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language
#'python'

# You can also strip whitespace from the left side of a string using the lstrip() method, 
# or from both sides at once using strip():
favorite_language = ' python '
favorite_language.rstrip()
#' python'
favorite_language.lstrip()
#'python '
favorite_language.strip()
#'python'

# Removing Prefixes
# When working with strings, another common task is to remove a prefix. Consider a URL with the common prefix https://. 
# We want to remove this prefix, so we can focus on just the part of the URL that users need to enter into an address bar
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
#'nostarch.com'
# Keep it permenantly 
simple_url = nostarch_url.removeprefix('https://')

# Numbers 
# Integers: You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.
2 + 3
#5
3 - 2
#1
3 ** 2
#9
# Python supports the order of operations too
2 + 3*4
#14
(2 + 3) * 4
#20

# Floats
# Python calls any number with a decimal point a float. 
0.1 + 0.1
#0.2
0.2 + 0.2
#0.4

# Python defaults to a float in any operation that uses a float, even if the output is a whole number.
# HOWEVER, be aware that you can sometimes get an arbitrary number of decimal places in your answer:
0.2 + 0.1
#0.30000000000000004
3 * 0.1
#0.30000000000000004

# Underscores in Numbers
# When you’re writing long numbers, you can group digits using underscores to make large numbers more readable:
universe_age = 14_000_000_000
print(universe_age)
#14000000000

# Multiple Assignment
# You can assign values to more than one variable using just a single line of code. 
x, y, z = 0, 0, 0

# Constants
# A constant is a variable whose value stays the same throughout the life of a program. 
# Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed
MAX_CONNECTIONS = 5000

# Comments
# Say hello to everyone.
print("Hello Python people!")

List
Tuple
Dictionary
