class Sea:
    
     def __init__(self):

        self._width = 5
        self._length = 5
        self.sea = []


        for x in range(self._width):
             for y in range(self._length):
                 key = (x * 5) + y + 1
                 self.sea.append([x,y,key])
           


    
    
