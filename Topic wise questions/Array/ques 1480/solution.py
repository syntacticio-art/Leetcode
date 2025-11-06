class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = 0
        result = []
        
        for x in nums:
            running += x          # keep adding the current number
            result.append(running)  # store the running total
        
        return result