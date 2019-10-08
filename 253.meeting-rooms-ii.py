#
# @lc app=leetcode id=253 lang=python
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (43.69%)
# Total Accepted:    191.2K
# Total Submissions: 437.1K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        
        sorted_intvls = sorted(intervals, key = lambda x: x[0])

        h = []
        heapq.heappush(h, sorted_intvls[0][1])
        max_room_num = 1
        for inv in sorted_intvls[1:]:
            if inv[0] >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, inv[1])
            max_room_num = max(max_room_num, len(h))
        return max_room_num
