class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        elems = {}

        for value in nums:
            if value in elems:
                elems[value] += 1
            else:
                elems[value] = 1

        sortedElems = sorted(elems.items(), key=lambda x:x[1], reverse=True)
        topPairs = sortedElems[:k]

        result = []
        for pair in topPairs:
            result.append(pair[0])
        return result
