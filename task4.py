import datetime as dt

current_date = dt.datetime.now()

print("Today:", current_date)
print("Next 5 days:")

for i in range(5):
    plus_1 = current_date + dt.timedelta(days=i+1)
    print(plus_1)