from datetime import * # Importing libraries. 

# Today's Date.
today = date.today()
print("Today: " +  today.strftime('%A %d, %b %Y'))

dobStr = input("What is your Date of Birth? dd/mm/yyyy ")

# Convert user input into a date.
dobData = dobStr.split("/")
dobDay = int(dobData[0])
dobMonth = int(dobData[1])
dobYear = int(dobData[2])
dob = date(dobYear,dobMonth,dobDay)

# Calculate number of days lived.
numberOfDays = (today - dob).days 

# Convert this into whole years to display the age.
age = numberOfDays // 365
print("You are " + str(age) + " years old.")

# Retrieve the day of the week (Monday to Sunday) corresponding to the date of birth.
day = dob.strftime("%A")
print("You were born on a " + day + ".")

print("You have spent " + str(numberOfDays) + " days on Earth.")

# Calculating the number of days until next birthday.
thisYear = today.year

nextBirthday = date(thisYear,dobMonth,dobDay)
if today<nextBirthday:
  gap = (nextBirthday - today).days
  print("Your birhday is in " + str(gap) + " days.")
elif  today == nextBirthday:
  print("Today is your birthday! Happy Birthday!")
else:
  nextBirthday = date(thisYear+1,dobMonth,dobDay)
  daysLeft = (nextBirthday - today).days
  print("Your birthday is in " + str(daysLeft) + " days.")