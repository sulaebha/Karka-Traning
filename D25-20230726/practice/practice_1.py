number=int(input("enter the number: "))
# design=input("enter your design: ")

# output=number*design
# print("ghu", type(output))
# print(output)
# for i in output:
#    print(i*number)

# num=1
# for i in range(number):
        
#     #    for j in range(number):
    
#     print(num,end=" ")  
#     num=num+1
# print("") 

    

# num=64
# for i in range(number):
    
#    for j in range(number):
   
#     print(num,end=" ")  
#     num=num-1
#    print("")    


# for i in range(1,(number*number)+1):
#     print(i,end=" ")  
#     if i%number==0:
#         print("\n") 

for i in range(number*number,0,-1):
   
    if i%number==0:
        print("\n") 
    print(i,end=" ")  