class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        pref=[0]*len(self.nums)
        pref[0]=self.nums[0]
        
    
        for i in range(1,len(self.nums)):
            pref[i]=self.nums[i]+pref[i-1]
        
        if(left==0):
            return pref[right]
        return pref[right]-pref[left-1]
    
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)