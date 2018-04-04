#define A 64
                                 #define/*++++[>++>+*/B 256
                           /*+++[>++++>+++++>[*/#include<time.h>
                       /*]<<<-]<<-]>>>++.+++>++*/#include<stdlib.h>
                   /*[>+>+<<-]>>.<+.<<<<[->>>+>->>>>>[*/#include"SDL.h"
                 #define/*]<<<<<<<<<]>>.>>>.<.<++.[>]<>[*/m(a,b,c)a##b##c
              typedef/**/Sint32 i;i/**/p[A][4][B][2],d[4][B][2],q=0,b[4][2]
            ,S,C,H,I,e,R,K,E=1,G,u,t,s=SDL_HWSURFACE|SDL_DOUBLEBUF,P[4][3]={{
           255,16,16},{00,255,00},{255,255,64},{64,128,255}},w=800,h=600; const
          SDL_VideoInfo*v;SDL_Surface*o;SDL_Event n;i O(i/**/x,i y){return(y-x)*
        (float)rand()/RAND_MAX+x;}void g(i z,i x,i/**/y){if(p[q][I][S][C]<z)d[I][
   S]  [C]+=O(x,y);if(p[q][I][S][C]>z)d[I][S][C]-=O  (x,y);e=d[I][S][C];d[I][S][C]
   =e<-H?-H:(e>H?H:e);}void c(i x,i/**/y,i/**/z){t   =SDL_MapRGB(o->format,x*S/A,y*
   #define r(Z){SDL_FillRect(o,NULL,t);for(S=1;S      <=A;S++){C=(q+S)%A;for(I=0;I<4\
 ;I++){c(255,255,255);for(H=0;H<B;H++){if(H==          1)c(P[I][0],P[I][1],P[I][2]);e\
  =p[C][I][H][0];e>>=16;if(e>=0&&e<w){R=p               [C][I][H][1];R>>=16;if(R>=0&&\
R<h)*(Z*)((Uint8*)(o->pixels)+R*(o                        ->pitch)+(e*K))=(Z)t;{;}}}}}}
 S/A,z*S/A);}int main(int                                  x,char**y){if(SDL_Init(m(SDL,
_INIT_,VIDEO))<0)puts(                     "SDL\40error.     ");else{;atexit(SDL_Quit);v=
SDL_GetVideoInfo();K=v->                                m(v     ,fm,t)->BytesPerPixel;if(K
  -2&&K!=4)puts(                                                  "Bad\40pixel\40format");
   else{if(x>                                     1)s|=              SDL_FULLSCREEN;o=m(SD,
   L_SetVideo     ,Mode)(                      w,h,K*8,s)            ;if(!o)puts("error!");
  else{;m(SDL    , _WM_SetC                    ,aption)(  "           Schierke",NULL);srand(
  time(NULL))   ; for  (I=                      0;I  <4;   ++         I){for(S=0;S<B;S++){p[
  0][I][S][0]     =O(0,w<<                      16);for(              p[C=0][I][S][1]=O(00,h
  <<16);C<2;d[       I][S]                       [C++]=O              (-3<<16,3<<16));}for(S
  =1;S<A;S+=1)      for(C                         =0;C                <B;C++)for(H=0;H<2;H++
  )p[S][I][C][                                                       H]=p[0][I][C][H];b[I][0
  ]=O(0,w<<16)               ;                                       b[I][1]=O(0,h<<16);}m(S
  ,DL_ShowCurs              ,                                        or)(SDL_DISABLE);for(u=
  SDL_GetTicks                                                      ();E;){u+=16;c(0,0,0);m(
  SD,L_LockSur                                                     ,face)(o);if(K-4)r(Uint16
  )else r(m(Ui                                                    ,nt,32))SDL_UnlockSurface
   (o);SDL_Flip                                                  (o);for(I=0;I<4;I++){if(!O
   (0,60)){b[I]                                                 [0]=O(50<<16,(w-50)<<16);b
   [I][1]=O(50<<                                      16      ,(h-50)<<16);}H=2<<16;g(b[I]
    [S=C=0],16,8<<9         );g(b[I][C=1]             ,16,8<<9);H*=2;for(S=1;S<B;S++){g(p
     [q][I][0][C=0]           ,32,3<<11)               ;g(p[q][I][0][C=1],32,3<<11);}H=(
      q+1)%A;for(S=             0;S<B;                 S++)for(C=0;C<2;C++)p[H][I][S][C
       ]=p[q][I][S][C                                   ]+d[I][S][C];}for(q=H;m(S,DL_,
         PollEvent)(&n)                                  ;)if(SDL_KEYDOWN==n.type||n
            .type==m(SDL_                              ,QU,IT))E=0;G=SDL_GetTicks()
               ;if(G<u)m(SDL                        ,_De     ,lay)(u-G);}m(S,DL_,
                 FreeSurface)(o                 );}}          SDL_Quit();}m(re,
                    tur,       n)/*       ]c2011                  omoikane[.>
                                   +]*/0;}
