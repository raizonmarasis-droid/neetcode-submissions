class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            s_count[index] += 1
        
        for char in t:
             index = ord(char) - ord('a')
             t_count[index] += 1
        
        if s_count == t_count:
            return True
        else:
            return False
    