# ARRAY

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
<!---->
## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
prev, maxim, cur = True, 0, 0
for num in nums:
    if num == 1 and prev:
        cur += 1
        if cur > maxim:
            maxim = cur
    else:
        cur = 0
return maxim

```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
old_r, old_c = len(nums), len(nums[0])
newMatrix = [[]]
temp = []
counter = 0
lvl = 0
if old_r*old_c == r*c:
    for i in range(old_r):
        for j in range(old_c):
            newMatrix[lvl].append(nums[i][j])
            counter += 1
            if counter%c == 0:
                counter = 0
                lvl += 1
                newMatrix.append([])
else:
    return nums
del newMatrix[-1]
return newMatrix

```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
new_M=[]
r,c=len(M),len(M[0])
cur, cur_all = 0, 0
for i in range(r):
    new_M.append([])
    for j in range(c):
        for i_n in range(3):
            for j_n in range(3):
                if((i - 1 + i_n) >= 0 and (i - 1 + i_n) < r and (j - 1 + j_n) >= 0 and (j - 1 + j_n) < c):
                    cur += M[i - 1 + i_n][j - 1 + j_n]
                    cur_all += 1
        new_M[i].append(cur//cur_all)
        cur, cur_all = 0, 0
return (new_M)

```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
r = len(A)
c = r
for i in A:
    i.reverse()
for i in range(r):
    for j in range(c):
        A[i][j] = 1 - A[i][j]
return A

```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
r, c = len(A), len(A[0])
new_A = []
for row in range(c):
    new_A.append([])
    for col in range(r):
        new_A[row].append(A[col][row])
return new_A

```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
for i in range(len(nums))[::-1]:
    if nums[i]==0:
        print(i)
        nums.pop(i)
        nums.append(0)

```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
negative, positive = [], []
for i in A:
    if i < 0:
        negative.append(i*i)
    else:
        positive.append(i*i)
sol = []
while(negative != [] or positive != []):
    if(negative == []):
        sol.append(positive.pop(0))
        continue
    if(positive == []):
        sol.append(negative.pop(-1))
        continue
    if(negative[-1] > positive[0]):
        sol.append(positive.pop(0))
    else:
        sol.append(negative.pop())
return sol

```

