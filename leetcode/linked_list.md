# LINKED_LIST

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Reorder List](#reorder-list)
<!---->
## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
prev, new = head, None
while prev:
   new = ListNode(prev.val, new)
   prev = prev.next
return new

```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
if(head.next is None):
    return head
next=head.next
double_next=head.next.next
while double_next is not None and double_next.next is not None:
    double_next=double_next.next.next
    next=next.next
return (next)

```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
if(head is None or head.next is None):
    return True
next = head.next
double_next = head.next.next
while double_next is not None and double_next.next is not None:
    double_next = double_next.next.next
    next = next.next
q = None
while next:
   q = ListNode(next.val, q)
   next = next.next
print(q)
print(head)
if(q.next == None):
    if(q.val == head.val):
        return True
    else:
        return False
while(q != None):
    if(head.val != q.val):
        return(False)
    head = head.next
    q = q.next
return(True)

```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
reversed=None
while(l1 is not None or l2 is not None):
    if(l1 is None):
        reversed=ListNode(l2.val,reversed)
        l2=l2.next
    elif(l2 is None):
        reversed=ListNode(l1.val,reversed)
        l1=l1.next
    else:
        if(l1.val>=l2.val):
            reversed=ListNode(l2.val,reversed)
            l2=l2.next
        else:
            reversed=ListNode(l1.val,reversed)
            l1=l1.next
Merged=None
while (reversed):
   Merged = ListNode(reversed.val, Merged)
   reversed = reversed.next
return (Merged)

```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
if (head.next is None and n==1):
    return None
counter=1
len=0
len_head=head
while len_head:
    len+=1
    len_head=len_head.next
n=len-n
if(n==0):
    return head.next
first=head
second=head.next
while (counter<n):
    first=first.next
    second=second.next
    counter+=1
first.next=second.next
return head

```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
if head is None: return None
node = head
arr = []
while node:
    arr.append(node)
    node = node.next
counter = head
temp = [i.val for i in arr]
i = 0
first, last = 0, len(arr) - 1
while first != last:
    if(i % 2 == 0):
        print(first)
        arr[i].val = temp[first]
        first += 1
    else:
        print(last)
        arr[i].val = temp[last]
        last -= 1
    i += 1
arr[i].val = temp[first]

```

