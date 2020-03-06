# https://leetcode.com/problems/design-hashset/

class MyHashSet

  =begin
      Initialize your data structure here.
  =end
      def initialize()
          @data = []
      end
  
  
  =begin
      :type key: Integer
      :rtype: Void
  =end
      def add(key)
          @data[key] = true
      end
  
      def exist?(n)
          !!@data[n]
      end
  
  =begin
      :type key: Integer
      :rtype: Void
  =end
      def remove(key)
          @data[key] = false
      end
  
  
  =begin
      Returns true if this set contains the specified element
      :type key: Integer
      :rtype: Boolean
  =end
      def contains(key)
          exist?(key)
      end
  
  
  end
  
  # Your MyHashSet object will be instantiated and called as such:
  # obj = MyHashSet.new()
  # obj.add(key)
  # obj.remove(key)
  # param_3 = obj.contains(key)