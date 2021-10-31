'7'
import datetime
a = eval(input("请输入年份"))
b = eval(input("请输入月份"))
c = eval(input("请输入日")) 
d1 = datetime.datetime(2001,1,1)
d2 = datetime.datetime(a,b,c)
interval = d2 - d1
interval.days
print(interval.days)
