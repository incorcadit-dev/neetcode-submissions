class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        __nums_dic = dict()

        for number in nums:
            if number not in __nums_dic:
                __nums_dic[number] = 0
            __nums_dic[number] +=1

        sorted_keys = sorted(__nums_dic.keys(), key = lambda x: __nums_dic[x], reverse=True)

        return sorted_keys[:k]

        