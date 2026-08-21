class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # let there be bad runtime 
        # string s 
        # split s into substrings where each substring is a palindrome
        # return a list of all possible substrings
        # write a recurive function
        # we want a start, and an end point
        # when we iterate we push the end point futhur 
        def check(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        res = []
        test = 0 
        def recurse(i, j, listing):
            temp = listing.copy()
            if j >= len(s):
                # bad
                return
            nonlocal res 
            # there are two cases either
            # 1. [i:j] is a valid palindrome
            # if so -> add s[i::j + 1] to the listing also note
            # note that if j is the last index -> add a copy of listing to res 
            # we want to check two more things
            # add palindrome to listing and then reset i and j to j + 1
            # then we pop from the listing, the push j by an index 
            # 2. [i:j] not a valid palindrome 
            if check(i, j):
                listing.append(s[i:j+1])
                if j == len(s) - 1:
                    res.append(listing.copy())
                    return
                # print("before: ", listing, temp)
                recurse(j + 1, j + 1, listing)
                # print("after: ", listing, temp)
            recurse(i, j + 1, temp)
        recurse(0, 0, [])
        return res