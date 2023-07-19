# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i, value in enumerate(nums): #1
#             remaining = target - nums[i] #2
            
#             if remaining in seen: #3
#                 return [i, seen[remaining]]  #4
#             else:
#                 seen[value] = i  #5
        
import time

start = time.time()

# print(23*2.3)


s=2
n=3
m=4
ans=pow(s,n,10)
print(pow(ans,m,1000000007))
end = time.time()
print(end - start)
