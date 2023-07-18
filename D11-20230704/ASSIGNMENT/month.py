month_num=int(input("Enter the number of the month:  "))
def month_name(month_num):
    if month_num==1:
        print("January")
    elif month_num==2:
        print("February")
    elif month_num==3:
        print("March")
    elif month_num==4:
        print("April")
    elif month_num==5:
        print("May")
    elif month_num==6:
        print("June")
    elif month_num==7:
        print("July")
    elif month_num==8:
        print("August")
    elif month_num==9:
        print("September")
    elif month_num==10:
        print("Actober")
    elif month_num==11:
        print("November")
    elif month_num==12:
        print("December")
    else:
        print("Error")  

    return 
      
month=month_name(month_num)
print(month)        