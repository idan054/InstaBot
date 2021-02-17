from datetime import datetime

# current date and time
now = datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"))

# from datetime to timestamp float
myTimestamp = datetime.timestamp(now)
print(type(myTimestamp))
print(myTimestamp)

# from timestamp float to datetime
myDatetime = datetime.fromtimestamp(myTimestamp)
print(type(myDatetime))
print(myDatetime)