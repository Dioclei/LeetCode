class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        # sort the list of people
        people.sort()
        # pointers point at next person to be allocated
        p1 = 0
        p2 = len(people) - 1
        boat_count = 0
        while p1 <= p2:
            if p1 == p2:
                boat_count += 1
                break
            elif people[p1] + people[p2] <= limit:
                # put 2 people on boat
                boat_count += 1
                p1 += 1
                p2 -= 1
            else:
                # put heaviest guy on boat
                boat_count += 1
                p2 -= 1
        return boat_count

