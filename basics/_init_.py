'''
    this is a multi-line comment
'''

from curses import raw
from matplotlib.cbook import is_math_text

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