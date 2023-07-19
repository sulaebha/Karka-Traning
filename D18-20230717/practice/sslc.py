# names=["Sulaebha","Rashika","Kavish","Devi priya","Rabin","Reshma","Aswin kumar"]
# for name in names:
#     print(name)

Names=[
        {"Name":"Sulaebha",
       "Place":"Panagudi",
       "Hobbies":["watching TV","Using mobile ","listening music"],
       "marks":{"tamil":93,"english":78,"maths":84,"science":92,"social":93}
        },

       {"Name":"Rashika",
        "Place":"Paraseri",
       "Hobbies":["watching TV","Sleeping","listening music"],
       "marks":{"tamil":90,"english":88,"maths":100,"science":73,"social":74}
        
       },

       {
           "Name":"Devi priya",
           "Place":"Aralvaimozhi",
           "Hobbies":["Watching Tv","listening music","playing dogs"],
           "marks":{"tamil":92,"english":98,"maths":74,"science":93,"social":64}
       },

       {
            "Name":"Kavish",
            "Place":"Vadaseri",
            "Hobbies":["Games","Bike ride"],
            "marks":{"tamil":83,"english":88,"maths":80,"science":90,"social":94}
       },

       {
           "Name":"Rabin",
           "PLace":"Raman puthur",
           "Hobbies":["Youtube","games","Watching movie"],
           "marks":{"tamil":93,"english":78,"maths":84,"science":93,"social":94}
       },
     
       {
           "Name":"Aswin kumar",
           "Place":"Nagarcoil",
           "Hobbies":["Watching movie","Playing cricket","cooking"],
           "marks":{"tamil":80,"english":68,"maths":99,"science":90,"social":44}
       },

       {
            "Name":"Reshma",
            "Place":"Marthandam",
            "Hobbies":["Gardening","Listening music"],
            "marks":{"tamil":83,"english":79,"maths":64,"science":93,"social":52}
       }
       ]

for name in Names:
    # print(name)
    # print(name["marks"])
    # for mark in name["marks"]:
    # print(name["marks"].keys())
    NAME=name["Name"]
    tamil=(name["marks"]["tamil"])
    english=(name["marks"]["english"])
    maths=(name["marks"]["maths"])
    science=(name["marks"]["science"])
    social=(name["marks"]["social"])
    total=tamil+english+maths+science+social
    
    print(total)
    percentage=total/5
    print(percentage)
    if percentage>90:
       print(f"{NAME} is eligible for maths biology \n")
    elif percentage>80 and percentage<90:
        print(f"{NAME} is eligible for computer science \n")
    elif percentage>75 and maths>98:
        print(f"{NAME} is eligible for maths biology \n")
    elif percentage>70 and maths>98:
        print(f"{NAME} is eligible for computer science \n")
    else:
        print(f"{NAME} not eligible for maths biology and computer science")