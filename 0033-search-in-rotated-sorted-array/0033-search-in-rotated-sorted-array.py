class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #리스트에서 target을 찾고 target의 원래 nums에서의인덱스를 반환한다.
        #만약에 target이 없다면 -1반환. 

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m -1

            else:
                if target < nums[m]:
                    r = m -1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

