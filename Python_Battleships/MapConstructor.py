class MapConstructor:
    def __init__(self):
        self._battle_map = ""
        z = -1
        y = 4
        #creats a new "map" ; for loop adding coordinates y and z to each row
        for x in range(25):
            z+=1
            if x > 0 and x % 5 == 0:
                self._battle_map+="\n"
                y-=1
                z-=5
            self._battle_map+= " " + str(z) + "," + str(y) + "  "

    
