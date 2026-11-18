class Solution:
    def minChanges(self, s: str) -> int:
        partition=0
        i=0
        while(i<len(s)):
            if s[i]!=s[i+1]:
                partition+=1
            i+=2
        return partition
