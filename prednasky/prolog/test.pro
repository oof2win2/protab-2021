person(kate).
person(maria).
person(roman).

all_different_people(X, Y, Z) :-
	dif(X, Y), dif(X, Z), dif(Y, Z),
	person(X), person(Y), person(Z).

solve(Doktor, Pravnik, Ucitel, Fletna, House, Piano) :-
	all_different_people(Doktor, Pravnik, Ucitel),
	all_different_people(Fletna, House, Piano),
	dif(maria, Doktor),
	Pravnik = Piano,
	dif(maria, Ucitel),
	House = Doktor,
	dif(kate, Doktor).

% % same
% %	is_empty([]).
% % 	is_empty(X) :- X = [].
% is_empty([]).

% % X is an item in an array and Y is the rest of the array
% % is_not_empty([X | Y]).
% % this however is better as if we dont want to access a variable but just match it, just use underscores
% is_not_empty([_ | _]).

% same_length([_ | L], [_ | M]) :- same_length(L, M).

% member(X, [Y | L]) :- (X = Y ; member(X, L)).

% ?- use_module(library(clpfd)).


% factorial(N, F) :- N #>= 1, M #= N - 1, factorial(M, O), F #= N * O.
% factorial(0, 1).

% sum_of_first_n(N, [X | L], Sum) :- M #= N - 1, sum_of_first_n(M, L, O), Sum #= O + X.
% sum_of_first_n(0, _, 0).
