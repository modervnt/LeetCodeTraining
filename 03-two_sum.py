**********************************************************************
*                    LEETCODE DUPLICATES CHALLENGE                   *
*                    Two Sum Problem                                 *
**********************************************************************
=== FAILED ATTEMPTS ===
1.Fist Attemps (Here's the problem: You never reset j to be i+1!)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        my_dict = {}
        while i < len(nums):
            my_dict[i] = nums[i]
            while j < len(nums):
                if nums[i] + nums[j] == target :
                    return [i, j]
                j +=1
            i+=1
[3,2,4] 6 Output :null

=== SUCCESSFUL SOLUTIONS ===

2- Second Attempt (Solution but very bad)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        the_dict = {}
        while i < len(nums) :
            the_dict[i] = nums[i]
            i += 1
        j = 1
        while j < len(nums):
            for key in the_dict:
                if the_dict[key] + nums[j] == target and key != j:
                    return [key, j]
            j += 1

The most optimal Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums): #i = index, num = value
            complement = target - num
            if complement in my_dict:
                return [my_dict[complement], i]
            my_dict[complement] = i

=== KEY LEARNINGS ===
1. enumerate is a convenient way to get both the index i and the value(num) while looping througth 
2. list.index()	You only need the first occurrence

