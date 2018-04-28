#ifdef o
                                                                 /*>++<[*/#include<stdio.h>
                                                        G*W[]={"baac","baac","dffe","dghe","i..j"}
                                                  ,*t[]={"....","....","....",".aa.",".aa."};Z/*##*/int
                                             i;using/**/namespace/**/std;_ V;i C,T,O,R,I,Q,U,E[0400];struct
                                        B{B(B*v):b(v){if(v)for(U=0;U<5;U++)for(Q=0;Q<4;Q++)A[U][Q]=v->A[U][Q];}
                                    H/**/c(i k,i a,i z,i u){i y=A[a][k];A[a][k]=A[a+u][k+z];A[a+u][k+z]=y;}i/**/d
                                 (i u,i v){j(v>       -  1&&v<     5&&u>-    1&&u<4)?A[v][u]:0;}i p(i u,i v){j E[d(u
                                ,v)];}i/**/q       ()  {for(T    =0;T <=     4 ;T++) for(C=0;C<4;C++)if(t[T][C]-46&&A[
                              T] [C  ]-t[T       ][   C])j+    0; j  1;     }  H D(){ V   .clear();for(U=0;U<5;U++)for(Q
                           =0  ;   Q<4;Q       ++)  V.o (     p ,   us     ,  h_back)( E   [ A[U][Q]]);}B*b;i A[5][4];};B*
                         r  ,*s   ;o(qu      ,eu   ,e )<    B *>   n;      o  (s, e,t)  <  _> m;G*e(B&v){j/**/v.d(C,T)-46?(
                       "  "):   "::";      }F f   (B &    v) {R    =C     -   1;j v.d(R ,   I  )-v.d(C,I)?v.d(R,I)-v.d(R,T)||
                    v.  d (C   , I)-      v .d   (C      ,  T     )?     +   43: 124 : v .   d (R,T)-v.d(C,T)?43:v.d(R,I)-v.d(
                  R,  T  )    ? 45:      * e   (v )    ;; }F     g(      B   & v ){j v .  d  (  C -1,T)-v.d(C,T)?(124):*e(v);}i
                h(  B   &   v){O=v      . b   ?1 +    h  (*     v.b     )    : 0 ;/* ]  > +   <  [ < */l"Move\40%d\n",O);for(T=0
               ;  T    <   6 ;) {     I= T   -1 ;    {  ;}     for      (    C = 0 ;    C  <   4 ;  C  ++)l"%c%s",f(v),v.d(C,I)-v
             .  d(    C   , T) ?      "-"    "-"    :  e(      v)       )   ;  ; l /* k  u j   o     u  */"%c\n",f(v));if(T<5){for
           (C  =     0   ; C< 4      ; C    +=1   )l  /*      ] >      [    >  + +  + >  >  >   [    */  "%c%s",g(v),e(v));l"%c\n"
          ,  g      (   v )) ;      } ++   T;}   j(  O);     }H Y      (    )  { (  * s   ) .   D     (   );if(m.insert(V).second){
         (  n      )   . push      (  s   );}   ;}H  w(      i k       ,    i    a  ,  i  z  ,  i      u   ,i y,i A,i v,i b){;s=new
       B( r)      ;   s ->c (     k, a   ,z,   u);  s->     c( y       ,    A    ,   v ,  b  )   ;     Y    ();}H/**/x(i k,i a,i z,i
      u) {       w   ( k,a,z      , u    ,0   ,0,   0,      0  )       ;    }    i     o   ( m   ,      a    ,in)(){B v(0);for(T=0;T
     <5 ;       ++  T )for (     C  =   0;    C <  4;       C ++       )    v    .      A  [ T]  [C     ]    =W[T][C];E[46]=5;for(T=0
    ;T <       5;   T++)for      ( C    =    0 ;   C<      4  ;C       =    +    1      +  C  )  if           (!E[O=v.d(C,T)])E[O]=O-
    v.d        (C  +1,T ) ?     O  -   v.   d( C  ,T+      1  )?       1    :              2  :  O-           v.d(C,T+1)?3:4;s=&v;for
   (Y(        );  n.size ()     ; ){   r    =  n  .o(      f ,ro       ,    nt             )  (  );            n.pop();if(r->q()){h(*
  r);o        (b  ,r  ,eak     )  ;   {;    }  } for       ( T =       0     ;    T        <  5  ;T            ++)for(C=0;C<4;C++)if(
  r->        d(   C, T )==    46  )   {{   ;   } for       ( R =        -    1    ;        R  <  2 ;           R +=2){O=r->p(C+R,T);if
 (01         ==  O)  x ( C    ,T  ,  R,0   )  ;; if(       O==  3       &&    (   *        r  )  . d           ( C+R,T)==r->d(C+R*2,T)
 )x(         C,  T,  R * 2    ,0  )  ;if   (  +5 ==O)      {if  (       (*    r            )  . p( C           +  R*2,T)==1)x(C,T,R*2,
 +0          );  if  (r->     p( C   + R   *  2, T)==      3&&   r      ->     d   (     C +  R *2 ,           T  )==r->d(C+R*3,T))w(C
,T,          R*  2,  0,C+     R, T   , R  *2  ,0 );}}      for   (I      =-    1   ;     I <  2 ;  I           =   I+2){O=r->p(C,T+   I
);          if(  +1 ==O)x     (C,T  ,0 ,I );  if ( +2      ==O    &&     r->    d   (     C, T  +  I           )   ==r->d(C,T+   I*   2
))          x(C  ,T ,0,I*2    );if  (   O==+  5 ){ if(      01     ==    r ->    p  (     C, T  +  I           *   2) )x (C ,T   ,0   ,
I*          2);  if (r-> p    (C,T+ I    * 2  ) ==  +2      &&r     ->   d  (        C     , T +I  *           2   )==(  *  r)  . d    (
C           ,T+   I  *3 ))     w (C ,    T,0   ,I*2 , C      ,T      +   I  ,0       ,     I*  2  );           }  } if(  '.'==  ( *    r
            ).d(  C  +1 ,T)    )for(I     =-     1;  I <     2;        I =   2        +   I )  {  if          (+  3  ==  ( * r  )  .   p
             (C,  T+ I) &&r    -> d(C,T+I)==     +r           ->        d(    C       +1  , T +I ))           w   (   C  , T , 0,  I   ,
             C+1, T,  0,  I)    ; if    (r->p     (            C                   ,T+I)  ==  4  &&           (  *r   ) . d  ( C,T +    I
             )==r  -> d(    C+  1 ,T  +I)&&r->                      d(C,T+I*02)         ==(*  r ) .           d  (C+ 1  , T  +I  *  2   )
             &&r-> d ( C     ,T  +    I)==r->d                     (C   ,T+I*2))w(C      ,T  ,  0,I           * 2  , C  +1,  T,  0  ,   I
              *2 ) ;if( 1     ==r->   p(C,T+I                        ))x(C,T+I,1,-I);   if   ( ( *            r )  . p   ( C +    +     1
              , T + I)==1)      x(C   +1,T+I,                        -1,-I);}if(46  ==  (*  r )  .           d (    C,   T + 1    )      )
               for(R =- 1;R<    2;     R+=2){                         if(2==r->p(C  +  R,   T ) &&           r->    d(  C  +R     ,T     )
                == ( r)  ->d(   C+      R,T                           +1))w(C,T,R     ,0   ,    C        ,T  +1 ,    R  ,   0      )      ;
                if  ( r   ->p(C  +                                     R,T)==4&&     (*        r         )  .d( C    + R,   T)     ==     (
                  *  r).   d   (C+R                                                 ,T         +        1)  &&   (   * r     )      .      d
                   (  C+         R*                                               2,T         )        ==r ->    d   ( C      +      R     *
                     2            ,                                             T+ 1          )       &&( *r)     .  d ((     C      )      +
                       R  ,T      )==                                             r->        d      (C  +R* 2     ,  T) )      w      (     C
                                    ,T,          R*2,0,                                    C,T  +1,R*        2    ,  0)  ;     if      (     (
                                    1 )==                                                 (* r)      .       p     ( C+   R     ,             T
                                   )  ) x(C                                            +R,     T     ,-       R    , 1)   ;     if            (
                                   1 ==r   ->p                                       (C+         R    ,T       +    1))    x     (             C
                                   + R ,    T +1,                                -R,-1                 );      }}   }j      0    ;              }
                                  /*] <    <   <[>+*/                      #else    /*                   >      +   ++      +    +              */
                                  # /*+  +>   [ */   define o(x,y,z)x##y##          /*]                   <      +           <   */               z
                                 /*  <  - ]  <  */  #include<string>/*-]>>>++       + +.                   +     <>  +       +    .               */
                                #   /*-  > [    */   define/**/Z/**/o(typed,/*      [   ]                   */    e  ,             f                )
                               #   /*    ]      <-     -.  -*/ include<set>/*      --     .<     +                 .          <    [                */
                              Z/* */    std::   o(        st,      rin     ,       g)        _    ;                Z          o    (                  c
                                                 ,       ha,        r)F            ;Z           o( co,              n              ,     st            )
                                                 F     G;/*         */Z            o                (vo,i           ,               d     )H            ;
                                                      /*+-          ]*/            #                       define                   l   printf           (
                                                                    /**/                                      # include             <queue>   /*[        */
                                                                                                               #/**/  define        j  o(ret,   ur,        n)
                                                                                                                             #include   /*]2011*/ __FILE__
                                                                                                                                  #/*     */endif
