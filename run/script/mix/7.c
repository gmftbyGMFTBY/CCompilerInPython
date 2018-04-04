(*      ,
                                                   177   ,o*)        open
                                                  Array (**)       module    L=
                             List          ;;let u,i,h,a,r,u_     =300,4,(0,0,
                              (0)),       float,truncate,(atan2( 0.)(-      1.0     ))
                               ;;let(  s,v   ,w)=L.split        ,fill          ,L.map;;      let(
                                c,n)=();a      (i),u  *           i;;           module    R=Random
                                 ;;let(o,k      )     =                        make_matrix(n)(n   )
                       (124,194,169),75.0*.  c;;     let              e(     p)=let(*o*)q=();(     r(   p
                     ))   mod(n)in(if(q     <(0)    )then(n+         (  q)   )        else(**)q         ) (*
               *);; let    t(p)q=(    q-.                p)<          0.5              ;;let          j(d)=L.
               fold_left    (fun        (p,      q)x   ->(                    min       (x)p,            max(
                x)q))(infinity,         (*bo .  d  *)-1.*.                      infinity)  d;;(*.    *)  exception(*_*)
             I;;let(*      *)x         (p)q=   ((  fst)(q)            )           -.       (fst(p   ));;let(**)y(p)q=
             (snd(         q)         )-.(snd  p  );;let z(          p)q           (     d)    =(x(p)d)*.(y(p)q)<(
       x(p)q)  *.(         y      (p)d);;              (   );;    let(**)m        (p)   q=     (p+.q     )/.2.0;;let
      f   (x)   w=L    (**)          .iter(fun  h(*   '      *)->let(x,y)=s(h)in(let(j,k),     (p,q        )=j(x),j(y
      )    in   (for  s= (r           (p))to(  r(q+.       0.5))do(let(**)y=(a)(s)in(let  a(x)=match       (h)with  (o)
      ::      p::      q->            (if(z(o)p(x,y))then(false)else(let(**)rec(*|  *)r  (u)      i=       match(     i)
    with    ([      ]                )->z(u)(x,y)o|b::d->(if((z)(u)b(x,y))then(1=77  )  else         (r(   b    )d     ))
    in(r    (p      )                q)))|_->(false)in(let(**)rec(**)u(p)q=if(t(p)q  )  then         (*[   ]    `;     *)
   (  raise(     I)       )else(let(**)x=m(p)(q)in(if(a(x))then(x)else(();try(u(p  )x)   with        I->         ();u(x)
    q) ))in    (let       rec(**)b(p)q=if(t(p)q)then(q)else(let(**)x=m(p)q in(if(a(x))   then    (b          )p (x)else(b
       )x(q)  ))in       (let(**)rec(**)d(p)q=if(t(p)q)then(p)else(let(*L1*)x=(m)p(q)in (if((a)(x))           then(d
)    x (q)else( d       )p(x)))in(try(let(**)x=(u)j(k)in(let(f,g,h)=e(b(j)x),e(d(x)k),e(y)in(if(f<=  g  )     then(v(
      o.(h))f   (g    -f)w)else(v(o.(h))0(g+1)w;v(o.(h))f(n-f)w))))with(I)->()))))))done)))x;;let(*. 8  ;    *)  g(b)p
      (q)=w  (    fun(x,y)->x+.p,y+.q)b;;let(*o*)t(x)=match(x)with[p;b;q;d]->let(**)rec(**)i(z)u=if(z=   64  )     then
      (L (* ;     *).rev(u))else(let(**)w(x)y=(x+.(a(z))*.(y-.x)/.64.0)in(let(f,g,h)=w(p)b,w(b)q,w(      q  )       (d(*
    -=*)   )     in(let(x,y)=w(f)g,w(g)(h)in(i(z+1)((w(x)y)::u)))))in(i)0 [d]|_->[];;let(*177*)j(p)q(d)    b         =let
      u=    w(fun(x,y)->((x*.c),(y*.c)))(b)in(let(* *)rec(**)b(f)=if (f=0  )then[]else(let(i,o)=s(g(*.   o   8         *)
      ( let  d =((((a(f))*.72.0)+.d)*.u_/.180.0)in( let(o,c)=cos(d),  sin(  d)in(w(fun(x,y)->(o*.x-.c*. y),(c*.x        +.
      o*.      y))u)))p(q))in(L.combine(t(i))(t(o))  ))::(b(f-1))in(   (b)   (5)));;let(**)t(p)(q)(o)(x)(y)(z)=let       u
      =j       (x)y(z)in(let(b,d)=u(p),u(q)in(let(*   *)p=(w)L.hd(d)    in    (f[p]o;f(b)h;f(d)o)));;let(**)e(x)(y)(z     )
      =(       t)[(3.290,-0.75);(19.61,-27.60  );((    -4.78),- 24.20);(-1.80  (*' *),-2.50)][(2.46,1.32);(17.7,-25.42)(*  |
       |      *);(-4.47,-21.44);(-1.92,(-0.62   ))]     (234,236,237     )( x)y(z);;let(**)rec(**)d(p)q=if(q=0)then[]else(let
       z=    0.2*.u_*.(a(q))in(p(**)*.cos(z),   p*.      sin(z)  )::      (          d(p)(q- 1)));;let(**)w(x)y(z)=t[(15.24
        ,   (**)-8.520);(39.81,-51.51);(-34.94   (*        2010   1                    `*),-  52.33);(-9.32,-11.85)][(14.42
         , (-6.64));(37.08,-48.54);((*     -       `        *)                             -    31.98,-48.81);(-7.94,-8.74)
          ]( 233,185,185)x(y)z;f[(g(d(                                                            5.*.c)10)x(y))]h;f[(g(d(c
             *.3.5)10)x(y))](221,  218                                      ,167);;                let(c,t)=R.float,Printf.
            printf(*01*);;let(h,g   ,                                   f)= iter,iteri,           init;;R.self_init();;let(*
             *)b()=(c(k*.0.4)) -.        (0.2*.                            k);;let(*^*)j(z        )=let(**)rec t(i)o=match(i)
             with (p)::q->();t(       q)(o+.p)|[]                          ->b()+.(  o/.4.0)      in(let(x,y)=s(z)in(t(x)0.,t(y
             )0.0 ));;let(**)s=      r((a(n))/.(                           k));;let(**)r(  p)     =let(x,y)=(p)in(x+.a(n),y);;let
             d(*'  *)(p)q=f(s)(    fun (z)->  if(                          z=0)then(j[p.(   s-   1);r(p.(0));q.(s-01);r(q.(0))])else
             (j[    p.(z);p(**)   .(z -1);q.(z);q                          .(z-1)]));;let    r   (x)(y)=f(s)(fun(z)->(**)(x+. b()+.(a(
              z)    )*.k,y+.b()   ))  ;;let(**)j=                           f    s(fun(z     )  ->r (b())((a(z))*.(k)));;let(r,
              k)=   i*i,f(s)(fun  (z   )->if(z=0)                               then(d(     j   .( s-1))(map(  fun(x,y)->x,y+.a(n
               ))   (j.(0))))else  (   (d)(j.(z))                             (j.(z-1)         )) );;let(**)a    (p)(q )=h(fun(d)->(
                h  )(fun(x,y)->p(x         )y(c(                                                  360.0)))d)      q;;a  (w   )j;a(e)
                   k;;let(**)a(x)         y=let                                                  (( ru,i,ko       )(**)   )
                  ,(ka,za,ri)=(x,                                                               y)  in((ka       +ru),i+
                 za,ri+ko);;for (*                     ob                                      /    *)y=0  to(   u-(1))do
                (for  z=(();0)to(i                     -1)                                          do( let(*  *)  b=(y*i+
                z     )in(o .(b)<-                                                                  (       let      (*-*)d
                      =(o.  (b))in(                                                                   let(**)o=
                     make    (u)(d.(                                                             0))in(for x=(1
                     -1       )to(u-                                                            1)do(let(**)rec
                               p(*( )                 *)              (q)                     =(if(q=1)then(d.(
                                 x* i)                  )else(a(d.(x*i                       +q-1))(p(q-1))))in
                                   ( o.                                                    (x)<-p(i)))done )(*[
                                       Oo                                                *);o))))done;o.(y  )<-o
                                         .(                                            y*i);let(**)p=o.(y)   in(
                                           for                                      z=( 1)to(i-1)do(g(fun(    x)
                                              q->                                 p.    (x)<-a(p.(x)) q)(o      .
                                                 (y*                           i+z      )))done))done  ;()
                                                   ;;let                   (*P'         @_@*)s='\x20'    ;;
                                                   t"P3\n%d"(          (*;'             *)u);t" %d"u;
                                                    t"\n255\n";g(fun(y                  )d->if(  (y)<
                                                    (u))then(h(fun                       (p,q,b   )->(
                                                     t)"%d %d%c"(p                       /r)(q/      r
                                                     )s;t   "%d\n"                       (b /r)
                                                     )d      )else                       (*   *)
                                                              ())o                       ;;
