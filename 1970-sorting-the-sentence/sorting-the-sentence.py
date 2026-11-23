class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        d=['']*len(s)
        for i in s:
            pos=int(i[-1])-1
            d[pos]=i[:-1]
        return ' '.join(d)


        