#python date

import datetime
x = datetime.datetime.now()
print("exact time of now " , x)

#creating date objects
import datetime
x = datetime.datetime(2022,9,27)
print(x)

#return the year and name of weekday
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#return weekday short version
import datetime
x = datetime.datetime.now()
print(x.strftime("%a"))

#print weekday as a number sunday as '0' and monday - 1 so on
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))
# to print day of month 01-31
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))
#to print month name we use %B
import datetime
x = datetime.datetime.now()
print(x.strftime("%B"))

#to print the day  of someday
import datetime
x = datetime.datetime(1998,9,14)
print(x.strftime("%A"))
