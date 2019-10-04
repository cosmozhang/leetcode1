#
# @lc app=leetcode id=273 lang=python
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (25.01%)
# Total Accepted:    120.8K
# Total Submissions: 483.2K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 2^31 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_stack, t_stack =[], []

        s_num = str(num)

        if len(s_num) > 9:

            num_stack.append(s_num[:-9])
            t_stack.append('Billion')

        if len(s_num) > 6:
            num_stack.append(s_num[-9:-6])
            t_stack.append('Million')

        if len(s_num) > 3:
            num_stack.append(s_num[-6:-3])
            t_stack.append('Thousand')

        num_stack.append(s_num[-3:])
        t_stack.append('')

        ret = ''
        while len(num_stack) > 0:

            chunk, t = num_stack.pop(0), t_stack.pop(0)
            s = self.convert(chunk)

            if s == 'Zero' and t != '':
                continue
            else:
                if s != '':
                    ret += s + ' ' + t + ' '


        return ret.strip()

    def convert(self, chunk):

        sd = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'}
        td = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}

        d = {'2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
        
        ret = ''

        if len(chunk) == 3:
            if chunk[0] != '0':
                ret += sd[chunk[0]] +' Hundred '
        if len(chunk) > 1:
            if chunk[-2] == '1':
                ret += td[chunk[-2:]]
            elif chunk[-2] != '0':
                if chunk[-1] != '0':
                    ret += d[chunk[-2]] + ' ' + sd[chunk[-1]]
                else:
                    ret += d[chunk[-2]]
            else:
                if chunk[-1] != '0':
                    ret += sd[chunk[-1]]
        elif len(chunk) == 1:
            ret += sd[chunk[0]]

        return ret.strip()
                

                
