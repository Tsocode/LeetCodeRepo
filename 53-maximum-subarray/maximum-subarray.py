class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
            
        #Proper Solution:
        # 2 3 4 5 6 7 8 10
        # discard when curSum is -ve, change to zero and continue with the loop



        # 2 3 4 5 6 7 8 10
        # p p p 
        #O(n^3) X

        # 2 3 4 5 6 7 8 10
        # do curSum + next num (num[j])


        