# Your solution to Exercise 15

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Initialize output variable
output = ""

# Check for leap year
is_leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# February and leap year logic
if month == 2:
    if is_leap_year and day == 29:
        day = 1
        month = 3
    elif not is_leap_year and day == 28:
        day = 1
        month = 3
    elif day < 28 or (is_leap_year and day < 29):
        day += 1
    else:
        output = "Invalid date"

# Months with 31 days
elif month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10:
    if day == 31:
        day = 1
        month += 1
    elif day < 31:
        day += 1
    else:
        output = "Invalid date"

# December to January transition
elif month == 12:
    if day == 31:
        day = 1
        month = 1
        year += 1
    elif day < 31:
        day += 1
    else:
        output = "Invalid date"

# Months with 30 days
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        day = 1
        month += 1
    elif day < 30:
        day += 1
    else:
        output = "Invalid date"

else:
    output = "Invalid date"

# Prepare the output message if the date is valid
if output == "":
    output = f"{day}.{month}.{year}"

# Output the next day's date, if valid
print(output)
            if a == 30:
                a = 1
                b += 1
            else: 
                a += 1
else:
    if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
        if a == 31:
            a = 1
            b += 1
        else:
            a += 1
    elif b == 2:
        if a == 28:
            a = 1
            b += 1
        else:
            a += 1
    else:
        if a == 30:
            a = 1
            b += 1
        else: 
            a += 1
if b == 13:
    b = 1
print(f"{a:02d}.{b:02d}.{c:04d}")
