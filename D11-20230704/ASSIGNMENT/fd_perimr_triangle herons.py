# To find the area of a triangle using Heron's formula, we have to follow two steps:

#     Find the perimeter of the given triangle.
#     Then, find the value of the semi-perimeter of the given triangle; s = (a + b + c)/2.
#     Now use Heron's formula to find the area of a triangle (√(s(s – a)(s – b)(s – c)))
First_side_a=int(input("Enter the First side value: \n>"))
Second_side_a=int(input("Enter the Second side value: \n>"))
Third_side_a=int(input("Enter the Third side value: \n>"))

s=(First_side_a+Second_side_a+Third_side_a)/2



# First step
# def peri_triangle():
#     perimeter=First_side_a+Second_side_a+Third_side_a
#     return perimeter
# perimeter=peri_triangle()
# print(perimeter)

# Secon step

# def semi_peri():
#     semi_perimeter=(First_side_a+Second_side_a+Third_side_a)/2
#     return semi_perimeter
# semi_perimeter=semi_peri()
# print(semi_perimeter)

# Final step---Herons formula



def area_triangle():
    area=s*((s-First_side_a)*(s-Second_side_a)*(s-Third_side_a))
    # s=semi_perimeter
    # part1=s-First_side_a
    # print(part1)
    # part2=s-Second_side_a
    # part3=s-Third_side_a
    final=area**0.5

    
    # print(type(area))
    return final
final=area_triangle()
print(final)    
