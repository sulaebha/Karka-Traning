Name=input("Hey, what is your name: ")
age=int(input(f"ok {Name},How old are you? "))
if age<16:
    print(f"You can't drive {Name}")
elif 16<=age<=17:
    print(f"You can drive but not vote {Name}")
elif 18<age<24:
    print(f"You can vote but not rent a car {Name}")
elif age>=25:
    print(f"You can do pretty much anything {Name}")
