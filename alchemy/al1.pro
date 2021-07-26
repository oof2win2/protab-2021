:- use_module(library(clpfd)).

is_even(X) :- mod(X, 2) #= 0.
is_odd(X) :- mod(X, 2) #\= 0.

is_offset(X, Y, Z) :- X + Z #= Y.
is_left(X, Y) :- is_offset(X, Y, -1).
is_right(X, Y) :- is_offset(X, Y, 1).


% TODO: check if whole array is lower than Z??
% lower_than([X | Y], Z)

solve(A, B, C, D, E, F, G, H) :-
	lower_than([A, B, C, D, E, F, G, H], 8),
	is_even(F),
	is_left(H, D),
	is_offset(A, E, 5),
	is_right(H, G),
	is_offset(G, C, 3),
	is_right(F, C),
	is_even(D),
	is_even(C),
	is_left(E, H),
	is_right(F, D),
	is_offset(D, C, 2),
	is_left(B, H).


% is_even(X) :- mod(X, 2) #= 0.
% is_idd(X) :- mod(X, 2) #\= 0.

% lower_than_three(X) :- X #=< 3.
% higher_than_one(X) :- X #>= 1.

% solve_test(X) :-
% 	lower_than_three(X),
% 	higher_than_one(X),
% 	is_even(X),
% 	indomain(X).