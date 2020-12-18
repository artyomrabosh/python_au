# TREE

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
<!---->
## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
if root is None: return None
q=[root]
res=[]
while(q != []):
    i=0
    new_res=[]
    for node in q:
        new_res.append(node.val)
    res.append(new_res)
    temp=[]
    for node in q:
        if(node.left is not None):
            temp.append(node.left)
            i+=1
        if(node.right is not None):
            temp.append(node.right)
            i+=1
        q=temp
return res

```

