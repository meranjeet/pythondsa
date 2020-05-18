import random
import sys
import os

tests=int(sys.argv[1])
n=int(sys.argv[2])

for i in range(tests):
    print('Test #'+str(i))
    os.system("python randomlist.py "+str(n)+" > inputpair.txt")
    os.system("more inputpair.txt >> all.csv")
    os.system("python pairproduct.py < inputpair.txt >> pairproduct.csv")
    os.system("python pairproduct_1.py < inputpair.txt >> pairproduct_1.csv")