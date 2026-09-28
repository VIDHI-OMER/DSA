class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1={}
        freq2={}
        for i in ransomNote:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1
        for i in magazine:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1
        for i in freq1:
            if i not in freq2 or freq1[i]>freq2[i]:
                return False
        return True

        
        