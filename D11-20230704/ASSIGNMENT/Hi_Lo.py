print("I am thinking of a number between 1-100. You have 7 guesses")
num=80
First_g=int(input("First guess: "))


if First_g>num:
    print("too hign")
elif First_g<num:
    print("too low")
elif First_g==num:
    print("correct")  
    print("You guessed it!")
    exit()

Second_g=int(input("Second guess:  "))    

if Second_g>num:
    print("too hign")
elif Second_g<num:
    print("too low")
elif Second_g==num:
    print("correct")
    print("You guessed it!")
    exit()


Third_g=int(input("Third guess:  "))


if Third_g>num:
    print("too hign")
elif Third_g<num:
    print("too low")
elif Third_g==num:
    print("correct") 
    print("You guessed it!")
    exit()


Fourth_g=int(input("Fourth guess:  "))

if Fourth_g>num:
    print("too hign")
elif Fourth_g<num:
    print("too low")
elif Fourth_g==num:
    print("correct")
    print("You guessed it!")
    exit()


Fivth_g=int(input("Fivth guess:  "))

if Fivth_g>num:
    print("too hign")
elif Fivth_g<num:
    print("too low")
elif Fivth_g==num:
    print("correct")
    print("You guessed it!")
    exit()


Sixth_g=int(input("Sixth guess:  "))

if Sixth_g>num:
    print("too hign")
elif Sixth_g<num:
    print("too low")
elif Sixth_g==num:
    print("correct") 
    print("You guessed it!")
    exit()

Seventh_g=int(input("Seventh guess:  "))

if Seventh_g>num:
    print("too hign")
elif Seventh_g<num:
    print("too low")
elif Seventh_g==num:
    print("correct")  
    print("You guessed it!")
    exit()
print("Sorry,you didn't guess it in 7 tries,you loss.  ")