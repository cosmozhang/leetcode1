# -*- coding: utf-8 -*-
# @lc app=leetcode id=301 lang=python
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (40.47%)
# Total Accepted:    148.5K
# Total Submissions: 367.1K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Example 1:
# 
# 
# Input: "()())()"
# Output: ["()()()", "(())()"]
# 
# 
# Example 2:
# 
# 
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# 
# 
# Example 3:
# 
# 
# Input: ")("
# Output: [""]
# 
#
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        if len(s)==0:
            return [s]
        
        q, visited, is_found, ret = [s], set([s, '']), False, set()

        new_q = []
        while len(q) > 0:
            cur_s = q.pop(0)
            if self.is_valid(cur_s):
                ret.add(cur_s)
                is_found = True
            else:
                if is_found:
                    continue
                else:
                    for i in range(len(cur_s)):
                        if cur_s[i] in ['(', ')']:
                            new_s = cur_s[:i]+cur_s[i+1:]
                            if new_s not in visited:
                                visited.add(new_s)
                                new_q.append(new_s)

            if len(q)==0 and not is_found:
                q, new_q = new_q, []
        
        return [""] if len(ret)==0 else list(ret)
            
    def is_valid(self, s):
        lc = 0
        for c in s:
            if c == '(':
                lc += 1
            elif c == ')':
                lc -= 1
                if lc < 0:
                    return False
            
        if lc > 0:
            return False
        elif lc == 0:
            return True
                            
                                
        
if __name__ == "__main__":
    s = Solution()
    s.removeInvalidParentheses("()())()())")
