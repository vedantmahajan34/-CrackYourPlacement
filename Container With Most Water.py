class Solution:
    def maxArea(self, height: List[int]) -> int:  
        area=0
        l=0
        r=len(height)-1

        while l<r:
            h=min(height[l],height[r])
            d=abs(l-r)
            area=max(area,d*h)
            if(height[l]>height[r]):
                r=r-1
            else:
                l=l+1
        return area