class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} #Create Hash
        for i, num in enumerate(nums):
            complement = target - num #get the diff
            if complement in num_map:#condition if there
                return [num_map[complement], i] #if there then skip
            num_map[num] = i #if not then store and compare
        return []    #return [] no solution 

        
        