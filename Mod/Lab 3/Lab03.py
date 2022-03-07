# 1. Name:
#      Ben Painter
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      The program is suppose to ask the user for a month and year and
#       and then display the calendar for that month.
# 4. What was the hardest part? Be as specific as possible.
#      I won't lie, this program went really smoothly. With the structure chart and
#       the display function already made for us, there wasn't too many problems. Even
#       calculating the offset went really smoothly this time. 
# 5. How long did it take for you to complete the assignment?
#      2 hours

def get_year():
    # Gets the year from the User and checks to make sure if the year is valid. 
    year_valid = False
    while(year_valid != True):

        try:
            year = int(input("Enter year: "))
            if year >= 1753:
                year_valid = True
                return year
            else:
                print("Please enter a year pass 1752")
        except:
            print("Please input a number")

def get_month():
    # Gets the month from the User and checks to make sure if the month is valid. 
    month_valid = False
    while(month_valid != True):

        try:
            month = int(input("Enter the month number: "))
            if month >= 1 and month <= 12:
                month_valid = True
                return month
            else:
                print("Please enter a valid month")
        except:
            print("Please input a number")
        
def compute_offset(year, month):
    # Calculates the offset by adding up all of the days from 1753 to the month the user inputs.
    num_days = 0
    for i_year in range (1753, year):
        if leap_year(i_year):
            num_days = num_days + 366
        else: 
            num_days = num_days + 365
    for i_month in range (1, month):
        num_days = num_days + num_month(i_month, year)

    return (num_days + 1) % 7

def num_month(month, year):
    # Returns how many days are in the month
    if month == 4 or month == 6 or month == 9 or month == 11:
        num_day = 30
    elif month == 2:
        if leap_year(year):
            num_day = 29
        else:
            num_day = 28
    else:
        num_day = 31

    return num_day


def leap_year(year):
    # Returns True or False whether it is a leap year
    isLeap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeap = True
            else:
                isLeap = False
        else:
            isLeap = True
    else:
        isLeap = False

    return isLeap


def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline



def main():
   
    month = get_month()
    year = get_year()

    offset = compute_offset(year, month)
    display_table(offset, num_month(month, year))

main()


