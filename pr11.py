n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,'elemente pentru vectorul creat')
#if n<10:
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print('a) Afiseaza pe ecran componentele tabloului la un interval de 5 pozitii:',a)
print('b) Afiseaza pe ecran numerele in ordinea inversa a introducerii in calculator:',a[::-1])
c=sorted(a)
c.sort(reverse=True)
print('c) Sorteaza componentele in ordine descrescatoare:',c)
d=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        p=a[i]
        d.extend([p])
print('d) Afiseaza pe ecran doar componentele pare:',d)
if len(d)>0:
    print('e) Afiseaza pe ecran media aritmetica a componentelor pare:',sum(d)/len(d))
f=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        s=a[i]
        f.extend([s])
print('f) Afiseaza pe ecran doar componentele impare:',f)
x=eval(input('x= '))
y=eval(input('y= '))
g=[]
for i in range(0,len(a)):
    if a[i]>x and a[i]%y!=0:
        t=a[i]
        g.extend([t])
print('g) Afiseaza pe ecran doar componentele care sunt mai mari ca x si nu sunt divizibile cu y',g)
h=[]
for i in range(0,len(a)):
    if a[i]>x and a[i]<y:
        q=a[i]
        h.extend([q])
print('h) Afiseaza pe ecran doar componentele care sunt mai mari ca x si mai mici decat y:',h)
i=[]
for i in range(0,len(a)):
    if a[i]%2!=0 and a[i]<0:
        i.append(i)
print('i) Afiseaza pe ecran pozitiile componentelor impare negative:',i)
j=[]
for i in range(0,len(a)):
    if a[i]/10>=1 and a[i]/10<10:
        z=a[i]
        j.extend([z])
print('j) Afiseaza pe ecran componentele ce contin doar doua cifre semnificative:',j)
k=a.copy()
k[0]=min(k)
print('k) Inlocuieste prima componenta a tabloului cu componenta de valoare minima din tabloul respectiv:',k)
l=a.copy()
l[l.index(min(l))]=l[0]
print('l) Inlocuieste componenta de valoare minima din tabloul respectiv cu prima componenta a acestuia:',l)
m=[]
for i in a:
    if i%2==0:
        m.append(i)
print('m) Creeaza un tablou nou format doar din componentele pare ale tabloului introdus de la tastatura:',m)
n=[]
for div in a:
    if div%3==0:
        n.extend([div])
print('n) Creeaza un tablou nou,format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatura:',n)
o=[]
for i in a:
    if i>0:
        w=0
        for j in range(1,i+1):
            if (i%j==0):
               w+=1
        if w<=4:
            o.extend([i])
print('o) Creaaza un tablou nou,format doar din acele componente ale tabloului introdus de la tastatura care au cel mult patru divizori:',o)
#else:
print('Numarul de elemente trebuie sa fie intre 0 si 10')