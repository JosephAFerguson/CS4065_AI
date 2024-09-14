class State:
    def __init__(self, currNode=0, cost=0, outcome=2, path=None):
        if path is None:
            path = []
        self.currNode = currNode
        self.cost = cost
        #outcome is mostly represented as booleans (1 is true, 0 is false),
        #however outcome is initialized as 2 which represents an undecided / in progress state.
        #thus outcome is only compared to numbers 0 and 1 respectively, because 2 is seen as false
        self.outcome = outcome
        self.path = path.copy()

#for informed searches, inherits all attributes and constuctor from State
class INF_State(State):
    f_cost = 0