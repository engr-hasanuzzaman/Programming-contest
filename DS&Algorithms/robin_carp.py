# s = string, t = text in which we will find text
def rabin_karp(s, t):
    p = 31
    m = 1000
    S = len(s)
    T = len(t)

    p_pow = [0] * max(S, T)
    p_pow[0] = 1; 
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i-1] * p) % m

    # h is hash
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

# s = "abc"
# t = "abdabcdedabcdabc"
# print(rabin_karp(s, t))

# easier to understand implementation
# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 1000003


def rabin_karp(pattern: str, text: str) -> bool:
    """
    The Rabin-Karp Algorithm for finding a pattern within a piece of text
    with complexity O(nm), most efficient when it is used with multiple patterns
    as it is able to check if any of a set of patterns match a section of text in o(1)
    given the precomputed hashes.

    This will be the simple version which only assumes one pattern is being searched
    for but it's not hard to modify

    1) Calculate pattern hash

    2) Step through the text one character at a time passing a window with the same
        length as the pattern
        calculating the hash of the text within the window compare it with the hash
        of the pattern. Only testing equality if the hashes match
    """
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return False

    p_hash = 0
    text_hash = 0
    # modulo powere of the size string p_len (c*p^0+c*p^1...c*p^(n-1)
    modulus_power = 1

    # Calculating the hash of pattern and substring of text
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        # take p-1 times (start with first power, m ^ (p-1)
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    for i in range(0, t_len - p_len + 1):
        if text_hash == p_hash and text[i : i + p_len] == pattern:
            return True
        if i == t_len - p_len:
            continue
        # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
        text_hash = (
            (text_hash - ord(text[i]) * modulus_power) * alphabet_size
            + ord(text[i + p_len])
        ) % modulus
    return False


def test_rabin_karp() -> None:
    """
    >>> test_rabin_karp()
    Success.
    """
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert rabin_karp(pattern, text1) and not rabin_karp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert rabin_karp(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert rabin_karp(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(pattern, text)

    # Test 5)
    pattern = "Lü"
    text = "Lüsai"
    assert rabin_karp(pattern, text)
    pattern = "Lue"
    assert not rabin_karp(pattern, text)
    print("Success.")


if __name__ == "__main__":
    test_rabin_karp()