print("COOL KEYCHAION SHOP")

Menu= ("1)Add keychains to order \n2)Remove keychains from order \n3)View current order \n4)Checkout")
print(Menu)

# total_keychain=0
cost=10



# cost=10
# order=cost+total_keychain

def add_keychain():
    global total_keychain
    total_keychain=0

    add_key=int(input(f"You have {total_keychain} ,How many you add? ") )
    
    total_keychain=total_keychain+add_key
    print(f"\nYou now have {total_keychain} keychains.\n")
    key_condition()
    # option1=("ADD KEYCHAINS ")
    return 0


def remove_keychain(total_keychain):

    remove_key=int(input(f"You have {total_keychain} ,How many you want to remove? "))
    total_keychain=total_keychain-remove_key   
    print(f"You now have {total_keychain} keychains.")
    key_condition()
    # option2=("REMOVE KEYCHAINS ")
    return  0

def view_keychain(total_keychain):
    print(f"You have {total_keychain} keychains cost {cost} each \n ")
    print(f"Total cost is {cost*total_keychain}\n")
    key_condition()
    # option3=("VIEW ORDER ")
    return 0

def check_keychain():
    print("Check out")
    return 0
    
def key_condition():
    choice=int(input("Enter your choice : "))

    if choice==1:
       add_keychain()
    # print(Menu) 
    

    if choice==2:
       remove_keychain(total_keychain)
    # print(Menu)

    if choice==3:
       view_keychain(total_keychain)
    # print(Menu)

    if choice==4:
         check_keychain()    

         name=input("What is your name: ")
         print(f"You have {total_keychain} keychains.\n keychain cost {cost}. each \n Total cost is {cost*total_keychain} .\n Thanks for your order {name}")

 

key_condition()