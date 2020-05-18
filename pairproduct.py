def pairproduct(n,s):
    s.sort()
    return s[len(s)-1]*s[len(s)-2]

import time
if __name__ == '__main__':
    i=int(input())
    input_numbers = [int(x) for x in input().split()]
    start_time = time.time()
    print(pairproduct(i,input_numbers))
    print("--- %s seconds ---" % (time.time() - start_time))