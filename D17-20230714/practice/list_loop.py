# names=["Sulaebha","Rashika","Kavish","Devi priya","Rabin","Reshma","Aswin kumar"]
# for name in names:
#     print(name)

Names=[
        {"Name":"Sulaebha",
       "Place":"Panagudi",
       "Hobbies":["watching TV","Using mobile ","listening music"]
        },

       {"Name":"Rashika",
        "Place":"Paraseri",
       "Hobbies":["watching TV","Sleeping","listening music"]
        
       },

       {
           "Name":"Devi priya",
           "Place":"Aralvaimozhi",
           "Hobbies":["Watching Tv","listening music","playing dogs"]
       },

       {
            "Name":"Kavish",
            "Place":"Vadaseri",
            "Hobbies":["Games","Bike ride"]
       },

       {
           "Name":"Rabin",
           "PLace":"Raman puthur",
           "Hobbies":["Youtube","games","Watching movie"]
       },
     
       {
           "Name":"Aswin kumar",
           "Place":"Nagarcoil",
           "Hobbies":["Watching movie","Playing cricket","cooking"]
       },

       {
            "Name":"Reshma",
            "Place":"Marthandam",
            "Hobbies":["Gardening","Listening music"]
       }
       ]

# for name in Names:
print(Names[1]["Hobbies"])
for hobby in Names[1]["Hobbies"]:
    print(hobby)



my_detail={"name":"sulaebha","age":21,"degree":"B.E"}
print(my_detail["age"])



marks={
    "tamil":100, "english":90,
    "maths":100, "social":99,"Science":98

}
print(marks.items())
print(marks.values())
print(marks.keys())

