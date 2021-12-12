from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 先頭時点を確保するpreheadとポインターとなるprevを共に初期化する。
        prehead = prev = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                # prevのNextへ数の小さいほうのノードを追加し、チェーン状態を作成していく
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        # どちらかのノードが無くなったら、残ったほうのノードを入れる。
        prev.next = list1 if list1 is not None else list2
    
        # 先頭のNextを指定することで、作成したノードリストが全て表示される
        return prehead.next