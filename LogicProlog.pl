
% Knowledge base
parent(juan, ana).
parent(juan, carlos).
parent(ana, maria).

% Logical rule
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Queries
?- grandparent(juan, maria).
?- grandparent(juan, carlos).
?- grandparent(ana, maria).



