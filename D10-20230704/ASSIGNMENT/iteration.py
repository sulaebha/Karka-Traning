# add numbers
# number_list=[20,21,30,40,10,10]
# sum=0
# for i,number in enumerate(number_list):
#     sum=sum+number
#     print(total)
    # else:
    #     print("nothing")
    
marks=[90,90,90,90,90]
total_marks=0
for i,mark in enumerate(marks):
    # print("before",total_marks)
    total_marks=total_marks+mark
    # print("after",total_marks)

print(total_marks)

average=total_marks/len(marks)
print(average)



marks=[90,90,90,90,90]
total_marks=0
enum_marks=enumerate(marks)
print(type(enum_marks))
for i,mark in enum_marks:
    print("Entering iteration process for item no:"+str(i))
    print("before",total_marks)
    total_marks=total_marks+mark
    print("after",total_marks)
    print("Exiting iteration process for item no:"+str(i))


print(total_marks)
print("\n")


prods = [500, 200, 700, 1000] 
product_list=[]
for i,product in enumerate(prods):
 products=("INR "+ str(product))
#  print(products)

 products_list=product_list.append(products)

print(product_list)