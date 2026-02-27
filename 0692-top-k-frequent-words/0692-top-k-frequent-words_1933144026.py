class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        topk = sorted(freq.items(), key=lambda item : (-item[1], item[0]))
        return ([s[0] for s in topk[:k]])