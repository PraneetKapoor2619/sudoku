import re
from os import system

def islist(cell):
	try:
		len(cell)
		return True
	except:
		return False

def buildgrid(filename):
	fp = open(filename, 'r')
	grid = []
	lno = 1
	for line in fp:
		extr = re.findall("[0-9]+", line)
		grid.insert(len(grid), [int(i) for i in extr])
	return grid

def printgrid(g):
	for i in range(0, 9):
		for j in range(0, 9):
			print(g[i][j], end = " ")
		print("")
	#system("PAUSE")

def fillblock(grid, block):
	R = int((block - 1) / 3)
	R *= 3
	C = int((block - 1) % 3)
	C *= 3
	#form a list of numbers which already exist in the block and those which do not
	existing = []
	for i in range(R, R + 3):
		for j in range(C, C + 3):
			if(grid[i][j] != 0):
				existing.insert(len(existing), grid[i][j])
	p = []
	for i in range(1, 10):
		if(existing.__contains__(i) == False):
			p.insert(len(p), i)
	#print("Block: " + str(block) + "\nP:" + str(p))
	
	#iterate cell by cell, checking for the possibility whether a number can be inserted in a cell or not.
	for i in range(R, R + 3):
		for j in range(C, C + 3):
			if(grid[i][j] == 0):
				tmp = []
				for n in p:
					if(rowcheck(grid, i, j, n) == True):
						continue
					if(columncheck(grid, i, j, n) == True):
						continue
					tmp.insert(len(tmp), n)
				grid[i][j] = tmp
	return grid

def rowcheck(grid, row, column, num):
	for i in range(0, 9):
		if(i != row):
			try:
				len(grid[i][column])
			except:
				if(grid[i][column] == num):
					return True
	return False

def columncheck(grid, row, column, num):
	for i in range(0, 9):
		if(i != column):
			try:
				len(grid[row][i])
			except:
				if(grid[row][i] == num):
					return True
	return False

def checknum(grid, num):
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

def checkgrid(grid):
	#printgrid(grid)
	for num in range(1, 10):
		if(checknum(grid, num) == False):
			#print("Test Failed!!")
			return False
	return True