# pythonStudies
Here you will find all stud notes for python language
It will include:
- Notes
- Practice code


# Books used:
- Fluent Python, 2nd Edition (Luciano Ramalho)
- Python Crash Course, 3rd Edition (Eric Matthes)
- Python Workout (Reuven M. Lerner)


## Note:

# chapt 1:
naming and variables:
-Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable message_1 but not 1_message.
- Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, greeting_message works but greeting message will cause errors.
- Avoid using Python keywords and function names as variable names. For example, do not use the word print as a variable name;
- Variable names should be short but descriptive.
- Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

running into error:
- A traceback is a record of where the interpreter ran into trouble when trying to execute your code.

Strings:
A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings
example
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

Changing case:
You typically won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them. 
name.title()
name.upper()
name.lower()



# chapt 2:
Using variables in string:
These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

Adding Whitespace to Strings with Tabs or Newlines:
You can use whitespace to organize your output so it’s easier for users to read.
>>>print("Languages:\nPython\nC\nJavaScript")
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript

Stripping whitespace:
To programmers, 'python' and 'python ' look pretty much the same. But to a program, they are two different strings. 
But to a program, they are two different strings. For right side of a string, use the rstrip(). It is only removed temporarily

Temporary:
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '

Permenant:
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'

You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'

Removing Prefixes:
When working with strings, another common task is to remove a prefix. Consider a URL with the common prefix https://. We want to remove this prefix, so we can focus on just the part of the URL that users need to enter into an address bar. Here’s how to do that:
>>> nostarch_url = 'https://nostarch.com'
>>> nostarch_url.removeprefix('https://')
'nostarch.com'


Numbers:
float, integer

Multiple Assignment:
>>> x, y, z = 0, 0, 0
You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its respective variable. As long as the number of values matches the number of variables, Python will match them up correctly.

Constants:
all capital letters to indicate a variable should be treated as a constant and never be changed
MAX_CONNECTIONS = 5000


# chapt 3:

