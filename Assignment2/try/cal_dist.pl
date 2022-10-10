/*
importing the file distance_route.csv in order to make the facts of distance between 2 cities */

/*
importing the file distance_route.csv in order to make the facts of distance between 2 cities */

import_all_route :-
            csv_read_file('road_distance.csv' ,R, [functor(edge), arity(3)]),
            maplist(assert, R).

connected(X,Y,L) :- edge(X,Y,L) ; edge(Y,X,L).

path(A,B,Path,Len) :-
       travel(A,B,[A],Q,Len),
       reverse(Q,Path).

travel(A,B,P,[B|P],L) :-
       connected(A,B,L).
travel(A,B,Visited,Path,L) :-
       connected(A,C,D),
       C \== B,
       \+member(C,Visited),
       travel(C,B,[C|Visited],Path,L1),
       L is D+L1.

shortest(A,B,Path,Length) :-
   setof([P,L],path(A,B,P,L),Set),
   Set = [_|_], % fail if empty
   minimal(Set,[Path,Length]).

minimal([F|R],M) :- min(R,F,M).

% minimal path
min([],M,M).
min([[P,L]|R],[_,M],Min) :- L < M, !, min(R,[P,L],Min).
min([_|R],M,Min) :- min(R,M,Min).
