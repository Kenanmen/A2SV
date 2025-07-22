class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            value = target - nums[i]
            if value in nums and nums.index(value) != i:
                ans.append(nums.index(value))
                ans.append(i)
                break
        return ans

        
        