class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = "" 
        for i in digits:
            res += str(i)
        res = int(res)
        res += 1
        res = str(res)
        arr = []
        for i in res:
            arr.append(i)
        
        return arr