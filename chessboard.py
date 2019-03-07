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

    # def set_arrs(self):
    #     self.preds = [ -1 for x in range(0 , self.size)]  
    #     self.front = [ [] for x in range(0 , self.size)]
    #     self.visited = set()

    def __init__(self , width , height ):
        self.width = width
        self.height = height
        self.size = width * height
        self.preds = {}
        self.front = []

    def get_neighbors(self , pos):
        x = Chessboard.get_x(pos , self.width)
        y = Chessboard.get_y(pos , self.width)
        neighbors = []
       
        #Checking borders
        borders = [(-1 , -2) , (-2 , -1) , (-2 , 1) , (-1 , 2) , (1 , 2) , (2 , 1) , (2 , -1 ) , (1 , -2)]
        for l, r in borders:
            if self.height > x + l >= 0 and self.width > y + r >= 0 :
                npos = Chessboard.get_pos(x + l , y + r , self.width)
                if npos not in self.visited:
                    neighbors.append(npos)

        return neighbors 


    def heuristics(self , neighbors) -> int:
        if len(neighbors) == 0:
            return []
        
        new_list = map(lambda x: (x , len(self.get_neighbors(x))) , neighbors)
            
        return list (map( lambda x : x[0], list(  sorted( new_list , key = lambda x: x[1]))))

    def depth_first_search(self , start):
        
        # self.set_arrs()
        i = 0
        self.front[i] = [start]
        # print(self.front)
        for limit in range(0 , 1000):
            # print(limit)
            # print(self.preds[i])
            # print(i)

            while i >=0 and not self.front[i] :
                self.visited.remove(self.preds[i])
                self.preds[i] = -1
                i -= 1
                # print('removed')

            if i < 0 :
                return False

            self.preds[i] = self.front[i].pop(0)
            self.visited.add(self.preds[i])
            children = self.heuristics(self.get_neighbors(self.preds[i]))

            if children:
                i += 1
                self.front[i] = children
            elif len(self.visited) == self.size:
                return self.preds
            elif self.preds[i] >= 0:
                self.visited.remove(self.preds[i])
                self.preds[i] = -1
                i -= 1
                # print('removed')
        
            

saska = Chessboard(5 , 5)

for i in range(0 , saska.size):
    out = saska.depth_first_search(i)
    print('output:' + str(out) )
    # print('set: ' + str(saska.visited) )

