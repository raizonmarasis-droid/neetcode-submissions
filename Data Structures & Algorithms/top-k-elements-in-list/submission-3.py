class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        nums_list = []

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
            sorted_list = sorted(frequencies.items(), key = lambda x:x[1], reverse = True)
        
        for i in range(k):
            nums_list.append(sorted_list[i][0])
        
        return nums_list




        
        


        



        