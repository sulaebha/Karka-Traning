# The area of a trapezium can be calculated using the formula: A = ½ × (a + b) × h.
# a and b are the length of parallel sides/bases of the trapezium. h is the height or distance between parallel sides.
base_side=int(input("Enter the base side value:  "))
top_side=int(input("Enter the top side value:  "))
height=int(input("Enter the height:  "))
sum_of_side=base_side+top_side
print(sum_of_side)
def area_trapezium():
    area=(sum_of_side)*(height)*(1/2)
    return area
area=area_trapezium()
print("are of trepazium is",area)