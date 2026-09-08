class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        # n gas stations on a CIRCULAR route
        # two int arrs 
        # gas -> amount of gas 
        # cost -> amount of gas needed to travel from ith to ith+1 station
        # gas storage unlimted, begin empty tank at ONE of the stations
        # return the one index that you can travel across the entire track 
        # brute force, try to naviagte the entire arr for each index

        # at each gas station, we should try to take the most amount of gas possible
        # what are the cases at each gas station? 
        # 1. we start at this gas station
        # 2. we continue from the previous gas station

        # will i have more gas if i started here, or if i started previous? 
        # the place that has the most gas is the winner
        res = -1
        running_gas = -1
        for i in range(len(gas)):
            temp = gas[i] - cost[i] # gas you get - cost to go
            # we want to see, is temp greater than the running gas
            if running_gas < 0:
                res = i
                running_gas = temp
            else:
                running_gas += temp
        return res