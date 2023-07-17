class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # 단순한 방식
        # s = s.strip()
        # words = s.split(' ')
        # return len(words[-1])
        
        
        last_word = ''
        string_size = len(s)
        for i in range(string_size-1, -1, -1):
            if s[i] == ' ':
                if last_word:
                    break
            else:
                last_word = s[i] + last_word
    
        return len(last_word)
        