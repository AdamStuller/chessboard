class Node:

    """Returns node_id from position on map and mapsize"""
    @staticmethod
    def get_node_id( state , pos , mapsize):
        return state * mapsize + pos

    """Returns position on the map from node_id and state"""
    @staticmethod
    def get_pos(node_id , mapsize):
        try:
            return node_id % mapsize
        except ZeroDivisionError:
            return 0

    """Returns state from node_id and position on the map"""
    @staticmethod
    def get_state(node_id , mapsize):
        return node_id // mapsize

    """Adds another field of position on map to visited"""
    @staticmethod
    def add_to_visited(state , pos):
        return state | ( 1 << pos ) 

    """"Checks wheter position has already been visited"""
    def visited(self ,  pos):
        return ( self.state >>  pos ) & 1 

    def __init__(self , pos , old_id ,  mapsize):
        self.pos = pos
        self.state = Node.add_to_visited(Node.get_state(old_id , mapsize) , pos)
        self.pred_id = old_id
        self.node_id = Node.get_node_id(self.state , pos , mapsize)


        
