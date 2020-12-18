# TREE

+ [Invert Binary Tree](#invert-binary-tree)
<!---->
## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(self, root: TreeNode) -> TreeNode:
    if root is None: return None
    self.invert(root)
    return root
def invert(self,node):
    if node.left is not None:
        self.invert(node.left)
    if node.right is not None:
        self.invert(node.right)
    node.left,node.right=node.right,node.left

```

