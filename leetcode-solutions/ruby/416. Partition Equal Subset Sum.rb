def can_partition(nums)
    sum = nums.sum
    # odd sum handling   
    return false if sum % 2 == 1
    
    half = sum/2
    
    dp = [false] * (half + 1)
    dp[0] = true # 0 if madable using any conbination
    nums.each do |n|
      temp = [false] * (half + 1)
      temp[0] = true
      1.upto(half) do |j|
        if dp[j]
          temp[j] = true
        elsif j < n
          temp[j] = dp[j]
        else
          temp[j] = dp[j-n]
        end
      end
      dp = temp
    end
    
    return dp.last
  end
  
  