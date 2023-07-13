Name=input("Hey, what is your name: ")
age=int(input(f"ok {Name},How old are you? "))
if age<16:
    print(f"You can't drive {Name}")
if age<18:
    print(f"You can't vote {Name}")
if age<25:
    print(f"You can't rent a car {Name}")
elif age>=25:
    print(f"You can do anything that's legal {Name}")
