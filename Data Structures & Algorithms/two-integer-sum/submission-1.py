class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addends_list = []
        for i in range (len(nums)):
            for j in range(0, len(nums)):    
                addends = target - nums[i]
                if addends == nums[j] and j != i:
                    addends_list.append(i)
                    addends_list.append(j)
                    return addends_list
                
        