class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_l = len(set(nums))
        nums_l = len(nums)

        return(True if set_l != nums_l else False )