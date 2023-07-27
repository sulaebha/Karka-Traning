# date time is the package and
#  date is the class from the datetime package
# today() is the funtion from date



from datetime import date

curr_date=date.today()     #date change dynamicaly
# curr_date=date(2023,7,25)     

# curr_date=date.today().year     #print the year of current date
# curr_date=date.today().month      #print the month of current date
# curr_date=date.today().day     #print the day of current date


print(curr_date)



from datetime import time
curr_time=time(1,23,44)
# curr_time=time(1,23,44).hour
# curr_time=time(1,23,44).minute
#curr_time=time(1,23,44) .second
print(curr_time)

from datetime import datetime
# curr_date_time=datetime(2023,7,25,1,23,44)
curr_date_time=datetime.now()

# curr_date=datetime.today().year
# print(curr_date)

print(curr_date_time)
print(curr_date_time.strftime("%D"))

from datetime import datetime
import pytz
# get the standard UTC time
UTC=pytz.utc
IST = pytz.timezone('Asia/Kolkata')
# print(IST)

print("UTC in Default Format : ", 
      datetime.now(UTC))
  
print("IST in Default Format : ", 
      datetime.now(IST))

# print the date and time in 
# specified format
datetime_utc = datetime.now(UTC)
print("Date & Time in UTC : ",
      datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
  
datetime_ist = datetime.now(IST)
print("Date & Time in IST : ", 
      datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))








date_str="24 december 2023"
print(type(date_str))
b=datetime.strptime(date_str,"%d %B %Y")
print(b)
print(type(b))



from datetime import timedelta

date_str="24 december 2023"

b=datetime.strptime(date_str,"%d %B %Y")

end_date=b+timedelta(days=5)
print(end_date)