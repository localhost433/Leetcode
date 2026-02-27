class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        ret = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        for _ in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret