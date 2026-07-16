from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        maxArr=0
        preGCD=[0]*n
        for i in range(n):
            maxArr=max(maxArr,nums[i])
            preGCD[i]=gcd(nums[i],maxArr)
        #print(preGCD)
        preGCD.sort()
        #print(preGCD)
        i=0
        j=n-1
        s=0
        while(i<j):
            s+=gcd(preGCD[i],preGCD[j])
            i+=1
            j-=1
        #print(s)
        return s