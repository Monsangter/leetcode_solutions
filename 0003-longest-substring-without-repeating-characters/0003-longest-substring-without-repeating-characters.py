class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #해쉬로 검색해서 넣고 찾기 하면 됨.이미 있다면 거기서 끝.
        # ex 1 같은경우 시작 인덱스를 바꿔가며
        # 처음부터 세줘야 결과가 나온다.
        # 내가 순회했던 문자열을 어떻게 메모라이징 할 것인가.
        #리스트로 넣으면 메모라이징 한다음 뺴서 비교할때 문제 생김.
        # 해쉬로 넣자잉.
        dict1 = {}
        result = 0
        cnt = 0
        if len(s) == 1 :
            return 1

        for i in range(len(s)):
            for j in range(i,len(s)):
                
                if s[j] in dict1:
                    result = max(cnt, result)
                    cnt = 0
                    dict1 = {}
                    break
                cnt += 1
                dict1[s[j]] = 0

               

        return result






