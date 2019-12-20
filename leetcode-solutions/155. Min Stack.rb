# https://leetcode.com/problems/min-stack/

class MinStack

  =begin
      initialize your data structure here.
  =end
      def initialize()
          @stack = []
      end
  
  
  =begin
      :type x: Integer
      :rtype: Void
  =end
      def push(x)
         @stack << x
          if !@min
              @min = x
          elsif @min > x
              @min = x
          end
      end
  
  
  =begin
      :rtype: Void
  =end
      def pop()
        @stack.pop  
      end
  
  
  =begin
      :rtype: Integer
  =end
      def top()
          @stack[-1]
      end
  
  
  =begin
      :rtype: Integer
  =end
      def get_min()
          @stack.min
      end
  
  
  end
  
  # Your MinStack object will be instantiated and called as such:
  # obj = MinStack.new()
  # obj.push(x)
  # obj.pop()
  # param_3 = obj.top()
  # param_4 = obj.get_min()

#  more faster solution
class MinStack

    =begin
        initialize your data structure here.
    =end
        def initialize()
            @top = -1
            @min_val = nil
            @s = []
        end
    
    
    =begin
        :type x: Integer
        :rtype: Void
    =end
        def push(x)
            if @top == -1
                @min_val = x
            else
                @min_val = [@min_val, x].min
            end
            
            @top += 1
            
            @s[@top] = x
        end
    
    
    =begin
        :rtype: Void
    =end
        def pop()
            return if @top == -1
            
            # update min val
            if @s[@top] == @min_val
                @min_val = @s[0]
                0.upto(@top-1) do |i|
                    if @min_val > @s[i]
                        @min_val = @s[i]
                    end
                end
            end
            
            @top -= 1
        end
    
    
    =begin
        :rtype: Integer
    =end
        def top()
            return nil if @top == -1
            
            @s[@top]
        end
    
    
    =begin
        :rtype: Integer
    =end
        def get_min()
            return nil if @top == -1
            
            @min_val
        end
    
    
    end
    
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack.new()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.get_min()