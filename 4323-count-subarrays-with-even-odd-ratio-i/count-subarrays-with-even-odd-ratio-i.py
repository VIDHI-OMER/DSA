class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            even=0
            odd=0
            for j in range(i,n):
                if nums[j]%2==0:
                    even+=1
                else:
                    odd+=1
                if odd>0:
                    if even/odd<=a/b :
                        c+=1
        return c

