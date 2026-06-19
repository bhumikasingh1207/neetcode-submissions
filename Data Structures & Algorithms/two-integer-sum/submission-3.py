class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} #value : idx
        for i , n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n] = i
        return 