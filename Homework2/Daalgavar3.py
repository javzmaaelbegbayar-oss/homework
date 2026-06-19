import datetime as dt
date=dt.datetime.strptime("2024/12/15", "%Y/%m/%d")
print(date)
date_timestamp=dt.datetime.timestamp(date)
newdate=dt.datetime.fromtimestamp(date_timestamp+7*24*60*60)
print(newdate)
newdate_1=newdate.strftime("%B %d, %Y")
print(newdate_1)
