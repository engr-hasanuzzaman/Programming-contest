# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet

  =begin
      Initialize your data structure here.
  =end
      def initialize()
          @dict = {}
          @keys = []
      end
  
  
  =begin
      Inserts a value to the set. Returns true if the set did not already contain the specified element.
      :type val: Integer
      :rtype: Boolean
  =end
      def insert(val)
          return false if @dict.key?(val)
          
          @keys << val
          @dict[val] = @keys.size - 1
          true
      end
  
  
  =begin
      Removes a value from the set. Returns true if the set contained the specified element.
      :type val: Integer
      :rtype: Boolean
  =end
      def remove(val)
          return false unless @dict.key?(val)
          index = @dict[val]
          @keys[index] = @keys[-1] 
          @keys.pop
          @dict.delete(val)
          @dict[@keys[index]] = index
          true
      end
  
  
  =begin
      Get a random element from the set.
      :rtype: Integer
  =end
      def get_random()
          @keys[rand(@keys.size)]
      end
  end
