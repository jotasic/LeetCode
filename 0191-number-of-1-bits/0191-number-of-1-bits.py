class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count_of_one = 0
        
        
        while n >= 2:
            n, remain = divmod(n, 2)
            count_of_one += remain
        
        return count_of_one + n
            