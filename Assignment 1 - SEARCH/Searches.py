from States import State, INF_State
from Romania import Romanian_Map

################################################################################
# Breadth-First Search
################################################################################
def print_BFS(n:int, targetName:str):
    res = breadthFirst(State(n), targetName)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timed_BFS(n:int, targetName:str):
    breadthFirst(State(n), targetName)

def measured_BFS(n:int, targetName:str)->int:
    res = breadthFirst(State(n), targetName)
    if res.outcome:
        return res.cost
    else:
        return 9999

def breadthFirst(st: State, targetName: str) -> State:
    # Initialize the frontier as a FIFO queue
    frontier = [State(currNode=st.currNode, cost=st.cost, path=[st.currNode])]
    # Explored as a set - does not allow duplicates
    explored = set()

    while frontier: #while frontier is not empty

        #pop first element from FIFO queue
        current_state = frontier.pop(0)
        current_node = current_state.currNode

        #if we arrived at goal, return State
        if Romanian_Map.NAMES[current_node - 1] == targetName:
            current_state.outcome = 1 #1=success
            return current_state

        #add the node we visited to explored
        explored.add(current_node)

        #iterate through all child nodes (or edges/paths to explore)
        for edge in Romanian_Map.ADJ_MAT[current_node - 1]:
            child_node, path_cost = edge #[node, weight]
            #add all child elements to FIFO queue if they are unexplored and not present in the FIFO queue
            if child_node not in explored and not any(st.currNode == child_node for st in frontier): #any() returns True, if any of the iterables in a list are True
                new_path = current_state.path + [child_node]
                new_cost = current_state.cost + path_cost
                new_st = State(currNode=child_node, cost=new_cost, path=new_path)

                #if any of the children are successes, return it immediately
                if Romanian_Map.NAMES[child_node - 1] == targetName:
                    new_st.outcome = 1
                    return new_st

                frontier.append(new_st)

    # If no solution is found, return with failure
    st.outcome = 0
    return st

################################################################################
# Depth-First Search
################################################################################
def print_DFS(n:int, targetName:str):
    res = depthFirst(n, targetName)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timed_DFS(n:int, targetName:str):
    depthFirst(n, targetName)

def measured_DFS(n:int, targetName:str)->int:
    res = depthFirst(n, targetName)
    if res.outcome:
        return res.cost
    else:
        return 9999

# calls the recursive function with a instantiated State and a limit of 20 recursive depth (only 20 nodes in the data)
def depthFirst(n: int, targetName: str) -> State:
    return recurDepthFirst(State(currNode=n, path=[n]), targetName, 20)

def recurDepthFirst(st: State, targetName: str, limit: int) -> State:
    #if we have arrived at the goal, return the successful State
    if Romanian_Map.NAMES[st.currNode - 1] == targetName:
        st.outcome = 1 #1=true
        return st

    #We have reached our maximum recursive depth, return the current State as a failure
    elif limit == 0:
        st.outcome = 0
        return st

    else:
        cutoff_occurred = False#to track cutoffs

        #Iterate through all the children (automatically in order as the adj_mat is in order already)
        for edge in Romanian_Map.ADJ_MAT[st.currNode - 1]:

            #create a new state with the options present - first to last
            child_node, path_cost = edge
            new_path = st.path + [child_node]
            new_cost = st.cost + path_cost
            new_st = State(currNode=child_node, cost=new_cost, path=new_path)

            #recursively check if that option results in a success or cutoff
            res = recurDepthFirst(new_st, targetName, limit - 1)

            if res.outcome:
                return res

            elif res.outcome == 0:
                cutoff_occurred = 1

            """To note*: State.outcome is by default the int 2, 
                so if the child option (we set the value to res) is not 1 or 0 (Success or failure)
                we will keep looping regardless
            """

        if cutoff_occurred:
            return State(currNode=st.currNode, cost=st.cost, path=st.path, outcome=0)
        return st

################################################################################
# Greedy Search
################################################################################
def print_greedy(n:int, targetName:str, option:int):
    if option ==1:
        res,cost =  lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.SLD_Heuristic)
    else:
        res,cost =  lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.NODES_AWAY_Heuristic)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timed_Greedy(n:int, targetName:str, option:int):
    if option ==1: #selected heuristic is SLD
        lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.SLD_Heuristic)
    else:
        lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.NODES_AWAY_Heuristic)

def measured_Greedy(n:int, targetName:str, option:int)->int:
    if option ==1: #selected heuristic is SLD
        res,c = lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.SLD_Heuristic)
    else:
        res,c = lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.NODES_AWAY_Heuristic)
    if res.outcome:
        return res.cost
    else:
        return 9999

def lim_greedy(targetName:str, st:INF_State, f_lim:int, INFORMED_Heur):
    #recursive function so we check if the current State is at the goal or not, and return if it is
    if Romanian_Map.NAMES[st.currNode - 1] == targetName:
        st.outcome = 1#1=true
        return st, st.f_cost
    
    #successors are a list of states with a measured f_cost using the heuristic of choice
    successors = []
    #make a new INF_State for each child option/dege
    for child in Romanian_Map.ADJ_MAT[st.currNode - 1]:
        child_node, child_cost = child
        new_path = st.path + [child_node]
        new_cost = st.cost + child_cost
        new_st = INF_State(currNode=child_node, path=new_path, cost=new_cost)
        successors.append(new_st)

    #if there are no options left to us, and since we already checked if we met the target yet, return a failure
    if not successors:
        st.outcome = 0
        return st, 9999  # 9999 is just a substitute for a cost since the function has to return a (State, int) tuple

    # Update f_cost for successors
    for node_st in successors:
        #f(n) = h(n)
        node_st.f_cost = INFORMED_Heur[node_st.currNode - 1]

    #Traverse States until a success or failure occurs
    while True: 
        #sort options by heuristic cost
        successors = sorted(successors, key=lambda x: x.f_cost)

        #find the best option
        best = successors[0]

        #if our best heuristic cost is worse than the maximum limit cost, return it as there is no need to traverse further
        if best.f_cost > f_lim:
            return st, best.f_cost

        #keep the second-best option if there is one
        alt = 9999 #high cost if no second-option
        if len(successors) > 1:
            alt = successors[1].f_cost

        #recursively call with our best child/option/path
        result, best.f_cost = lim_greedy(targetName, best, min(f_lim, alt), INFORMED_Heur)

        if result.outcome == 0:
            return st, best.f_cost
        if result.outcome == 1:
            return result, best.f_cost
        
        """To note*: State.outcome is by default the int 2, 
                so if the child option (we set the value to res) is not 1 or 0 (Success or failure)
                we will keep looping regardless
        """

################################################################################
# A* Search
################################################################################
def print_A_star(n:int, targetName:str, option:int):
    if option ==1: #selected heuristic is SLD
        res,cost =  lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.SLD_Heuristic)
    else:
        res,cost =  lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800, [i*100 for i in Romanian_Map.NODES_AWAY_Heuristic]) #The way the A* f_cost is calculated the base values of the nodes away heuristic won't work, so we approximate them to be larger
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timed_A_Star(n:int, targetName:str, option:int):
    if option ==1: #selected heuristic is SLD
        lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.SLD_Heuristic)
    else:
        lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800, [i*100 for i in Romanian_Map.NODES_AWAY_Heuristic]) #The way the A* f_cost is calculated the base values of the nodes away heuristic won't work, so we approximate them to be larger

def measured_A_Star(n:int, targetName:str, option:int)->int:
    if option ==1: #selected heuristic is SLD
        res,c = lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800, Romanian_Map.SLD_Heuristic)
    else:
        res,c = lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800, [i*100 for i in Romanian_Map.NODES_AWAY_Heuristic]) #The way the A* f_cost is calculated the base values of the nodes away heuristic won't work, so we approximate them to be larger
    if res.outcome:
        return res.cost
    else:
        return 9999
    
def lim_A_Star(targetName: str, st: INF_State, f_lim: int, INFORMED_Heur):
    #recursive function so we check if the current State is at the goal or not, and return if it is
    if Romanian_Map.NAMES[st.currNode - 1] == targetName:
        st.outcome = True
        return st, st.f_cost

    #successors are a list of states with a measured f_cost using the heuristic of choice
    successors = []
    #make a new INF_State for each child option/dege
    for child in Romanian_Map.ADJ_MAT[st.currNode - 1]:
        child_node, child_cost = child
        new_path = st.path + [child_node]
        new_cost = st.cost + child_cost
        new_st = INF_State(currNode=child_node, path=new_path, cost=new_cost)
        successors.append(new_st)

    #if there are no options left to us, and since we already checked if we met the target yet, return a failure
    if not successors:
        st.outcome = 0
        return st, 9999  # 9999 is just a substitute for a cost since the function has to return a (State, int) tuple

    # Update f_cost for successors
    for node_st in successors:
        #f(n) = g(n) + h(n)
        node_st.f_cost = max(node_st.cost + INFORMED_Heur[node_st.currNode - 1], st.f_cost)

    #Traverse States until a success or failure occurs
    while True: 
        #sort options by heuristic cost
        successors = sorted(successors, key=lambda x: x.f_cost)
        best = successors[0]

        #find the best option
        best = successors[0]

        #if our best heuristic cost is worse than the maximum limit cost, return it as there is no need to traverse further
        if best.f_cost > f_lim:
            return st, best.f_cost

        #keep the second-best option if there is one
        alt = 9999 #high cost if no second-option
        if len(successors) > 1:
            alt = successors[1].f_cost

        #recursively call with our best child/option/path
        res, best.f_cost = lim_A_Star(targetName, best, min(f_lim, alt), INFORMED_Heur)

        if res.outcome == 0:
            return st, best.f_cost

        if res.outcome == 1:
            return res, best.f_cost
        
        """To note*: State.outcome is by default the int 2, 
                so if the child option (we set the value to res) is not 1 or 0 (Success or failure)
                we will keep looping regardless
        """