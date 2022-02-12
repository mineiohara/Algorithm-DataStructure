from typing import List, Tuple, Optional

def getPair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()

    for num in nums:
        val = target - num
        if val in cache: return val, num
        cache.add(num)

def getPairHalfSum(nums: List[int]) -> Optional[Tuple[int]]:
    sumNUm = sum(nums)

    halfSum, remainder = divmod(sumNUm, 2)
    if remainder != 0: return

    cache = set()
    for num in nums:
        val = halfSum - num
        if val in cache: return val, num
        cache.add(num)


if __name__ == "__main__":
    l = [2,6,9,10,5,2]
    target = 12
    print(getPair(l, target))
    print(getPairHalfSum(l))

