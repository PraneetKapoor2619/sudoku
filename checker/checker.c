#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

void entermatrix();
void printmatrix();
void resetflag();
void rowcheck(uint8_t);
void columncheck(uint8_t);
void blockcheck(uint8_t);
void check();

struct grid
{
	uint8_t matrix[9][9];
	uint8_t f[9];
};
struct grid g1;

int main(int argc, char ** argv)
{
	entermatrix();
	printmatrix();
	resetflag();
	for(int i = 0; i < 9; ++i)
	{
		rowcheck(i);
		columncheck(i);
		blockcheck(i + 1);

	}
	check();
	return 0;
}

void entermatrix()
{
	FILE *fp;
	fp = fopen("grid.txt", "r");
	if(fp == NULL)
	{
		fprintf(stdout, "\nNo file detected!!\n");
		exit(0);
	}
	for(int i = 0; i < 9; ++i)
	{
		fscanf(fp, "%d %d %d %d %d %d %d %d %d", 
			&g1.matrix[i][0],
			&g1.matrix[i][1],
			&g1.matrix[i][2],
			&g1.matrix[i][3],
			&g1.matrix[i][4],
			&g1.matrix[i][5],
			&g1.matrix[i][6],
			&g1.matrix[i][7],
			&g1.matrix[i][8]);
	}
}

void printmatrix()
{
	for(int i = 0; i < 9; ++i)
	{
		printf("\n");
		for(int j = 0; j < 9; ++j)
		{
			printf("%d ", g1.matrix[i][j]);
		}
	}
	printf("\n");
}

void resetflag()
{
	for(int i = 0; i < 9; ++i)
	{
		g1.f[i] = 0;
	}
}

void rowcheck(uint8_t R)
{
	for(int i = 0; i < 9; ++i)
	{
		++g1.f[g1.matrix[R][i] - 1];
	}
}

void columncheck(uint8_t C)
{
	for(int i = 0; i < 9; ++i)
	{
		++g1.f[g1.matrix[i][C] - 1];
	}
}

void blockcheck(uint8_t B)
{
	int R, C;
	R = (int)((B - 1) / 3);
	R *= 3;
	C = (int)((B - 1) % 3);
	C *= 3;
	for(int i = R; i < R + 3; ++i)
	{
		for(int j = C; j < C + 3; ++j)
		{
			++g1.f[g1.matrix[i][j] - 1];
		}
	}
}

void check()
{
	int val = 0;
	for(int i = 0; i < 9; ++i)
	{
		if(g1.f[i] != 27)
		{
			printf("Error in %d\n", i + 1); 
			++val;
		}
	}
	if(val == 0)
		printf("The solution is correct\n");
	else
		printf("Incorrect solution\n");
}
