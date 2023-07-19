items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
]
# fruits=[] 
# vegetables=[]
#  #if you need the new list in the output first you need to create the empty list

Fruit_vegetable={
    "fruits":[],
    "vegetable":[]
}
for items in items_list:
    if items['category']=='Fruits':
        # print(items['name'])
        Fruit_vegetable["fruits"].append(items['name'])    #use append for add items in the list
    if items['category']=='Vegetables':
        Fruit_vegetable["vegetable"].append(items['name'])
# print(fruits)
# fruit_dict={'fruits':fruits}  #for creating new dictinory
# print(fruit_dict)


# for items in items_list:
    

# print(vegetables)
# vegetables_dict={'vegetables':vegetables}
print(Fruit_vegetable)
