#reverse a linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        if head.next == None:
            head.next=None
            return head
        else:
            tail = self.reverseList(head.next)
            
            last=tail
            while last.next!=None:
                last=last.next
                
            last.next=head
            head.next=None

            return tail

n5=ListNode(5,None)
n4=ListNode(4,n5)
n3=ListNode(3,n4)
n2=ListNode(2,n3)
n1=ListNode(1,n2)

print("before reverse")

n=n1
while n!=None:
    print(n.val)
    n=n.next

sol=Solution()
n1=sol.reverseList(n1)

print("after reverse")

n=n1
while n!=None:
    print(n.val)
    n=n.next
