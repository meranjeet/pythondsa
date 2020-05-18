def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    def F(n):
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

    def pisanoPeriod(m):
        previous, current = 0, 1
        for i in range(0, m * m):
            previous, current = current, (previous + current) % m
            if (previous == 0 and current == 1):
                return i + 1

    c=n%pisanoPeriod(m)
    return F(c)%m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
