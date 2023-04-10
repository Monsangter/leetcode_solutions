class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #그냥 리스트에서 최저 최고 뽑는건 안된다.
        #시간을 따르고 있기 때문에.. 사기전에 팔 수 없기 떄문에..
        #min num 을 만들고 그 다음 수랑 더해 리스트에 추가한다.
        # 생각해봐.. 중요한건 최대 프로핏임. 민값갱신과, 프로핏 저장.

        min_num = 100000
        max_profit = 0

        for i in prices:
            if i <= min_num:
                min_num = i
            
            if i-min_num > max_profit:
                max_profit = i - min_num

    
        return max_profit