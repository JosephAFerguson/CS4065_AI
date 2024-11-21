%%%%% Program Structure %%%%%
% Define blocks in the world
blocks([a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]).


% A generic block, say X, is a member of the list of blocks.
block(X) :-
    blocks(BLOCKS), % This extracts the list BLOCKS
    member(X, BLOCKS).

% There is a path from state S1 to state S2 when there is a move from S1 to S2.
%path(S1, S2) :-
%    action(_, S1, S2).

% Connect is the symmetric version of path: states S1 and S2 are connected 
% if there is a path from S1 to S2 or a path from S2 to S1.
%connect(S1, S2) :- path(S1, S2).
%connect(S1, S2) :- path(S2, S1).

% Ensure the state has not yet been visited
notYetVisited(State, PathSoFar) :-
    list_to_ord_set(State, OrdState),
    list_to_ord_set(PathSoFar, OrdPathSoFar),
    \+ member(OrdState, OrdPathSoFar).%just make them both ordered sets and compare them (faster than permutations)

% Define start and goal states
start([[on, i , f],[on, f, d],[on, d, g], [on, g, h],[on, h, table], [on, o, k], [on, k, e],
        [on, e, table], [clear, i], [clear, o]]).
goal([[on, h, g],[on, g, d], [on, d, f], [on, f, i], [on, i, table], [on, o, table], [on, k, table]
        ,[on, e , table],[clear, h],[clear, o], [clear, k], [clear, e]]).


% Find solution with Iterative Deepening set to a limit of 10 moves
solveWithIDS(Path) :-
    statistics(cputime, T0),
    ids(10, Path),
    statistics(cputime, T1),
    Time is T1-T0,
    format('CPU time: ~w', [Time]),
    flush_output. % Output time taken

solveWithIDS(Start, Goal, Path) :-
    statistics(cputime, T0),
    ids(Start, Goal, 10, Path),
    statistics(cputime, T1),
    Time is T1-T0,
    format('CPU time: ~w', [Time]),
    flush_output. % Output time taken

%%%%% Search/Sequence Builder %%%%%
% Iterative deepening search
ids(Start0, Goal0, Limit, Path) :-
    list_to_ord_set(Start0, Start),
    list_to_ord_set(Goal0, Goal),
    between(0, Limit, Len),%make sure we are not over limit
    length(Path, Len),%match path length to our depth ength
    dfs(Start, Goal, [Start], Path).%peform dfs

ids(Limit, Path) :-
    start(Start0),
    goal(Goal0),
    list_to_ord_set(Start0, Start),
    list_to_ord_set(Goal0, Goal),
    between(0, Limit, Len),%make sure we are not over limit
    Len =< Limit,
    length(Path, Len),%match path length to our depth ength
    dfs(Start, Goal, [Start], Path).%peform dfs

dfs(State, Goal, _Visited, []) :-
    list_to_ord_set(State, OrderedState), %ensure ordering to compare to goal
    list_to_ord_set(Goal, OrderedGoal),
    OrderedState = OrderedGoal,
    format("Goal reached: ~w~n", [State]).

dfs(State, Goal, Visited, [Action | Actions]) :-
    action(Action, State, Next),%generate an action / move and the next state
    notYetVisited(Next, Visited),%make sure the next state hasn't been reached before
    dfs(Next, Goal, [Next | Visited], Actions).%continue searching

%%%%% Helpers %%%%%

% Compare two elements for inequality
notequal(X, X) :- !, fail. % Fail if equal
notequal(_, _).

% Substitute element E with E1 in a list
%substitute(X, Y, [X | T], [Y | T]).
%substitute(X, Y, [H | T], [H | T1]) :-
%    substitute(X, Y, T, T1).

%%%%% Rules %%%%%

% Rule 2: Move block X from block Y onto block Z
action(moveBlocks(X, Y, Z), S1, S2) :-
    member([clear, X], S1), block(Z),% X must be clear
    member([on, X, Y], S1), block(Y), % X is on Y
    member([clear, Z], S1), block(Z), notequal(X, Z), % Z is clear, X and Z are not the same
    ord_subtract(S1, [[clear, Z], [on, X, Y]], INT), % Take X off of Y and z from being clear 
    ord_union([[clear, Y], [on, X, Z]], INT, S2), % Move X onto Z, Y is now clear
    format("Moved ~w from ~w to ~w~n", [X, Y, Z]).

% Rule 3: Move block X from block Y onto the table
action(moveToTable(X, Y), S1, S2) :-
    member([clear, X], S1), % X must be clear
    member([on, X, Y], S1), % X must be on Y
    block(Y),block(Y), % Y is a block
    ord_subtract(S1,[[on, X, Y]],INT), % Move X off of Y
    ord_union([ [clear, Y], [on, X, table]], INT, S2), %Move X onto the table and clear Y
    format("Moved ~w from ~w to the table~n", [X, Y]).

% Rule 4: Move block X from the table onto block Y
action(moveToBlock(X, Y), S1, S2) :-
    member([clear, X], S1), % X must be clear
    member([on, X, table], S1), % X is on the table
    member([clear, Y], S1), % Y must be clear
    block(Y),block(Y),
    notequal(X, Y), % X and Y are not the same block
    ord_subtract(S1, [[clear, Y], [on, X, table]], INT), % Move X off table and y from being clear
    ord_union([[on, X, Y]],INT,  S2), %Move X to Y
    format("Moved ~w from the table to ~w~n", [X, Y]).

%%%%% END %%%%%
