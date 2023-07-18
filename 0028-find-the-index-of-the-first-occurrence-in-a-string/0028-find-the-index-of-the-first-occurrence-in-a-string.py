class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #idx = haystack.find(needle)
        #return idx
        
        hl, nl = len(haystack), len(needle)
        
        for i in range(0, hl-nl+1):
            if needle == haystack[i:i+nl]:
                return i
        else:
            return -1