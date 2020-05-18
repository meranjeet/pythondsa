def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n==0:
        return 0
    if n==1:
        return 1
    else:
        l=[0]*(n+1)
        l[0]=0
        l[1]=1
        for i in range(2,n+1):
            l[i]=(l[i-1]%10)+(l[i-2]%10)
        return l[n]%10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
