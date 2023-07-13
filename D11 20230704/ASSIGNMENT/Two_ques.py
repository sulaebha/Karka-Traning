print("TWO QUESTIONS!")
print("Think of an object,and i will try to guess it.")
Question_1=input("Question 1)Is it animal,vegetable or mineral? \n>")
Question_2=input("Is it bigger then the breadbox? \n>")
if Question_1=="animal" and Question_2=="yes":
    print("My guess is that you thinking of a mouse.")
if Question_1=="vegetable" and Question_2=="yes":
    print("My guess is that you thinking of a water melon.")
if Question_1=="mineral" and Question_2=="yes":
    print("My guess is that you thinking of a camaro.")

if Question_1=="animal" and Question_2=="no":
    print("My guess is that you thinking of a Squirrel.")
if Question_1=="vegetable" and Question_2=="no":
    print("My guess is that you thinking of a carrot.")
if Question_1=="mineral" and Question_2=="no":
    print("My guess is that you thinking of a paper clip.")
    exit()
# else:
#     print("please,Enter the crt value")
print("I would ask you If I'am right, but i don't actually care.")
