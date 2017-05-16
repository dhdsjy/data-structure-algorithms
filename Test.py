# -*- coding: utf-8 -*-
"""
@author: Lee
@file: Test.py
@time: 2017/4/22 21:08
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    # in python next is a reversed word
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

head = ListNode(1)
b = ListNode(2)
c = ListNode(3);
head.next = b;
b.next=c
def traverse(head):
    p = head
    while p:
        print p.val
        p = p.next
traverse(head)
res = b.reverse(head)
traverse(res)