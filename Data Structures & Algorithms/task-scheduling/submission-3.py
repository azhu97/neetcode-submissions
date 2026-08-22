class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # array of CPU tasks -> tasks 
        # tasks[i] is an uppercase letter 
        # CPU cycle can complete one of the tasks 
        # identical tasks must be seperated by atleast n CPU cycles 
        # return min number of cycles 
        # i can think of an nlogn solution using a heap with tuples 
        # can we throw everything in to a hashmap?
        # and then try to cycle through each count? 
        count = Counter(tasks)
        res = 0
        while count:
            temp = n + 1 if n != 1 else n
            keys = count.keys()
            marked = []
            for task in count.keys():
                # print("Task: ", task)
                res += 1
                temp -= 1
                count[task] -= 1
                if count[task] == 0:
                    marked.append(task)
            for task in marked:
                del count[task]
            if temp > 0 and count:
                print("Idle for: ", temp)
                res += temp
        return res