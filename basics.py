print(my_var:="Hello, World!")
print (my_var)

# Concatenation
print ('allice' + 'bob') #allicebob
print ('allice' + ' ' + 'bob') #allice bob
print('alice'*5) #alicealicealicealicealice
print ('allice' 'bob')  #allicebob
# Comments:

# This is a single line comment

""" This is a docstring """ 

#The End Keyowrd; 
#The end keyword is used to print the output in the same line. Like \n in C, the end in Python is used to print the output in the same line. The default value of end is \n.
phrase = ['printed', 'with', 'a', 'dash']
for word in phrase: 
    print(word, end = '-')

#The Sep Keyword: 

print('deepak', 'shivam', 'rohit', 'yash', sep = ' ,')

"""
we are using sep = ' , ' to separate the words with a comma and space.

Output: deepak ,shivam ,rohit ,yash

"""

#The Input Function:

"""
The input() function is used to take input from the user. 
The input() function reads the input from the user as a string. 
If you want to take an integer input, you can typecast the input to an integer using the int() function.

"""
print('What is your name ?')
my_name = input()
print('My name is ' + my_name)

#Then why use .format() method? 

"""

The .format() method is used to format the string.

Why to format when we can clearly do it with the + operator?



"""

#How to convert types in Python?

"""
There are several ways to convert types in Python.
str() – converts any type into a string 
int() – converts a string into an integer
float() – converts a string into a float
"""