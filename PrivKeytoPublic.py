from eth_keys import keys
from eth_utils import decode_hex
f = open('j:/out1.txt', 'r')
lines = []
for line in f:
    lines.append(line)
    for c in line.strip('\n').split():
        dec = c
        priv_key_bytes = decode_hex(c)
        priv_key = keys.PrivateKey(priv_key_bytes)
        pub_key = priv_key.public_key
        pub_key.to_hex()
        #print (pub_key.to_checksum_address() + "\n")
        f1 = open('j:/out2.txt', 'a')
        f1.write(pub_key.to_checksum_address() + "\n")
        f1.close()
    #print (line.strip('\n'))
    
