monthly_gold_rate=[{"month_name":"jan","gold_rate":1500,"jwel_list":[{"name":"chain",
                                                                      "making_cost":17},
                                                                      {"name":"bangle",
                                                                      "making_cost":14}
                                                                      ]},
                   {"month_name":"feb","gold_rate":500,"jwel_list":[{"name":"ring",
                                                                      "making_cost":9},
                                                                      {"name":"earings",
                                                                      "making_cost":17}]},
                   {"month_name":"march","gold_rate":1000,"jwel_list":[{"name":"bracelet",
                                                                      "making_cost":10},
                                                                      {"name":"chain",
                                                                      "making_cost":20}]},
                   {"month_name":"apr","gold_rate":8000,"jwel_list":[{"name":"earings",
                                                                      "making_cost":12},
                                                                      {"name":"bangles",
                                                                      "making_cost":25}]},
                   ]



for goldrate in monthly_gold_rate:
    for j_list in goldrate["jwel_list"] :
        # print(j_list)
        Jwel_name=j_list['name']
        Making_cost=j_list['making_cost']
        Rate=goldrate["gold_rate"]
        month=goldrate["month_name"]

        total_rate=(Rate*Making_cost/100)+Rate
        # print(total_rate)
        # 
        # print(f"at the month of {month} gold rate is {Rate} for {Jwel_name} is {total_rate} ")        
        # print(Jwel_name)
        # print({
        #     "month":month,
        #     "gold_rate":Rate,
        #           Jwel_name:total_rate

        # })
        # print([Jwel_name]+[1])
        output=(f"Month:{month},\nGoldrate:{Rate},\n\t{Jwel_name}_rate:{total_rate}")
            

        # }

        print(output)

        # for i in output.items():
        #     print(i) 

        
