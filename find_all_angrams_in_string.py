#Find All Anagrams in a String

#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.


class solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        p = sorted(p)
        arr = []

        for i in range(len(s) - len(p) +1):
            if sorted(s[i : i + len(p)])==p:
                arr.append(i)

        return arr
