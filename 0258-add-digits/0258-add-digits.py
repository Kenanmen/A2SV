class Solution:
    def addDigits(self, num: int) -> int:
    
        while num > 9:
            String = str(num)
            total_sum = 0
            for c in String:
                total_sum += int(c)
            num = total_sum
        return num

