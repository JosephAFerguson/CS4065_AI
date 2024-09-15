from States import State, INF_State
from Romania import Romanian_Map

################################################################################
# Breadth-First Search
################################################################################
def BFS(n:int, targetName:str):
    res = breadthFirst(State(n), targetName)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timedBRS(n:int, targetName:str):
    breadthFirst(State(n), targetName)

def breadthFirst(st: State, targetName: str) -> State:
    # Initialize the frontier as a FIFO queue
    frontier = [State(currNode=st.currNode, cost=st.cost, path=[st.currNode])]
    explored = set()

    while frontier:
        current_state = frontier.pop(0)
        current_node = current_state.currNode

        if Romanian_Map.NAMES[current_node-1] == targetName:
            current_state.outcome = 1
            return current_state

        explored.add(current_node)

        for edge in Romanian_Map.ADJ_MAT[current_node - 1]:
            child_node, path_cost = edge
            if child_node not in explored and not any(state.currNode == child_node for state in frontier):
                new_path = current_state.path + [child_node]
                new_cost = current_state.cost + path_cost
                new_st = State(currNode=child_node, cost=new_cost, path=new_path)

                if Romanian_Map.NAMES[child_node-1] == targetName:
                    new_st.outcome = 1
                    return new_st

                frontier.append(new_st)

    # If no solution is found, return with failure
    st.outcome = 0
    return st

################################################################################
# Depth-First Search
################################################################################
def DFS(n:int, targetName:str):
    res = depthFirst(n, targetName)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timedDFS(n:int, targetName:str):
    depthFirst(n, targetName)

#dfs may not work as expected
def depthFirst(n: int, targetName: str) -> State:
    return recurDepthFirst(State(currNode=n, path=[n]), targetName, 20)

def recurDepthFirst(st: State, targetName: str, limit: int) -> State:
    if Romanian_Map.NAMES[st.currNode - 1] == targetName:
        st.outcome = 1
        return st

    elif limit == 0:
        st.outcome = 0
        return st

    else:
        cutoff_occurred = False
        for edge in Romanian_Map.ADJ_MAT[st.currNode - 1]:
            child_node, path_cost = edge
            new_path = st.path + [child_node]
            new_cost = st.cost + path_cost
            new_st = State(currNode=child_node, cost=new_cost, path=new_path)

            res = recurDepthFirst(new_st, targetName, limit - 1)

            if res.outcome:
                return res

            elif res.outcome == 0:
                cutoff_occurred = 1

        if cutoff_occurred:
            return State(currNode=st.currNode, cost=st.cost, path=st.path, outcome=0)
        return st

################################################################################
# Greedy Search
################################################################################
def greedy(n:int, targetName:str):
    res,cost =  lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timedGreedy(n:int, targetName:str):
    lim_greedy(targetName, INF_State(currNode=n, path=[n]), 800)

def lim_greedy(targetName:str, st:INF_State, f_lim:int):
    if Romanian_Map.NAMES[st.currNode - 1] == targetName:
        st.outcome = True
        return st, st.f_cost
    successors = []
    for child in Romanian_Map.ADJ_MAT[st.currNode - 1]:
        child_node, child_cost = child
        new_path = st.path + [child_node]
        new_cost = st.cost + child_cost
        new_st = INF_State(currNode=child_node, path=new_path, cost=new_cost)
        new_st.f_cost = new_cost + Romanian_Map.INFORMED_Heur[child_node - 1]
        successors.append(new_st)

    if not successors:
        st.outcome = 0
        return st, 9999  # No successors, return failure

    # Update f_cost for successors
    for node_st in successors:
        #f(n) = g(n) + h(n)
        node_st.f_cost = Romanian_Map.INFORMED_Heur[node_st.currNode - 1]

    while True:
        successors = sorted(successors, key=lambda x: x.f_cost)
        best = successors[0]

        if best.f_cost > f_lim:
            return st, best.f_cost

        alt = int(9999)

        if len(successors) > 1:
            alt = successors[1].f_cost
        else:
            alt = int(9999)  # If only one successor, no alternative

        result, best.f_cost = lim_greedy(targetName, best, min(f_lim, alt))

        if result.outcome == 0:
            return st, best.f_cost

        if result.outcome == 1:
            return result, best.f_cost

################################################################################
# A* Search
################################################################################
def A_star(n:int, targetName:str):
    res,cost =  lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800)
    if res.outcome:
        print("Cost:", res.cost)
        print("Path:", [Romanian_Map.NAMES[node - 1] for node in res.path])

def timedA_Star(n:int, targetName:str):
    lim_A_Star(targetName, INF_State(currNode=n, path=[n]), 800)

def lim_A_Star(targetName: str, st: INF_State, f_lim: int):
    if Romanian_Map.NAMES[st.currNode - 1] == targetName:
        st.outcome = True
        return st, st.f_cost

    # Generate successors
    successors = []
    for child in Romanian_Map.ADJ_MAT[st.currNode - 1]:
        child_node, child_cost = child
        new_path = st.path + [child_node]
        new_cost = st.cost + child_cost
        new_st = INF_State(currNode=child_node, path=new_path, cost=new_cost)
        new_st.f_cost = new_cost + Romanian_Map.INFORMED_Heur[child_node - 1]
        successors.append(new_st)

    if not successors:
        st.outcome = 0
        return st, 9999  # No successors, return failure

    # Update f_cost for successors
    for node_st in successors:
        #f(n) = g(n) + h(n)
        node_st.f_cost = max(node_st.cost + Romanian_Map.INFORMED_Heur[node_st.currNode - 1], st.f_cost)

    while True:
        successors = sorted(successors, key=lambda x: x.f_cost)
        best = successors[0]

        if best.f_cost > f_lim:
            return st, best.f_cost

        alt = int(9999)

        if len(successors) > 1:
            alt = successors[1].f_cost
        else:
            alt = int(9999)  # If only one successor, no alternative

        result, best.f_cost = lim_A_Star(targetName, best, min(f_lim, alt))


        if result.outcome == 0:
            return st, best.f_cost


        if result.outcome == True:
            return result, best.f_cost
