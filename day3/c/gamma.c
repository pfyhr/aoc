#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int * bitCnts(long int input[1000])
{
    static int bincnts[12] = {0};
    for (int cnt=0; cnt<1000; cnt++)
    {
        //printf("input[cnt] is: %ld\n", input[cnt]);
        for (int bit=0; bit != 12; bit++)
        {
            if ( input[cnt] & (1 << bit) ) /* if the value at bit is 1, increment counter */
            {
                bincnts[bit] += 1;
            }
        }
    }
    return bincnts;
}
int gammaRate(long int input[1000])
{
    static int gamma = 0;
    static int epsilon = 0;
    static char * pEnd;
    static int *bincnts;

    bincnts = bitCnts(input);
    
    for (int bit=0; bit != 12; bit++)
    {
        printf("bincnts for bit %d is %d\n", bit, bincnts[bit]);
        if ( bincnts[bit] > 500)
        {
            gamma |= (1 << bit);
            epsilon |= (0 << bit);
        }
        else
        {
            gamma |= (0 << bit);
            epsilon |= (1 << bit);
        }
    }
    printf("gamma as int is: %d, eps %d, power = %d\n", gamma, epsilon, gamma * epsilon);
    return (int) gamma;
}
int cumsum(int maxval)
{
    int value = 0;
    for (int counter=0; counter < maxval; counter++)
    {
        value += counter;
    }
    return value;
}
int lifeSupp(long int input[1000], int cnt)
{
    static int *bincnts = NULL;
    bincnts = bitCnts(input);
    static int o2cands; /* 500500 magic index number */
    static int co2cands;
    static int o2 = 0;
    static int co2 = 0;
    static int row = 0;
    static int bit = 0;
    static int hexmax = 0x7F; //0xFFF

    printf("%d\n",cnt);
    o2cands = cumsum(cnt);
    co2cands = o2cands;
    printf("o2cands=%d\n", o2cands);

    while (o2cands >= cnt )
    {
        /* Do the stuff here */ 
        if (row < cnt)
        {
            row++;
        }
        else
        {
            row = 0;
            bit++;
        }
    }
    //printf("o2 is %ld, co2 is %ld, rating is %ld\n", input[o2cands], input[co2cands], input[o2cands] * input[co2cands]);
    printf("o2 is %ld, pos is %d \n", input[o2cands], o2cands);
}


int readFile(char *filename, int problem)
{
    static int retval = 1;
    static int cnt;
    static int gamma;
    cnt = 0;
    static FILE *fp;
    static char binLine[12];
    static char temp[16];
    static long int bits[1000];
    static char * pEnd;
    fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("no such file.\n");
        return retval;
    }
    while ( fscanf(fp, "%s", &binLine[0]) != EOF)
    {
        if (1==1) 
        {
            //printf("%s\n", binLine);
            bits[cnt] = strtol( binLine, &pEnd, 2);
        }
        else
        {
            printf("unknown instruction read");
            return 1;
        }
        cnt++;
    }

    retval = fclose(fp);
    if (problem == 1)
    {
        gamma = gammaRate(bits);
    }
    else if (problem == 2)
    {
        lifeSupp(bits, cnt);
    }
    else
    {
        printf("Unknown problem, exiting\n");
        return 0;
    }
    printf( "%d lines read\n", cnt);
    return retval;
}

int main(int argc, char *argv[])
{
    static int retval = 1;
    static int problem;

    if (argc > 3)
    {
        printf("Too many arguments, usage is: ./position path/to/file.txt n\n");
    }
    else if (argc > 2)
    {

        retval = sscanf (argv[2], "%d", &problem);
        if (retval == 1 && (problem == 1 || problem == 2))
        {
            retval = readFile(argv[1], problem);
        }
        else
        {
            printf("second input n, must be either 1 or 2\n");
            return 0;
        }
    }
    else if (argc > 1)
    {
        printf("Too few arguments, usage is: ./position path/to/file.txt n\n");
        printf("Defaulting to problem 2\n");
        problem = 2;
        retval = readFile(argv[1], problem);
    }
    else
    {
        printf("no input file provided, usage is: ./position path/to/file.txt n\n");
    }

    return retval;
}