import datetime as dt

year = int(input("Input a year: "))
current_date = dt.datetime(year, 1, 1)

print("Output:")
for i in range(365):
    if current_date.strftime("%w") == "0":
        print(current_date.strftime("%Y-%m-%d"))

    current_date = current_date + dt.timedelta(days=1)