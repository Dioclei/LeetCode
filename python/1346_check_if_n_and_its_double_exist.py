class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, num1 in enumerate(arr):
            for num2 in arr[i+1:]:
                if num1 * 2 == num2 or num2 * 2 == num1:
                    return True
                
        return False