class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "0#95882#%"
        string = ""
        for i, s in enumerate(strs):
            string += s
            if i != len(strs) - 1:
                string += "0#95882#%"
            print(string)
        return string

    def decode(self, s: str) -> List[str]:
        if s == "0#95882#%":
            return []
        return s.split("0#95882#%")