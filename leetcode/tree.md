# TREE

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
<!---->
## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
q=[root]
res=[]
while(q != []):
    for node in q:
        res.append(node.val)
    for node in q[:]:
        if(node.left is not None):
            q.append(node.left)
        if(node.right is not None):
            q.append(node.right)
        q.remove(node)
res.sort()
print(res)
return res[k-1]

```

