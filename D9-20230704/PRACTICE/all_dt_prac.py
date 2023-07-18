# list bacics
Fruits=["apple","orange","banana","kivi","pinapple"]
print(Fruits[2])
for i,fruit in enumerate(Fruits):
    # print(str(i)+fruit)
    if(i<=3):
        print(fruit)
    else:
        break
# tuble
Fruits=("apple","orange","banana","kivi","pinapple")
print(Fruits[2:5])
# dic
student_detail={"name":"sulaebha","age":21,"CGP":8}
print(student_detail["name"])
# SET
# Fruits={"apple","orange","banana","kivi","pinapple"}
# print(Fruits[2:3])




for i,fruit in enumerate(Fruits):
    if(i<3):
        continue
    else:
        print(fruit)



     
     
for i,fruit in enumerate(Fruits):
    if(i>2):
        continue
    else:
        print(fruit)