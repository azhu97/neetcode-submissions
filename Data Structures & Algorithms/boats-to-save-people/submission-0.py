class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people = array of integers
        # people[i] = weight of the ith person
        # there are an infinite number of boats, where each boat can carry 
        #   max weight limit
        # each boat can carry at most two people at the same time
        #   provided the sum of the weight is at most limit 2

        # return the min number of boats to carry every body
        people.sort()
        res = 0
        mark = [1 for i in range(len(people))]
        # brute force o(n^2) time does not work
        # think of having two pointers, left and right
        # if w[l] + w[r] > limit: res += 1, r -= 1
        # means that guy on the right is too FAT 
        # else: res +=1, l += 1, r -= 1
        # both left and right can fit on the boat
        # might be too greedy
        l, r = 0, len(people) - 1
        while l <= r:
            w_l, w_r = people[l], people[r]
            if w_l + w_r > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            res += 1
        return res