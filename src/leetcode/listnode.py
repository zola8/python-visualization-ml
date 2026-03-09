class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def self_print(self):
        pointer = self
        while pointer:
            print(pointer.val)
            pointer = pointer.next



def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next

    return head


def example1():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.self_print()


if __name__ == '__main__':
    # example1()

    ln = build_linked_list([1,2,3])
    ln.self_print()
