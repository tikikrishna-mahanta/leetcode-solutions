class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Ek dictionary banayein numbers aur unke index ko store karne ke liye
        num_map = {}
        
        for i, num in enumerate(nums):
            # Target se current number ko minus karke required number dhundhein
            complement = target - num
            
            # Agar required number pehle se dictionary mein hai, to result mil gaya
            if complement in num_map:
                return [num_map[complement], i]
            
            # Agar nahi hai, to current number aur uska index dictionary mein save karein
            num_map[num] = i
            
        return []
