**********************************************************************
*                    LEETCODE DUPLICATES CHALLENGE                   *
*                    Valid Anagram Problem                           *
**********************************************************************

=== FAILED ATTEMPTS ===

1-First Attempt (Problem: )
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        s_dict = {}
        t_dict = {}
        for letter in s:
            s_dict[letter] = s.count(letter) 
        for letter in t:
            t_dict[letter] = t.count(letter) 
        if len(s_dict) == len(t_dict):
            for theletter in s_dict:
                if theletter in t_dict and t_dict[theletter] != s_dict[theletter] : 
                    return False
        return True

For the first test its works but for "car" and "rat" because 'c' is in s_dict
but not in t_dict so the condition if the letter is in t_dict fail.

2-
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #calcul of weigth
        weigth_S = 0
        weigth_T = 0
        for letter in s:
            weigth_S = weigth_S + ord(letter)
        for letter in t:
            weigth_T = weigth_T +ord(letter)
        if weigth_T == weigth_S:
            return True
        return False
Fail in the test:
"ggii" and "eekk"
#The motherfuckers m'ont eu Those string have the same ascii wait but their are completely different

3-
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list()
        t_list = list()
        for letter in s:
            s_list.append(letter)
        for letter in t:
            t_list.append(letter)
        for letter in s:
            s_list.remove(letter)
            if letter in t_list:
                t_list.remove(letter)
        return (len(t_list) == len(s_list) == 0 )
Fail in test:
"ab" and "a" #almost good. Just that the length of the strings should be equal


4-
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list()
        t_list = list()
        for letter in s:
            s_list.append(letter)
        for letter in t:
            t_list.append(letter)
        for letter in s:
            s_list.remove(letter)
            if letter in t_list:
                t_list.remove(letter)
        return (len(t_list) == len(s_list) == 0 ) and (len(s) == len(t))
Its correct but not optimal: 20ms.

=== OTHERS SOLUTIONS ===

5- The most optimal Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        return s_count==t_count

6- A solution with the dictionnary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1
        
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        return s_dict == t_dict

7-
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26 #For lowercase English Letters 
        #I think this is for create a tab of 26 charactere

        for char in s:
            freq[ord(char) - ord('a')] += 1
        for char in t:
            freq[ord(char) - ord('a')] -=1
            if freq[ord(char) - ord('a')] < 0:
                return False
        return True #this is a beautiful mutual exclusion.
8-
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) #The sorted Method is for sort a string.

=== KEY LEARNINGS ===
1.s_dict[ch] = s_dict.get(ch, 0) + 1 counts the frequency of a charactere in a string
    if ch exist -> return it current count
    else -> return 0

    EXAMPLE:
    s = "hello"
    s_dict = {}
    for ch in s:
    s_dict[ch] = s_dict.get(ch, 0) + 1

    print(s_dict)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    Equivalent to:
    if ch in s_dict:
        s_dict[ch] += 1
    else:
        s_dict = 1
2. s_count = collections.Counter(s)
    EXAMPLE
    from collections import Counter
    s = "hello"
    s_count = Counter(s)
    print(s_count)  # Output: Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
3. == Compares value (works for most type)