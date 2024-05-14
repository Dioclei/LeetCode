import heapq
class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # we are going to attempt to pay the lowest wage, so we want a worker that asks for a "low" wage
        # consider that if the worker asks for a low wage and gives shit work means we need to pay others a proportionally high wage
        # consider that if the best worker asks for a low wage and gives high quality work, we will then need to pay others less proportionally
        
        # we want to minimise wage/quality, so as to pay each worker as low a unit wage as possible
        # at the same time we want to minimise quality, so as to pay as low a total amount as possible

        workers_by_unit_cost = []
        workers_by_quality = []
        for i in range(len(quality)):
            w = wage[i]
            q = quality[i]
            w_q = w / q
            workers_by_unit_cost.append((-w_q, i))
            workers_by_quality.append((-q, i))
        heapq.heapify(workers_by_unit_cost)
        heapq.heapify(workers_by_quality)
        # find an overlap of k length, with the best unit cost workers and the lowest quality workers
        # we do this by starting from a state of maximum overlap i.e. overlap = n, a.k.a choose all workers at first
        # then pop from a maxheap until overlap = k
        chosen_workers = set([i for i in range(len(quality))])
        while len(chosen_workers) > k:
            uc, w1 = heapq.heappop(workers_by_unit_cost)
            chosen_workers.discard(w1)
            ql, w2 = heapq.heappop(workers_by_quality)
            chosen_workers.discard(w2)
        print(chosen_workers)
        # calculate total cost
        unit_cost = 0
        total_quality = 0
        for i in chosen_workers:
            w = wage[i]
            q = quality[i]
            unit_cost = max(unit_cost, w / q)
            total_quality += q
        return unit_cost * total_quality


