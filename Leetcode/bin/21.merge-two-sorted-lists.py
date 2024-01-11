#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = build = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                build.next = list1
                build, list1 = list1, list1.next
            else:
                build.next = list2
                build, list2 = list2, list2.next
        if list1 or list2:
            build.next = list1 if list1 else list2
        return head.next
# @lc code=end

# [1,2,4],[1,3,4]
# [],[]
#  [],[0]