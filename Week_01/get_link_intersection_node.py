# coding: utf-8

# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def get_loop_node(self, head):
        p1, p2 = head

        while p2 and p2.next:
            if p1 == p2:
                break

            p1 = p1.next
            p2 = p2.next.next

        if p1 != p2:
            return None

        p1 = head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


    def get_noloop_node(self, headA, headB):
        p1, p2 = headA, headB

        len_a, len_b = 0, 0

        while p1.next:
            p1 = p1.next
            len_a += 1

        while p2.next:
            p2 = p2.next
            len_b += 1

        if p1 != p2:
            return None

        if len_a < len_b:
            p1, p2 = p2, p1

        k = len_b - len_a
        while k > 0:
            p1 = p1.next
            k -= 1

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


    def get_loop_node(self, headA, loopA, headB, loopB):
        if loopA == loopB:
            tmpA, tmpB = loopA.netx, loopB.next
            loopA.next loopB.next = None, None

            i_node = get_noloop_node(loopA, loopb)
            loopA.next loopB.next = tmpA, tmpB

            return i_node
        else:
            end = loopA.next

            while end != loopA:
                if loopA == loopB:
                    return loopA

                loopA = loopA.next

        return None


    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # 1. determine if headA, headB has loop
        loopA = self.get_loop_node(headA)
        loopB = self.get_loop_node(headB)

        # 2. no loop
        if loopA is None and loopB is None:
            return self.get_noloop_node(headA, headB)


        # 3. both loop
        if loopA is not None and loopB is not None:
            return self.get_loop_node(headA, loopA, headB, loopB)

        #4. one loop, anther noloop
        return None
