# @param {Integer[]} time_series
# @param {Integer} duration
# @return {Integer}
def find_poisoned_duration(time_series, duration)
    result = 0
    
    time_series.size.times do |i|
        if time_series[i.next].nil? || (time_series[i.next] - time_series[i] >= duration)
            result += duration
        elsif 
            result += (time_series[i.next] - time_series[i])
        end
    end
    
    return result         
end
