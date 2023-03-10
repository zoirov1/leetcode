#https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_sum = 0
        common = []
        for i in range(len(list1)):
            if list1[i] in list2:
                index_sum=i+list2.index(list1[i])
                common.append([list1[i],index_sum])

        answer = []
        min = common[0][1]
        for i in common:
            if i[1]<min:
                min = i[1]
        for j in common:
            if j[1]==min:
                answer.append(j[0])

        return answer

