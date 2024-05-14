class Solution:
    # O(n^2 solution)
    # def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
    #     fractions = []
    #     for n in arr:
    #         for m in arr:
    #             fraction = (n / m, n, m)
    #             fractions.append(fraction)
    #     fractions.sort(key=lambda tup: tup[0])
    #     return (fractions[k - 1][1], fractions[k - 1][2])
    
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        # consider array [1, 2, 3, 5]
        # 1. smallest is 1/5
        # 1a. 1/5 is followed by either: 1/3 or 2/5
        # 2. next is 1/3
        # 2a. 1/3 is followed by either: 2/5, 2/3, or 1/2
        # 3. next is 2/5
        # 3a. 2/5 is followed by either: 2/3 or 3/5
        # 4. next is 1/2
        # 4a. 1/2 is followed by either: 2/3 or 2/2
        # 5. next is 3/5
        # 5a. 3/5 is followed by either: 3/3

        # ..???