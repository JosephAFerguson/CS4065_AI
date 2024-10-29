
/*Assignment 3 Search in Prolog - Joe Ferguson*/

 /***MAP OF ROMANIA EDGES/PATHS***/
% Define paths with costs based on the adjacency matrix

% Paths from Arad
path(arad, timisoara, 118).
path(arad, sibiu, 140).
path(arad, zerind, 75).

% Paths from Bucharest
path(bucharest, giurgiu, 90).
path(bucharest, hirsova, 85).
path(bucharest, pitesti, 101).
path(bucharest, craiova, 211).
path(bucharest, fagaras, 211).
path(bucharest, urziceni, 85).

% Paths from Craiova
path(craiova, drobeta, 120).
path(craiova, pitesti, 138).
path(craiova, rimnicu_vilcea, 146).

% Paths from Drobeta
path(drobeta, mehadia, 75).
path(drobeta, craiova, 120).

% Paths from Eforie
path(eforie, hirsova, 86).

% Paths from Fagaras
path(fagaras, bucharest, 211).
path(fagaras, sibiu, 99).

% Paths from Giurgiu
path(giurgiu, bucharest, 90).

% Paths from Hirsova
path(hirsova, eforie, 86).
path(hirsova, urziceni, 98).

% Paths from Iasi
path(iasi, neamt, 87).
path(iasi, vaslui, 92).

% Paths from Lugoj
path(lugoj, timisoara, 111).
path(lugoj, mehadia, 70).

% Paths from Mehadia
path(mehadia, drobeta, 75).
path(mehadia, lugoj, 70).

% Paths from Neamt
path(neamt, iasi, 87).

% Paths from Oradea
path(oradea, zerind, 71).
path(oradea, sibiu, 151).

% Paths from Pitesti
path(pitesti, rimnicu_vilcea, 97).
path(pitesti, craiova, 138).
path(pitesti, bucharest, 101).

% Paths from Rimnicu Vilcea
path(rimnicu_vilcea, pitesti, 97).
path(rimnicu_vilcea, craiova, 146).
path(rimnicu_vilcea, sibiu, 80).

% Paths from Sibiu
path(sibiu, arad, 140).
path(sibiu, fagaras, 99).
path(sibiu, rimnicu_vilcea, 80).
path(sibiu, oradea, 151).
path(sibiu, timisoara, 111).

% Paths from Timisoara
path(timisoara, lugoj, 70).
path(timisoara, arad, 118).

% Paths from Urziceni
path(urziceni, hirsova, 85).
path(urziceni, bucharest, 85).

% Paths from Vaslui
path(vaslui, iasi, 92).
path(vaslui, urziceni, 142).

% Paths from Zerind
path(zerind, arad, 75).
path(zerind, oradea, 71).

%failure paths for depth_first check (or others)
path(nowhere, othernowhere,30).
path(othernowhere, nowhere, 30).

% Define SLD Heuristic from Bucharest for A*
sld(arad, 366).
sld(bucharest, 0).
sld(craiova, 160).
sld(drobeta, 242).
sld(eforie, 161).
sld(fagaras, 176).
sld(giurgiu, 77).
sld(hirsova, 151).
sld(iasi, 226).
sld(lugoj, 244).
sld(mehadia, 241).
sld(neamt, 234).
sld(oradea, 380).
sld(pitesti, 100).
sld(rimnicu_vilcea, 193).
sld(sibiu, 253).
sld(timisoara, 329).
sld(urziceni, 80).
sld(vaslui, 199).
sld(zerind, 374).

/*Note: Prolog has compound terms,
*state() is an example of them,
*it stores the goal node (referenced as node), the path, the cost, and the outcome(failure or success)
*/

/******BREADTH FIRST SEARCH ALG*****/
%Here is our query-call where we pass the startnode and targetnode to our actual predicate to find the solution.
%Solution is a state()
breadth_first(StartNode, TargetNode, Solution) :-
    breadth_first([[StartNode, 0, [StartNode]]], [], TargetNode, Solution).

% Base case: the first path
breadth_first([[Node, Cost, Path] | _], _, TargetNode, Solution) :-
    %Note that the operator "=" is a unification operator,
    % it essentially is finding a path from node to target so that eventually (after our travels)
    % we are at the goal
    Node = TargetNode,
    reverse(Path, SolutionPath),
    Solution = state(Node, SolutionPath, Cost, success), % return our solution, or failure
    !. % Cut here to prevent further search once goal is found

% Recursive case: expand the paths and their children
breadth_first([[Node, PathCost, Path] | Frontier], Explored, TargetNode, Solution) :-
    findall( %find all the child/neighbors of this path and define the new path and cost for each one
        [Child, NewCost, [Child | Path]],
        (path(Node, Child, StepCost), NewCost is PathCost + StepCost /*Sum the costs*/, 
         \+ member(Child, Path), \+ member(Child, Explored)),/*holds true if child is not already explored*/
        NewPaths
    ),
    append(Frontier, NewPaths, UpdatedFrontier), %add these children to the end of our frontier
    breadth_first(UpdatedFrontier, [Node | Explored], TargetNode, Solution). %check if the child paths contain our goal

% Failure case: if the frontier is empty and no solution is found
breadth_first([], _, _, state(_, [], 0, failure)).
/***END***/
/******DEPTH FIRST SEARCH******/ 
% Here is our query-call where we pass the start node and target node to our actual predicate to find the solution.
% Solution is a state()
depth_first(StartNode, TargetNode, Solution) :- 
    depth_first([[StartNode, 0, [StartNode]]], [], TargetNode, Solution).

% Base case: if the first path in the stack reaches the target node
depth_first([[Node, Cost, Path] | _], _, TargetNode, Solution) :- 
    Node = TargetNode,
    reverse(Path, SolutionPath),
    Solution = state(Node, SolutionPath, Cost, success), 
    !. % Cut here to prevent further search once the goal is found

% Recursive case: expand the paths going deeper each time (depth-first)
depth_first([[Node, PathCost, Path] | Frontier], Explored, TargetNode, Solution) :- 
    path(Node, Child, StepCost), 
    NewCost is PathCost + StepCost,
    \+ member(Child, Path), 
    \+ member(Child, Explored),
    UpdatedFrontier = [[Child, NewCost, [Child | Path]] | Frontier], % Add to the front
    depth_first(UpdatedFrontier, [Node | Explored], TargetNode, Solution).

% Failure case: if the frontier is empty and no solution is found
depth_first([], _, _, state(_, [], 0, failure)). 
/***END***/
/******A* SEARCH******/
%Here is our query-call where we pass the startnode and targetnode to our actual predicate to find the solution.
%Solution is a state()
a_star(StartNode, TargetNode, Solution) :-
    a_star([[StartNode, 0, [StartNode]]], [], TargetNode, Solution).

% Base case: if the first path in the stack reaches the target node
a_star([[Node, PathCost, Path] | _], _, TargetNode, Solution) :-
    Node = TargetNode,
    reverse(Path, SolutionPath),
    Solution = state(Node, SolutionPath, PathCost, success),
    !.

% Recursive case: expand the paths by using SLD heuristic
a_star([[Node, PathCost, Path] | Frontier], Explored, TargetNode, Solution) :-
    findall(
        [Child, NewPathCost, [Child | Path]],
        ( path(Node, Child, StepCost),
          NewPathCost is PathCost + StepCost, % Calculate the new path cost
          sld(Child, HeuristicCost), % Get the heuristic cost
          TotalCost is NewPathCost + HeuristicCost, % Calculate the total cost
          \+ member(Child, Path), 
          \+ member(Child, Explored) % Holds true if child is not already explored
        ),
        NewPaths
    ),
    insert_paths(NewPaths, Frontier, UpdatedFrontier), % Insert new paths into the sorted frontier
    a_star(UpdatedFrontier, [Node | Explored], TargetNode, Solution).

% Insert new paths into the sorted list maintaining the order based on TotalCost
insert_paths([], Frontier, Frontier). % If there are no new paths, return the original frontier.
insert_paths([[Child, NewPathCost, Path] | Rest], Frontier, UpdatedFrontier) :-
    insert_path([Child, NewPathCost, Path], Frontier, FrontierAfterInsert),
    insert_paths(Rest, FrontierAfterInsert, UpdatedFrontier).

% Insert a single path into the sorted list based on the total cost
insert_path(NewPath, [], [NewPath]). % If the frontier is empty, just add the new path.
insert_path([Child, NewPathCost, Path], [[OtherChild, OtherPathCost, OtherPath] | Rest], [[Child, NewPathCost, Path], [OtherChild, OtherPathCost, OtherPath] | Rest]) :-
    NewPathCost =< OtherPathCost, !. % Insert before the current path if it's cheaper or equal.
insert_path(NewPath, [Current | Rest], [Current | UpdatedRest]) :-
    insert_path(NewPath, Rest, UpdatedRest). % Recur down the list if the new path is more expensive.

% Failure case: if the frontier is empty and no solution is found
a_star([], _, _, state(_, [], 0, failure)).

/****END****/
/***Calling of all the algs for Oradea, Timisoara, and Neamt ***/
%chatgpt was used for this part
do_prog() :-
    % List of test cases
    TestCases = [
        oradea,
        timisoara,
        neamt
    ],
    % Call search algorithms for each test case
    forall(member(StartNode, TestCases), 
        (   call_search_algorithms(StartNode, bucharest)
        )
    ).

% Helper predicate to call all search algorithms
call_search_algorithms(StartNode, TargetNode) :-
    (   call(breadth_first, StartNode, TargetNode, BF_Solution),
        format("Breadth-First Search from ~w to ~w Result: ~w~n", [StartNode, TargetNode, BF_Solution])
    ;   format("Breadth-First Search from ~w to ~w failed.~n", [StartNode, TargetNode])
    ),
    (   call(depth_first, StartNode, TargetNode, DF_Solution),
        format("Depth-First Search from ~w to ~w Result: ~w~n", [StartNode, TargetNode, DF_Solution])
    ;   format("Depth-First Search from ~w to ~w failed.~n", [StartNode, TargetNode])
    ),
    (   call(a_star, StartNode, TargetNode, AStar_Solution),
        format("A* Search from ~w to ~w Result: ~w~n", [StartNode, TargetNode, AStar_Solution])
    ;   format("A* Search from ~w to ~w failed.~n", [StartNode, TargetNode])
    ).

