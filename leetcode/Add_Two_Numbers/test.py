#!/bin/python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp_l1 = l1
        temp_l2 = l2
        l3 = ListNode()
        temp_l3 = l3
        carry_flag = 0
        while temp_l1 or temp_l2 or carry_flag:
            temp_l3.next = ListNode()
            temp_l3 = temp_l3.next
            p1 = 0
            p2 = 0
            if temp_l1:
                p1 = temp_l1.val
                temp_l1 = temp_l1.next
            if temp_l2:
                p2 = temp_l2.val
                temp_l2 = temp_l2.next
                
            temp_l3.val = p1 + p2 + carry_flag
            carry_flag = 0
            if temp_l3.val >= 10:
                temp_l3.val -= 10
                carry_flag = 1

            
        return l3.next
