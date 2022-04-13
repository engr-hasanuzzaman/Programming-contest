# /**
#  * We have an array with three lettered strings.
#  * We can swap either the first two or the last two characters of the strings.

#  * Create a function that will return the maximum number of same strings that we can generate.

#  * Examples:
#  * ["aab", "cab", "baa", "baa"] = should return 3.
#  * ["aba", "cab", "aba", "aba"]
#  * ["zzz", "zbz", "zbz", "dgf"] = should return 2.
#  */
 
 def max_freq(arr)
     freq_count = Hash.new(0)
     max_count = 0
     arr.each do |s|
         # swap first two
         n_str = s[1] + s[0] + s[2..-1]
         freq_count[n_str] += 1
         max_count = [max_count, freq_count[n_str]].max

         # swap last two
         n_str = s[0..-3] + s[-1] + s[-2]
         freq_count[n_str] += 1
         max_count = [max_count, freq_count[n_str]].max
     end
     puts "-----max #{freq_count}"
     max_count
 end
 puts max_freq(["abc", "cba", "cab", "bac", "bca"])
#  ["abc", "cba", "cab", "bac", "bca"]
# abc -> bac, acb
# cba -> bca, cab
# cab -> acb, cba
# bac -> abc, bca
# bca -> cba, bac
 # Time complexity O(n) , considering swapting char is constant time O(1)
 