# TREE

+ [Symmetric Tree](#symmetric-tree)
<!---->
## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
def isSymmetric(self, root: TreeNode) -> bool:
    return self.is_mirror(root, root)
def is_mirror(self, r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is not None and r2 is not None:
        if r1.val == r2.val:
            return (self.is_mirror(r1.left, r2.right) and self.is_mirror(r1.right, r2.left))

```

