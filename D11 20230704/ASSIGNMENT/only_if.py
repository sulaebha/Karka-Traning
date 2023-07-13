print("TWO MORE QUESTIONS BABY!")
print("Think of an object,and i will try to guess it.")
Question_1=input("Does it belong inside or outside or both?  \n>  ")
Question_2=input("Is it a living thing \n>  ")
if Question_1=="inside" and Question_2=="yes":
    print("My guess is that you thinking of a Houseplant. ")
if Question_1=="outside" and Question_2=="yes":
    print("My guess is that you thinking of a Bison. ")
if Question_1=="both" and Question_2=="yes":
    print("My guess is that you thinking of a Dog. ")  
if Question_1=="inside" and Question_2=="no":
    print("My guess is that you thinking of a Shower curtain. ")  
if Question_1=="outside" and Question_2=="no":
    print("My guess is that you thinking of a Bill board. ")        
if Question_1=="both" and Question_2=="no":
    print("My guess is that you thinking of a Cell phone. ")