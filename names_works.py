from random import randrange

from names import(
    a,b,c,d,e,f,g,h,i,j,k,l,m,o,p,q,r,s,t,u,v
    )


namelist=[a,b,c,d,e,f,g,h,i,j,k,l,m,o,p,q,r,s,t,u,v]  
random_index = randrange(len(namelist))
postme = ('Thanks for donating {}! Hello from Space! \n '.format(namelist[random_index]))
