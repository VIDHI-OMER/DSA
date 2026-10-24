class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days={1:'31',2:'28',3:'31',4:'30',5:'31',6:'30',7:'31',8:'31',9:'30',10:'31',11:'30',12:'31'}
        arriveA=arriveAlice.split('-')
        leaveA=leaveAlice.split('-')
        arriveB=arriveBob.split('-')
        leaveB=leaveBob.split('-')
        TD1=0
        ED1=0
        for i in range(1,int(arriveA[0])):
            TD1+=int(days[i])
        TD1+=int(arriveA[1])
        for i in range(1,int(leaveA[0])):
            ED1+=int(days[i])
        ED1+=int(leaveA[1])
        #print(TD1,ED1)
        TD2=0
        ED2=0
        for i in range(1,int(arriveB[0])):
            TD2+=int(days[i])
        TD2+=int(arriveB[1])
        for i in range(1,int(leaveB[0])):
            ED2+=int(days[i])
        ED2+=int(leaveB[1])
        print(TD1,ED1)
        print(TD2,ED2)
        start=max(TD1,TD2)
        end=min(ED1,ED2)
        if start>end:
            return 0
        return end-start+1