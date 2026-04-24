class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_c = set()
            set_r = set()
            for j in range(9):

                if board[i][j] in set_c:
                    return False

                if board[i][j] != '.':
                    set_c.add(board[i][j])

                if board[j][i] in set_r:
                    return False

                if board[j][i] != '.':
                    set_r.add(board[j][i])

        for i in range(0,9, +3):
            for j in range (0,9, +3):
                set_t = set()
                for c in range (3):
                    for r in range(3):
                        if board[i+c][j+r] in set_t:
                            return False
                        if board[i+c][j+r] != '.':
                            set_t.add(board[i+c][j+r])

        return True              


