class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_pointer = 0
        r_pointer = len(numbers) - 1

        while r_pointer > l_pointer:
            if numbers[l_pointer] + numbers[r_pointer] > target:
                r_pointer -= 1
            elif numbers[l_pointer] + numbers[r_pointer] < target:
                l_pointer += 1
            elif numbers[l_pointer] + numbers[r_pointer] == target:
                break
        return [l_pointer + 1,r_pointer + 1]
        