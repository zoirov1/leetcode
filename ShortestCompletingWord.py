# 748. Shortest Completing Word
#https://leetcode.com/problems/shortest-completing-word/
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        myList = []
        strs = ''
        for k in licensePlate:
            if k.isalpha():
                strs+=k
        strs = strs.lower()
        count = 0
        for i in words:
            for j in strs:
                if j in i and i.count(j)>=strs.count(j):
                    count+=1
            if count==len(strs):
                myList.append(i)
            count=0
        myList = sorted(myList,key = lambda x: len(x))
        return myList[0]           
