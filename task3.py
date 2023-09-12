import datetime as dt

current_date = dt.datetime.now()
add_5 = current_date + dt.timedelta(seconds=5)


print("Current time:", current_date)
print("After adding 5 seconds:", add_5)