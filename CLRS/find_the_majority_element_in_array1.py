# Using Moore’s Voting Algorithm)
def majorityElement(A,N):
    candidate = find_the_candidate(A, N)
    count = 0
    for num in A:
        if num == candidate:
            count += 1
            if count > (N // 2):
                return num
    return -1

# it will return correct num if any or candidate
def find_the_candidate(A, N):
    maj_index = 0 
    count = 1
    for i in range(1, N):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]
            
