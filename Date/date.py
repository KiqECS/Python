import datetime

data_today = datetime.datetime.now()
data_nasc = datetime.datetime(2002,9,24)

days_of_life = data_today - data_nasc

print(days_of_life)