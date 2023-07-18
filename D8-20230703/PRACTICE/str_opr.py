name="SULAEBHA "
myage=21

print(name)
print(name[3])
print(name[3:])
print("hhhhhhhhh",name[ :6])
print(name[0:5])
length=len(name)
print(length)
# intro="my name is sulaebha,i am "+myage
intro= f"my name is sulaebha,i am {myage}"
introduction="Hi im Sulaebha"
intro=introduction.startswith("Hii")

print(intro)
# name1=name.lower()
# name1=name.strip()
name1=name.replace("BHA","bha")
print(name1)
# count()	Returns the number of times a specified value occurs in a string
print(name.count("A"))
# Converts the first character to upper case-capitalize()
print(name.capitalize())
# casefold()	Converts string into lower case
print(name.casefold())
# center()	Returns a centered string-------padding value must
print(name.center(30))
# encode()	Returns an encoded version of the string
print(name.encode())
# endswith()	Returns true if the string ends with the specified value
corect=name.endswith(" ")
print(corect)
# expandtabs()	Sets the tab size of the string
print(name.expandtabs())
# find()	Searches the string for a specified value and returns the position of where it was found
print(name. find("A"))
# isalnum()	Returns True if all characters in the string are alphanumeric
print(name.isalnum())