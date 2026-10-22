class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        We have to have array that point from class-> prereq and we have a seen that we backtrack from
        """
        prereq = {}

        for p in prerequisites:
            if p[0] in prereq:
                prereq[p[0]].append(p[1])
            else:
                prereq[p[0]] = [p[1]]
        
        visited = set()
        visiting = set()

        def dfs(course):
            if course in visited:
                return True
            if course not in prereq:
                return True
            if course in visiting:
                return False
            
            visiting.add(course)

            for c in prereq[course]:
                if not dfs(c):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True



            



