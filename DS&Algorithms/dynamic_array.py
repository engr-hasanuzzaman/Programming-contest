import unittest

class DArray:
    def __init__(self, size) -> None:
        self.array = [None] * size
        self.length = 0
        self.capacity = size
    
    def add(self, x):
        # re-size the array and copay the existing element
        if self.length + 1 >= self.capacity:
            self.capacity *= 2
            newArr = [None] * self.capacity
            for i in range(self.length):
                newArr[i] = self.array[i]
            self.array = newArr
        self.array[self.length] = x
        self.length += 1


class Testing(unittest.TestCase):
    def test_new_array_len(self):
        arr = DArray(4)
        self.assertEqual(arr.length, 0)
        arr.add(1)
        self.assertEqual(arr.length, 1)

if __name__ == '__main__':
    unittest.main()