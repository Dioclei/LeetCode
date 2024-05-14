import heapq

class Solution:
    # O(nlogn) for sorting
    # def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
    #     # sort happiness values to get the happiest children
    #     happiness.sort(reverse=True)
    #     # select k happiest children
    #     happiest_children = happiness[:k]
    #     # sum up happiness
    #     decrement = 0
    #     total = 0
    #     for child in happiest_children:
    #         val = max(0, child + decrement)
    #         decrement -= 1
    #         total += val
    #     return total

    # O(n + klogn) for O(n) heapify and O(klogn) popping operation
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        # build max heap
        happiness = [-h for h in happiness]
        heapq.heapify(happiness)
        decrement = 0
        total = 0
        for _ in range(k):
            h = -(heapq.heappop(happiness))
            val = max(0, h + decrement)
            decrement -= 1
            total += val
        return total
        

s = Solution()
print(s.maximumHappinessSum([1, 2, 3], 2))
