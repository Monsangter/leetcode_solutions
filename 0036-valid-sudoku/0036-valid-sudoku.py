class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 먼저 한줄씩 찾는다. 중복되면 바로 invalid 해쉬 이용.
        check = {}

        # 가로 검사.
        for r in board:
            for c in range(9):
                if r[c] in check and r[c] != ".":
                    return False
                check[r[c]] = 0

            check = {}

        # 세로 검사.
        for c in range(9):
            check = {}
            for r in range(9):
                if board[r][c] in check and board[r][c] != ".":
                    return False
                check[board[r][c]] = 0

        
        #하위박스 검사.
        for i in range(3):
            for j in range(3):
                check = {}  # 각 서브 박스마다 새로운 check 딕셔너리를 초기화
                # 3x3 서브 박스 내부의 모든 셀을 순회
                for x in range(3):
                    for y in range(3):
                        value = board[3*i + x][3*j + y]
                        if value != '.' and value in check:
                            return False
                        check[value] = 0



        return True

        # i = 0 ~ 2
        # [3*i] 3*i 3*i+1 3*i+2
        # [3*i+1] 3*i 3*i+1 3*i+2
        # [3*i+2] *i 3*i+1 3*i+2