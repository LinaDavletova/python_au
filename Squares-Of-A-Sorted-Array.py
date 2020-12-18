class Solution:
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
