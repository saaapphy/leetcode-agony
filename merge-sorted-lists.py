# LeetCode #21 - Merge Two Sorted Lists :: June 2, 2024

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def MergeTwoLists(list1, list2):
  dummy = ListNode()
  current = dummy

  # create pointers for list traverse
  p1, p2 = list1, list2

  # traverse until lists exhausted
  while p1 and p2:
    if p1.val < p2.val:
      current.next = p1
      p1 = p1.next
    else:
      current.next = p2
      p2 = p2.next
    
    current = current.next

  # if list contents exhausted, attach remaining elements
  current.next = p1 if p1 else p2

  # merged list will start from the next node of the dummy
  return dummy.next




    
