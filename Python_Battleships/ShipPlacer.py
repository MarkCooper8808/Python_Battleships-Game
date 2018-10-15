from Sea import Sea



class ShipPlacer(Sea):
        #this function checks if the ships are valid, and then places them in the player Sea list.
        def check_ship(ships, sea, i):
                ship1 = ships[0]
                ship2 = ships[1]
                ship1_o = ships[0][0]
                ship1_x = int(ships[0][1])
                ship1_y = int(ships[0][2])
                ship2_o = ships[1][0]
                ship2_x = int(ships[1][1])
                ship2_y = int(ships[1][2])
                s1_co = []
                s2_co = []
                ship_valid = []
                ship_valid.append(True)
                ship_valid.append(i)
                
                if ship1_o == "v":
                        s1_c = ship1_x * 5 + ship1_y
                        s1_co.append(s1_c)
                        for i in range (1,3,1):
                                s1_c = ship1_x * 5 + ship1_y - i
                                s1_co.append(s1_c)
                elif ship1_o =="h":
                        s1_c = ship1_x * 5 + ship1_y
                        s1_co.append(s1_c)
                        for i in range (2):
                                s1_c = (ship1_x + i) * 5
                                s1_co.append(s1_c)

                if ship2_o == "v":
                        s2_c = ship2_x * 5 + ship2_y
                        s2_co.append(s2_c)
                        for i in range (1,3,1):
                                s2_c = (ship2_x * 5) + ship2_y - i
                                s2_co.append(s2_c)
                elif ship2_o =="h":
                        s2_c = ship2_x * 5 + ship2_y
                        s2_co.append(s2_c)
                        for i in range (1,3,1):
                                s2_c = (ship2_x + i) * 5 + ship2_y
                                s2_co.append(s2_c)

                for item in s1_co:
                        for item2 in s2_co:
                                if item == item2:
                                        ship_valid[0] = False
                                        ships = []
                
                               
                if ship_valid[0] == True:
                        for j in range(0, 3, 1):
                                if j == 0:
                                        ship_part = "end"
                                elif j == 1:
                                        ship_part = "middle"
                                elif j == 2:
                                        ship_part = "front"
                                sea[s1_co[j]].append("ship 1 {0}".format(ship_part))
                                sea[s2_co[j]].append("ship 2 {0}".format(ship_part))
                                ship_valid[1]+=2
                                ship_valid.append(sea)
                                
                                
                #print(s1_co, s2_co)
                return ship_valid
                
        
               
        
        #This function is the first function called and asks the human player to place their 2 ships
        def prompt_placement(self, sea, new_map):
               battlefield_map = new_map
               
               print("Your battle area: \n" + battlefield_map)
               game_started = True
               #for i in range(0,2):
               i = 0
               m = False
               s = 1

               ships = []
               
               #moving some of these falses into the while loop may work better - Mark.
               
               while i < 2:
                       try:
                               ship_out_of_bounds = False
                               x_true = False
                               y_true = False
                               o_true = False

                               ship_oxy = input("\nType out SHIP orientation, v for vert(down), h for horiz(right) and coordinates (x,y)" +
                                       "to place ship format example: v,4,4 . Enter Ship {} here: ".format(s))
                               o,x,y = ship_oxy.split(",")
                               o = o.lower()
                               x = int(x)
                               y = int(y)
                               #series of if statements to determine if the player's input was valid
                               if o == "v" and y < 2 or o == "h" and x > 3:
                                       ship_out_of_bounds = True
                               if o != "v" and o != "h":
                                       o_true = True
                               if int(x) > 4 or int(x) < 0:
                                       x_true = True
                               if int(y) > 4 or int(y) < 0:
                                       y_true = True

                               if o_true or x_true or y_true or ship_out_of_bounds:
                                       print(o,x,y)
                                       if ship_out_of_bounds:
                                               print("Placing your 3 tile ship there would put it off the map! Please try placing ship again.")
                                       else:
                                               print("Oops! Not a valid format to place your ship, try again.\n")
                                       x_true = False
                                       y_true = False
                                       o_true = False
                                       ship_out_of_bounds = False
                                       for item in ships:
                                               ships.remove(item)
                                               s = 1
                                       continue


                               if s == 1:
                                       ships.append([o,x,y])
                                       
                                       first_map = ShipPlacer.draw_map(o,x,y,battlefield_map, m, s)
                                       print(first_map)
                                       s+=1
                                       continue
                               if s == 2:
                                       ships.append([o,x,y])
                                       #print(ships)
                                       ships_valid = ShipPlacer.check_ship(ships, sea, i)
                                       #print(ships_valid)
                                       #the 2 lines below are the ones that stop the program getting further
                                       second_map = ShipPlacer.draw_map(o,x,y,first_map, m, s)
                                     
                                     
                                       #ships_valid[0] = False

                               if ships_valid[0] == False:
                                       print(o,x,y)
                                       ships = []
                                       s-=1
                                       print("WARNING: ")
                                       print("Invalid ship placements entered. Ships overlap! Try entering your ships again")
                                       continue
                                       
                                       
                               

                               print(second_map)
                               print()
                               print("Your ships have been placed. Good Luck!")
                       except ValueError:
                               print("Oops! Not a valid format to place your ship, try again.\n")
                               continue
                       
                       
                       #i_valid_input = ShipPlacer.place_ship(o,x,y,sea,i, battlefield_map, game_started,ships)
                       i = ships_valid[1]
        
               i = ships_valid[1]
               sea = ships_valid[2]
               
               sea_and_map = [sea,second_map]
               return sea_and_map
                        
                    
                            


         #this function draws the "map" string for display in the console.
        def draw_map(ori, map_x, map_y, new_map, m, s):
        
            x = map_x
            y = map_y
            o = ori
            sm = []
            map_placement = []
            ship = s
                    
               
            if o == "v" or o == "h":
                    for i in range(0, 3):
                            sm = str(x) + ',' + str(y - i)
                            ym = str(x + i) + ',' + str(y) 
 
                            if i == 0 and m == False and o == "v":
                                    m = True
                                    m = new_map
                                    m1 = m.replace(sm,"S{0}R".format(ship))
                                    xcoord_1 = sm
                            elif i == 0 and m == True and o =="v":
                                    m = m
                                    m1 = m.replace(sm,"S{0}R".format(ship))
                                    xcoord_1 = sm
                            elif i == 1 and o == "v":
                                    m2 = m1
                                    m3 = m2.replace(sm,"S{0}M".format(ship))
                                    xcoord_2 = sm
                            elif i == 2 and o == "v":
                                    final_map = m3.replace(sm,"S{0}F".format(ship))
                                    xcoord_3 = sm
                                    final_map+= "\nShip {3}: [{0}, {1}, {2}]".format(xcoord_1,xcoord_2,xcoord_3, ship)
                            elif i == 0 and m == False and o == "h":
                                    m = True
                                    m = new_map
                                    m1 = m.replace(ym,"S{0}R".format(ship))
                                    ycoord_1 = ym
                            elif i == 0 and m == True and o =="h":
                                    m = m
                                    m1 = m.replace(ym,"S{0}R".format(ship))
                                    ycoord_1 = ym
                            elif i == 1 and o == "h":
                                    m2 = m1
                                    m3 = m2.replace(ym,"S{0}M".format(ship))
                                    ycoord_2 = ym
                            elif i == 2 and o == "h":
                                    final_map = m3.replace(ym,"S{0}F".format(ship))
                                    ycoord_3 = ym
                                    final_map+= "\nShip {3}: [{0}, {1}, {2}]".format(ycoord_1, ycoord_2, ycoord_3, ship)
                                                
                                    
                                
                    
                    return final_map
            


        
            

            
               
        


 
         

        


     

    #prompt_placement()
                      
