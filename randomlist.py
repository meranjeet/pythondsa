import random
import sys


s=int(sys.argv[1])
print(s)
print(' '.join([str(random.randint(-1000,1000)) for i in  range(s)]))
