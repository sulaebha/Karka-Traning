amounts=[1000,900,3,4,5,6,1000000]
def large(amounts):
 largest_num=amounts[0]
 for amount in amounts:



    if  amount>largest_num:
     largest_num=amount



 return largest_num   

# print(large_number)
large_number=large(amounts)
print("The largest num is",large_number)
    


    # number_list=[20,21,30,40,10,10]
# sum=0
# for i,number in enumerate(number_list):
#     sum=sum+number
#     print(total)
    # else:
    #     print("nothing")