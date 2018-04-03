#include <stdio.h>

int main()
{
    int a,b,c;
    a=0,b=0,c=0;
    c=a++ + ++b+b+++a--;
    c ^=a;
    printf("%d\n", c);
    return 0;
}
