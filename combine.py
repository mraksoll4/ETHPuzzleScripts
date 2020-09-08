from itertools import *
from collections import Counter
for i in permutations(['CPD','BTC','ETH','Bitcoin','Token','creation','2020May12','2020June1','2020July1','2020August1','2020September1','2020June01','2020July01','2020August01','2020September01','2020February02','2020February2','#629999','Block','CPDProject.com','CPDProject','CPD_Project','629999','Genesis','2021January3','2021January03','distribution','100','Address','Ownership','Verification','Roadmap'], 5):
    #print (''.join(i))
    f = open('f:/permutatedpuzzle.txt', 'a')
    f.write(''.join(i) + "\n")
    f.close()
