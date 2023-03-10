# 2418. Sort the People
# https://leetcode.com/problems/sort-the-people/
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        dtc = {}
        for i in range(len(names)):
            dtc[heights[i]]=names[i]
        dct = list(sorted(dtc.items(),key=lambda x:x[0],reverse=True))
        myList = []
        for i in dct:
            myList.append(i[1])
        return myList



        