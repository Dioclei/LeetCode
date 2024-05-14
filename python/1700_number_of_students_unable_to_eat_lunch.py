# easy

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        
        # it doesn't matter what order the students are in...

        prefer_square = 0
        prefer_circle = 0
        for x in students:
            if x == 0:
                prefer_circle += 1
            else:
                prefer_square += 1
        
        while len(sandwiches) > 0:
            s = sandwiches.pop(0)
            if s == 0:
                if prefer_circle > 0:
                    prefer_circle -= 1
                else:
                    return len(sandwiches) + 1
            if s == 1:
                if prefer_square > 0:
                    prefer_square -= 1
                else:
                    return len(sandwiches) + 1
        return 0
            
