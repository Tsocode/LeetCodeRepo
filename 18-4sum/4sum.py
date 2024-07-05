from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to make it easier to handle duplicates
        res = []  # To store the result
        
        def kSum(k, start, target):
            if k == 2:  # Base case: two-sum problem
                l, r = start, len(nums) - 1
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum == target:
                        res.append(temp + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:  # Skip duplicates
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:  # Skip duplicates
                            r -= 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                        continue
                    temp.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    temp.pop()  # Backtrack

        temp = []  # To store the current combination
        kSum(4, 0, target)  # Start with k = 4
        return res

# Test case 1
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
solution = Solution()
print(solution.fourSum(nums1, target1))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

# Test case 2
nums2 = [2, 2, 2, 2, 2]
target2 = 8
print(solution.fourSum(nums2, target2))  # Output: [[2, 2, 2, 2]]
