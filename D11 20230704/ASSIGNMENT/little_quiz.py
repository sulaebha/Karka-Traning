Ready="yes"
not_ready="no"
right_ans=0
num_of_ques=0
ask_for_quiz=input("are you ready for a quiz?  ")
if ask_for_quiz=="yes":
    print("okay,here it comes!")
else:
    print("Thank you for the interest")
    exit() 
capital=int(input("Q1)What is the capital of india? \n\t 1)melbourne \n\t 2)New Delhi \n\t 3)Jakarta\n>"))
if capital==2:
    right_ans =right_ans+1
    print("That's right") 
else:
    print("Sorry,That's wrong")
num_of_ques=num_of_ques+1       

value=int(input("Q2)Can you store the value 'cat'in the variable of type int? \n\t 1)Yes \n\t 2)No\n>"))  
if value==1:
  
    print("'cat is the string ,int can only store numbers")   
else:
    right_ans=right_ans+1
    print("That's correct")
num_of_ques=num_of_ques+1       


result=int(input("Q3)What is the result of 5**5? \n\t 1)30 \n\t 2)20 \n\t 3)25\n>"))
if result==3:
    right_ans=right_ans+1
    print("That's right") 
else:
    print("Sorry,That's wrong")
num_of_ques=num_of_ques+1       

print(f"Overall, you got{right_ans} out of {num_of_ques} correct \n Thanks for playing ")

