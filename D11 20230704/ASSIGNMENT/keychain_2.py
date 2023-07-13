print("COOL KEYCHAION SHOP")

Menu= ("1)Add keychains to order \n2)Remove keychains from order \n3)View current order \n4)Checkout")
print(Menu)

total_keychain=0
price_per_keychain=1.00
tax=8.25
tax_base_shipping=5.00
per_keychain_shipping=1.00



def add_keychain():
    
    global total_keychain
    total_keychain=0
    add_key=int(input(f"You have {total_keychain} ,How many you add? ") )
    if add_key>=0:
        total_keychain=total_keychain+add_key
        print(f"\nYou now have {total_keychain} keychains.\n")
    else:
        print("Enter the positive number.")
        exit()
    # key_condition()
    # option1=("ADD KEYCHAINS ")
    return 0
def remove_keychain(total_keychain):

    remove_key=int(input(f"You have {total_keychain} ,How many you want to remove? "))
    total_keychain=total_keychain-remove_key   
    print(f"You now have {total_keychain} keychains.")
    # key_condition()
    # option2=("REMOVE KEYCHAINS ")
    return  0

def view_keychain(total_keychain):
    print(f"You have {total_keychain} keychains cost ${price_per_keychain} each \n ")
    # print("tax=8.25%")
    print("tax_base_shipping=$5.00")
    print("per_keychain_shipping=$1.00")
    percentage=0.0825*total_keychain
    print(f"Total cost is ${(price_per_keychain*total_keychain)+tax_base_shipping+percentage}\n")
    # key_conditio
    # option3=("VIEW ORDER ")
    return 

def check_keychain():
    print("Check out")
    name=input("What is your name: ")
    print(f"You have {total_keychain} keychains.\n keychain cost ${price_per_keychain}. each \n Total cost is ${price_per_keychain*total_keychain} .\n Thanks for your order {name}")


    return

while True:
    choice=int(input("Enter your choice : "))

    if choice==1:
        add_keychain()
 
    # print(Menu) 
    elif choice==2:
        remove_keychain(total_keychain)  
   

    elif choice==3:
        view_keychain(total_keychain)  


    elif choice==4:
        check_keychain()    
        break
    else:
        print("enter the correct option") 
        break

      