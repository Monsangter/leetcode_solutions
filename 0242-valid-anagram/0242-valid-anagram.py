class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 각 문자의 개수가 일치하는가?
        # s의 각 문자 개수를 해쉬맵으로
        # t의 각 문자 개수를 해쉬맵으로
        # 걍 쏘트해서 비교하면 되는거 아님?
        
        ls_s = list(s) 
        ls_t = list(t)
        ls_s.sort()
        ls_t.sort()
        return True if ls_s == ls_t else False 