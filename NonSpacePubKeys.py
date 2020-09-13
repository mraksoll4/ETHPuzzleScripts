from eth_keys import keys
from eth_utils import decode_hex
from itertools import *
from collections import Counter
for i in permutations(['2009January3',
                       '2020February2',
                       'BTC',
                       'CPD',
                       'ETH'], 5): # Pemutation  - Generator of N to M placements.
    b = (''.join(i)) # join all to line.
    #print (b.strip())
    if len (b.strip()) < 41: # remove all spaces from start and end lines , and cheek if len at line have no more than 41 symbols.
        #print (b.strip());
        asciitodec = (''.join(str(ord(c)) for c in b.strip())) # join with convesion to Decimal of ASCII table symbols.
        #print (''.join(str(ord(c)) for c in b.strip()))
        #print (line.strip('\n'))
        #print (asciitodec)
        if len (asciitodec) < 79: # cheek if len  no more than 79 symbols .
            decimal = int(asciitodec); # make decimal int.
            inHexadecimal = hex(decimal); # convert decimals to hex .
            #print (inHexadecimal)
            addzeroshex = inHexadecimal.strip("0x").zfill(64) # we remove 0x from hexes and add 0000 to make it 64 symbols len hex line as example 00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff.
            #print (asciitodec)
            restorehexformat = ('0x'+ addzeroshex) # We again add 0x to start of hex line.
            #print (restorehexformat)
            if len (restorehexformat) == 66: # extra cheek if hex with 0x have only 66 len of line.
                #print (inHexadecimal);
                priv_key_bytes = decode_hex(restorehexformat) # conversion to pub key start
                priv_key = keys.PrivateKey(priv_key_bytes)
                pub_key = priv_key.public_key
                pub_key.to_hex() # conversion to pub key start
                #print (pub_key.to_checksum_address())
                #f1 = open('m:/out/NonSpace.txt', 'a')
                #f1.write((restorehexformat + "\n")+''+str(pub_key.to_checksum_address()) + "\n")
                #f1.close()
                if (pub_key.to_hex() == '0x9f35c793522be1fdcfd50c3fb15f455cda37fb3fb779b9e4707c89a49cdf47242c3dc34778f7361a44c074a6a21e5972bbf5ca5265c9ea121ce4f2a5dc4964b6'): # cheek pub key of need address.
                    print ((restorehexformat + "\n")+''+str(pub_key.to_checksum_address()) + "\n") # print if find priv key + cheecksum address ( standart address format )
                    f1 = open('m:/out/NonSpace.txt', 'a')
                    f1.write((restorehexformat + "\n")+''+str(pub_key.to_checksum_address()) + "\n") # write to file if find priv key + cheecksum address ( standart address format )
                    f1.close()
