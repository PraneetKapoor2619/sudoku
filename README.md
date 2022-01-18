# Sudoku Solver and Checker  
  
This repo contains sudoku solver and checker which I have written. The repo. contains three folders:  
&nbsp;|->`checker`  
&nbsp;|&nbsp;|->`checker.c`  
&nbsp;|&nbsp;|->`grid.txt`  
&nbsp;|&nbsp;|->`Makefile`  
&nbsp;|->`My solution`  
&nbsp;|&nbsp;|->`sudoku.py`  
&nbsp;|&nbsp;|->`sudoku_utility.py`  
&nbsp;|&nbsp;|->`grid.txt`  
&nbsp;|&nbsp;|->`puzzle.txt`  
&nbsp;|->`Computerphile solution`  
&nbsp;|&nbsp;|->`sudoku.py`  
&nbsp;|&nbsp;|->`puzzle.txt`  
  
## checker  
  
In this folder is a C program which will check whether the sudoku grid given in `grid.txt` is correct or not. `Makefile` contains the build and execution instructions.  
  
  
## My solution  
  
In this folder are two Python3 scripts which can be used to either check a grid or solve a grid stored in a text file. `sudoku.py` is the main script which uses various functions described in `sudoku_utility.py` to get its job done.  
The solver uses recursion to solve a puzzle. This works fine as long as the number of digits which could possibly be entered in an empty cell does not exceed 2 or 3. If they do, however, exceed this, then the solver will take eternity to solve the puzzle. This makes my solution a perfect example of an overengineered solution.  
  
  
## Computerphile solution  
  
This folder contains a single Python3 script, `sudoku.py` which either checks or solves a grid stored in a text file. Two functions, namely `possible(y, x, n)` and `solve()` in it have been directly copied from [the video on the subject by Computerphile](https://youtu.be/G_UYXzGuqvM). Unlike the video, which made use of numpy, I have used my own functions to build, and print the grid beautifully. The code also throws sarcastic remarks if the user enters stupid options :-).