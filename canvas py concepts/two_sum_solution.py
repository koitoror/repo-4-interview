# from typing import List

class Solution:

    @staticmethod
    
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    # def twoSum(self, nums, target):
    def twoSum(nums, target):
    # def twoSum(nums: List[int], target: int) -> List[int]:
    

        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
                # return [nums[dic[num]], nums[i]]
            else:
                diff = target - num
                dic[diff] = i 

nums = [2,7,11,15]
target = 9
# target = 17

sList = Solution.twoSum
print(sList(nums, target))
