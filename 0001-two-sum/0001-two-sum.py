from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # ~을 뽑아서  타겟값을 만든다. 아웃풋으로 그 재료의 인다이스값 반환.
        # 다만 조건에서 두개만 뽑으면 됨을 말하고 있다.
        # 브루트포스? 일단 타겟보다 크거나 같은 수는 조사할 필요가 없지.
        # 라기엔 음양수가 있다. 한번 뽑은 거 또 뽑기는 안됨.
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        