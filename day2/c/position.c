#include <stdio.h>
#include <string.h>

int readFile(char *filename, int problem)
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
    static FILE *fp;
    static char direction[16];
    static char temp[16];

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
            if (problem ==2)
            {
                ypos += aim * stepl;
            }
        }
        else if (direction[0] == 117) /* up aim */
        {
            if (problem == 2)
            {
                aim -= stepl;
            }
            else
            {
                ypos -= stepl;
            }
        }
        else if (direction[0] == 100) /* down aim */
        {
            if ( problem == 2)
            {
                aim += stepl;
            }
            else
            {
                ypos += stepl;
            }
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