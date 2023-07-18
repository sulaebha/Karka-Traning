length=int(input("Enter the length of the triangle: "))
width=int(input("Enter the width of the triangle: "))
def area_rec():
    area=length*width
    return area
area=area_rec()
print("Area of the rectangle is",area)