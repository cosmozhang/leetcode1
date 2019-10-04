#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (56.81%)
# Total Accepted:    314.6K
# Total Submissions: 553.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        fw = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            fw[i] = fw[i-1] * nums[i]
        
        bw = [nums[-1]] * len(nums)
        for j in range(len(nums)-2, -1, -1):
            bw[j] = bw[j+1] * nums[j]

        ret = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                ret[i] = bw[i+1]
            elif i == len(nums)-1:
                ret[i] = fw[i-1]
            else:
                ret[i] = bw[i+1] * fw[i-1]

        return ret
        """

        ret = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            ret[i] = ret[i-1] * nums[i]

        r = 1

        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                ret[i] = r
            else:
                ret[i] = ret[i-1] * r
                r *= nums[i]
        return ret
            
        
