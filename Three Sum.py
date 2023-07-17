class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen=set()
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1

            while left<right:
                check=nums[i]+nums[left]+nums[right]
                if check==0:
                    seen.add((nums[i],nums[left],nums[right]))
                    left=left+1
                    right=right-1
                elif check<0:
                    left=left+1
                else:
                    right=right-1
        return seen



