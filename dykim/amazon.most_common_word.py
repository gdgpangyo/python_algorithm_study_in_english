# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2973/
# elapsed time : 22 min

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'([^\s\w]|_)+', ' ', paragraph).lower().split()
        counts = collections.Counter(words)
        print(counts)
        for b in banned:
            if b in counts:
                counts.pop(b)
        
        if len(counts) == 0: return None
        return counts.most_common(1)[0][0]
        
