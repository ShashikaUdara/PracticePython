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