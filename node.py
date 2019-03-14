class Node:

    @staticmethod
    def get_node_id( state , pos , mapsize):
        """
        Utility method to calculate node id
        :param state: int
            Node state
        :param pos: int
            Position on the board
        :param mapsize: int
            Size of chessboard
        :return: int
            Node id
        """
        return state * mapsize + pos

    @staticmethod
    def get_pos(node_id , mapsize):
        """
        Utility method to calculate position on board
        :param node_id: int
        :param mapsize: int
            Size of chessboard
        :return: int
            Position on the chessboard
        """
        try:
            return node_id % mapsize
        except ZeroDivisionError:
            return 0


    @staticmethod
    def get_state(node_id , mapsize):
        """
        Utility method that returns state of node
        :param node_id: int
        :param mapsize: int
            Size of chessboard
        :return: int
            State of node
        """
        return node_id // mapsize

    @staticmethod
    def add_to_visited(state , pos):
        """
        Utility method that modifies state of old node, adding its position to visited. It does so by setting bit that
        belongs to old position in state to 1.
        :param state: int
            Old state
        :param pos: int
            Position on the map
        :return: int
            New state that knows old position has already been visited
        """
        return state | ( 1 << pos ) 

    def visited(self ,  pos):
        """
        Utility method that checks wheter position has already been visited in current state. It checks if 1 on
        position-th bit in state.
        :param pos: int
            Current position that is validated
        :return: int
            Either 1 or 0 depending on what is on checked position.
        """
        return ( self.state >>  pos ) & 1 

    def __init__(self , pos , old_id ,  mapsize):
        self.pos = pos
        self.state = Node.add_to_visited(Node.get_state(old_id , mapsize) , pos)
        self.pred_id = old_id
        self.node_id = Node.get_node_id(self.state , pos , mapsize)


        
