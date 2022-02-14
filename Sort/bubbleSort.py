#Bubble sort

import random
from typing import List

def bogo_sort(nums: List[int]) -> List[int]:
    for i in range(1,len(nums)):
        for j in range(len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums


if __name__ == "__main__":
    nums = [random.randint(0,10) for _ in range(5)]
    print(nums)
    print(bogo_sort(nums))