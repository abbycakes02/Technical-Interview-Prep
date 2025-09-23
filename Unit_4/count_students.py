from ast import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0
        while counter < len(students):
            if students[0] == sandwiches[0]:
                counter = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                x = students.pop(0)
                students.append(x)
                counter+=1
        
        return counter
