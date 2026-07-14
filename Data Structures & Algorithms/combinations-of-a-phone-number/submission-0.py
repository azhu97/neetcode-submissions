class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        res = []
        arr = [[] for i in range(9)]
        index = 97
        for i in range(9):
            if i == 0:
                continue
            for b in range(3):
                arr[i].append(chr(index))
                index += 1
            if i == 6 or i == 8:
                arr[i].append(chr(index))
                index += 1

        def rec(i, word):
            # when the word is complete
            if i >= len(digits):
                res.append(word)
                return
            temp = int(digits[i])
            temp_arr = arr[temp - 1]
            for char in temp_arr:
                rec(i + 1, word + char)
        
        rec(0, "")
        return res
            
        