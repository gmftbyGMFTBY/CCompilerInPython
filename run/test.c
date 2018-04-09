#define NUM 4

/* this is a demo program */

char* function(int i)
{
    return 'a';
}

int main(){
	int a = 0;
	a = NUM * 5 + 6 - 7; //here is a macro

    for(int i = 1; i <= 10; i++) {
        printf("Something will be compiled here!\n");
        function(i);
    }
	return a;
}
