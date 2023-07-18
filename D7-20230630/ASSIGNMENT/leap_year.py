year=input("enter the year:")
year=int(year)
is_leap_year=(year%4)==0 or (year%400)==0  and (year/100)!=0
print(is_leap_year)
if is_leap_year:
    print("the given year is leap year")
else:
    print("the given year is not a leap year")