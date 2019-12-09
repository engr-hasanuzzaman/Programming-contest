# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue

  =begin
      Initialize your data structure here.
  =end
      def initialize()
          @p_stack = []
          @pop_stack = []
      end
  
  
  =begin
      Push element x to the back of queue.
      :type x: Integer
      :rtype: Void
  =end
      def push(x)
          @p_stack << x
      end
  
  
  =begin
      Removes the element from in front of queue and returns that element.
      :rtype: Integer
  =end
      def pop()
          if @pop_stack.empty?
              while !@p_stack.empty?
                  @pop_stack << @p_stack.pop
              end
          end
          
          @pop_stack.pop
      end
  
  
  =begin
      Get the front element.
      :rtype: Integer
  =end
      def peek()
          if @pop_stack.empty?
              while !@p_stack.empty?
                  @pop_stack << @p_stack.pop
              end
          end
          
          @pop_stack.last
      end
  
  
  =begin
      Returns whether the queue is empty.
      :rtype: Boolean
  =end
      def empty()
          @pop_stack.empty? && @p_stack.empty?
      end
  
  
  end
  
  # Your MyQueue object will be instantiated and called as such:
  # obj = MyQueue.new()
  # obj.push(x)
  # param_2 = obj.pop()
  # param_3 = obj.peek()
  # param_4 = obj.empty()