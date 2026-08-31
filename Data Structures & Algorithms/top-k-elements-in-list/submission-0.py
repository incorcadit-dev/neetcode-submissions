class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        _nums_dic: dict = {}

        for integer in nums:
            if integer not in _nums_dic:
                _nums_dic[integer] = 1
            else:
                _nums_dic[integer] += 1

        return sorted(_nums_dic, key=_nums_dic.get, reverse=True)[:k]
        