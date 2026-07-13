from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q=deque()
        for i in range(1,9):
            q.append(i)
        res=[]
        while q:
            n=q.popleft()
            if n>=low and n<=high:
                res.append(n)
            lst=n%10
            if(lst+1<=9):
                q.append((n*10)+(lst+1))
        return res
                