'''
    this is a multi-line comment
'''

from sqlalchemy import false, true


print("it's init")

# variable types
first_name = "Udara"
last_name = "Abeyrathne"
email = "udaraabeyrathne2000@gmail.com"
age = 31
is_married = false
height_in_cm = 178.5

print("My name is", first_name, last_name,". I'm 31 years old and", "Married" if is_married == true else "Single", ". I'm", height_in_cm, " cm tall. My mail address is", email)

# deleting variables (objects) re possible in python
del first_name, last_name, email, age, is_married, height_in_cm
# after deleting variables following line will give error
# print("My name is", first_name, last_name,". I'm 31 years old and", "Married" if is_married == true else "Single", ". I'm", height_in_cm, " cm tall. My mail address is", email)

# python strings can be included inside single quatations or inside double quotations
str = 'Udara Abeyrathne'
print(str) # prints entire string (Udara Abeyrathne)
print(str[0]) # prints first letter of the string (U)
print(str[6:17]) # prints starting from 7th letter onwards up to 10 characters (Abeyrathne)
print(str[1:]) # prints starting from 2nd charater upto end of the sting (dara Abeyrathne)
print(str * 2) # prints string two times (Udara AbeyrathneUdara Abeyrathne)
print(str + " Is My Name") # concatinate "Is My Name" to the end of the string (Udara Abeyrathne Is My name)

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