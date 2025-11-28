class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicts = {}
        for i in range(len(nums)):
            if nums[i] in dicts:
               if abs(dicts[nums[i]]- i) <= k:
                    return True
               
            dicts[nums[i]] = i
        return False
        