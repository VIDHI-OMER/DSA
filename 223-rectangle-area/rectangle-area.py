class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        w1=ax2-ax1
        h1=ay2-ay1
        a1=w1*h1
        w2=bx2-bx1
        h2= by2-by1
        a2=w2*h2
        
        w3=max(0, min(ax2, bx2) - max(ax1, bx1))
        h3=max(0, min(ay2, by2) - max(ay1, by1))
        a3=w3*h3
        totalArea=(a1+a2)-a3
        return totalArea