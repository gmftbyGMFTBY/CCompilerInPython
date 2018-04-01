#define NUM 4

/* this is a demo program */

int main(int argc, char* argv[]){
	int a = 0;
    int b = - 5;
	a = NUM * 5 + 6 - 7; //here is a macro

    a ++;
    a += 1;

    a --;
    a -= 1;

    b = a * 2;
    b *= a;

    b = a / 2;
    b /= a;

    b = a % 2;
    b %= a;

    b == a;
    b != a;
    b <= a;
    b < a;
    b >= a;
    b > a;
    b >> 2;
    b << 2;

    a = ~b;
    
    a && b;
    a & b;

    a | b;
    a || b;

	return 0;
}
