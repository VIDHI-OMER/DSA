class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        s=s.split()
        for i in s:
            if i.isdigit():
                l.append(int(i))
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i]>=l[j]:
                    return False
        return True
        