class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)[2:]
        print(b)
        return b.count('1')
