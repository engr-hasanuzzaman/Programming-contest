# transform string such that lowere case become uppercase and vise versa
def swap_case(s):
    ans = []
    for i in range(len(s)):
        if s[i].isupper():
            ans.append(s[i].lower())
        else:
            ans.append(s[i].upper())
            
    return "".join(ans)