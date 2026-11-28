class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k=k%n

        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

        reverse(0,n-1)    #reverse whole nums
        reverse(0,k-1)    #reverse first k elements
        reverse(k,n-1)    #reverse remaining elemrnts



        