class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap in python is min
        # so lets have a heap with tuples 
        # -> (-task_count, task)
        # task_que holding -> task, execution cycle, remaining count
        # whenever the heap is empty, we have to push the cycle time forward
        # and continue
        c = Counter(tasks)
        heap = []
        que = deque()
        cycle = 0
        for key, value in c.items():
            heapq.heappush(heap, (-value, key))
        while heap or que:
            if heap:
                # print("HEAP: ", heap)
                count, task = heapq.heappop(heap)
                count *= -1 
                count -= 1
                if count > 0:
                    que.append((task, count, cycle))
                cycle += 1
                # print("CYCLE: ", cycle)
            while que:
                # print("QUE: ", que)
                # check if we can put it on the que
                # if so, pop and continue
                # if not, check if the heap is empty
                # if it is empty, skip the cycle forward
                # else break the while loop
                if que[0][-1] + n + 1 > cycle:
                    if len(heap) != 0:
                        break # break the while loop
                    else:
                        # time skip
                        # print("TIMESKIP")
                        cycle = que[0][-1] + 1 + n
                task, count, _ = que.popleft()
                heapq.heappush(heap, (-count, task))
        return cycle