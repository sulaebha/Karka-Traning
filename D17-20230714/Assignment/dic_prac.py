Frds_details=[{"name":"Sulaebha","age":21,"place":"panagudi"
    },
    {"name":"Rama laksmi","age":22,"place":"panagudi"
},
{
    "name":"jensi","age":21,"place":"tisayanvilai"}
]

def format_dic():
    for frd in Frds_details:
        name=frd["name"]
        age=frd["age"]

        place=frd["place"]
        print(f"I am {name}, I'm {age} years old, and I'm from {place}.")
    # print(frd)
       
format_dic()        


def age_dic():
    for frd in Frds_details:
       if frd["age"]>21:
        name=frd["name"]
        place=frd["place"]
        print(f"I am {name}, I'm from {place}.")
    # print(frd)
       
age_dic()      