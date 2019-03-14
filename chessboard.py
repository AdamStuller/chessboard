from node import Node
from config import __config_values as config

class Chessboard:

    @staticmethod
    def get_x(pos : int, width : int) -> int:
        """
        Utility method used for calculating x coordinate
        :param pos: int
            Field position number
        :param width: int
            Width of the board
        :return: int
            X coordinate
        """
        return pos % width


    @staticmethod
    def get_y(pos : int , width : int) -> int:
        """
        Utility method used for calculating y coordinate
        :param pos:  int
            Field position number
        :param width: int
            Width of board
        :return: int
            Y coordinate
        """
        return pos // width

    @staticmethod
    def get_pos(x : int, y : int, width : int) -> int:
        """
        Utility method used for calculating position on chessboard
        :param x: int
            X coordinate
        :param y: int
            Y coordinate
        :param width: int
            Width of board
        :return: int
            Position of field on chessboard
        """
        return y * width + x

    def get_final_state(self):
        """Calculates final state, that needs to be achieved for solution to be found
        :return: int
            Final state
        """
        f = 0 
        for i in range(0 , self.__size):
            f |= 1 << i
        return f

    def init_arrs(self):
        """
        Initializes empty preds dictionary, that contains predecessors and front that is used for search
        """
        self.__preds = {}
        self.__front = []

    def __init__(self , width , height ):
        self.__width = width
        self.__height = height
        self.__size = width * height
        self.init_arrs()
        self.__finalstate = self.get_final_state()
       

    def get_neighbors(self ,old_node) :
        """
        Returns list of all possible next nodes. Tries every position within horse's reach and validates it.
        If the position has not yet been visited and is within the borders of board, it is added to neighbors list.

        :param old_node: Node
            Predecessor node, instance of Node class.
        :return: list
            List of all possible neighboring node IDs.
        """
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


    def heuristics(self , neighbors):
        """
        Applies heuristic on given list of neighbors and reorders the list according to heuristics.

        :param neighbors: list
            List of all reachable neighboring fields on chessboard that can be futher explored.
        :return: list
            Reordered list of neighbors or empty list if no neighbors are available.
        """
        if len(neighbors) == 0:
            return []
        
        new_list = map(lambda x: (x, len(self.get_neighbors(x))), neighbors)
            
        return list(map(lambda x: x[0], list(reversed(sorted(new_list, key=lambda x: x[1])))))

    def backtrace(self , node_id ):
        """
        Backtraces predecessors of nodes, thus reconstructing path from initial state to final one.
        :param node_id: int
            ID of last, final node
        :return: list
            Complete list of positions one must go on with horse to get to final state.
        """
        output = []
        while node_id != 0:
            output.append(Node.get_pos(node_id , self.__size))
            node_id = self.__preds[str(node_id)]
        return list(reversed(output))
         

    def depth_first_search(self , start , limit):
        """
        Function that implements depth first search to find final state.
        :param start: int
            Starting position of the search
        :param limit: int
            Maximum number of iterations the loop does before terminating and giving up on finding solution.
        :return: list
            Backtraced list of positions
        """
        self.init_arrs()
        self.__front.append(Node(start , 0 , self.__size))

        for i in range(0, limit):
            
            if not self.__front:
                break
            curr = self.__front.pop()
            
            self.__preds[str(curr.node_id)] = curr.pred_id
            
            if self.__finalstate == curr.state:
                return self.backtrace(curr.node_id)
            
            if config.get("heuristics"):
                neighbors = self.heuristics(self.get_neighbors(curr))
            else:
                neighbors = self.get_neighbors(curr)

            for item in neighbors:
                self.__front.append(item)

        return []

    def get_tours(self):
        """
        Method that runs depth first search on all possible positions on chessboard
        """

        limit = config.get('limit')

        for i in range(0 , self.__size):
            out = self.depth_first_search(i , limit)
            if out:
                print('Start: ' + str(i) + ', Output: ' + str(out))
                if config.get("print_board"):
                    self.print_board(list(map(lambda x: out.index(x) , range(0 , self.__size))))
                print()
            else:
                print('Start: ' + str(i) + ' has no tour or could not be found')
        

    def print_board(self , output):
        """
        Method that prints the chessboard with numbered fields. So the result of search can be manually validated.
        :param output: list
            Output from depth first search.
        """
        for i in range(0 , self.__size):
            if not i % self.__width:
                print('\n' + self.__width * '-----')
                print('|',end = ' ')
            print(output[i] , end=" | ")
        print('\n' + self.__width * '-----')
             


def main():
    my_chessboard = Chessboard(config.get('width'), config.get('height'))
    my_chessboard.get_tours()

if __name__== "__main__":
    main()

