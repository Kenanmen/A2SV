class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = Counter(nums)
        return len(nums) > len(num)
        