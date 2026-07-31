class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = {}

        for letter in word:
            freq[letter] = freq.get(letter, 0) + 1

        counts = sorted(freq.values(), reverse=True)

        return sum(count * (i // 8 + 1)
                   for i, count in enumerate(counts))