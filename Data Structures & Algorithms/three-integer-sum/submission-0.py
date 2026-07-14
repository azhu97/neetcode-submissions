class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # can iterate through once, doing whatever function
        answer = []
        answer_set = []

        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                for z in range(y + 1, len(nums)):
                    temp_set = {nums[x], nums[y], nums[z]}
                    if nums[x] + nums[y] + nums[z] == 0 and temp_set not in answer_set:
                        temp = [nums[x], nums[y], nums[z]]
                        answer_set.append(temp_set)
                        answer.append(temp)
    
        return answer