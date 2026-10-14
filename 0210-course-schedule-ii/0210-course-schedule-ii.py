class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        We can create a dict where we have class-> prereqs for that class

        We have a visited set and we
        """
        prereqs = {}

        for course, pre in prerequisites:
            if course in prereqs:
                prereqs[course].append(pre)
            else:
                prereqs[course]  = [pre]
        
        visited = set()
        visiting = set()
        result = []
        def dfs(course):
            #means that we already visisted and its valid
            if course in visited:
                return True
            #cycle
            if course in visiting:
                return False
            
            visiting.add(course)

            if course in prereqs:
                for pre in prereqs[course]:
                    if not dfs(pre):
                        return False
            
            visiting.remove(course)
            visited.add(course)
            result.append(course)

            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result
