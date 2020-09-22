def printConsecutiveWithSumN(N):
    for i in range(2, N/2):
        if i % 2 == 1:
            if N % i == 0 and N / i >= i:
                a = [x for x in range(N / i - i / 2, N / i + i / 2 + 1)]
                print a
        else:
            if N / i >= i and N % i > 0:
                q = N / i
                f = N - q * (i - 1)
                if f == q + i / 2:
                    a = [x for x in range(q - i / 2 + 1, f + 1)]
                    print a

N = 125
printConsecutiveWithSumN(N)