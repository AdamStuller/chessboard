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

    def set_arrs(self):
        self.preds = [ -1 for x in range(0 , self.size)]  
        self.front = [ [] for x in range(0 , self.size)]
        self.visited = set()

    def __init__(self , width , height ):
        self.width = width
        self.height = height
        self.size = width * height
        # self.visited = set()    # already visited fields
        # self.preds = [ -1 for x in range(0 , self.size)]         # predecessors

        # self.front = [ [] for x in range(0 , self.size)]
        self.set_arrs

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
        
    def backtrace(self , last_pos):
        temp = last_pos
        output = []
        while temp != -1:
            output.append(temp)
            temp = self.preds[str(temp)]
        return list(reversed(output))

    def depth_first_search(self , start):
        
        self.set_arrs()
        i = 0
        self.front[i] = [start]
        while len(self.front) > 0:

            if i < 0 :
                return False

            print(str(i) + str(self.visited))
            print(str(i) + str(self.preds))
            if self.front[i]:
                curr = self.front[i].pop(0)
            else:
                print('empty!')
                print(self.preds)
                print(self.visited)
                print('removing: '+ str(self.preds[i]))
                self.visited.remove(self.preds[i])
                self.preds[i] = -1
                print(self.preds)
                print(self.visited)
                i = i - 1
                continue
            print('halloc')
            self.visited.add(curr)
            self.preds[i] = curr
            children = self.heuristics(self.get_neighbors(curr))
            # print('children: ' + str(i) + str(children) + str(curr))
            # print(self.preds)
            

            if children:
                i = i + 1
                self.front[i] = children
                print(i)
            else:
                if len(self.visited) == self.size:
                    return self.preds
                
                print(self.preds)
                print(self.visited)
                print('removing: '+ str(self.preds[i]) + ' ' + str(i))
                self.visited.remove(self.preds[i])
                self.preds[i] = -1
                i = i - 1
                print(self.preds)
                print(self.visited)

            

saska = Chessboard(5 , 5)

# for i in range(0 , saska.size):
out = saska.depth_first_search(1)
print('output:' + str(out) )
print('set: ' + str(saska.visited) )

