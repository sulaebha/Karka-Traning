import BMI

Height=float(input("Your height in meter: "))
Weight=float(input("Your weight in kg: "))
Catagory=BMI.bmi(Height,Weight)
print(Catagory)

print(f"your BMI is {Catagory}")

# bmi_cal=Weight/(Height**Height)
# print(bmi_cal)
# print(f"your BMI is {bmi_cal}")

if Catagory<18.5:
    print("BMI category : under weight")
elif 18.5<Catagory<24.9:
    print("BMI category : normal weight")
elif 25.0<Catagory<29.9:
    print("BMI category : over weight")
elif Catagory>30.0:
    print("BMI category : under obese")
