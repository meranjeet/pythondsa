def fibonacci_number(n):
    #assert 0 <= n <= 45

    if n==0:
        return 0
    if n==1:
        return 1
    else:
        a=0
        b=1
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
