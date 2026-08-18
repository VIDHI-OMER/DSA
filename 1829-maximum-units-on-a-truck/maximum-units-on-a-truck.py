class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n=len(boxTypes)
        ans=0
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        for i in range(n):
            qua=boxTypes[i][0]
            unit=boxTypes[i][1]
            conc=min(qua,truckSize)
            ans+=conc*unit
            truckSize-=conc
            if (truckSize==0):
                break
        return ans