from Sea import Sea
from ShipPlacer import ShipPlacer
import random

class AI(Sea):
    

    def placement(self,sea):
        
        ships_valid = True
        k = 0
        while k < 2:
            ships = []
            k = 0
            for i in range(2):
                
                o = random.randint(1,2)
                #if ship is placed vertically, reduce possible veritcal range
                #this prevents ships falling off the edge of the battlefield.
                if i == 0:
                    o = "v"
                    y = random.randint(2,4)
                    x = random.randint(0,4)
                    ships.append([o,x,y])
                #elif ship is placed horizontally, reduce horizontal range
                elif i == 1:
                    o = "h"
                    x = random.randint(0,2)
                    y = random.randint(0,4)
                    ships.append([o,x,y])
                    

            if len(ships) == 2:
                computer_sea = ShipPlacer.check_ship(ships,sea, k)
            else:
                continue

            k = computer_sea[1]
            #sea[2] = sea

        #print(ships)
        ##input("hai")
        ##print(sea[2])
        return computer_sea[2]
        

        
    

