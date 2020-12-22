# Array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num = 0
    n = 0
    for i in nums:
        if i == 1:
            n += 1
        else:
            if n > num:
                num = n
            n = 0
    if n > num:
            num = n
            n = 0
    return num
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    new = []
    newstr = [j for i in nums for j in i]
    if len(newstr) != r * c:
        return nums
    for i in range(r):
        new.append(newstr[i*c:(i+1)*c])
    return new
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    def average(M, x, y):
        s = 0
        kol = 0
        lenx = len(M)
        leny = len(M[0])
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < lenx and j >= 0 and j < leny:
                    kol += 1
                    s += M[i][j]
        return int(s/kol)

    return [[average(M, x, y) for y in range(len(M[0]))] for x in range(len(M))]
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    def reverse(A, x, y):
        if A[x][len(A[x]) - y - 1]:
            return 0
        return 1

    return [[reverse(A, x, y) for y in range(len(A[0]))] for x in range(len(A))]
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    def reverse(A, x, y):
        return A[x][y]

    return [[reverse(A, x, y) for x in range(len(A))] for y in range(len(A[0]))]
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    n0 = 0
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
        if abs(nums[i]) < abs(nums[n0]):
            n0 = i
    sortnums = []
    left = n0
    right = n0 + 1
    while left >= 0 or right != len(nums):
        if left < 0:
            sortnums.append(nums[right])
            right += 1
        elif right == len(nums):
            sortnums.append(nums[left])
            left -= 1
        elif nums[left] < nums[right]:
            sortnums.append(nums[left])
            left -= 1
        else:
            sortnums.append(nums[right])
            right += 1
    return sortnums
```

