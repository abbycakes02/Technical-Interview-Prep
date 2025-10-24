class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # left to right
        # right to left

        dist = float('inf')
        answer = [float('inf')] * len(s)
        for i in range(len(s)):
            if s[i]== c:
                dist = 0
            else:
                dist += 1
            answer[i] = dist
        dist = float('inf')
        for i in range(len(s)-1, -1 ,- 1):
            if s[i] == c:
                dist = 0
            else:
                dist+=1
            answer[i] = min(answer[i], dist)
        return answer


        