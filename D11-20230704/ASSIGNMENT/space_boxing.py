Earth_weight=float(input("Please enter your current earth weight: "))
print("I have information for the following planets: ")
print("1.Venus \t 2.Mars \t 3.Jupiter \n 4.Saturn \t 5.Uranus \t 6.Neptune")
# planet1,planet2,planet3,planet4,planet5,planet6="Venus","Mars","Jupiter","Saturn","Uranus","Neptune"
visiting=int(input("Which planet are you visiting: "))
if visiting==1:
    weight=Earth_weight*0.78
    print(f"Your weight would be {weight} pounds on that planet.")

elif visiting==2:
    weight=Earth_weight*0.39
    print(f"Your weight would be {weight} pounds on that planet.")

elif visiting==3:
    weight=Earth_weight*2.65
    print(f"Your weight would be {weight} pounds on that planet.")

elif visiting==4:
    weight=Earth_weight*1.17
    print(f"Your weight would be {weight} pounds on that planet.")

elif visiting==5:
    weight=Earth_weight*1.05
    print(f"Your weight would be {weight} pounds on that planet.")

elif visiting==6:
    weight=Earth_weight*1.23
    print(f"Your weight would be {weight} pounds on that planet.")

else:
    print("Enter the given planet number")

