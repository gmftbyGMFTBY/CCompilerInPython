#include <stdio.h>

char \
         w[10];

int main()
{
    int a,b,c;
    a=0,b=0,c=0;
    c=a++ + ++b+b+++a--;
    c ^=a;
    c = 2012.3E+1;
    c = 20.+2;
    printf("%d, %d\n", c, 0x78e2);
    return 0;
}
