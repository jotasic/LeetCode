class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # 단순한 방식
        # s = s.strip()
        # words = s.split(' ')
        # return len(words[-1])
        
        
        last_word = ''
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == ' ':
                if last_word:
                    break
            else:
                last_word = s[i] + last_word
            
            i = i-1
    
        return len(last_word)
        