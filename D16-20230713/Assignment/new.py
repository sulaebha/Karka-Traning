# number=int(input("enter a number: "))
# # list=[]
# for i in range(1,number+1):
#     if i%2==0:
#         print("#",end="")
#     else:
#         print(i,end="")
# print(list.append(i))
number=int(input("enter a number: "))
srt=''' '''
for i in range(1,number+1):
    if i%2!=0:
        print(i,end="")
        srt.join(i)
    else:
        print("#",end="")
        print("\n")
        srt.join(i)

            


