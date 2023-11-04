class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea= 0 #answer we need
        left = 0 #create left pointer
        right = len(height)-1 #create right pointer

        while(left < right): #until left pointer passes the right one
            currArea = min(height[left],height[right]) * (right-left) #height value * distance value
            maxArea = max(maxArea, currArea) #highest max Area value
            if (height[left] < height[right]): #when left side < right side values
                left += 1 #move left side
            else: 
                right -= 1#move right side back
        return maxArea  #answer we want 
