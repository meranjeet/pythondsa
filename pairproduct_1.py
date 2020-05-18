def MaxPairwiseProductFast(n,s):
    max_index1 = -1
    for i in range(0,n):
        if s[i] > s[max_index1]:
            max_index1 = i
        else:
            continue

    max_index2 = -1
    for j in range(0,n):
        if s[j] > s[max_index2] and s[j] != s[max_index1]:
            max_index2 = j
        else:
            continue

    Product = s[max_index1]*s[max_index2]
    return Product

import time
if __name__ == '__main__':
    i=int(input())
    input_numbers = [int(x) for x in input().split()]
    start_time = time.time()
    print(MaxPairwiseProductFast(i,input_numbers))
    print("--- %s seconds ---" % (time.time() - start_time))