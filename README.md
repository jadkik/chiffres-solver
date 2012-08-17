chiffres-solver
===============

"Des Chiffres et des Lettres" game solver

What is it?
===========

There's a Freanch TV game called  "Des Chiffres et des Lettres", in which there are word games, and number games.
This code is made to solve the number game. The players are given 6 numbers
(generally ranging from to 10 and some big common numbers like 11, 25, 50, 75, 100, 150, etc. to make it easier)
and a bigger number (generally a 3-digit number). The objective is to figure out the shortest combination
of basic operations (+,-,x,/) to get as close as possible to the 3-digit target number (because sometimes you cannot
get to the exact number).

How does the solver work?
=========================

Simply, it tries all possible combinatinations. And tries to eliminate solutions as it's going. It's a "light" brute-force attack.

As this might take time, everytime it finds a solution that is shorter than the last one found, it outputs it.
Also, this way, you will see that after a minute or so, you will end up with something like 1,000 or 20,000 solutions.
If you look closely at them (I didn't), you will see that the difference is really minimal between 60-70% of them.
The really different solutions are usually just a few.

Improving
=========

The challenge is to filter these duplicates out as soon as possible, or detect useless operations as they are generated.

For example, you might have (1,2,3,4), to get 12. The obvious solution is: `3x4=12`; however, there's also this:

    1*2=2
    3*4=12

Or even:

    1*3=3
    3*4=12

And many more: `1*4=4; 4*3=12`, `4*1=4; 4*3=12`, `4*1=4; 3*4=12` and all other possible permutations of all the previous cases.
For n=6 numbers, and a target in the hundreds, these can get quite a few.

In all these cases, the first operation is either not used (case 1) or useless (case 2) or plain duplicates (case 3+).

One way to solve this is to figure out one solution, and based on that one, simplify, factor and expand to deduce all other and potentially shorter ones.
Another possible technique would be to go from the target, and simplify to get to the result, which should be the shortest solution.

Using
=====

Install [http://www.python.org Python] v2.7 then run `python main.py`

Choose a language, either `fr` or `en`. Then keep writing the numbers, and when you're done, leave empty and press enter.

You will be asked for the target number. Type it and press enter, and then wait, until you see a message saying
`it found 1024 solutions in 1m50s`.

Examples
========

    Numero suivant (laisser vide si complet)? 10
    Numero suivant (laisser vide si complet)? 25
    Numero suivant (laisser vide si complet)? 7
    Numero suivant (laisser vide si complet)? 9
    Numero suivant (laisser vide si complet)? 4
    Numero suivant (laisser vide si complet)? 5
    Numero suivant (laisser vide si complet)?
    Compte? 135
    Compte 135, avec (10, 25, 7, 9, 4, 5) en 4 etapes:
    10 + 25 = 35
    7 + 9 = 16
    4 * 35 = 140
    140 - 5 = 135
    **********
    Compte 135, avec (10, 25, 7, 9, 4, 5) en 3 etapes:
    10 + 25 = 35
    4 * 35 = 140
    140 - 5 = 135
    **********
    Compte 135, avec (10, 25, 7, 9, 4, 5) en 2 etapes:
    10 + 5 = 15
    9 * 15 = 135
    **********
    Recherche de la plus courte solution en cours...
    Compte 135, avec (10, 25, 7, 9, 4, 5) en 2 etapes:
    5 * 25 = 125
    125 + 10 = 135
    **********
    Trouve 21240 solutions en 2m31s.
    ********************

    Numero suivant (laisser vide si complet)? 75
    Numero suivant (laisser vide si complet)? 100
    Numero suivant (laisser vide si complet)? 6
    Numero suivant (laisser vide si complet)? 3
    Numero suivant (laisser vide si complet)? 25
    Numero suivant (laisser vide si complet)? 2
    Numero suivant (laisser vide si complet)?
    Compte? 489
    Compte 489, avec (75, 100, 6, 3, 25, 2) en 4 etapes:
    75 + 100 = 175
    6 * 2 = 12
    175 - 12 = 163
    3 * 163 = 489
    **********
    Recherche de la plus courte solution en cours...
    Compte 489, avec (75, 100, 6, 3, 25, 2) en 4 etapes:
    2 * 3 = 6
    100 - 6 = 94
    94 * 6 = 564
    564 - 75 = 489
    **********
    Trouve 936 solutions en 2m53s.
    ********************

    Numero suivant (laisser vide si complet)? 3
    Numero suivant (laisser vide si complet)? 5
    Numero suivant (laisser vide si complet)? 7
    Numero suivant (laisser vide si complet)? 9
    Numero suivant (laisser vide si complet)? 2
    Numero suivant (laisser vide si complet)? 3
    Numero suivant (laisser vide si complet)?
    Compte? 953
    Recherche de la plus courte solution en cours...
    Pas de solution!
    Trouve 0 solutions en 2m45s.
    ********************

    Numero suivant (laisser vide si complet)? 4
    Numero suivant (laisser vide si complet)? 7
    Numero suivant (laisser vide si complet)? 2
    Numero suivant (laisser vide si complet)? 25
    Numero suivant (laisser vide si complet)? 8
    Numero suivant (laisser vide si complet)? 9
    Numero suivant (laisser vide si complet)?
    Compte? 331
    Compte 331, avec (4, 7, 2, 25, 8, 9) en 5 etapes:
    4 + 7 = 11
    2 + 25 = 27
    8 * 11 = 88
    9 * 27 = 243
    88 + 243 = 331
    **********
    Compte 331, avec (4, 7, 2, 25, 8, 9) en 4 etapes:
    4 + 25 = 29
    8 + 29 = 37
    9 * 37 = 333
    333 - 2 = 331
    **********
    Recherche de la plus courte solution en cours...
    Compte 331, avec (4, 7, 2, 25, 8, 9) en 4 etapes:
    9 * 8 = 72
    72 - 25 = 47
    47 * 7 = 329
    329 + 2 = 331
    **********
    Trouve 2952 solutions en 2m34s.
    ********************

You might have noticed there's one here which has no solution, the solver does not look for the closest yet,
it just tries to find an exact match. Also, some have 1000 solutions and others up to 20000. Some take a minute
and sometimes less, some take up to 3+. But usually you should see a solution pop up after a few seconds
(0-30, which is the time limit in the TV game).