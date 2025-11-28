class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def slidingwindow(nums,k):
            left = 0
            ans  = 0
            window = Counter()
            for right in range(len(nums)):
                
                
                window[nums[right]] += 1
                
                while len(window) > k:
                    window[nums[left]] -=1
                    if window[nums[left]] == 0:
                        window.pop(nums[left])
                    left +=1
                
                ans += right-left +1
            return ans
        return slidingwindow(nums,k) - slidingwindow(nums,k-1)
                
       