# Import libraries
from datetime import date

# Today's date
today = date.today()
print(f"Today: {today.strftime('%A %d, %b %Y')}")

# Get user input
dob_str = input("What is your date of birth? [dd/mm/yyyy]: ")

# Convert user input into a date
dob_data = dob_str.split('/')
dob_day = int(dob_data[0])
dob_month = int(dob_data[1])
dob_year = int(dob_data[2])
dob = date(dob_year, dob_month, dob_day)

# Calculate number of days lived
number_of_days = (today - dob).days

# Convert this into whole years to display the age
age = number_of_days // 365
print(f"You are {age} years old.")

# Retrieve the day of the week (Monday to Sunday) corresponding to the date of birth
day = dob.strftime('%A')
print(f"You were born on a {day}.")

# Print number of days lived
print(f"You have spent {number_of_days} days on Earth.")

# Calculate number of days until next birthday
this_year = today.year
next_birthday = date(this_year, dob_month, dob_day)
if today < next_birthday:
    days_left = (next_birthday - today).days
    print(f"Your birhday is in {days_left} days.")
elif today == next_birthday:
    print("Today is your birthday! Happy Birthday!")
else:
    next_birthday = date(this_year + 1, dob_month, dob_day)
    days_left = (next_birthday - today).days
    print(f"Your birthday is in {days_left} days.")
