class Solution:
    def findMin(self, nums: List[int]) -> int:
        #최소값을 구하라. 제약조건 log n
        #최소값이 리스트 맨 뒤에 있다면?


        res = nums[0]
        l, r =0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            


        return res