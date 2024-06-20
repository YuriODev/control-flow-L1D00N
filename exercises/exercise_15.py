# Your solution to Exercise 15
def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
def get_next_date(day, month, year):
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap_year(year):
    days_in_month[1] = 29
  if day == days_in_month[month - 1]:
    day = 1
    if month == 12:
      month = 1
      year += 1
    else:
      month += 1
  else:
    day += 1
  return day, month, year
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
next_day, next_month, next_year = get_next_date(day, month, year)
print(f"{next_day:02}.{next_month:02}.{next_year}")
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
