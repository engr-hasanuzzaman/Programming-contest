import math



# sparse table st[i][j]  will store the answer for the range  of length [i, i + 2^j-1]
# we can divide [i, i + 2^j-1] into tow -> [i, i + 2^(j-1)-1] & [i + 2^(j-1), i + 2^j-1]
# where 2 ^(j-1) is the length
# ex. j = 3 -> 2 ^ j -> 8 can be divided into two size of 
# j-1 => 4 elements
class Solution:
    def __init__(self, arr) -> None:
        self.elements = arr
        self.row_size = len(arr)  # row size
        # col size, each column will hold next level of binary length
        self.k = int(math.log2(self.row_size)) + 1
        self.min_range_query = [[None] * self.k for _ in range(self.row_size)]
        # print("-------- initial min range ", self.min_range_query)
        self.prepare()
        # self.K = 25 # math.log2()

    """
    N = max_array_size
    for (int i = 0; i < N; i++)
      st[i][0] = f(array[i]);

    for (int j = 1; j <= K; j++)
        for (int i = 0; i + (1 << j) <= N; i++)
            st[i][j] = f(st[i][j-1], st[i + (1 << (j - 1))][j - 1]);
    """
    # Reference: https://www.geeksforgeeks.org/sparse-table/?ref=gcse
    # min_range_query[i][j] will containt min value start from i and length (2^j)
    def prepare(self):
        # initialized singele interval (row wise)
        for i in range(len(self.elements)):
            self.min_range_query[i][0] = self.elements[i]

        j = 1
        # 2^j is the interval which is <= max array length
        while (1 << j) <= self.row_size: # or (j <= k where k = math.floor(math.log2(size))) + 1
            # ex. 2^j = 2, range (0,1), (1,2), (2,3) ....
            # ex. 2^j = 4, range (0,3), (1,4), (2,5) ....
            i = 0
            # for 0-based index, < self.row_size
            while (i + (2 ** j) - 1) < self.row_size:
                # j is range, length of that level
                # print(f"i {i}, j-1 = {j-1} i + (1 << (j - 1)) {i + (1 << (j - 1))}")
                self.min_range_query[i][j] = min(
                    self.min_range_query[i][j-1],
                    self.min_range_query[i + (1 << (j - 1))][j-1]
                )
                i += 1
            j += 1
        # print("--------- after perparing ", self.min_range_query)

    def query(self, L, R):
        # j is largets powere of 2 which is less than or = to n
        # size is R - L + 1
        j = int(math.log2(R - L + 1))
        # print("---- the value of j is ", j)
        # Compute minimum of last 2^j elements
        # with first 2^j elements in range.
        # For [2, 10], we compare arr[lookup[0][3]]
        # and arr[lookup[3][3]],
        # return min(self.min_range_query[L][j], self.min_range_query[R - (1 << j) + 1][j])
        return min(self.min_range_query[L][j], self.min_range_query[R - (2 ** j) + 1][j])


arr = [1, 2, 3, 4, 4, 5, 5, 60, -2, 35, 6, 7, 0, 1]
s = Solution(arr)
print("----MRQ between 0, 6 is ", s.query(0, 6))
print("----MRQ between 0, 8 is ", s.query(1, 8))
