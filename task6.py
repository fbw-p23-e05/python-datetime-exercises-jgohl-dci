import datetime as dt

current_date = dt.datetime.now()

result = dt.timedelta(days=int(current_date.strftime("%w")) - 1)

result2 = current_date - result
print("The first Monday of this week was:", result2.strftime("%Y-%m-%d"))