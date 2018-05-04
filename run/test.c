int globala = 1;
char globalb = 'a';

int test_func(int a, char b)
{
    int c = 1;
    int d=2;
    test_func(c, d);
    while (d < 3) {
        if (c == 1) return 0;
        else {
            a = a + 1;
            printf("%d\n", a);
        }
    }
}

int main(){
	int a = 0;
	a = 4 * 5 + 6 - 7;

    for (a = 1; a = 10; a = a - 1) {
        int p = 1;
        p = p + 1;

        if (p) {
            p = p + 1;
        }
        else if (k < 1) p=p-1;
        else {
            a = a * p - p / (a + p);
        }
        int res = test_func(a, p);
    }
	return a;
}
