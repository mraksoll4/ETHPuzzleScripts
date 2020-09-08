f = open('j:/permutated.txt', 'r')
lines = []
for line in f:
    lines.append(line)
    f1 = open('j:/out.txt', 'a')
    #print (''.join(str(ord(c)) for c in line.strip('\n')))
    f1.write(''.join(str(ord(c)) for c in line.strip('\n')) + "\n")
    f1.close()
    #print (line.strip('\n'))
    
