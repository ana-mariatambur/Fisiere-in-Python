with open('text.txt', 'r') as f:
    sir=list(f.read())
with open('litereA.txt', 'w') as f:
    f.write(str(list(filter(str.isupper, sir)))
with open('litereB.txt', 'w') as f:
    f.write(str(list(filter(str.islower, sir))))
with open('semnedepuntuatie.txt', 'w') as f:
    f.write(str(list(filter(lambda a: a in ['[',']','(',')','{','}',"'",'*','/','//','%','**',',',';','.','!'],sir))))
with open('cifrele.txt', 'w') as f:
    f.write(str(list(filter(lambda b: b in ['1','2','3','4','5','6','7','8','9'], sir))))