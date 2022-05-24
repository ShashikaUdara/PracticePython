'''
    this is a multi-line comment
'''

# from sqlalchemy import false, true


import calendar
from pickle import FALSE, TRUE
from re import L
import time
import test_module
from Phone import directory



print("it's init")

# variable types
first_name = "Udara"
last_name = "Abeyrathne"
email = "udaraabeyrathne2000@gmail.com"
age = 31
is_married = FALSE
height_in_cm = 178.5

print("My name is", first_name, last_name,". I'm 31 years old and", "Married" if is_married == TRUE else "Single", ". I'm", height_in_cm, " cm tall. My mail address is", email)

# deleting variables (objects) re possible in python
del first_name, last_name, email, age, is_married, height_in_cm
# after deleting variables following line will give error
# print("My name is", first_name, last_name,". I'm 31 years old and", "Married" if is_married == true else "Single", ". I'm", height_in_cm, " cm tall. My mail address is", email)

# python strings can be included inside single quatations or inside double quotations
str_1 = 'Udara Abeyrathne'
print(str_1) # prints entire string (Udara Abeyrathne)
print(str_1[0]) # prints first letter of the string (U)
print(str_1[6:17]) # prints starting from 7th letter onwards up to 10 characters (Abeyrathne)
print(str_1[1:]) # prints starting from 2nd charater upto end of the sting (dara Abeyrathne)
print(str_1 * 2) # prints string two times (Udara AbeyrathneUdara Abeyrathne)
print(str_1 + " Is My Name") # concatinate "Is My Name" to the end of the string (Udara Abeyrathne Is My name)

# python lists
# not like any other language python lists can have multiple data type in its values
my_list = ['Udara', 31, 178.5, "Udara Abeyrahtne"]
temp_list = ['University of Mora', 'Sumangala college Kandy']

print(my_list) # full list
print(my_list[0]) # first element
print(my_list[0:2]) # first 2 elements from first element
print(my_list[1]) # print second element
print(my_list * 2) # print list two times
print(my_list + temp_list) # aff temp_list to the my_list
print(my_list[0][2:5]) # print fist elements 3rd charater onwards up to 5 characters (ara)

# python tuples
# the only difference between tuples and lists is tuples are read-only list. once tuples are enclosed using parentheses
# they can not be modifies in the run time, but list can

# defining the tuple
my_tuple = ('Udara', 31, 178.5, "Udara Abeyrahtne")
temp_tuple = ('University of Mora', 'Sumangala college Kandy')
print(my_tuple) # full tuple
print(my_tuple[0]) # first element
print(my_tuple[0:2]) # first 2 elements from first element
print(my_tuple[1]) # print second element
print(my_tuple * 2) # print tuple two times
print(my_tuple + temp_tuple) # aff temp_tuple to the my_tuple
print(my_tuple[0][2:5]) # print fist elements 3rd charater onwards up to 5 characters (ara)

my_list[3] = "Apple" # valied
print(my_list) # full list
# my_tuple[3] = "Apple" # invalied
# print(my_tuple) # full tuple

# python dictionaries key-value pair enclosed with {} and access with []
_dict = {} # defining empty dictionary
# adding values
_dict['one'] = 'this is one'
_dict['two'] = 'this is two'
_dict['ten'] = 'this is ten'
print(_dict) # prints entire dictionary
print(_dict.keys()) # prints only keys
print(_dict.values()) # print only the values
print(_dict.get('one')) # getting the value of 'one' key

# multiple variable assignment
num_1 = num_2 = num_3 = 12
print(num_1, num_2, num_3)

num_4, str_2, b_status_1, b_status_2 = 15, "Udara Abeyrathne", TRUE, FALSE
print(num_4, str_2, b_status_1, b_status_2)

# data type conversions
test_int = 16
test_float = 24.567
test_string = "1234"
test_string_float = "123.456"
test_string_chars = "Udara Abeyrathne"
test_tuple = ('Udara', 12345, TRUE, 12.2356, "my name is abeyrathne")
test_list = ['Udara', 12345, TRUE, 12.2356, "my name is abeyrathne"]
test_set = {'Udara', 12345, TRUE, 12.2356, "my name is abeyrathne"}

print(type(test_int))
print(type(test_float))
print(type(test_string))

# converting int to string
new_string = str(test_int)
print("int converted to string:", new_string, type(new_string))

# converting float to string
new_string = str(test_float)
print("float converted to string:", new_string, type(new_string))

# converting to integer
new_int = int(test_string)
print("string converted to int:", new_int, type(new_int))

new_int = int(test_float)
print("float converted to int:", new_int, type(new_int))

# converting to float
new_float = float(test_string_float)
print("string converted to float:", new_float, type(new_float))

new_float = float(test_int)
print("int converted to float:", new_float, type(new_float))

# float type number string to integer
new_int = int(float(test_string_float))
print("float type number string converted to int:", new_int, type(new_int))

# string to tuple
new_tuple = tuple(test_string_chars)
print("string converted to tuple:", new_tuple, type(new_tuple))

# list to tuple
new_tuple = tuple(test_list)
print("list converted to tuple:", new_tuple, type(new_tuple))

# int to tuple
new_tuple = tuple(str(test_int))
print("int converted to tuple:", new_tuple, type(new_tuple))

# float to tuple
new_tuple = tuple(str(test_float))
print("float converted to tuple:", new_tuple, type(new_tuple))

# string to list
new_list = list(test_string_chars)
print("string converted to list:", new_list, type(new_list))

# tuple to list
new_list = list(test_tuple)
print("tuple converted to list:", new_list, type(new_list))

# int to list
new_list = list(str(test_int))
print("int converted to list:", new_list, type(new_list))

# float to list
new_list = list(str(test_float))
print("float converted to list:", new_list, type(new_list))

# set to list
new_list = list(test_set)
print("set converted to list:", new_list, type(new_list))

# list to set
new_set = set(test_list)
print("list converted to set", new_set, type(new_set))

# tuple to set
new_set = set(test_tuple)
print("tuple converted to set", new_set, type(new_set))

# list to set
new_set = set(test_list)
print("list converted to set", new_set, type(new_set))

# string to set
new_set = set(test_string_chars)
print("string converted to set", new_set, type(new_set))

# basic arithmatic operations
_a = 5
_b = 4
print("_a + _b  = ", _a + _b)
print("_a - _b  = ", _a - _b)
print("_a / _b  = ", _a / _b)
print("_a * _b  = ", _a * _b)
print("_a % _b  = ", _a % _b)
print("_a ** _b = ", _a **_b)

# user input
# _name = input("Enter you name: ")
_name = "Udara" # hard coded for the easyness
set_vowel = {'a', 'e', 'i', 'o', 'u'}
if _name[0].lower() in set_vowel:
    print("Your name starts with a vowel")
else:
    print("Your name is not starting with a vowel")

# for with range
for x in range(10):
    if x == 0:
        print("passing if the iterater equels to 0")
        pass
    elif x == 5 or x == 7:
        print("continue the iteration if 5 or 7")
    elif x == 9:
        print("braking from the loop")
        break
    else:
        print("counting:",x)

# for with list/set or a tuple
for x in test_list:
    print("list item: ", x)

for x in test_set:
    print("set item: ", x)

for x in test_tuple:
    print("tuple item: ", x)

# printing stars :P
stars = ""
levels = 50
for i in range(levels):
    for j in range(levels-i):
        stars += " "
    for k in range(2*i+1):
        stars += "*"
    print(stars)
    stars = ""

# while loops
count = levels
stars = ""
while(count > 0):
    for j in range(levels-count):
        stars += " "
    for k in range(2*count+1):
        stars += "+"
    print(stars)
    stars = ""
    count -= 1
# String Formatting Operator
print("My name is %s and I have %d cars" % (test_string_chars, test_int))

# Triple Quotes
triple_qoted_str = """When the above code is executed, it produces the following 
result. Note how every single special character has been 
converted to its printed form, right down to the last NEWLINE 
at the end of the string between the "up." and closing triple 
quotes. Also note that NEWLINEs occur either with an explicit 
carriage return at the end of a line or its escape code"""
print("The message is: %s" % (triple_qoted_str))

# Raw strings
normal_string = "This is double backslash C\\my_folder"
row_string = r"This is double backslash C\\my_folder"
print("%s" % (normal_string)) # without 'r' expression
print("%s" % (row_string)) # with 'r' expression

# python date and time
ticks = time.time()
print("Number of ticks since 12:00AM, January 1st, 1970:", ticks)

# getting local time
local_time = time.localtime(time.time())
print("local time is:", local_time)

# getting formatted local time
local_time = time.asctime(time.localtime(time.time()))
print("formatted local time is:", local_time)

# Getting calendar for a month
_calender = calendar.month(2022, 5)
print("Calender May 2022")
print(_calender)

# Python time clock() Method
# This is the function to use for benchmarking Python or timing algorithms

# defining a function to monitor the time consumption
def operation():
    time.sleep(2.5)

# t_0s = time.clock()
# operation()
# print("Time cunsumption of the operation (Seconds process time) : ", time.clock())

t_0s = time.time()
operation()
t_ends = time.time()
print("Time cunsumption of the operation (Seconds wall time) : ", t_ends - t_0s)

# python functions
''' 
In python you are passing paramiters by reference, which means that is you 
chage a passed value inside of the function, it will reflects all the calling functions as well.
'''

def display_string(my_name_temp, my_address_temp):
    my_name_temp += " Shashika" # here my_name_temp act as a local variable, hence the changes will not be affected to the caling function
    my_address_temp += "A"
    print(my_name_temp)
    print(my_address_temp)

my_name = "Udara Abeyrathne"
my_address = "Kandy"
display_string(my_name, my_address)
print("My name is: ", my_name)
print("My address is: ", my_address)

def display_list(my_list):
    my_list.extend([2, 3, 4])
    print(my_list)

test_list_2 = [5, 6, 7]
display_list(test_list_2)
print(test_list_2)

# Required arguments
# Required arguments are the arguments passed to a function in correct positional order.

# Keyword arguments
# Keyword arguments are related to the function calls. 
# When you use keyword arguments in a function call, the caller 
# identifies the arguments by the parameter name.
# simply you can skip the arguments

def keyword_function_1(string_test_3):
    print(string_test_3)

keyword_function_1(string_test_3 = "Udara Abeyrathne")

def keyword_function_2(_address, _name, _age = 28):
    print(_address)
    print(_age)
    print(_name)

#  calling the function without considering the paramiter order
keyword_function_2(_age = 31, _name = "Udara Abeyrathne", _address = "Kandy, Sri Lanka")
keyword_function_2( _name = "Anonymous", _address = "USA")

# Variable-length arguments
'''
You may need to process a function for more arguments than you specified 
while defining the function. These arguments are called variable-length 
arguments and are not named in the function definition, unlike required 
and default arguments.
'''

def variable_length_args(arg1, *vartuple):
    print("+++++++++++++++++++++++++++++")
    print(arg1)
    for i in vartuple:
        print(i)
    print("+++++++++++++++++++++++++++++")
    return

variable_length_args(11)
variable_length_args("Udara", 89, 12)
variable_length_args(234, "Apple", "Bee", TRUE, 987)

# The Anonymous Functions
'''
These functions are called anonymous because they are not 
declared in the standard manner by using the def keyword. 
You can use the lambda keyword to create small anonymous functions.

Such function can take many arguments but return only one value
Can't have multiple expressions
Cannot be direct call to print
have their local namespace
not inline functions
'''
sum = lambda num_1, num_2: num_1 + num_2;

print("sum(11,22):", sum(11,22))
print("sum(80,97):", sum(80,97))

# modules
test_module.simple_function(15, "This is a seperated module")

# Packages in Python
directory.my_phone_number() 

# python exception handling
# Assertions in Python

def power_of_two(num_val):
    assert(num_val >= 0), "Number is lesser that 0"
    return num_val ** 2

print(power_of_two(25))
print(power_of_two(0))
print(power_of_two(-5))