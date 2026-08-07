from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):

        freq = Counter(nums)

        answer = []

        for num, count in freq.most_common(k):
            answer.append(num)

        return answer