#this is for OSSP 6th week assignment

"""
Contents
- Return the indices of two integers from the given array "nums" that add up
to the specified integer "target"
- Assume that only one possible solution exists, and each array element can only be used once.
(cannot be used twice or more times.)
- You can return the answer in any order    
"""

from typing import List
def twoSum(self,nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    for i in range(0, len(nums)):
        #i랑 중복 방지
        for j in range(i+1, len(nums)):
            #조건문
	        if nums[i] + nums[j] == target:
	            return [i, j]