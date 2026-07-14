class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1) 
        m = len(s2)
        l, r = 0, n - 1
        if n > m:
            return False

        n_arr = [0] * 26
        m_arr = [0] * 26
        for c in s1:
            n_arr[ord(c) % 97] += 1
        for c in s2[:n]:
            m_arr[ord(c) % 97] += 1
            
        while r < m:
            if m_arr == n_arr:
                return True
            m_arr[ord(s2[l]) % 97] -= 1
            l += 1
            r += 1
            if r >= m:
                return False
            m_arr[ord(s2[r]) % 97] += 1
        
        return False
    