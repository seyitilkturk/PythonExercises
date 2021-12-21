"""

Write a Python program to calculate number of days between two dates.

"""


from datetime import date


first_date = date(2014, 7, 2)
last_date = date(2015, 7, 2)
delta = first_date - last_date

print(abs(delta.days))

