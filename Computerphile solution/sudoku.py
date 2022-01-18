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

def checknum(num):
	global grid
	#first check rows
	for i in range(0, 9):
		if (grid[i].count(num) == 1):
			continue
		else:
			return False
	#check columns
	for i in range(0, 9):
		cnt = 0
		for j in range(0, 9):
			if(grid[i][j] == num):
				cnt += 1
		if(cnt != 1):
			return False
	#check 3x3 grid
	for B in range(1, 10):
		R = int((B - 1) / 3)
		R *= 3
		C = int((B - 3) % 3)
		C *= 3
		cnt = 0
		for r in range(R, R + 3):
			for c in range(C, C + 3):
				if(grid[r][c] == num):
					cnt += 1
		if(cnt != 1):
			return False
	return True

def checkgrid():
	global grid
	for num in range(1, 10):
		if(checknum(num) == False):
			print("Test Failed!!")
			return False
	return True

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
	mode = int(input("1. Check a grid\n2. Solve a grid\n >> "))
	if mode == 1 or mode == 2:
		filename = input("Please enter the file which contains the grid: ")
		try:
			fp = open(filename, 'r')
			fp.close()
		except:
			print("Did your mama never give you milk?\nTHERE IS NO FILE NAMED " + filename + "!!!\n")
			exit(0)
		
		buildgrid(filename)
		printgrid()
		if mode == 1:
			if(checkgrid()):
				print("Grid is correct!!")
			else:
				print("Grid is not correct!!")
		elif mode == 2:
			solve()
	else:
		print("Reading is hard, isn't it?")