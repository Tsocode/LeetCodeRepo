class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        # Stack to keep track of elements whose next greater element hasn't been found yet
        stack = []
        
        # Traverse nums2 to find the next greater elements
        for num in nums2:
            # While stack is not empty and current number is greater than the stack's top element
            while stack and num > stack[-1]:
                # Pop the top of the stack and assign the current number as the next greater element
                top = stack.pop()
                next_greater[top] = num
            # Push the current number onto the stack
            stack.append(num)
        
        # For remaining elements in the stack, there is no next greater element, so set -1
        while stack:
            top = stack.pop()
            next_greater[top] = -1
        
        # Build the result for nums1 using the next_greater dictionary
        result = [next_greater[num] for num in nums1]
        
        return result
