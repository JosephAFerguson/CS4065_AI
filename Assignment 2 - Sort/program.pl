/*swap the first two elements if they are not in order*/
swap([X, Y|T], [Y, X | T]):-
    Y =< X.

/*swap elements in the tail*/
swap([H|T], [H|T1]):-
    swap(T, T1).

/* Comment describing bubbleSort */
bubbleSort(L,SL):-
    swap(L, L1), % at least one swap is needed
    !,
    bubbleSort(L1, SL).
bubbleSort(L, L). % here, the list is already sorted

/* Comment describing ordered */
ordered([]).
ordered([_X]).
ordered([H1, H2|T]):-
    H1 =< H2,
    ordered([H2|T]).

/*Comment describing insert(E, SL, SLE) ...*/
/*Comment describing the 1st clause of insert ...*/
insert(X, [],[X]).
insert(E, [H|T], [E,H|T]):-
    ordered(T),
    E =< H,
    !.

/*Comment describing the 2nd clause of insert ...*/
insert(E, [H|T], [H|T1]):-
    ordered(T),
    insert(E, T, T1).

/* Comment describing insertionSort */
insertionSort([], []).
insertionSort([H|T], SORTED) :-
    insertionSort(T, T1),
    insert(H, T1, SORTED).

/* Comment to describe meregeSort... */
mergeSort([], []). % The empty list is sorted
mergeSort([X], [X]):-!.
mergeSort(L, SL):-
    split_in_half(L, L1, L2),
    mergeSort(L1, S1),
    mergeSort(L2, S2),
    merge(S1, S2, SL).

/* Comment to describe split_in_half...*/
intDiv(N,N1, R):- R is div(N,N1).
split_in_half([], _, _):-!, fail.
split_in_half([X],[],[X]).
split_in_half(L, L1, L2):-
    length(L,N),
    intDiv(N,2,N1),
    length(L1, N1),
    append(L1, L2, L).

/* Comment describing merge(S1, S2, S) */
merge([], L, L). % comment
merge(L, [],L). % comment
merge([H1|T1],[H2|T2],[H1|T]):- 
    H1 =< H2,
    merge(T1,[H2|T2],T).
merge([H1|T1], [H2|T2], [H2|T]):-
    H1 > H2, 
    merge([H1|T1], T2, T).

/* Comment describing split for quickSort */
split(_, [],[],[]).
split(X, [H|T], [H|SMALL], BIG):-
    H =< X,
split(X, T, SMALL, FILLINHERE).
split(X, [H|T], SMALL, [H|BIG]):-
    X =< H,
split(X, T, FILLINHERE, BIG).

/* Comment describing quickSort */
quickSort([], []).
quickSort([H|T], LS):-
    split(H, T, SMALL, FILLINHERE),
    quickSort(SMALL, S),
    quickSort(BIG, B),
    append(S, [H|B], FILLINHERE).

/* Comment describing hybridSort */
hybridSort(LIST, SMALLALG, BIGALG, THRESHOLD, SLIST):-
    length(LIST, N), N=< THRESHOLD,
    SMALLALG(LIST, FILLINHERE).

hybridSort(LIST, SMALLALG, BIGALG, THRESHOLD, SLIST):-
    length(LIST, N), N > THRESHOLD,
    FILLINHERE. % Comment: fill in the behavior of BIGALG
