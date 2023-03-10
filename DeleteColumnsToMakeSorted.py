## 944. Delete Columns to Make Sorted
## https://leetcode.com/problems/delete-columns-to-make-sorted/
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        myList = []
        st = '';mystr = '';add_str=''
        for i in range(len(strs[0])):
            for j in range(len(strs)):
               st+=strs[j][i]
            myList.append(st)
            st=''
        count = 0
        for i in myList:
            mystr = ''
            mystr = i
            mystr = sorted(mystr)
            for s in mystr:
                add_str+=s
            if add_str!=i:
                count+=1
            add_str=''
        return count
            