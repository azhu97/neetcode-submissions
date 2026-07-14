class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        visited = set()
        for i, string in enumerate(strs):
            if i not in visited:
                visited.add(i)
                temp_array = [string]
                temp_dict = self.returnDict(string)
                for j, other in enumerate(strs):
                    if j not in visited and temp_dict == self.returnDict(other):
                        visited.add(j)
                        temp_array.append(other)
                answer.append(temp_array)
        return answer     

    def returnDict(self, string):
        new_dict = {}
        for letter in string:
            if letter not in new_dict:
                new_dict[letter] = 1
            else:
                new_dict[letter] += 1
        return new_dict

        
        