# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack

  =begin
      Initialize your data structure here.
  =end
      def initialize()
          @q = []
      end
  
  
  =begin
      Push element x onto stack.
      :type x: Integer
      :rtype: Void
  =end
      def push(x)
          @top = x
          s = @q.size
          @q << x
          s.times { @q << @q.shift }
      end
  
  
  =begin
      Removes the element on top of the stack and returns that element.
      :rtype: Integer
  =end
      def pop()
          @q.shift
      end
  
  
  =begin
      Get the top element.
      :rtype: Integer
  =end
      def top()
          @q[0]
      end
  
  
  =begin
      Returns whether the stack is empty.
      :rtype: Boolean
  =end
      def empty()
          @q.empty?
      end
  
  
  end
  
  # Your MyStack object will be instantiated and called as such:
  # obj = MyStack.new()
  # obj.push(x)
  # param_2 = obj.pop()
  # param_3 = obj.top()
  # param_4 = obj.empty()