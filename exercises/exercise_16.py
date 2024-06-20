
def get_previous_date(day, month, year):
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    days_in_month[1] = 29
  if day == 1:
    if month == 1:
      month = 12
      year -= 1
      day = days_in_month[month - 1]
    else:
      month -= 1
      day = days_in_month[month - 1]
  else:
    day -= 1
  return day, month, year
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
previous_day, previous_month, previous_year = get_previous_date(day, month, year)

print(f"{previous_day:02}.{previous_month:02}.{previous_year}")
