# https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter
  def initialize()
      @pings = []
  end


=begin
  :type t: Integer
  :rtype: Integer
=end
  def ping(t)
      @pings << t
      s_time = t - 3000 > 0 ? t - 3000 : 0
      if t - @pings.last > 3000
          return 1
      else
          @pings = @pings.select{|ts| ts >= s_time && ts <= t}
          @pings.size
      end
  end

end

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter.new()
# param_1 = obj.ping(t)