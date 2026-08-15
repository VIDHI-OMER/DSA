class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        i=0
        j=n-1
        c=0
        while(i<=j):
            if people[i]+people[j]<=limit:
                c+=1
                i+=1
                j-=1
            else:
                c+=1
                j-=1
        return c