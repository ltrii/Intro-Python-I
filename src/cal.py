# """
# The Python standard library's 'calendar' module allows you to 
# render a calendar to your terminal.
# https://docs.python.org/3.6/library/calendar.html

# Write a program that accepts user input of the form
#   `calendar.py month [year]`
# and does the following:
#  - If the user doesn't specify any input, your program should 
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.
#  - If the user specifies one argument, assume they passed in a
#    month and render the calendar for that month of the current year.
#  - If the user specifies two arguments, assume they passed in
#    both the month and the year. Render the calendar for that 
#    month and year.
#  - Otherwise, print a usage statement to the terminal indicating
#    the format that your program expects arguments to be given.
#    Then exit the program.
# """
import sys
import calendar
from datetime import datetime

dt = datetime.today()

if len(sys.argv) == 3:
  month = str(sys.argv[1])
  year = str(sys.argv[2])
elif len(sys.argv) == 2:
  month = str(sys.argv[1])
  year = dt.year
elif len(sys.argv) == 1:
  month = dt.month
  year = dt.year

month = int(month)
year = int(year)

if month & year == None:
  print("Please provide at least one argument (month, year).")

if year == None:
  year = datetime.date.today().strftime("%Y")

if month == None:
  month = datetime.date.today().strftime("%B")

if month > 12 & month < 1:
  print("Month provided is outside of range (1-12)")

month = int(month)
year = int(year)

cal = calendar.TextCalendar(firstweekday=6)
curCal = cal.formatmonth(year, month)
print(curCal)

