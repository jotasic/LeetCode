ROMAN_NUM = {
    'M' : 1000,
    'D' : 500,
    'C' : 100,
    'L' : 50,
    'X' : 10,
    'V' : 5,
    'I' : 1
}

class Solution:
    def romanToInt(self, s: str) -> int:
        bf_num = 10000
        total_num = 0
        
        for ch in s:
            cur_num = ROMAN_NUM[ch]
            
            if bf_num < cur_num:
                total_num += cur_num - bf_num * 2
            else:
                total_num += cur_num
            
            bf_num = cur_num
        
        return total_num
    
        