from unittest import result

from src.leetcode.listnode import ListNode


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2
        head = ListNode(None) # dummy element, we return back from the next
        tail = head

        while p1 or p2:
            if p1 is None:
                tail.next = p2
                return head.next
            if p2 is None:
                tail.next = p1
                return head.next

            if p1.val <= p2.val:
                tail.next = ListNode(p1.val)
                p1 = p1.next
                tail = tail.next
            else:
                tail.next = ListNode(p2.val)
                p2 = p2.next
                tail = tail.next
        return head.next


    def mergeTwoLists_net(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(None)
        tail = dummy

        # iterate while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # one of them may still have nodes; append directly
        tail.next = list1 if list1 else list2

        return dummy.next



if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    print('----- list 1')
    l1.self_print()

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print('\n----- list 2')
    l2.self_print()

    print('\n----- merge')
    res = Solution().mergeTwoLists_net(l1, l2)
    res.self_print()
