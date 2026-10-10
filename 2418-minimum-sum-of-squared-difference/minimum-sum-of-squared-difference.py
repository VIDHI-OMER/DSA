class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff=[0]*((10**5)+1)
        for i in range(len(nums1)):
            n=abs(nums1[i]-nums2[i]) 
            diff[n]+=1
        K=k1+k2
        s=len(diff)-1
        while(K>0 and s>0):
            if diff[s]==0:
                s-=1
                continue
            op=min(diff[s],K)
            diff[s]-=op
            diff[s-1]+=op
            K-=op
        res=0
        for i in range(len(diff)):
            if diff[i]!=0:
                res+=(i*i*diff[i])
        return res




        


        