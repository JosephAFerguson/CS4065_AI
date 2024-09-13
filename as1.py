class State:
    def __init__(self, currNode=0, cost=0, outcome=2, path=None):
        if path is None:
            path = []
        self.currNode = currNode
        self.cost = cost
        self.outcome = outcome
        self.path = path.copy()

# SLD heuristics can be found in page 93 of the textbook, or page 112 of the pdf
NODES = [i+1 for i in range(20)]
# Alphabetical list of names
NAMES = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras',
         'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj',
         'Mehadia', 'Neamt', 'Oradea', 'Pitesti',  'Rimnicu Vilcea', 'Sibiu', 
         'Timisoara', 'Urziceni', 'Vaslui', 'Zerind']
INFORMED_Heur = [366,0,160,242,161,176,77,151,226,244,241,234,380,100,193,253,329,80,199,374]
# Adjacency matrix
ADJ_MAT = [ 
    [[17,118], [16,140],[20,75]],   # Arad [node of dest, weight/cost of path]
    [[6,211],[7,90],[14,101],[17,85]],  # Bucharest
    [[4,120],[14,138],[15,146]],   # Craiova
    [[3,120], [11,75]],   # Drobeta
    [[8,86]],   # Eforie
    [[2,211],[16,99]],   # Fagaras
    [[2,90]],   # Giurgiu
    [[5,86],[18,98]],   # Hirsova
    [[12,87],[19,92]],   # Iasi
    [[11,70],[17,111]],   # Lugoj
    [[4,75],[10,70]],   # Mehadia
    [[9,87]],   # Neamt
    [[16,151],[20,71]],   # Oradea
    [[2,101],[3,138],[15,97]],   # Pitesti
    [[3,146],[14,97],[16,80]],   # Rimnicu Vilcea
    [[1,140],[6,99],[13,151],[16,80]],   # Sibiu
    [[1,118],[10,111]],   # Timisoara
    [[2,85],[8,98],[19,142]],   # Urziceni
    [[9,92],[18,142]],   # Vaslui
    [[1,75],[13,71]],   # Zerind
]

def breadthFirst(st: State, targetName: str) -> State:
    # Initialize the frontier as a FIFO queue
    frontier = [State(currNode=st.currNode, cost=st.cost, path=[st.currNode])]
    explored = set()
    
    while frontier:
        current_state = frontier.pop(0)
        current_node = current_state.currNode
        
        if NAMES[current_node-1] == targetName:
            current_state.outcome = 1
            return current_state
        
        explored.add(current_node)
        
        for edge in ADJ_MAT[current_node - 1]:
            child_node, path_cost = edge
            if child_node not in explored and not any(state.currNode == child_node for state in frontier):
                new_path = current_state.path + [child_node]
                new_cost = current_state.cost + path_cost
                new_state = State(currNode=child_node, cost=new_cost, path=new_path)
                
                if NAMES[child_node-1] == targetName:
                    new_state.outcome = 1
                    return new_state
                
                frontier.append(new_state)

    # If no solution is found, return with failure
    st.outcome = 0
    return st

def depthFirst(n: int, targetName: str, limit: int) -> State:
    return recurDepthFirst(State(currNode=n, path=[n]), targetName, limit)

def recurDepthFirst(st: State, targetName: str, limit: int) -> State:
    if NAMES[st.currNode - 1] == targetName:
        st.outcome = True
        return st
    
    elif limit == 0:
        st.outcome = False
        return st
    
    else:
        cutoff_occurred = False
        for edge in ADJ_MAT[st.currNode - 1]:
            child_node, path_cost = edge
            new_path = st.path + [child_node]
            new_cost = st.cost + path_cost
            new_st = State(currNode=child_node, cost=new_cost, path=new_path)
            
            res = recurDepthFirst(new_st, targetName, limit - 1)
            
            if res.outcome:
                return res
            
            elif res.outcome == 0:
                cutoff_occurred = True
        
        if cutoff_occurred:
            return State(currNode=st.currNode, cost=st.cost, path=st.path, outcome=False)
        return st
def greedy(st:State, targetName:str)->State:
    
"""
# Perform depth-limited search from each node with a depth limit
depth_limit = 10  # Adjust the depth limit as necessary
goals = []
for i in range(20):
    goals.append(depthFirst(i + 1, 'Bucharest', depth_limit))

# Print the results for each search
for goal in goals:
    if goal.outcome:
        print("Cost:", goal.cost)
        print("Path:", [NAMES[node - 1] for node in goal.path])
"""
