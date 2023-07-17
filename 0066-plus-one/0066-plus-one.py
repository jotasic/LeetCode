class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l = len(digits) - 1
        is_add_one = False
        
        for i in range(l, -1, -1):
            number = digits[i] + 1
            
            digits[i] = number % 10
            
            if number < 10:
                is_add_one = False
                break
            else:
                is_add_one = True
        else:
            if is_add_one:
                digits.insert(0, 1)
            
        
        return digits
        