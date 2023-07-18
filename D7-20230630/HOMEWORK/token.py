# GET THE AMOUNT FOR FOUR ITEMS AS A INPUT FROM THE USER AND ADD THEM,IF THE TOTAL IS BTWEEN 500 TO 100 THEN PRINT YOU HAVER OWNED A SILVER TOKEN,ABOVE 1000 YOW WON GOLD TOKEN 
item1=int(input("Enter the amout of item1:"))
item2=int(input("Enter the amout of item2:"))
item3=int(input("Enter the amout of item3:"))
item4=int(input("Enter the amout of item4:"))
sum_of_items=item1+item2+item3+item4
Silver=sum_of_items<1000 and 500<=sum_of_items
# Golden=sum_of_items>1000
if Silver:
    print("You have owned a silver token")
    
if sum_of_items>1000:
    print("You have owend a golden token")
else:
    print("Nothing you Owned")


