# TREE

+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
<!---->
## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def traverse(self,node,order):
    if(node is None):
        return
    self.traverse(node.left,order)
    order.append(node.val)
    self.traverse(node.right,order)
def inorderTraversal(self, root: TreeNode) -> List[int]:
    res=[]
    self.traverse(root,res)
    return res

```

