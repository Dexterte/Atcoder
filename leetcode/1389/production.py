from typing import List


class Solution:
    def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i,j in zip(nums,index):
            result.insert(j,i)
        return result
