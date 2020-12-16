# INTERVALS

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
<!---->
## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
intervals = sorted(intervals, key=lambda x: x[1])
lenght = len(intervals)
sol = []
while len(intervals) > 0:
    min = intervals[0]
    sol.append(min)
    removal = []
    for i in range(len(intervals)):
        if(intervals[i][0] < min[1]):
            removal.append(intervals[i])
        else:
            break
    for i in removal:
        intervals.remove(i)
return (lenght-len(sol))

```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
intervals.sort()
if (len(intervals)>1):
    i = 0
    j = 1
    solution = []
    while j < len(intervals):
        if (intervals[j][0] > intervals[i][1]):
            solution.append(intervals[i])
            i = j
        else:
            if intervals[i][1] > intervals[j][1]:
                intervals[i][1] = intervals[i][1]
            else:
                intervals[i][1] = intervals[j][1]
        j += 1
    print(intervals[i][1])
    solution.append(intervals[i])
    j += 1
    return(solution)
return(intervals)
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
intervals.sort()
if(len(intervals)==0):
    return([newInterval])
if(len(intervals)==1):
    intervals.append(newInterval)
    intervals.sort()
    if intervals[0][1]>=intervals[1][0]:
        if intervals[0][1]>=intervals[1][1]:
            return([[intervals[0][0],intervals[0][1]]])
        else:
            return([[intervals[0][0],intervals[1][1]]])
    else:
        return(intervals)
begin = -100
end = -10
isSearching=0
solution=[]
for item in intervals:
    if newInterval[0] <= item[1] and begin == -100:
        if newInterval[0]<=item[0]:
            begin = newInterval[0]
            isSearching=1
        else:
            begin = item[0]
            isSearching=1
    print (item)
    if isSearching==1:
        if newInterval[1] < item[0]:
            end=newInterval[1]
            solution.append([begin,end])
            solution.append(item)
            isSearching=0
            begin=-111
            continue
        elif newInterval[1]<=item[1]:
            end=item[1]
            solution.append([begin,end])
            isSearching=0
            begin=-111
            continue
        continue
    solution.append(item)
if(begin == -100):
    solution.append(newInterval)
if(isSearching==1):
    solution.append([begin,newInterval[1]])
return(solution)

```

