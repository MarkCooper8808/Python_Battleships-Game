import random
from ShipPlacer import ShipPlacer


class PositionTracker():
            def update_visual_map(ship_string, player_map):
                #pinpoints what part of string representing player map to delete after a hit
                ship_description = ship_string
                update_map = player_map
        
                
                if ship_description == "ship 1 end":
                    new_map = update_map.replace("S1R","HIT")
                elif ship_description == "ship 1 middle":
                    new_map = update_map.replace("S1M","HIT")
                elif ship_description == "ship 1 front":
                    new_map = update_map.replace("S1F","HIT")
                elif ship_description == "ship 2 end":
                    new_map = update_map.replace("S2R","HIT")
                elif ship_description == "ship 2 middle":
                    new_map = update_map.replace("S2M","HIT")
                elif ship_description == "ship 2 front":
                    new_map = update_map.replace("S2F","HIT")
                
                return new_map       

            #function that handles the computer guessing and updating of player map if they are hit by the AI

            def computer_guess(sea, mapp, cord_pool_x,i1,i2):
                
                     
            
                hits = 0
                i1 = len(cord_pool_x) -1
                
  
                index_cord = random.randint(0,i1)
                
                guess_coord = cord_pool_x[index_cord]
                guess_coord_1 = int(guess_coord[0])
                guess_coord_2 = int(guess_coord[-1])

                del cord_pool_x[index_cord]

                #added functionality so computer doesn't have the same guess twice in a row..
                cannon_shot = guess_coord_1 + guess_coord_2
                hit_box = (guess_coord_1 * 5) + guess_coord_2 + 1
                #print(hit_box)
                #print(sea)
                for i in range(1):
                    if len(sea[hit_box - 1]) > 3:
                        hits+=1
                        #Remove ship front,mid or rear from list
                        print()
                        print("=" * 60)
                        print("Computer guess: " + str(guess_coord_1) + "," + str(guess_coord_2), " It's a hit!")
                        print("=" * 60)
                        #update map string for user when ship is hit
                        mapp = PositionTracker.update_visual_map(sea[hit_box-1][3],mapp)
                        print(mapp)
                        print("You hit ",sea[hit_box-1][3])
                        del sea[hit_box-1][3]
                    else:
                        miss_message = str(guess_coord_1) + "," + str(guess_coord_2)
                        print("The Computer guesses: " + miss_message + ". It's a miss!..")
                        #new_mapp = mapp.replace(miss_message, " X ")
                        #print(new_mapp)
                return mapp

    
                
    

            def hit_detector(self, sea_map, computer_sea):
                turn = 1
                game_is_running = True
                rounds_survived = 0
                sea = sea_map[0]
                player_map = sea_map[1]
                player_guess_record = []
                mapp = player_map

                
                i1 = 24
                i2 = 24
                        
                cord_pool_x = []
                for i in range(5):
                    for j in range(5):
                        new_cord = str(i) + ',' + str(j)
                        cord_pool_x.append(new_cord)
                


                print("Format for entering coordinates is, for example 'v,4,4' no single quotes/n")
                 #Ships have been placed, this while loop controls the computer turns and hit detection
                while game_is_running == True:
                    #turn incrementor; controls who's turn it is using % 2
                    

                    
                    #check to see if all ship parts have been removed from either the computer or the players "sea" list
                    #game ends if this is the case

                    ship_parts_remaining = 0
                    for item in sea:
                        if len(item) > 3:
                            ship_parts_remaining+=1
                    if ship_parts_remaining == 0:
                        print("\nGAME OVER! Your ships have been sunk.\n You lasted:",rounds_survived)
                        game_is_running = False
                        continue
                    computer_ship_parts_remaining = 0
                    for item in computer_sea:
                        if len(item) > 3:
                            computer_ship_parts_remaining+=1
                    if computer_ship_parts_remaining == 0:
                        print("\nYou WIN!\n You sank all enemy ships!:",'\n',"Rounds played:",rounds_survived)
                        game_is_running = False
                        continue

                    print("-" * 60)
                    if rounds_survived % 2 == 0 and rounds_survived > 0:
                        print("\nHere are your guesses so far: ")
                        print(player_guess_record)
                            
                    
                    #prompts the player to enter a coordinate guess. I really wanted to make a visual map much like the one that
                    #displays when the computer lands a hit, unfortunately the project scope was getting a bit out of hand.
                    
                    player_guess = input("Enter the coordinates you wish to bombard the enemy ship:")
                    if len(player_guess) == 3:
                        player_guess_record.append(player_guess)
                    
                    
                    
                    try:
                     
                        x,y = player_guess.split(",")
                        x = int(x)
                        y = int(y)
                        if x > 4 or x < 0 or y > 4 or y < 0:
                            print("Invalid value! Both numbers must be a number between 0 and 4")
                            continue
                        player_hit = (x * 5) + y + 1
                    except ValueError:
                        print("Wrong format. Try, for example '2,3'")
                        continue

                    if len(computer_sea[player_hit - 1]) > 3:

                        del computer_sea[player_hit -1][3]
                        print("\n" + "*" * 100 + "\n" + "HIT! You landed a hit on a section of one of the computer's ships!")
                        print("*" * 100)
                    else:
                        print("...You missed, unlucky\n" + "-" * 60)
                    turn+=1
                    #hit_box = 0
                    #if turn is an even number(incremented by one after each player turn) it is the computers turn.
                    if turn % 2 == 0:
                        
                        input("\nEnter when you are ready for the computer's turn...\n")
                        turn+=1
                        rounds_survived+=1


                    mapp = PositionTracker.computer_guess(sea, mapp, cord_pool_x, i1, i2)
