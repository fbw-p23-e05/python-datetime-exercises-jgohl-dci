import datetime as dt

current_date = dt.datetime.now()

print("Today:", current_date)
print("Day of year:", current_date.strftime("%j"))
