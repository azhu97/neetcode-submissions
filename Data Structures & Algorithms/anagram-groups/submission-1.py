class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            count = [0] * 26 #for the 26 letters in the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1

            answer[tuple(count)].append(s)
        
        return answer.values()


        
        