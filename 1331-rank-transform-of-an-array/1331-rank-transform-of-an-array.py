class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}

        for i, num in enumerate(sorted(set(arr))):
            rank[num] = i + 1

        result = []
        for num in arr:
            result.append(rank[num])

        return result