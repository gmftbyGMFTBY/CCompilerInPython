#include <stdio.h>

int main()
{
    int a,b,c;
    a=0,b=0,c=0;
    c=a++ + ++b+b+++a--;
    c ^=a;
    printf("%d, %d\n", c, 0x78e2);
    return 0;
}
