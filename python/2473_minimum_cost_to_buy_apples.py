import heapq

class Solution:
    def minCost(self, n: int, roads: list[list[int]], appleCost: list[int], k: int) -> list[int]:
        # O(E)
        # construct a map of cities to neighbouring cities
        # contains shortest distance from point A to point B
        shortest_dist = [[0 if i == j else None for j in range(n)] for i in range(n)]
        # contains direct distance from point A to point B for O(1) access time later on, for O(E) cost
        edges = [[] for i in range(n)]
        for road in roads:
            city_from = road[0] - 1
            city_to = road[1] - 1
            city_dist = road[2]
            edges[city_from].append((city_dist, city_to))
            edges[city_to].append((city_dist, city_from))

        print("edges: ", edges)

        # conduct djikstra's algorithm for each city
        # Djikstra's algorithm complexity is O((V + E)logV) with min heap
        # Total complexity should be O(V(V+E)logV))
        for i in range(n):
            pq = [(0, i)]
            heapq.heapify(pq)
            # add all connected cities to pq
            while len(pq) > 0:
                # pop closest city out of pq
                dist_source, city_source = heapq.heappop(pq)
                # add all connected cities to pq with appropriate distance
                for dist_dest, city_dest in edges[city_source]:
                    # update shortest_dist
                    if shortest_dist[i][city_dest] is None or dist_source + dist_dest < shortest_dist[i][city_dest]:
                        shortest_dist[i][city_dest] = dist_source + dist_dest
                        heapq.heappush(pq, (dist_source + dist_dest, city_dest))
        # calculate, for every city, the cost of buying an apple from each city
        # this part is O(V^2)
    
        least_costs = [None for i in range(n)]
        for i, city in enumerate(shortest_dist):
            for j, distance in enumerate(city):
                if distance is None:
                    # city is unreachable
                    continue
                apple_cost = appleCost[j]
                total_cost = apple_cost + distance + distance * k
                if least_costs[i] is None or total_cost < least_costs[i]:
                    least_costs[i] = total_cost
        return least_costs
    
s = Solution()
# print(s.minCost(4, [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], [56,42,102,301], 2))
n = 19
roads = [[2,13,816],[7,9,192],[1,16,298],[4,8,358],[6,15,250],[14,10,128],[2,5,113],[11,3,136],[18,1,307],[16,5,128],[9,16,895],[13,11,420],[16,19,856],[2,14,91],[5,1,732],[1,4,405],[3,1,783],[18,15,170],[10,5,865],[16,12,542],[1,11,35],[17,19,329],[15,5,354],[8,12,772],[9,15,846],[8,16,189],[10,4,659],[2,9,855],[3,17,94],[6,16,346],[10,3,161],[1,12,313],[11,9,269],[16,14,14],[8,15,694],[2,1,37],[14,17,579],[14,7,816],[10,6,47],[8,13,811],[4,9,719],[3,9,395],[12,11,887],[4,14,80],[18,12,323],[4,12,277],[4,3,822],[15,13,761],[2,11,10],[15,4,638],[16,18,960],[2,19,872],[15,19,319],[14,12,290],[12,7,577],[7,10,257],[8,19,179],[19,3,118],[8,10,68],[5,6,478],[6,8,635],[2,18,82],[4,5,203],[18,11,509],[3,14,703],[1,15,109],[13,7,744],[14,8,725],[5,17,748],[14,1,669],[19,13,349]]
appleCost = [18474,61063,43090,54688,35205,37991,45885,96303,71092,70988,30033,55454,50690,2346,53812,54289,17591,25025,54874]
k = 49
print(s.minCost(n, roads, appleCost, k))





        