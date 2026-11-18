class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxConsecutiveOnes = 0
        i = 0
        while i < len(nums) :

            consecutiveOnes = 0
            for j in range(i,len(nums)):

                if nums[j] == 0 : 
                    break
                consecutiveOnes += 1
                i+=1
            
            i+= 1
            if consecutiveOnes > maxConsecutiveOnes:
                maxConsecutiveOnes = consecutiveOnes
        
        return maxConsecutiveOnes
        