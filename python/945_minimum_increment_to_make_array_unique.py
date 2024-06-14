from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # sort the list
        nums.sort()
        p = 1
        moves = 0
        dupe_queue = [] # use a queue to keep track of dupes
        while p < len(nums):
            if nums[p] == nums[p-1]:
                # this is a dupe, slot it back in later
                dupe_queue.append(nums[p])
            else:
                # if this is not a dupe, attempt to slot dupes in between this and last number
                slots = nums[p] - nums[p-1] - 1
                number_slotted_dupes = min(len(dupe_queue), slots)
                for i in range(number_slotted_dupes):
                    dupe = dupe_queue.pop(0)
                    moves += (nums[p-1]+1+i - dupe)
            p += 1
        # for the rest of the dupes, slot it at the back of the list
        current_slot = nums[-1] + 1
        while len(dupe_queue) > 0:
            dupe = dupe_queue.pop(0)
            moves += (current_slot - dupe)
            current_slot += 1
        return moves
    
    ### EDITORIAL SOLUTION

    # Sorting solution by the editorial is much cleaner, because it doesn't hold on to dupes
    # it increments the most recent element to be a non-dupe (but the future ones may be dupes)
    # maintaining the invariant that for every element in indexes < i, they are all not dupes

    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0

        nums.sort()

        for i in range(1, len(nums)):
            # Ensure each element is greater than its previous
            if nums[i] <= nums[i - 1]:
                # Add the required increment to minIncrements
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment

                # Set the element to be greater than its previous
                nums[i] = nums[i - 1] + 1

        return min_increments
    
    # the other solution is a counting solution, with a time complexity of O(n + max)
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        min_increments = 0

        # Create a frequencyCount array to store the frequency of each value in nums
        frequency_count = [0] * (n + max_val + 1)

        # Populate frequencyCount array with the frequency of each value in nums
        for val in nums:
            frequency_count[val] += 1

        # Iterate over the frequencyCount array to make all values unique
        for i in range(len(frequency_count)):
            if frequency_count[i] <= 1:
                continue

            # Determine excess occurrences, carry them over to the next value,
            # ensure single occurrence for current value, and update min_increments.
            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            frequency_count[i] = 1
            min_increments += duplicates

        return min_increments
