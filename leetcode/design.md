# OUT

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Design Twitter](#design-twitter)
<!---->
## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self):
    self.stack=[]
    print('created')
def push(self, num):
    if self.stack == []:
        self.stack.append([num,num])
    else:
        if num < self.stack[-1][1]:
            self.stack.append([num,num])
        else:
            self.stack.append([num, self.stack[-1][1]])
def pop(self):
    return self.stack.pop()
def getMin(self):
    return self.stack[-1][1]
def top(self):
    return self.stack[-1][0]
```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
def __init__(self):
    self.q=[]
    print('created')
def push(self, x):
    self.q.insert(0,x)
def pop(self):
    return self.q.pop()
def peek(self):
    return self.q[-1]
def empty(self):
    if self.q == []:
        return True
    return False
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
def __init__(self):
    self.stack=[]
    print('created')
def push(self, x):
    self.stack.append(x)
def pop(self):
    return self.stack.pop()
def top(self):
    return self.stack[-1]
def empty(self):
    if self.stack == []:
        return True
    else: return False

```

## Design Twitter

https://leetcode.com/problems/design-twitter/

```python
def __init__(self):
    self.timer = itertools.count(step=-1)
    self.tweets = collections.defaultdict(collections.deque)
    self.followees = collections.defaultdict(set)
def postTweet(self, userId, tweetId):
    self.tweets[userId].appendleft((next(self.timer), tweetId))
def getNewsFeed(self, userId):
    tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
    return [t for _, t in itertools.islice(tweets, 10)]
def follow(self, followerId, followeeId):
    self.followees[followerId].add(followeeId)
def unfollow(self, followerId, followeeId):
    self.followees[followerId].discard(followeeId)

```

