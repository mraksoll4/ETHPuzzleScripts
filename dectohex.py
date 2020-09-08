f = open('j:/out.txt', 'r')
lines = []
for line in f:
    lines.append(line)
    for c in line.strip('\n').split():
        dec = c
        decimal = int(dec);
        inHexadecimal = hex(decimal);
        #print (inHexadecimal);
        f1 = open('j:/out1.txt', 'a')
        f1.write(inHexadecimal + "\n")
        f1.close()
    #print (line.strip('\n'))
    
