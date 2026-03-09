def check_board_size_constraints(board):
    if len(board) != 9:
        return False
    for i in range(9):
        if len(board[i]) != 9:
            return False
    for i in range(9):
        for j in range(9):
            if board[i][j] not in '.123456789':
                return False
    return True


def valid_rows(board):
    for row in board:
        nums = [x for x in row if x != '.']
        if len(nums) != len(set(nums)):
            return False
    return True


def valid_columns(board):
    for row in range(9):
        nums = [board[col][row] for col in range(9)]
        # print('-- ', nums)
        numbers = [x for x in nums if x != '.']
        if len(numbers) != len(set(numbers)):
            return False
    return True


def valid3x3(board):
    for i in range(3):
        for j in range(3):
            small_board = [row[i * 3:i * 3 + 3] for row in board[j * 3:j * 3 + 3]]
            flat = [col for row in small_board for col in row]
            numbers = [x for x in flat if x != '.']
            if len(numbers) != len(set(numbers)):
                return False

    return True


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not check_board_size_constraints(board):
            return False
        if not valid_rows(board):
            return False
        if not valid_columns(board):
            return False
        if not valid3x3(board):
            return False

        return True


# https://leetcode.com/problems/valid-sudoku/description/

if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    assert Solution().isValidSudoku(board) == True
    print("\n---\n")

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    assert Solution().isValidSudoku(board) == False

    print("All tests passed")
