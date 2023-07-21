eb_bill_details=[{'month': 1, 'unit consumed': 100, 'bill_amount': 200}, 
                 {'month': 2, 'unit consumed': 150, 'bill_amount': 300},
                 {'month': 3, 'unit consumed': 300, 'bill_amount': 1500}, 
                 {'month': 4, 'unit consumed': 400, 'bill_amount': 2000}]


# string = ",".join([item['month']['unit consumed']['bill_amount'] for item in eb_bill_details])
# print(string)
# def listToString(eb_bill_details):
 
#     # initialize an empty string
#     str1 = ""
 
#     # traverse in the string
#     for ele in eb_bill_details:
#         str1 += ele
 
#     # return string
#     return str1
 
eb_string=str(eb_bill_details)
# print(eb_string)
# print(listToString(eb_bill_details))

eb_string_open=open("/home/sulaebha/karka/D21-20230720/practice/convert_str.txt",'r')
for line in eb_string_open:
    print(line)
