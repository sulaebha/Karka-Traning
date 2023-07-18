print("COOL KEYCHAION SHOP")

Menu= ("1)Add keychains to order \n\2)Remove keychains from order \n3)View current order \n4)Checkout")
print(Menu)





def add_keychain():
    print("ADD KEYCHAINS \n",Menu)
    key_condition()
    return 0

def remove_keychain():
    print("REMOVE KEYCHAINS \n",Menu)
    key_condition()
    return 0
def view_keychain():
    print("VIEW ORDER  \n",Menu)
    key_condition()
    return 0

def check_keychain():
    print("Check out")
    return
def key_condition():
    choice=int(input("Enter your choice : "))


    if choice==1:
        add_keychain()
        
      

    elif choice==2:
        remove_keychain()
        

    elif choice==3:
        view_keychain()
        

    elif choice==4:
        check_keychain()    

key_condition()