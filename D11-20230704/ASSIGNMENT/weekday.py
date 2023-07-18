# weeks=["1) Sunday","2) Monday","3) Tuesday","4) Wednesday","5) Thursday","6) Friday","7) Saturday"]
# def Weeksdays():
#     for week in weeks:
#         print("Weekday :"+week)
# weekday=Weeksdays()        
# print(weekday)
Weekday=int(input("Weekday "))
if Weekday==1:
    print("Today is Sunday")
elif Weekday==2:
    print("Today is Monday")
elif Weekday==3:
    print("Today is Tuesday")
elif Weekday==4:
    print("Today is Wednesday")
elif Weekday==5:
    print("Today is Thursday")
elif Weekday==6:
    print("Today is Friday")
elif Weekday==7:
    print(" Today isSaturday")
elif Weekday==0:
    print(" Today is Saturday")
else:
 print("error")