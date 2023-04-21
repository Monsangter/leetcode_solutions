from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #인덱스가 중복되지 않게 세개를 뽑는다.  0이되는 것을 반환.

        #모든 조합을 구하고
        #구한 조합중 겹치는게 있다면 0으로 만들면 어떨까?


        res = []
        nums.sort()
        
        for i,a in enumerate(nums):
            if i > 0 and a ==nums[i-1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = a +nums[l] + nums[r]
                if threeSum >0:
                    r -= 1
                elif threeSum <0:
                    l+= 1
                else:
                    res.append([a,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                        
    
        return res
                        
                