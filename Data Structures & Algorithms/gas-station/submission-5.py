class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # use a left and right pointer
        # try to expand the right pointer or 
        #   if we have gas, we add to tank then expand 
        #   if we don't have gas, we move back, then add the back the gas we would have taken if we started back a position
        # try to shrink the left pointer
        l, r = len(gas) - 1, 0
        tank = gas[l] - cost[l] # what we take - what we use
        while l > r:
            # if we have enough gas, take gas and push r
            if tank > 0:
                tank += gas[r] - cost[r]
                r += 1
            else:
                l -= 1
                tank += gas[l] - cost[l]
        return l if tank >= 0 else -1
        