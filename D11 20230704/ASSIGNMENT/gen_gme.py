Gender=input("What is your gender (M or F)? :  ")
F_name=input("Enter your first name:  ")
L_name=input("Enter your Last name:  ")
age=int(input("Enter your age :  "))
if Gender=='F' and age>=20:
    M_status=input("Are you married: ")
    if M_status=='yes':
     print(f"Then i shall call you Mrs.{F_name}")
    else:
     print(f"Then i shall call you Ms.{F_name}")
if Gender=='M' and age>=20:
  print(f"Then i shall call you Mr.{F_name}")
else:
  print(f"Then i shall call you {F_name} {L_name} .") 
