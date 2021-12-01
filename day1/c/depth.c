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

int readFile(char *filename, int window)
{
    int retval = 1;
    int cnt;
    int ticker;
    cnt = 0;
    ticker = 0;
    FILE *fp;
    int buff;
    int prev[10] = { 0 };

    fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("no such file.\n");
        return retval;
    }
    while ( fscanf(fp, "%d", &buff) == 1)
    {
        prev[window] = buff;
        if ( ticker < window )
        {
        } /*do nothing*/
        else
        {
            if ( arraysum(prev, window, 0) < arraysum(prev, window+1, 1) )
            {
                cnt++;
            }
        }
        /*do poppy things here */
        memmove( &prev[0], &prev[1], (window) * sizeof(int) );
        ticker++;
    }
    retval = fclose(fp);

    printf( "cnt is: %d", cnt);
    return retval;
}

int main()
{
    int retval = 1;

    int movWind;
    char filename[100];

    printf( "input filename " );
    scanf("%s %d", &filename[0], &movWind);

    printf( "\ninput is: %s", filename);
    printf( " and window is: %d", movWind);
    printf( "\n");

    retval = readFile(&filename[0], movWind);

    return retval;
}