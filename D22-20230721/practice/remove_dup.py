dup_value_list=[1,2,3,2,5,1,5]
original_value_list=[]



dup_value_list.sort()
# [1, 1, 2, 2, 3, 5, 5]
# print(dup_value_list)


for value in dup_value_list:
#     # print(value)
   if value not in original_value_list:
      original_value_list.append(value)

print(original_value_list)        