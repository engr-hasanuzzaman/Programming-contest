# https://leetcode.com/problems/regular-expression-matching/

# solve using using recursion
def is_match(s, p)
  return s.empty? if p.empty?

  first_match = !!s[0] && ['.', s[0]].include?(p[0])

  if (p.size >= 2) && (p[1] == '*')
    # puts("-----s #{s}, p #{p}, #{first_match}")
    # two carse
    # 1. we can ingore this pattern or 
    # 2. keep the same patter to match multiple element if curent char matct with pattern
    is_match(s, p[2..-1]) || (first_match && is_match(s[1..-1], p))
  else
    first_match && is_match(s[1..-1], p[1..-1])
  end
end
