# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/add-two-numbers/solutions/1486136/python-listnode-explained-no-spoilers-be-h8ys/

class Solution(object):
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        return None


def add_lists(l1, l2):
    result = []
    i = 0
    carry = 0

    while i < len(l1) or i < len(l2) or carry:
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[i] if i < len(l2) else 0
        total = val1 + val2 + carry
        carry = total // 10
        result.append(total % 10)
        i += 1

    return result


if __name__ == '__main__':
    # print("[7,0,8] = ", add_lists([2, 4, 3], [5, 6, 4]))
    # print("[8,9,9,9,0,0,0,1] = ", add_lists([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    # print(Solution.addTwoNumbers(l1, l2))

    print(Solution.addTwoNumbers([243],[564]))


