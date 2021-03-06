'''
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
'''

import sys
from calendar import TextCalendar
from datetime import datetime

cal = TextCalendar()
today = datetime.now()

def createCalendar(month = today.month, year = today.year):
  return cal.formatmonth(year, month)

try:
  dates = map(int, sys.argv[1:])
  calendar = createCalendar(*dates)
  print('\n=====================\n')
  print(calendar)
  print('=====================\n')
except ValueError:
  print('\nYour supplied argument(s) could not be parsed as integers.')
  print('This should be used as:') 
  print('cal.py 4 2019')
  print('4 being the month, 1-12, and 2019 being the year; negative values are B.C.\n')
except IndexError:
  print("Your supplied month doesn't seem to be 1-12. Please don't use larger or smaller numbers.")
