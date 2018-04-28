#define NUM 4

/* this is a demo program */

int w = 1;
int* s;
char* pp;
char filename[100];

struct aaa {
    int p;
    int h;
};

char* function(int i)
{
    int h = i + function(2) - 5;
    while (1) {
        printf("nothing is need here!\n");
        if (h != 2) continue;
        else break;
    }
    return 'a';
}

int main(){
	int a = 0;
	a = NUM * 5 + 6 - 7; //here is a macro

    if (a < 1 && (function(a) == 1) || a !=2 ) {
        filename[1 + function(2)] = NULL;
        strcpy(filename, "ok nothing !\n");
    }
    else if (a == NULL) {
        ;
    }
    else if (a == ((12 + 3) < *s)) a = 1;
    else {
        a = 3;
    }

    switch (a) {
        case 1: function(1);
                break;
        case 2: a = 2 * 3 + (4 * 11 - 5) / 36;
                break;
        default:break;
    }

    for(int i = 1; i <= 10; i++) {
        printf("Something will be compiled here!\n");
        char* p = function(function(2));
        break;
    }
	return a;
}
