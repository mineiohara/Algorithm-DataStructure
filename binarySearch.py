# Binary search

from optparse import Option
import random
from typing import List, Optional, NewType

IndexNum = NewType("IndexNum", int)

def linearSearch(nums: List[int], value: int) -> Optional[IndexNum]:
    for i in range(len(nums)):
        if nums[i] == value: return i

    return None


def binarySearch(nums: List[int], value: int) -> Optional[IndexNum]:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) //2
        if nums[mid] == value: return mid
        elif nums[mid] < value: left = mid + 1
        else: right = mid - 1
    
    return None


def binarySearchRecursive(nums: List[int], value: int) -> Optional[IndexNum]:
    def _binarySearchRecursive_(nums: List[int], value: int, left: int, right: int) -> Optional[IndexNum]:
        if left > right: return None

        mid = (left + right) // 2

        if nums[mid] == value: return mid
        elif nums[mid] < value: return _binarySearchRecursive_(nums, value, mid + 1, right)
        else: return _binarySearchRecursive_(nums, value, left, mid - 1)
    
    return _binarySearchRecursive_(nums, value, 0, len(nums) - 1)




if __name__ == "__main__":
    nums = [random.randint(0, 30) for i in range(10)]
    nums.sort()
    value = random.randint(0, 30)
    print("Value " + str(value))
    print(nums)
    print(binarySearchRecursive(nums, value))