# easy

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        number_of_steps = [0] * (n + 1)
        number_of_steps[0] = 1
        number_of_steps[1] = 1
        def dp_climb_stairs(i):
            if i > n: return
            number_of_steps[i] = number_of_steps[i - 1] + number_of_steps[i - 2]
            # evaluate next step
            dp_climb_stairs(i + 1)

        dp_climb_stairs(2)
        return number_of_steps[n]
    

        
        
