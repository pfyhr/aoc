#include <stdio.h>

int readFile(char *filename)
{
    int retval = 1;
    int cnt;
    cnt = 0;
    FILE *fp;
    int buff;
    int prev=0;
    fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("no such file.\n");
        return retval;
    }
    while ( fscanf(fp, "%d", &buff) == 1)
    {
        if (prev==0)
        {
            prev=buff;
        }
        if ( buff > prev )
        {
            cnt++;
        }
        prev=buff;
        //printf( "%s",buff);
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

    retval = readFile(&filename[0]);

    return retval;
}