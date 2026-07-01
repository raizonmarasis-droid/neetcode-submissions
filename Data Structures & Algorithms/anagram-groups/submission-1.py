class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def charCounter (s: str) -> List[int]:
            ana_count = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                ana_count[index] += 1
            return tuple(ana_count)

        grouped = {}
        for word in strs:
            char_count = charCounter(word)
            if char_count not in grouped:
                grouped[char_count] = []
            grouped[char_count].append(word)
        return list(grouped.values())
            

           
           
           




        