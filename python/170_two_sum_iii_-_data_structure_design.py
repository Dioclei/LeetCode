# Problem: design a data structure for that can hold a stream of integers, and checks if it has a pair of integers that sum up to a value
# Intuition:
# - I want the best data structure possible, can I do O(1) insert and O(1) find?
# - Let's use a HashMap to store all the values. it will be an O(1) insert and O(n) find

# Comments
# - can't really beat this method
# - possible to use a list and sort it before running the actual two sum algorithm with 2 pointers, but that takes O(nlogn) runtime for find

class TwoSum:

    def __init__(self):
        self.m = {}

    def add(self, number: int) -> None:
        if number in self.m:
            self.m[number] += 1
        else:
            self.m[number] = 1

    def find(self, value: int) -> bool:
        for num in self.m:
            other = value - num
            if other == num and self.m[num] >= 2:
                return True
            elif other != num and other in self.m:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)