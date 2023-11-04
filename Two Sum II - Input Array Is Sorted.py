class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 #at position 0
        right = len(numbers) - 1 #last index of the array since begins at 0
#we are looking for the diff by subtracting it from target and see if diff can be found in the array
        #GOING THROUGH IT NORMALLY
        while left < right: #as long as left pointer index < right pointer index you still on right part
            total = numbers[right] + numbers[left] #add leftmost pointer and rightmost pointer to get total
            if total == target:
                return [left +1, right +1] #return the values gotten
            elif total > target:
                right -= 1 #right pointer moves back a step
            elif total < target:
                left += 1#left pointer moves forward a step
            else:
                pass #do not do anything after

# #MEMORY USED HERE IS EXECPTIONAL
