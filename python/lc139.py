"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

from collections import deque
from functools import cache


class Solution:
    def wordBreak1(self, s: str, wordDict: list[str]) -> bool:
        # use queue
        words = set(wordDict)
        queue = deque([0])
        seen = set()
        
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue
                
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
                
        return False
        
    def wordBreak2(self, s, wordDict):
        # dp
        # dp(i)=any(s[i - word.length + 1, i]==word && dp(i - word.length))
        @cache
        def dp(i):
            if i < 0: 
                return True

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            
            return False
        
        return dp(len(s) - 1)


s = "ccaccc"
wordDict = ["cc","ac"]
print(Solution.wordBreak1(Solution, s, wordDict))