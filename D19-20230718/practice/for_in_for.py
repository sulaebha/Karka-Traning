Education_details=[
    {
    "study":"B.Tech","Institute":"cape","semester_marks":[
        {'semester_name':1,"Subjects":['aaa','bbbb','cccc'],"semester_grade":"A"},
        {'semester_name':2,"Subjects":['aaa','bbbb','cccc'],"semester_grade":"A"}

    ]
},
  {
    "study":"M.Tech","Institute":"cape","semester_marks":[
        {'semester_name':1,"Subjects":['aaa','bbbb','cccc'],"semester_grade":"A"},
        {'semester_name':2,"Subjects":['aaa','bbbb','cccc'],"semester_grade":"A"}

    ]
},
  {
    "study":"MBA","Institute":"cape","semester_marks":[
        {'semester_name':1,"Subjects":['aaa','bbbb','cccc'],"semester_grade":"A"},
        {'semester_name':2,"Subjects":['aaa','bbbb','cccc'],"semester_grade":"A"}

    ]
}

]

for details in Education_details:
    print(details["study"])
    for marks in details["semester_marks"]:
        print(marks)
        for mark in marks:
            print(mark)