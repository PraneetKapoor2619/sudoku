#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

void enterrow(uint8_t *);
void rowcheck(uint8_t *);
void columncheck(uint8_t);

struct grid
{
	uint8_t row1[9];
	uint8_t row2[9];
	uint8_t row3[9];
	uint8_t row4[9];
	uint8_t row5[9];
	uint8_t row6[9];
	uint8_t row7[9];
	uint8_t row8[9];
	uint8_t row9[9];
	uint8_t f[9];
};
struct grid grid1;

int main(int argc, char ** argv)
{
	enterrow(grid1.row1);
	enterrow(grid1.row2);
	enterrow(grid1.row3);	
	enterrow(grid1.row4);
	enterrow(grid1.row5);
	enterrow(grid1.row6);
	enterrow(grid1.row7);
	enterrow(grid1.row8);
	enterrow(grid1.row9);
	rowcheck(grid1.row1);
	rowcheck(grid1.row2);
	rowcheck(grid1.row3);
	rowcheck(grid1.row4);
	rowcheck(grid1.row5);
	rowcheck(grid1.row6);
	rowcheck(grid1.row7);
	rowcheck(grid1.row8);
	rowcheck(grid1.row9);
	columncheck(1);
	columncheck(2);
	columncheck(3);
	columncheck(4);
	columncheck(5);
	columncheck(6);
	columncheck(7);
	columncheck(8);
	columncheck(9);
	int flag = 0;
	for(int i = 0; i < 9; ++i)
	{
		if(grid1.f[i] != 18)
		{
			printf("ERROR in %d\n", i);
			++flag;
		}
	}
	if(flag > 0)
	{
		exit(0);
	}
	else
	{
		printf("ALL CLEAR\n");
	}
	return 0;
}

void enterrow(uint8_t *ptr)
{
	scanf("%d %d %d %d %d %d %d %d %d", ptr, ptr + 1, ptr + 2, ptr + 3, ptr + 4, ptr + 5, ptr + 6, ptr + 7, ptr + 8);
}

void rowcheck(uint8_t *ptr)
{
	for(int i = 0; i < 9; ++i)
	{
		++grid1.f[*(ptr + i) - 1];	
	}
}

void columncheck(uint8_t cno)
{
	++grid1.f[grid1.row1[cno - 1] - 1];
	++grid1.f[grid1.row2[cno - 1] - 1];
	++grid1.f[grid1.row3[cno - 1] - 1];
	++grid1.f[grid1.row4[cno - 1] - 1];
	++grid1.f[grid1.row5[cno - 1] - 1];
	++grid1.f[grid1.row6[cno - 1] - 1];
	++grid1.f[grid1.row7[cno - 1] - 1];
	++grid1.f[grid1.row8[cno - 1] - 1];
	++grid1.f[grid1.row9[cno - 1] - 1];
}
