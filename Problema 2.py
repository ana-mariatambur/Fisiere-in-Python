"""Se dau două numere. Să se înmulţească cel mai mare cu doi şi cel mai mic cu trei şi să se afişeze rezultatele. 
Exemplu : date de intrare « numere.txt »: 3  7  date de ieşire « produs.txt »: 9  14"""
with open('numere.txt','r')as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x=int(a)
    y=int(b)
if int(a)<int(b):
    x=int(b)
    y=int(a)
n=x*2
m=y*3
with open('minim.txt','w')as f:
    f.write(str(n))
    f.write('      ')
    f.write(str(m))