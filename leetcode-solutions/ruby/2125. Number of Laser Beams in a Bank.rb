# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

# @param {String[]} bank
# @return {Integer}
def number_of_beams(bank)
    ledger_on_last_row = 0
    ans = 0
    bank.each do |row|
        cur_count = row.count('1')
        next if cur_count.zero?
        ans += (cur_count * ledger_on_last_row)
        ledger_on_last_row = cur_count
    end
    ans
end
