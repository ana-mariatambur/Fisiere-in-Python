"""Afişaţi tabla înmulţirii cu numărul n. Exemplu: pentru n=5, se va afişa pe verticală 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50. 
Din fişierul « numar.txt » se citeşte un număr, în fişierul « inmultire.txt » - se înscrie tabla înmulţirii cu acest număr."""

with open('numar.txt','r')as f:
    a=f.readline()
    n=int(a)
with open('inmultire.txt','w')as f:
    f.write(str(n*1))
    f.write('   ')
    f.write(str(n*2))
    f.write('   ')
    f.write(str(n*3))
    f.write('   ')
    f.write(str(n*4))
    f.write('   ')
    f.write(str(n*5))
    f.write('   ')
    f.write(str(n*6))
    f.write('   ')
    f.write(str(n*7))
    f.write('   ')
    f.write(str(n*8))
    f.write('   ')
    f.write(str(n*9))
    f.write('   ')
    f.write(str(n*10))