# Definition for an interval.
class Interval
    attr_accessor :start, :end
    def initialize(s=0, e=0)
        @start = s
        @end = e
    end
end

# @param {Interval[]} intervals
# @return {Interval[]}
def merge(intervals)
    return [] if intervals.size == 0
    
    intervals.sort_by!{|i| i.start }
    result = []
    s = nil
    e = nil
    
    intervals.each do |i|
        if s.nil? || e.nil?
            s = i.start
            e =  i.end
        elsif (s..e) === i.start
            if (s..e) === i.end
            else
                e = i.end
            end
        else
            result << Interval.new(s, e)
            s = i.start
            e =  i.end
        end
    end
    
    result << Interval.new(s, e)
    
    return result
end
