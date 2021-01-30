def rotateRight(A,D,N):
    if D > N:
        D = D % N
    for i in range(gcd(N, D)):
        j = i
        # this value we are going to rotate
        temp = A[N - 1 - i]
        while 1:
            # next value that we will place at j
            k = j +  D
            # if k is larger than array size that means we have to rotate
            if k >= N:
                k = k - N
            # array rotated and back to start position
            if k == i:
                break
            A[N - 1 - j] = A[N - 1 - k]
            j = k
        A[N - 1 - j] = temp 


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)