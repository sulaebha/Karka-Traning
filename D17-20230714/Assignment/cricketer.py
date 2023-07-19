cricket_players = [
    {
        'name': 'Virat Kohli',
        'country': 'India',
        'centuries': 43,
        'half_centuries': 59,
        'wickets': 4,
        'hat_tricks': 0,
        'top_score': [254,345,34,976,86]
    },
    {
        'name': 'Kane Williamson',
        'country': 'New Zealand',
        'centuries': 24,
        'half_centuries': 34,
        'wickets': 28,
        'hat_tricks': 0,
        'top_score': [251,76,65,654,876]    },
    {
        'name': 'Steve Smith',
        'country': 'Australia',
        'centuries': 27,
        'half_centuries': 31,
        'wickets': 17,
        'hat_tricks': 0,
        'top_score': [239,876,90,987,89]
    },
    {
        'name': 'Joe Root',
        'country': 'England',
        'centuries': 21,
        'half_centuries': 49,
        'wickets': 16,
        'hat_tricks': 1,
        'top_score':[254,34,145,221]
    },
    {
        'name': 'Babar Azam',
        'country': 'Pakistan',
        'centuries': 18,
        'half_centuries': 28,
        'wickets': 1,
        'hat_tricks': 0,
        'top_score': [185,876,543,987,67]
    }
]



def cricket_function():
    for players in cricket_players:
        name=players["name"]
        # country=player["country"]
        centuries=players["centuries"]
        # half_centuries=player["half_centuries"]
        # wickets=player["wickets"]
        hat_tricks=players["hat_tricks"]
        # =player["top_score"]
        

    #    .Determine and display the number of players who have scored more than 10 centuries from the list.


        if centuries>10:
                print(name,"have scored more than 10 centuries \n")


                # .Find and display the players who have taken more than 5 hat-trick wickets.
       
        # else:
        #     print("No one take more than 5 hat_tricks \n")
                #    Identify and display the top batting score achieved by the players.
                
       
        elif hat_tricks>5:
            print(name,"have taken more than  5 hat_tricks \n")
        else:
            print("no one have  more than  5 hat_tricks \n")
            exit()

         
        def top():
           
           topscore=players["top_score"][0]
        
           for player in players["top_score"]:
        # 'top_score': [254,345,34,976,86]
            

            if player>topscore:
                
                topscore=player
                print(topscore)

                #  print(players)

        top()    

            # if top_score>i["top_score"]:
            # print(top_score ,"\n ")
cricket_function()