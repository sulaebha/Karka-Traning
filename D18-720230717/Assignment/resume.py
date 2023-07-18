my_resume={
    "Name":"Sulaebha M",
    "E-mail":"rosesulaebha@gmail.com",
    "Mobile-no":9769243278,
    "Soft Skills":['problem solving','Time Management','Teamwork','Dicision Making'],
    "Hard Skills":['python','html','css','MS-office'],
    "Educational Qualification":[{'Qualification':'SSLC','School name':'SHSS','passedout_year':2016,'percentage':88},
                                 {'Qualification':' HSC','School name':'GHSS','passedout_year':2018,'percentage':84},
                                 {'Qualification':'B.E','College name':'AVCE','passedout_year':2022,'percentage':80}],

    "Projects":"BRAIN TUMOR IDENTIFICATION AND CLASIFICATION OF MRI USING DEEP LEARNING TECHNIQUES",
    "Experience":{'Company name':'code genie solutions','location':'tirunelveli','duration':'1 month'},
    "Hobbies":['using mobile','listening music','coding'],
    "Personal Details":{"Father's name":"Mr Mahalingam","Father's Occupation":"Coolie worker",
                        "Languages known":['tamil','english'],"DOB":"29-11-2001","Gender":"Female",
                        "Marital Status":"Unmarried",
                        "Address":{'door-no':"3L","street name":"mainroad","village":" sri Regunathapuram","town":"panagudi","pin-no":627109}

                                                 
}
}
for skill in my_resume["Hard Skills"]:
    print(skill,"\n")
# print(my_resume["Educational Qualification"][0]["percentage"])
# print(my_resume["Educational Qualification"][0]["passedout_year"])

# print(my_resume["Personal Details"]["Languages known"])
# print(my_resume["Personal Details"]["Address"])
# def resume():
for content in my_resume["Educational Qualification"]:
      percentage=content["percentage"]
      print(percentage,"\n")
      Passesdout_year=content["passedout_year"]
      print(Passesdout_year ,"\n")
      break
     
# print(personal)
for language in  my_resume["Personal Details"][ "Languages known"]:
      
      print(language,"\n")
      #   address=details["Address"]
      #   print(address)      
for adrss in my_resume["Personal Details"] [ "Address"]:
#      address=my_resume["Personal Details"] [ "Address"]['door-no']
     print(my_resume["Personal Details"] [ "Address"][adrss],"\n")
     break
# for Details in my_resume["Personal Details"]:
#       if Details=="DOB":
#             # print([Details])
#          print(my_resume["Personal Details"][Details])
print(my_resume["Personal Details"]["DOB"])     
# exit()
# resume()   

