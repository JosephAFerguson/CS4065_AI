/*Random List generates a random list of N elements
 *by prepending elements onto a list until there is only one
 *element left to add, the last element
 */
randomList(1, [X]):-
    random(0,999,X).
randomList(N, [X | LIST]):-
    N > 1,
    N1 is N - 1, %decrement
    random(0,999,X),
    randomList(N1, LIST).

/*swap the first two elements if they are not in order*/
swap([X, Y|T], [Y, X | T]):-
    Y =< X.

/*swap elements in the tail*/
swap([H|T], [H|T1]):-
    swap(T, T1).

/* bubbleSort generates a sorted list (SL) via
 * swapping adjacent elements until no more swaps are needed,
 * which means the list is sorted
*/
bubbleSort(L,SL):-
    swap(L, L1), % at least one swap is needed
    !,
    bubbleSort(L1, SL).
bubbleSort(L, L). % here, the list is already sorted

/* ordered returns true as long as the list
 * satisfies the predicate that an element before another element in the list
 * is less than or equal to it (a non-decreasing sorted list)
 * It moves up the list as long as this ordering holds true for each pair of elements.
 */
ordered([]).
ordered([_X]).
ordered([H1, H2|T]):-
    H1 =< H2,
    ordered([H2|T]).

/*insert(E, SL, SLE) inserts an element in order into a sorted list
 *it does this by both checking if the list is sorted(a predicate),
 *and finding where E, the element can be placed into the list to satisfy it still being sorted
 */
/*Base case: On an empty list just insert the element we have into it
 *Check if the rest of the list is ordered(sorted) and place E in the current spot in the list
 *if E is less than or equal to the first element(head,H) of the rest of the list
 */
insert(X, [],[X]).
insert(E, [H|T], [E,H|T]):-
    ordered(T),
    E =< H,
    !.

/*Upon a case where E cannot be inserting into the list,
 *it must be the largest element, so append it to the end of the list
 */
insert(E, [H|T], [H|T1]):-
    ordered(T),
    insert(E, T, T1).

/*insertionSort sorts a list by inserting elements of the list into a sorted portion of the list
 *it uses the insert algorithm to insert elements into the list while it traverses through the list
 */
insertionSort([], []).
insertionSort([H|T], SORTED) :-
    insertionSort(T, T1),
    insert(H, T1, SORTED).

/*mergeSort recursively splits the list into half and sorts both of the halves
 *because it keeps splitting the list is half to do this,
 *we have base cases to indicate how empty or single element lists are already sorted
 */
mergeSort([], []). % The empty list is sorted
mergeSort([X], [X]):-!.
mergeSort(L, SL):-
    split_in_half(L, L1, L2),
    mergeSort(L1, S1),
    mergeSort(L2, S2),
    merge(S1, S2, SL).

/*split_in_half splits a list in half and handles 
 *the case where the length is odd by using intDiv.
 *The base cases handle single element and empty lists.
 */
intDiv(N,N1, R):- R is div(N,N1).
split_in_half([], _, _):-!, fail.
split_in_half([X],[],[X]).
split_in_half(L, L1, L2):-
    length(L,N),
    intDiv(N,2,N1),
    length(L1, N1),
    append(L1, L2, L).

/*merge(S1, S2, S) uses two predicates to merge two sorted lists,
 *one to handle the head element h1 being less than or equal to the head element h2 of the other list,
 *and one to handle the head element h1 being greater than the head element h2 of the other list.
 *Depending on the scenario, it keeps moving through both lists while splicing the lists into
 *head elements and rests(tails) and inserting elements in an ordered fashion.
 */
merge([], L, L). %merging an empty list into a non-empty list L, just gives us the non-empty list L.
merge(L, [],L). %merging a non-empty list L into an empty list, just gives us the non-empty list L.
merge([H1|T1],[H2|T2],[H1|T]):- 
    H1 =< H2,
    merge(T1,[H2|T2],T).
merge([H1|T1], [H2|T2], [H2|T]):-
    H1 > H2, 
    merge([H1|T1], T2, T).

/*split partitions list into two portions:
 *SMALL, with elements less than or equal to the given Pivot element X
 *BIG, with elements greater than the given Pivot elemtent X
 *it does this similarly to merge from mergeSort, with 2 cases for an element being <= or > than the pivot
 */
split(_, [],[],[]).
split(X, [H|T], [H|SMALL], BIG):-
    H =< X,
    split(X, T, SMALL, BIG).
split(X, [H|T], SMALL, [H|BIG]):-
    H > X,
    split(X, T, SMALL, BIG).

/*quickSort recursively selects a pivot element, in this case the first element of the list,
 *and splits the list into two partitions, those greater than the pivot element, and those less than the pivot element.
 *Each of these lists are recursively sorted in the same fashion, and then combined for the final sorted list
 */
quickSort([], []).
quickSort([H|T], LS):-
    split(H, T, SMALL, BIG),
    quickSort(SMALL, S),
    quickSort(BIG, B),
    append(S, [H|B], LS).

/*hybridSort sorts a given list accordingly to two given sorting algorithms,
 *one to use when the size of the list is below a threshold, and the other to use when the size
 *of the list is above the threshold (threshold is given)
 *
 *!!!Note!!!:
 *a small change was made to the function, the addition of call.
 *  call was a necessary addition as prolog does not allow for functions/rules
 *  to be passed explicitly as arguments, and then used like (PARAMFUNCTION(ARGS**))
 *  call() predicate allows use to do this and call the given algorithm with the appropriate params.
 *This also allows hybridSort on BIGALG to not "recall" hybridSort 
 *on cases where the BIGALG has split the list into smaller, below threshold sizes.
 *Thus call() allows hybridSort to behave like and only like BIGALG when used.
 */
hybridSort(LIST, SMALLALG, BIGALG, THRESHOLD, SLIST):-
    length(LIST, N), N=< THRESHOLD,
    call(SMALLALG,LIST, SLIST).

hybridSort(LIST, SMALLALG, BIGALG, THRESHOLD, SLIST):-
    length(LIST, N), N > THRESHOLD,
    call(BIGALG,LIST,SLIST). %BIGALG is called and used to find the sorted list when the list is above our threshold size


/* Execution of tests*/
/*
Results on 50 Lists sizes 10-100:
    bubbleSort: Fails, stalls indefinitely,
    insertionSort: 5.26 seconds
    mergeSort: 0.0003125 seconds
    quickSort: 0.0 seconds
*/
/*
Results on 50 Lists sizes 100-1000:
    bubbleSort: Fails, stalls indefinitely,
    insertionSort: 5.26 seconds
    mergeSort: 0.0003125 seconds
    quickSort: 0.0 seconds
*/
/*
Results on 50 Lists sizes 1000-10000:
    bubbleSort: Untested, stalls
    insertionSort: Untested, stalls
    mergeSort: 0.0009375 seconds
    quickSort: 0.0009374 seconds
*/

:- dynamic random_list/2.  % Declares that random_list/2 will be dynamic.

listsGeneration(0).
listsGeneration(N) :-
    N > 0,
    random(10, 50, ListSize), 
    randomList(ListSize, List), 
    assertz(random_list(N, List)),  % Store the list
    N1 is N - 1,
    listsGeneration(N1).

hybridSort1(LIST, SLIST) :-
    hybridSort(LIST, insertionSort, quickSort, 200, SLIST).
hybridSort2(LIST, SLIST) :-
    hybridSort(LIST, bubbleSort, mergeSort, 200, SLIST).
hybridSort3(LIST, SLIST) :-
    hybridSort(LIST, insertionSort, mergeSort, 200, SLIST).
hybridSort4(LIST, SLIST) :-
    hybridSort(LIST, bubbleSort, quickSort, 200, SLIST).

timeAlg(SORTALG, LIST, T) :-
    statistics(cputime, T0),
    call(SORTALG, LIST, SL),
    statistics(cputime, T1),
    T is T1 - T0,
    format('~w CPU time: ~w~n', [SORTALG, T]),
    flush_output. % Output time taken

:- dynamic sorting_times/3.  % Stores (ListNum, SortingAlgorithm, Time).

run_sorts(ListNum, List) :-
    writeln('Running sorts for list number':ListNum),
    timeAlg(bubbleSort, List, TimeBubble),
    assertz(sorting_times(ListNum, bubbleSort, TimeBubble)),
    timeAlg(insertionSort, List, TimeInsert),
    assertz(sorting_times(ListNum, insertionSort, TimeInsert)),
    timeAlg(mergeSort, List, TimeMerge),
    assertz(sorting_times(ListNum, mergeSort, TimeMerge)),
    timeAlg(quickSort, List, TimeQuick),
    assertz(sorting_times(ListNum, quickSort, TimeQuick)),
    timeAlg(hybridSort1, List, TimeHybrid1),
    assertz(sorting_times(ListNum, hybridSort1, TimeHybrid1)),
    %timeAlg(hybridSort2, List, TimeHybrid2),
    %assertz(sorting_times(ListNum, hybridSort2, TimeHybrid2)),
    timeAlg(hybridSort3, List, TimeHybrid3),
    assertz(sorting_times(ListNum, hybridSort3, TimeHybrid3)).
    %timeAlg(hybridSort4, List, TimeHybrid4),
    %assertz(sorting_times(ListNum, hybridSort4, TimeHybrid4)),

average_time(SortAlg, AvgTime) :-
    findall(Time, sorting_times(_, SortAlg, Time), Times),
    sumlist(Times, TotalTime),
    length(Times, Count),
    AvgTime is TotalTime / Count.

run_prog :-
    forall(random_list(ListNum, List),
           run_sorts(ListNum, List)).


/*END EXECUTION OF TESTS | START OF ALGORITHMS*/
