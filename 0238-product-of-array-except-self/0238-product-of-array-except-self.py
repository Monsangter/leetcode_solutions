class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ls1 = []

        cnt = 0
        ans = 1

        for i in nums:
            if i == 0 and cnt == 0:
                cnt += 1
                ans *= 1

            elif i == 0 and cnt > 1:
                ans = 0
                cnt += 1
                break

            else:
                ans *= i
        

                    
        for i in nums:
            
            if i == 0 and cnt == 1:
                ls1.append(ans)
            elif cnt > 0:
                ls1.append(0)
            elif i == 0:
                ls1.append(0)
            else:
                ls1.append(ans / i)
            
        return ls1
                    
        
        # 모든 수를 곱한 값을 구해놓고, 해당 인덱스에서 뺴서 반환하면 되지 않을까?
        # 원본 리스트를 해하지 않으면서, 해당 값만 제외한 곱값을 구할 수 있는 방법?