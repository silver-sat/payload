import random
import names

from names import(
    a,b,c,d,e,f,g,h,i,j,k,l,m,o,p,q,r,s,t,u,v
    )


namelist=[a,b,c,d,e,f,g,h,i,j,k,l,m,o,p,q,r,s,t,u,v]
for i in range(0, 21):
    nameindex = random.randint(0, 21)
postme = 'Thanks for donating {}! Hello from Space! \n '.format(namelist[nameindex])

