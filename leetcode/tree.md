# TREE

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
<!---->
## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python

    root=[]
    index=-1
    def __init__(self, root: TreeNode):
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
        res.append(None)
        self.root=res
        print(self.root)
        
    def next(self) -> int:
        if self.root[self.index+1] is None: return None
        self.index+=1
        return self.root[self.index]

    def hasNext(self) -> bool:
        if(self.root[self.index+1] is not None): return True
        else: return False

```

