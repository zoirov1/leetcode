# 2506. Count Pairs Of Similar Strings
# https://leetcode.com/problems/count-pairs-of-similar-strings/
class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0;i_count = 0;j_count = 0
        just_count = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                for k in words[i]:
                    if k in words[j]:
                        i_count+=1
                for m in words[j]:
                    if m in words[i]:
                        j_count+=1
                if len(words[j])==j_count and len(words[i])==i_count:
                    just_count+=1
                if just_count==1:
                    count+=1
                just_count=0
                i_count=0;j_count=0
        return count
