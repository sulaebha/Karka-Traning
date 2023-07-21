readings=[]
num_of_ele=int(input("Enter the no of elements: "))
for i in range(1,num_of_ele+1):
     element=int(input())
     readings.append(element)
# print(readings)     


consumer_data={
    "consumer_name":"sulaebha",
    "eb_reading": readings
}
#  [1100, 1200, 1350, 1650, 2050]
# bill_amount=[]
name=consumer_data["consumer_name"]
eb_read=consumer_data["eb_reading"]
bill_details=[]
# print(eb_read)
# print(consumer_data['eb_reading'][1]-consumer_data['eb_reading'][0])
# def calculate_electricity_bill(consumer_data):
    # elec_bill_1=90
total_bill_amount=0

for bill in  range(1,len(eb_read)):
    elec_bill=0
    # print(bill)
    elec_bill_unit=eb_read[bill]-eb_read[bill-1]
    # print(eb_read[bill])
    # print(elec_bill_unit,"unit")
    if elec_bill_unit<100:
        print("There is no amount to pay")
    elif 100<=elec_bill_unit<200: 
        # print("dfg",elec_bill_unit)
        elec_bill= (2*elec_bill_unit) 
        # print(elec_bill,'rs')  
    elif 200<=elec_bill_unit<500: 
            elec_bill=(5*elec_bill_unit) 
        # print(b)

    elif 500<=elec_bill_unit<1000: 
        elec_bill=(10*elec_bill_unit) 
    #   print(c)

    elif elec_bill_unit>=1000: 
            elec_bill=(14*elec_bill_unit) 
        # print(d)

    total_bill_amount=total_bill_amount+elec_bill
    # print(total_bill_amount)


# calculate_electricity_bill(consumer_data)
    bill_detail={
        'month':bill,
        'unit consumed': elec_bill_unit,
        'bill_amount':elec_bill
    }
    bill_details.append(bill_detail)

# print(bill_details)
for detail in bill_details:
     print(detail)
print(total_bill_amount)

    # elec_bill_2=consumer_data['eb_reading'][1]-consumer_data['eb_reading'][0]
    # elec_bill_3=consumer_data['eb_reading'][2]-consumer_data['eb_reading'][1]
    # elec_bill_4=consumer_data['eb_reading'][3]-consumer_data['eb_reading'][2]
    # elec_bill_5=consumer_data['eb_reading'][4]-consumer_data['eb_reading'][3]


