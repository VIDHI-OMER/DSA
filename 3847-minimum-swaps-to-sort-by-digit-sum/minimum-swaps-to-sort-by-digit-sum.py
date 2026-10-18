class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        new=sorted(nums,key=lambda x:(sum(int(d) for d in str(x)),x))
        #print(new)
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
        