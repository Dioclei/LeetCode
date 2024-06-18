from typing import List
import heapq

class Solution:
    # memoization solution (after reading editorial)
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # idea is to memoise the highest profit job at each difficulty
        # find max difficulty
        max_diff = max(worker)
        max_profit = [0] * max_diff
        for i in range(len(difficulty)):
            d = difficulty[i]
            p = profit[i]
            if d > max_diff:
                continue
            else:
                idx = d - 1
                max_profit[idx] = max(max_profit[idx], p)
        prev = 0
        for j in range(len(max_profit)):
            if max_profit[j] > prev:
                prev = max_profit[j]
            max_profit[j] = prev
        result = 0
        for w in worker:
            result += max_profit[w-1]
        return result            


    # heap solution
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # goal: have each worker do the highest profit job that they can do
        # create a max-heap with (profit, difficulty)
        jobs = list(zip(map(lambda x: -x, profit), map(lambda x: -x, difficulty)))
        heapq.heapify(jobs)
        # create a max-heap for workers
        worker = list(map(lambda x: -x, worker))
        heapq.heapify(worker)
        # invariant:
        # if the first worker cannot do the first job, then no other worker can do the first job.
        max_profit = 0
        while len(jobs) > 0 and len(worker) > 0:
            job = jobs[0]
            # check if workers can do it
            w = worker[0] * -1
            d = job[1] * -1
            p = job[0] * -1
            if w >= d:
                # worker can do it
                max_profit += p
                heapq.heappop(worker)
            else:
                # worker cannot do the job
                heapq.heappop(jobs)
        return max_profit

    




        
