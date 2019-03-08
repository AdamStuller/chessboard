from node import Node
import config
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

    def get_final_state(self):
        f = 0 
        for i in range(0 , self.__size):
            f |= 1 << i
        return f

    def init_arrs(self):
        self.__preds = {}
        self.__front = []

    def __init__(self , width , height ):
        self.__width = width
        self.__height = height
        self.__size = width * height
        self.init_arrs()
        self.__finalstate = self.get_final_state()
       

    def get_neighbors(self ,old_node):

        x = Chessboard.get_x(old_node.pos , self.__width)
        y = Chessboard.get_y(old_node.pos , self.__width)
        neighbors = []
       
        borders = [(-1 , -2) , (-2 , -1) , (-2 , 1) , (-1 , 2) , (1 , 2) , (2 , 1) , (2 , -1 ) , (1 , -2)]
        for l, r in borders:
            if self.__height > x + l >= 0 and self.__width > y + r >= 0 :
                npos = Chessboard.get_pos(x + l , y + r , self.__width)
                
                if not old_node.visited(npos):
                    new_node = Node(npos , old_node.node_id , self.__size)
                    neighbors.append(new_node)

        return neighbors 


    def heuristics(self , neighbors) -> int:
        if len(neighbors) == 0:
            return []
        
        new_list = map(lambda x: (x , len(self.get_neighbors(x))) , neighbors)
            
        return list (map( lambda x : x[0], list(  reversed(sorted( new_list , key = lambda x: x[1])))))  

    def backtrace(self , node_id ):
        output = []
        while node_id != 0:
            output.append(Node.get_pos(node_id , self.__size))
            node_id = self.__preds[str(node_id)]
        return list(reversed(output))
         

    def depth_first_search(self , start , limit):
        self.init_arrs()
        self.__front.append(Node(start , 0 , self.__size))

        for i in range(0 , limit) :
            
            if not self.__front:
                break
            curr = self.__front.pop()
            
            self.__preds[str(curr.node_id)] = curr.pred_id
            
            if self.__finalstate == curr.state:
                return self.backtrace(curr.node_id )
            
            neighbors = self.heuristics(self.get_neighbors(curr))

            for item in neighbors:
                self.__front.append(item)

        return []

    def get_tours(self ):

        limit = config.get('limit')

        for i in range(0 , self.__size):
            out = self.depth_first_search(i , limit)
            if out:
                print('Start: ' + str(i) + ', Output: ' + str(out))
                self.print_board(list(map(lambda x: out.index(x) , range(0 , self.__size))))
                print()
            else:
                print('Start: ' + str(i) + ' has no tour or could not be found')
        

    def print_board(self , output):
        for i in range(0 , self.__size):
            if not i % self.__width:
                print('\n-----------------------')
                print('|' ,end = ' ')
            print(output[i] , end=" | ")
        print('\n-------------------------')
             
            
    
my_chessboard = Chessboard(config.get('width') , config.get('height'))
my_chessboard.get_tours()

