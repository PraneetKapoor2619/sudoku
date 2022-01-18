import re

grid = []

def buildgrid(filename):
	global grid
	fp = open(filename, 'r')
	lno = 1
	for line in fp:
		extr = re.findall("[0-9]+", line)
		grid.insert(len(grid), [int(i) for i in extr])
	return grid

def printgrid():
	global grid
	print("\n---------------------------------\n")
	for i in range(0, 9):
		for j in range(0, 9):
			print(grid[i][j], end = " ")
		print("")
	print("\n---------------------------------\n")

def possible(y, x, n):
	global grid
	for i in range(0, 9):
		if grid[y][i] == n:
			return False
	for i in range(0, 9):
		if grid[i][x] == n:
			return False
	x0 = (x // 3) * 3
	y0 = (y // 3) * 3
	for i in range(0, 3):
		for j in range(0, 3):
			if grid[y0 + i][x0 + j] == n:
				return False
	return True

def solve():
	global grid
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				for n in range(1, 10):
					if possible(y, x, n):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	printgrid()
	input("More?")

if __name__ == "__main__":
	buildgrid("puzzle.txt")
	printgrid()
	solve()