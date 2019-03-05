class Chessboard:

    """Returns x coordinate from position and width"""
    @staticmethod
    def get_x(pos : int, width : int) -> int: 
        return pos % width

    """Returns y coordinate from position and width"""
    @staticmethod
    def get_y(pos : int , width : int) -> int:
        return pos // width

    """Returns position from x and y coordinates"""
    @staticmethod
    def get_pos(x : int, y : int, width : int) -> int :
        return y * width + x

    def __init__(self , width , height ):
        self.width = width
        self.height = height
        self.size = width * height
        self.visited = set()    # already visited fields
        self.preds = {}         # predecessors

    def get_neighbors(self , pos):
        x = Chessboard.get_x(pos , self.width)
        y = Chessboard.get_y(pos , self.width)
        neighbors = []
       
        #Checking borders
        borders = [(-1 , -2) , (-2 , -1) , (-2 , 1) , (-1 , 2) , (1 , 2) , (2 , 1) , (2 , -1 ) , (1 , -2)]
        for l, r in borders:
            if self.height > x + l >= 0 and self.width > y + r >= 0 :
                npos = Chessboard.get_pos(x + l , y + r , self.width)
                try:
                    if npos not in self.visited and self.preds[str(npos)] != pos:
                        neighbors.append(npos)
                    elif self.preds[str(npos)] == pos:
                        print(npos)
                except KeyError:
                    neighbors.append(npos)

        return neighbors 


    def heuristics(self , neighbors) -> int:
        if len(neighbors) == 0:
            return -1
        
        min = [9 , 0] # maximum number of adjacent fields is 8
        for field in neighbors:
            degree = len(self.get_neighbors(field))
            if degree < min[0]:
                min[0] = degree
                min[1] = field 
        return min[1]
        
    def backtrace(self , last_pos):
        temp = last_pos
        output = []
        while temp != -1:
            output.append(temp)
            temp = self.preds[str(temp)]
        return list(reversed(output))

    def deep_first_search(self , start):
        
        new_pos = start
        old_pos = -1

        neighbors = ['dummy :)']

        for i in range(0, 100):

            self.preds[str(new_pos)] = old_pos
            self.visited.add(old_pos)

            neighbors = self.get_neighbors(new_pos)
            
            old_pos = new_pos
            new_pos = self.heuristics(neighbors)
            # print('haloc' + str(new_pos))

            

            if new_pos == -1:
                output = []
                if len(self.visited) == self.size:
                    output = self.backtrace(old_pos)
                    self.preds = {}
                    self.visited = set()
                    return output
                else:
                    old_temp = old_pos
                    self.visited.add(old_pos)
                    #here we have to return back so we can find another way
                    while neighbors == []:
                        temp = self.preds[str(old_temp)]
                        # print(old_temp)
                        # print(temp)
                        #print(self.visited)
                        self.visited.remove(old_temp)
                        old_temp = temp
                        neighbors = self.get_neighbors(temp)
                        # print(neighbors)
                    print('returned to:' + str(temp))
                    new_pos = temp
                    old_pos = self.preds[str(new_pos)]
                    
                

    def find_way(self):
        for  i in range(0 , self.size):
            output = self.deep_first_search(i)
            if len(output) > 0 :
                print(output)    

saska = Chessboard(5 , 5)
saska.find_way()
