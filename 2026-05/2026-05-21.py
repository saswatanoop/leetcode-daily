# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2026-05-21

from typing import List

class Node:
    def __init__(self):
        self.children={}

class Solution:
    def __init__(self):
        self.head=Node()

    def _insert(self,val):
        temp=self.head
        for c in val:
            if c not in temp.children:
                temp.children[c]=Node()
            temp=temp.children[c]

    def _longest_prefix(self,val):
        pref=0
        temp=self.head

        for c in val:
            if c not in temp.children:
                break
            pref+=1
            temp=temp.children[c]
        return pref

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ans=0
        for val in arr1:
            self._insert(str(val))
        for val in arr2:
            pref=self._longest_prefix(str(val))
            ans=max(ans,pref)
        return ans
        