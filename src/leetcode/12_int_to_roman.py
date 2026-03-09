class Solution(object):

    conversion_table: dict = {
        4: {
            'curr_symbol': 'M',
        },
        3: {
            'curr_symbol': 'C',
            'five_symbol': 'D',
            'next_digit_symbol': 'M',
        },
        2: {
            'curr_symbol': 'X',
            'five_symbol': 'L',
            'next_digit_symbol': 'C',
        },
        1: {
            'curr_symbol': 'I',
            'five_symbol': 'V',
            'next_digit_symbol': 'X',
        },
    }

    def intToRoman(self, num: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        if (num < 1) or (num > 3999):
            return ''

        s = str(num)
        i1000 = int(s[-4]) if len(s) >= 4 else 0
        i100 = int(s[-3]) if len(s) >= 3 else 0
        i10 = int(s[-2]) if len(s) >= 2 else 0
        i1 = int(s[-1])
        s1000 = self.convert_to_roman(4, i1000)
        s100 = self.convert_to_roman(3, i100)
        s10 = self.convert_to_roman(2, i10)
        s1 = self.convert_to_roman(1, i1)
        return s1000 + s100 + s10 + s1


    def convert_to_roman(self, i: int, curr_digit: int) -> str:
        idict = self.conversion_table.get(i)
        if (curr_digit == 4):
            return f"{idict.get('curr_symbol')}{idict.get('five_symbol')}"
        if (curr_digit == 9):
            return f"{idict.get('curr_symbol')}{idict.get('next_digit_symbol')}"
        if curr_digit >= 5:
            return f"{idict.get('five_symbol')}{idict.get('curr_symbol') * (curr_digit % 5)}"
        return idict.get('curr_symbol') * curr_digit


if __name__ == '__main__':
    solution = Solution()

    num = 3749
    expected = "MMMDCCXLIX"

    # result = solution.intToRoman(num)
    # print(f"num       = {num}, \nexpected  = {expected}, \nresult    = {result} \n")

    # assert expected == result
    # print("All tests passed")

    print(solution.intToRoman(3549))
