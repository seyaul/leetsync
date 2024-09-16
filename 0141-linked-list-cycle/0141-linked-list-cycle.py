# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        references = defaultdict(int)
        while head:
            references[head.next] += 1
            head = head.next
            if references[head] > 1:
                for key in references:
                    print(key.val, references[key])
                return True
        return False
        