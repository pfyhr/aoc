#include <stdio.h>
#include <string.h>

int arraysum(int arr[], int window, int iter)
{
    int sum=0;
    for ( iter; iter<window; iter++)
    {
        sum += arr[iter];
    }
    return sum;
}

int readFile(char *filename)
{
    static int retval = 1;
    static int stepl;
    static int xpos;
    static int ypos;
    static int aim;
    static int cnt;
    stepl = 0;
    xpos = 0;
    ypos = 0;
    aim = 0;
    cnt = 0;
    FILE *fp;
    char direction[16];
    char temp[16];

    fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("no such file.\n");
        return retval;
    }
    while ( fscanf(fp, "%s %d", direction, &stepl) != EOF)
    {
        if (direction[0] == 102) /* forward */
        {
            xpos += stepl;
            ypos += aim * stepl;
        }
        else if (direction[0] == 117) /* up aim */
        {
            aim -= stepl;
        }
        else if (direction[0] == 100) /* down aim */
        {
            aim += stepl;
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
    printf( "%d lines read\n", cnt);
    printf( "xpos * ypos is: %d * %d = %d\n", xpos, ypos, xpos * ypos);
    return retval;
}

int main(int argc, char *argv[])
{
    static int retval = 1;

    if (argc > 2)
    {
        printf("Too many arguments, usage is: ./depth path/to/file.txt n\n");
    }
    else if (argc > 1)
    {
        retval = readFile(argv[1]);
    }
    else
    {
        printf("no input file provided, usage is: ./depth path/to/file.txt n\n");
    }

    return retval;
}