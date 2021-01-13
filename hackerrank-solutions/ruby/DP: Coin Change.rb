def ways(n, coins)
    combination = Array.new(n+1){0}
    combination[0] = 1
    coins.sort!
    coins.each do |coin|
        1.upto(n) do |amount|
            if amount >= coin
                combination[amount] += combination[amount - coin]
            end
        end
    end
    combination.last
end
