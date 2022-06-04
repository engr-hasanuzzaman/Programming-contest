# assume M & N are valid
def insertion(M, N, i, j):
    # store i-1 to 0 positions
    capture_mask = (1 << i) - 1
    capture_bits = N & capture_mask

    # reset jth bit to 0th bit. if we have bits with jth to 0th with 0
    # and j+1th bit to top set to 1 we can reset jth to 0
    clear_mask = -1 << (j + 1)
    N = N & clear_mask

    # insert m into N
    # adjust M, since we have to place M between i-j
    M = M << i
    # insert M between i-j th bits 
    N = N | M

    # add capture bits
    N = N | capture_bits
    print("new N is ", N)
    return N

'''
N = 1024 (10000000000),
M = 19 (10011),
i = 2, j = 6 
Output : 1100 (10001001100)
'''
assert insertion(19, 1024, 2, 6) == 1100

'''
N = 1201 (10010110001)
M = 8 (1000)
i = 3, j = 6
Output: 1217 (10011000001)
'''
assert insertion(8, 1201, 3, 6) == 1217