class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #일단 어제 했던대로 -면 제거해버린다는 생각. 아니지. -여도, 뒤에 - 더큰게 나오면.
        #두번쨰는 max cur 비교해서 날려버려버리는 생각. 0만아니면 무조건 길어지는게 유리.
        #카운트가 -인 리스트의 개수를 세고,그 개수가 1이된다면, 그 1의 뒤는 무시하는게 가능.
    

        result = nums[0]
        min_prod = max_prod = 1
        
        for n in nums:

            max_prod, min_prod = (
                max(max_prod * n , min_prod * n, n),
                min(max_prod * n , min_prod * n, n)
            )
            result = max(result,max_prod)

        return result