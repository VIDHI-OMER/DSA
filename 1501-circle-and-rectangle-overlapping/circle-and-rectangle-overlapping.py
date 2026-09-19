class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        #Checking nearest point of circle to rec or vice-versa
        if xCenter<x1:
            xpoint=x1
        elif(x2<xCenter):
            xpoint=x2
        else:
            xpoint=xCenter 
        if yCenter<y1:
            ypoint=y1
        elif(y2<yCenter):
            ypoint=y2
        else:
            ypoint=yCenter
        dis=((xpoint-xCenter)**2+(ypoint-yCenter)**2)**0.5   #distance
        
        return abs(dis)<=radius

        