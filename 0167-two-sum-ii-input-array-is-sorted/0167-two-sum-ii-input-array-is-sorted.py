class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}

        for i, v in enumerate(numbers):
            diff = target - v
            if diff in d: return [d[diff]+1, i+1]
            d[v] = i