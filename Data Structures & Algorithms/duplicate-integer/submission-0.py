class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap={}
        for n in nums:
            if n in prevMap:
                return True
            prevMap[n]=True
        return False    