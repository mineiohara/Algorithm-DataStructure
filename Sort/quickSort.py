# Quick sort Ave:O(n log n)

import random
from typing import List

def partition(nums: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = nums[high]
    for j in range(low, high):
        if pivot >= nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[high], nums[i+1] = nums[i+1], nums[high]

    return i+1

def quickSort(nums: List[int]) -> List[int]:
    def _quickSort_(nums: List[int], low: int, high: int) -> None:
        if low < high:
            partitionIndex = partition(nums, low, high)
            _quickSort_(nums, low, partitionIndex-1)
            _quickSort_(nums, partitionIndex+1, high)
    
    _quickSort_(nums, 0, len(nums)-1)
    return nums



if __name__ == "__main__":
    nums = [random.randint(0,10) for _ in range(10)]
    print(nums)
    print(quickSort(nums))