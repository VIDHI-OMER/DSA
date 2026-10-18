class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        def dig_sum(val):
            s=0
            while(val):
                rem=val%10
                s+=rem
                val=val//10
            return s
        new=sorted(nums,key=lambda val:(dig_sum(val),val))
        mp={}
        swap=0
        for i in range(n):
            mp[nums[i]]=i
        for i in range(n):
            curr=nums[i]
            expected=new[i]
            expected_val=mp[expected]
            if curr==expected:
                continue
            nums[i]=expected
            nums[expected_val]=curr
            mp[expected]=i
            mp[curr]=expected_val
            swap+=1
        return swap
        