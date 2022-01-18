from sudoku_utility import *
import sys
import time
import os
import copy

grid = []		#contains the given numbers and the list of possible values for each cell
iterable = []		#contains tuples which have the indices of cells which are iterable
solution = []		#this one will store all the solutions

def solve(sol, index):
	global grid, iterable, solution
	i, j = iterable[index]
	#print("\n", "(", i, ",", j, ") :")
	for tmp in grid[i][j]:
		#print("\t>>", tmp)
		sol[i][j] = tmp
		if(index < (len(iterable) - 1)):
			solve(sol, index + 1)
		else:
			#printgrid(sol)
			if(checkgrid(sol) == True):
				solution.insert(len(solution), sol)
	return 0

if __name__ == "__main__":
	#sys.tracebacklimit = 0
	mode = int(input("1. Solver mode\n2. Checker mode\n>> "))
	if(mode == 1):
		grid = buildgrid("puzzle.txt")
		sol = []
		sol = copy.deepcopy(grid)
		#fill grid with the possibilities
		for block in range(1, 10):
			grid = fillblock(grid, block)
		
		printgrid(grid)
		os.system("pause")
		#form a list of tuples containing the indices of cells which are grids
		for i in range(0, 9):
			for j in range(0, 9):
				if(islist(grid[i][j]) == True):
					iterable.insert(len(iterable), (i, j))
				else:
					continue
		#now use brute force through the possibilites to find the solution
		solve(sol, 0)
		print("\n----------------------------------\n")
		for i in range(len(solution)):
			printgrid(solution[i])
		
	elif(mode == 2):
		grid = buildgrid("grid.txt")
		printgrid(grid)
		print(checkgrid(grid))
	else:
		print("Reading is hard, isn't it?")