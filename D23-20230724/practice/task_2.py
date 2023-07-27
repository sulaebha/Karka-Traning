monthly_gold_rate=[{"month_name":"jan","gold_rate":1500},
                   {"month_name":"feb","gold_rate":500},
                   {"month_name":"march","gold_rate":1000},
                   {"month_name":"apr","gold_rate":8000},
                   ]

rate=0
rate_1=1500
for goldrate in monthly_gold_rate:  

    if goldrate["gold_rate"]>rate:
       rate=goldrate["gold_rate"]
       month=goldrate["month_name"]

    elif goldrate["gold_rate"]<rate_1:
        rate_1=goldrate["gold_rate"]
        month_1=goldrate["month_name"]

print(f"Maximun gold rate is {rate} at the month of {month}")

print(f"Minimun gold rate is {rate_1} at the month of {month_1}")

    
   

