 
char * function ( int i ) 
 { 
 return 'a' ; 
 } 
int main ( ) { 
 int a = 0 ; 
 a = 4 * 5 + 6 - 7 ; 
 for ( int i = 1 ; i <= 10 ; i ++ ) { 
 printf ( "Something will be compiled here!\n" ) ; 
 function ( i ) ; 
 } 
 return a ; 
 } 
