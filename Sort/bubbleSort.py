# Bubble sort Ave:O(n^2)

import random
from typing import List

def bubbleSort(nums: List[int]) -> List[int]:
    length = len(nums)

    for i in range(length):
        for j in range(length-1-i):
            if nums[j] > nums[j+1]: nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums


if __name__ == "__main__":
    nums = [random.randint(0,10) for _ in range(10)]
    print(nums)
    print(bubbleSort(nums))