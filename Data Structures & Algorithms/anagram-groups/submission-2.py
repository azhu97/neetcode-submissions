class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            mapping[key].append(word)

        return list(mapping.values())