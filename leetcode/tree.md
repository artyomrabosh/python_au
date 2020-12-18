# TREE

+ [Validate Binary Search Tree](#validate-binary-search-tree)
<!---->
## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
def dfs(node, low, high):
    if not node: return True
    if not low < node.val < high: return False
    return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
return dfs(root, -float("inf"), float("inf"))

```

