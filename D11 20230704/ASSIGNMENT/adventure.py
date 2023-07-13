print("WELCOME TO MITCHELL'S TINY ADVENTURE")
Rooms=input("You are in the creepy house! would you like to go 'upstairs' or into the 'kitchen'\n >  ")
# Top_room=input("Their is the big 'music hall' and 'bed room' where you want to go\n")
if Rooms=="kitchen":
   in_kitchen= input("Their is the long countertop with the dirty dishes everywhere. off to one sife their is,as you'd expected a 'refrigerator' or look in the 'cabinet' \n>  ")
   if in_kitchen=="refrigerator":
      In_refgrtor=input("Inside the refrigeretor you see food and stuff.Its look preety nasty, \n Would you like to eat some of the food?(yes or no)\n >  ")
      if In_refgrtor=="yes":
       print("You can alive......somedays")
      if In_refgrtor=="no":
       print("You die of Starvation........Eventually") 

   if in_kitchen=="cabinet":
      In_cabnt=input("Inside the cabinet you see the potato chips and mango juice.\n Would you like to eat it?(yes or no)\n>  ")
      if In_cabnt=="yes":
       print("Enjoy your Snacks.....")
      if In_cabnt=="no":
       print("You miss your tasty snacks.......")
     

elif Rooms=="upstairs":
   Top_room=input("Their is the big 'music hall' and 'bed room' where you want to go\n>  ")
   if Top_room=="music hall":
      In_hall=input("I think you good in music,Is it Correct or not? (yes or no)\n>  ")
      if In_hall=="yes":
       print("Go and enjoy the music......")
      if In_hall=="no":
       print("I think your selection is wrong.....")


   if Top_room=="bedroom":
      In_broom=input("I think you are so tired ? (yes or no)\n>  ")
      if In_broom=="yes":
       print("Go and sleep well......")   
      if In_broom=="no":
        print("I think you are verty healthy......")
    
else:
   print("choose one of the selection ")   


   
