class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt_nums = {}
        ls = []

        for i in range(len(nums)):
            cnt_nums[nums[i]] = 1+ cnt_nums.get(nums[i], 0)

        sorted_cnt_nums = sorted(cnt_nums.items(), key = lambda item: item[1], reverse = True)

        
        
        for i in range(k):
           ls.append(sorted_cnt_nums[i][0])

        return ls