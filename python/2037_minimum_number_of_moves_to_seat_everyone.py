from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # index the number of seats and students at each position
        number_of_seats = {}
        number_of_students = {}
        for s in seats:
            if s in number_of_seats:
                number_of_seats[s] += 1
            else:
                number_of_seats[s] = 1
        for st in students:
            if st in number_of_students:
                number_of_students[st] += 1
            else:
                number_of_students[st] = 1
        
        seat_list = sorted(number_of_seats.keys())
        student_list = sorted(number_of_students.keys())

        p1 = 0
        p2 = 0
        dist = 0
        while p1 < len(seat_list):
            # allocate seat to student
            seat_pos = seat_list[p1]
            number_of_seats[seat_pos] -= 1
            if number_of_seats[seat_pos] == 0:
                p1 += 1
            student_pos = student_list[p2]
            number_of_students[student_pos] -= 1
            if number_of_students[student_pos] == 0:
                p2 += 1
            dist += abs(seat_pos - student_pos)
        return dist

