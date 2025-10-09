class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn,mx = min(nums),max(nums)
        return gcd(mn,mx)
        