# TowersOfHanoi
Simple solver for the classic "Towers Of Hanoi" puzzle

1. Run the main function in main.py.
2. Quick by typing 'n', continue by typing anything else and hit Enter.
3. Input a number to set rings on the first rod and press Enter.
4. Press Enter to run the solver.

Example:

Ready to start? (y/n)
y
How many rings should there be on the first tower? (<20)
3
[[0 0 0]
 [1 0 0]
 [2 0 0]
 [3 0 0]]
Press ENTER to start solving.

=====

Solving in 7 moves...

1. Move ring number 1 from A to C
[[0 0 0]
 [0 0 0]
 [2 0 0]
 [3 0 1]]

2. Move ring number 2 from A to B
[[0 0 0]
 [0 0 0]
 [0 0 0]
 [3 2 1]]

...
...
...

6. Move ring number 2 from B to C
[[0 0 0]
 [0 0 0]
 [0 0 2]
 [1 0 3]]

7. Move ring number 1 from A to C
[[0 0 0]
 [0 0 1]
 [0 0 2]
 [0 0 3]]

Solved!

=====

Ready to start? (y/n)
