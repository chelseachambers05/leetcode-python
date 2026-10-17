from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)
        for s in strs:
            sortedStr = ''.join(sorted(s))
            group[sortedStr].append(s)
        return list(group.values())