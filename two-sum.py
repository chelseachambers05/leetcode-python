# brute force
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            
# efficient solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        myHashMap = {}
        for index, num in enumerate(nums):
            value = target - num
            if value in myHashMap:
                return [myHashMap[value], index]
            myHashMap[num] = index
    