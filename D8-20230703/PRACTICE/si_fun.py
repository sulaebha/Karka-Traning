# calculate SI using funtion
principal=1000
num_of_yrs=10
rate_of_interest=2
def calc_SI(principal,num_of_yrs,rate_of_interest):
    simple_in=(principal*num_of_yrs*rate_of_interest)/100
    return simple_in
    
# SI=calc_SI(principal,num_of_yrs,rate_of_interest)
# print(SI)


a=20
def twice(a):
    b=2*a
    print(3333)
    return b
# b=twice(a)
# print(b)


#passed_out_year=int(input("Enter the passedout year:"))

def eligible(passed_out_year):
    is_eligible=passed_out_year>2021
    return is_eligible

# is_eligible=eligible(passed_out_year)
# print(is_eligible)