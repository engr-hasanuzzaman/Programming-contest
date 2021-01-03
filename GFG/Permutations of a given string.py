def permutations(s, current_p, p):
    if len(s) == 0:
        p.append("".join(current_p))
    
    for i, c in enumerate(s):
        current_p.append(c)
        permutations(s[:i] + s[i+1:], current_p, p)
        current_p.pop()
    
n = int(input())
ans = []
for _ in range(n):
    p = []
    current_p = []
    s = "".join(sorted(input()))
    permutations(s, current_p, p)
    p.sort()
    print(" ".join(p))

    