class Solution:
    def minimumDeletions(self, s: str) -> int:
        bs=0
        rem=0

        for i in s:
            if i=='b':
                bs+=1
            else:
                rem=min(rem+1,bs)
        return rem
        