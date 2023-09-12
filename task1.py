import datetime as dt

current_date = dt.datetime.now()
print("Current date and time:", current_date)
print("Current year:", current_date.year)
print("Month of year:", current_date.month)
print("Week number of the year:", current_date.strftime("%W"))
print("Weekday of the week:", current_date.strftime("%A"))
print("Day of year:", current_date.strftime("%j"))
print("Day of the month :", current_date.day)
print("Day of week:", current_date.strftime("%w"))