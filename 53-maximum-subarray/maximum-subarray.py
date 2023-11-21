class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] #initialize maxSub to first element
        curSum = 0 #initialize curSum to 0
        for n in nums: #iterate over nums array
            if curSum < 0: #check if curSum is -ve
                curSum = 0 #make it zero
            curSum += n #we add the next element in the array
            maxSub = max(maxSub, curSum) #max of it to get maxSub
        return maxSub #maxSub
            
        #Proper Solution:
        # 2 3 4 5 6 7 8 10
        # discard when curSum is -ve, change to zero and continue with the loop



        # 2 3 4 5 6 7 8 10
        # p p p 
        #O(n^3) X

        # 2 3 4 5 6 7 8 10
        # do curSum + next num (num[j])


        