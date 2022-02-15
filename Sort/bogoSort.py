# Bogo sort Ave:O((n+1)!)

import random
from typing import List

def inOrder(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]: return False
    
    return True

def bogoSort(nums: List[int]) -> List[int]:
    while not inOrder(nums):
        random.shuffle(nums)
    return nums


if __name__ == "__main__":
    nums = [random.randint(0, 10) for _ in range(10)]
    print(nums)
    print(bogoSort(nums))