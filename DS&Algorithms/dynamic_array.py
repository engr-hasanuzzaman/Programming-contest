import unittest

class DArray:
    def __init__(self, size) -> None:
        self.__array = [None] * size
        self.length = 0
        self.capacity = size
    
    def add(self, x):
        # re-size the array and copay the existing element
        if self.length + 1 >= self.capacity:
            self.capacity *= 2
            newArr = [None] * self.capacity
            for i in range(self.length):
                newArr[i] = self.__array[i]
            self.__array = newArr
        self.__array[self.length] = x
        self.length += 1

    def remove(self, element):
        i, j, size = 0, 0, self.length
        while i < size:
            # if expected elemen, skip copying to new array
            if self.__array[i] == element:
                i += 1
                self.length -= 1
            else:
                self.__array[j] = self.__array[i]
                i += 1
                j += 1
        return element

    def elements(self):
        return self.__array[:self.length]

class Testing(unittest.TestCase):
    def test_new_array_len(self):
        arr = DArray(4)
        self.assertEqual(arr.length, 0)
        arr.add(1)
        self.assertEqual(arr.length, 1)

    def test_remove(self):
        arr = DArray(4)
        arr.add(1)
        arr.add(2)
        arr.add(1)
        self.assertEqual(arr.length, 3)
        self.assertEqual(arr.elements(), [1,2,1])
        self.assertEqual(arr.remove(1), 1)
        self.assertEqual(arr.length, 1)
        self.assertEqual(arr.elements(), [2])

if __name__ == '__main__':
    unittest.main()