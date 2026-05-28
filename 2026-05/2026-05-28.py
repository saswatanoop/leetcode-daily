# https://leetcode.com/problems/longest-common-suffix-queries/?envType=daily-question&envId=2026-05-28

from typing import List

class TrieNode:
    __slots__ = ['children', 'index']
    def __init__(self):
        self.children={}
        self.index=-1

class Solution:
    
    def __init__(self):
        self.head=TrieNode()
        self.wordsContainer=[]
    
    # T:O(m) where m is the length of word to insert and S:O(1)
    def insert(self, word, idx):
        word_size=len(word)
        temp=self.head

        if temp.index == -1 or len(self.wordsContainer[temp.index])>word_size:
            temp.index = idx
        
        for i in range(word_size-1,-1,-1):
            c=word[i]
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
            if temp.index == -1 or len(self.wordsContainer[temp.index])>word_size:
                temp.index = idx
    
    # T: O(m) where m is the length of query word and S:O(1)
    def check_suffix(self, word):
        word_size=len(word)
        temp=self.head

        for i in range(word_size-1,-1,-1):
            c=word[i]
            if c not in temp.children:
                return temp.index
            temp=temp.children[c]
        
        return temp.index



    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        self.head=TrieNode()
        self.wordsContainer=wordsContainer

        # T:O(n*m) where n is number of words in container and m is average length of words in container and S:O(n*m) for trie
        for i in range(len(wordsContainer)):
            self.insert(wordsContainer[i],i)
        
        n=len(wordsQuery)
        res=[0]*n
        for i in range(n):
            res[i]=self.check_suffix(wordsQuery[i])
        return res