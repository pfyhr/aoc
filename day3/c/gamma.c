#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int gammaRate(long int input[1000])
{
    static int cnt;
    static int bit, bit2;
    static int gamma = 0;
    static int epsilon = 0;
    cnt = 0;
    static int bincnts[12] = {0};

    static char * pEnd;
    for (cnt; cnt<1000; cnt++)
    {
        printf("input[cnt] is: %ld\n", input[cnt]);
        for (bit=0; bit != 12; bit++)
        {
            if ( input[cnt] & (1 << bit) ) /* if the value at bit is 1, increment counter */
            {
                bincnts[bit] += 1;
            }
        }
    }
    for (bit=0; bit != 12; bit++)
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
    printf("gamma as int is:%d, eps %d, power = %d\n", gamma, epsilon, gamma * epsilon);
    //printf("integer gamma is %ld\n", strtol( gamma, &pEnd, 2) );

    return (int) gamma;
}

int readFile(char *filename, int problem)
{
    static int retval = 1;
    static int stepl;
    static int xpos;
    static int ypos;
    static int aim;
    static int cnt;
    static int gamma;
    stepl = 0;
    xpos = 0;
    ypos = 0;
    aim = 0;
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
        stepl = 0;
        cnt++;
    }

    retval = fclose(fp);
    
    gamma = gammaRate(bits);
    printf( "%d lines read\n", cnt);
    printf( "last interpreted int is: %ld\n", bits[cnt-1]);
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