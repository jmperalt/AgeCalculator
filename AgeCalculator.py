# import the date class from the datetime module
from datetime import date

# define a function to calculate age given a birth date
def calculate_age(birth_date):
    # get the current date
    today = date.today()
    # calculate the age based on the year, month, and day of the birth date
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    # return the calculated age
    return age

# prompt the user to enter their birth year, month, and day
while True:
    try:
        # use input() to get the year, month, and day as strings and convert them to integers using int()
        year = int(input("Enter your birth year: "))
        # validate that the year is not negative
        if year < 0:
            raise ValueError("Invalid year. Please enter a positive integer.")
        month = int(input("Enter your birth month: "))
        # validate that the month is between 1 and 12
        if month < 1 or month > 12:
            raise ValueError("Invalid month. Please enter an integer between 1 and 12.")
        day = int(input("Enter your birth day: "))
        # validate that the day is between 1 and 31 (the maximum number of days in a month)
        if day < 1 or day > 31:
            raise ValueError("Invalid day. Please enter an integer between 1 and 31.")

        # create a date object from the year, month, and day using the date() constructor
        birthdate = date(year, month, day)
        # break out of the loop if all inputs are valid
        break
    except ValueError:
        # if a ValueError occurs (e.g., if the user enters a non-integer value), print an error message and continue the loop
        print("Invalid input. Please enter a valid integer.")

# calculate the age using the calculate_age() function and print the result
age = calculate_age(birthdate)
print(f"You are {age} years old")

