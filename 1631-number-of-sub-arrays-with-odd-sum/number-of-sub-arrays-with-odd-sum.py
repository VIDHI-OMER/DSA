class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD=(10**9)+7
        even=1  #sum=0, 0 is even
        odd=0
        ans=0
        pre=0
        for i in arr:
            pre+=i
            if pre%2==0:
                ans+=odd     #diff is odd
                even+=1
            else:
                ans+=even
                odd+=1
        return ans%MOD

        