class Solution(object):
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if abs(x) >= 0x80000000:
            return 0

        st = str(abs(x))
        result = int(st[::-1]) * -1 if x < 0 else int(st[::-1])
        return result if abs(result) <= 0x80000000 else 0


# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# x =       1534236469
# Output =  9646324351


if __name__ == '__main__':
    solution = Solution()

    x = 1534236469
    expected = 0

    result = solution.reverse(x)
    print(f"x         = {x}, \nexpected  = {expected}, \nresult    = {result} \n")

    assert expected == result
    print("All tests passed")
