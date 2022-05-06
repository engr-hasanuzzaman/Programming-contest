def rabin_karp(s, t):
    p = 31
    m = 1000
    S = len(s)
    T = len(t)

    p_pow = [0] * max(S, T)
    p_pow[0] = 1; 
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i-1] * p) % m

    h = [0] * (T + 1) 
    for i in range(T):
        h[i+1] = (h[i] + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % m
    
    h_s = 0; 
    for i in range(S):
        h_s = (h_s + (ord(s[i]) - ord('a') + 1) * p_pow[i]) % m; 

    occurences = []
    i = 0
    while i + S - 1 < T:
        # to convert neg (ex. 20 - 30 + 50) % 50 = 40) -> position 10, we arr
        cur_h = (h[i+S] + m - h[i]) % m; 
        if (cur_h == h_s * p_pow[i] % m):
            occurences.append(i)
        i += 1
    return occurences

s = "abc"
t = "abdabcdedabcdabc"
print(rabin_karp(s, t))

