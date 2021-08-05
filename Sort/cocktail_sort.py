import random
from typing import List

def cocktail_sort(nums: List[int]) -> List[int]:
    swap = True
    start = 0
    end = len(nums) - 1
    while swap:
        swap = False
        for i in range(start,end):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swap = True
        
        if not swap: break
        swap = False
        end -= 1

        for i in range(end,start,-1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                swap = True
        
        start += 1
    
    return nums


if __name__ == "__main__":
    nums = [random.randint(0,10) for _ in range(6)]
    print(nums)
    print(cocktail_sort(nums))