# Math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0
    y = 0
    if x > 0:
        k = 1
    else:
        k = -1
        x *= -1
    while x > 0:
        y = 10 * y + x % 10
        x //= 10
        if y > 2 ** 31 - 1 or y < -2 ** 31:
            return 0
    return y * k
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    y = 0
    x1 = x
    while x1 > 0:
        y = 10 * y + x1 % 10
        x1 //= 10
    return y == x
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    ret = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            ret.append("FizzBuzz")
        elif i % 5 == 0:
            ret.append("Buzz")
        elif i % 3 == 0:
            ret.append("Fizz")
        else:
            ret.append(str(i))
    return ret
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num):
    """
    :type num: int
    :rtype: str
    """
    num7 = 0
    d = 1
    k = 0
    if num < 0:
        k = -1
        num *= -1
    else:
        k = 1
    while num > 0:
        num7 = num7 + num % 7 * d
        num //= 7
        d *= 10
    return str((num7) * k)
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N):
    """
    :type N: int
    :rtype: int
    """
    if N == 1 or N == 0:
        return N
    prev = 0
    cur = 1
    for i in range(N - 1):
        f = prev + cur
        prev = cur
        cur = f
    return cur
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    B = sorted(A, reverse=True)
    n = len(B)
    i = 0
    while i != n - 2 and B[i] >= B[i + 1] + B[i + 2]:
        i += 1
    if i == n - 2:
        return 0
    return B[i] + B[i + 1] + B[i + 2]
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    sqrtx = int(x ** (0.5))
    return sqrtx
```

