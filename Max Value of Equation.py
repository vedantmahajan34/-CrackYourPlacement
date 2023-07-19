import sys
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        sum = -sys.maxsize - 1
        for i in range(1,len(points)):
            l=i-1
            if(abs(points[i][0]-points[l][0])<=k):
                print(points[i][0]-points[l][0])
                print((i,l))
                z=points[i][1]+points[l][1]+abs(points[l][0]-points[i][0])
                print(z)
                sum=max(sum,z)
        return sum

        