#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:49:35 2020

@author: tomasferrer

  Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

"""

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         # longest limited to length of min(text1, text2)
#         # try to find the shortes in the longest
        
        
        
          
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not(text1) or not(text2): return 0
        dp = {(0,0) : int(text1[0] == text2[0])}
        for i in range(1,len(text1)):
            dp[(i,0)] = 1 if dp[(i-1,0)] else int(text1[i] == text2[0])
        for j in range(1,len(text2)):
            dp[(0,j)] = 1 if dp[(0,j-1)] else int(text1[0] == text2[j])
        for i in range(1,len(text1)):
            for j in range(1,len(text2)):
                dp[(i,j)] = dp[(i-1,j-1)]+1 if text1[i] == text2[j] else max(dp[(i-1,j)],dp[(i,j-1)])
        return dp[(len(text1)-1,len(text2)-1)]
        
        
        
text1= ''
text2= 'ababbdbb'
print(Solution().longestCommonSubsequence(text1, text2))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        