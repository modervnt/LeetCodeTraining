**********************************************************************
*                    LEETCODE DUPLICATES CHALLENGE                   *
*                    Contains Duplicate Problem                      *
**********************************************************************

=== TEST CASE 1 ===
[274,-735,-911,80,454,-511,922,-775,985,-669,-463,-896,-629,-586,
910,-361,288,-375,88,556,-578,-406,-87,25,377,-635,-445,-289,646,
-962,-487,-924,-968,-962,502,36,129,-611,54,-27,-496,915,-84,-782,
349,678,332,-114,345,14,119,710,821,-194,988,38,-369,409,-559,-529,
-298,-593,705]

=== TEST CASE 2 ===
[-92,-333,255,994,36,242,49,-591,419,-432,-73,41,93,654,-20,40,929,
-492,432,72,796,795,930,901,-468,890,146,829,932,-585,721,-83,-719,
-146,-750,-196,-94,-352,-851,375,-507,-122,-850,-564,372,-379,606,
-749,838,592,-683]

=== FAILED ATTEMPTS ===

1. First Attempt (Problem: Modifying list during iteration):
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            nums.remove(x)  # Dangerous: Modifying list while iterating
            if x in nums:
                return True
        return False

2. Second Attempt (Problem: Nested loop makes it O(n²)):
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            nums.remove(x)
            for n in nums:  # Inefficient nested loop
                if x == n:
                    return True
        return False

3. Third Attempt (Problem: Wrong assumption about negatives):
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            nums.remove(x)
            if x in nums or -x in nums:  # -x check is incorrect logic
                return True
        return False

=== SUCCESSFUL SOLUTIONS ===

1. Using Set Property (Optimal - O(n) time):
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        # Converts list to set (automatically removes duplicates)
        # Compares lengths to detect duplicates

2. Using Seen Set (Explicit - O(n) time):
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Empty set to track seen numbers
        for num in nums:
            if num in seen:  # O(1) membership check
                return True
            seen.add(num)  # Add new number to set
        return False

=== KEY LEARNINGS ===
1. Never modify a list while iterating over it
2. Sets provide O(1) membership testing
3. Python's set() automatically handles duplicates
4. Negative numbers require no special handling
5. The optimal solution compares set vs list lengths
**********************************************************************