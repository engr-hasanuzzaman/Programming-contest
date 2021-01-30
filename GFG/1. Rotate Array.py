# divide the array into sub-set of the element GCD(N, D) where
# N array size, D number rotateion and rotate one element to from each subset
#  
def rotateLeft(A,D,N):
    if D > N:
        D = D % N
    for i in range(gcd(N, D)):
        j = i
        # this value we are going to rotate
        temp = A[i]
        while 1:
            # next value that we will place at j
            k = j + D
            # if k is larger than array that means we have to rotate
            if k >= N:
                k = k -N
            # array rotated and back to start position
            if k == i:
                break
            A[j] = A[k]
            j = k
        A[j] = temp 

def rotateRight(A,D,N):
    if D > N:
        D = D % N
    for i in range(gcd(N, D)):
        j = i
        # this value we are going to rotate
        # for i N-1-i will be from the last to first
        # so, replace A[i] with A[N - 1 - i] for right rotate
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