# MATH

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)
<!---->
## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
new_x = 0
if x < 0:
    x = -1 * x
    while x > 0:
        new_x *= 10
        new_x += x % 10
        x = x // 10
    if new_x < 2147483648:
        return -new_x
    else:
        return 0
while x > 0:
    new_x *= 10
    new_x += x % 10
    x = x // 10
if new_x < 2147483648:
        return new_x
else:
        return 0

```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
x = str(x)
num = -1
isPalindrome = 1
print(x[0])
for i in range(len(x)):
    if x[i] != x[-i-1]:
        isPalindrome = 0
    print(x[i])
if (isPalindrome == 1):
    return True
else:
    return False

```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
Solution = []
for i in range(n):
    mod3 = (i + 1) % 3
    mod5 = (i + 1) % 5
    if(mod3 == 0 and mod5 == 0):
        print("1")
        Solution.append("FizzBuzz")
    elif(mod5 == 0):
        Solution.append("Buzz")
    elif(mod3 == 0):
        Solution.append("Fizz")
    else:
        Solution.append("{}".format(i+1))
return Solution

```

## Base 7

https://leetcode.com/problems/base-7/

```python
if num == 0:
    return "0"
solution = ""
if(num < 0):
    num = num*- 1
    while(num > 0):
        solution = solution + "{}".format(num % 7)
        num = num // 7
    solution += "-"
    return solution[::-1]
while (num > 0):
    solution = solution + "{}".format(num % 7)
    num = num // 7
return solution[::-1]

```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
   return self.f(N)

def f(self, N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return (self.f(N - 1) + self.f(N - 2))

```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
A.sort(reverse = True)
i = 0
while i < len(A) - 2:
    if A[i] < A[i + 1] + A[i + 2]:
        return A[i] + A[i + 1] + A[i + 2]
    else:
        i += 1
return 0

```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
num = 1
while(num * num <= x):
    num += 1
return num - 1

```
