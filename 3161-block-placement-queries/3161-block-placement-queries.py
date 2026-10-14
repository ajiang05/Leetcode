class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.tree[i] = max(self.tree[i], val)
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result = max(result, self.tree[i])
            i -= i & -i
        return result

from typing import List
from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Collect all obstacles
        max_x = max(q[1] for q in queries)
        obstacles = SortedList([0, max_x + 1])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        ft = FenwickTree(max_x + 1)

        # Initialize the gaps
        for i in range(1, len(obstacles)):
            left = obstacles[i - 1]
            right = obstacles[i]

            ft.update(right, right - left)

        results = []

        # Process queries backward
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                # Find obstacle x
                idx = obstacles.bisect_left(x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                # Merge the gaps
                ft.update(right, right - left)

                # Remove obstacle
                obstacles.remove(x)

            else:
                _, x, size = q

                # Find rightmost obstacle <= x
                idx = obstacles.bisect_right(x)
                prev = obstacles[idx - 1]

                # Maximum completed gap before x
                max_gap = ft.query(prev)

                # Also consider gap from prev to x
                max_gap = max(max_gap, x - prev)

                results.append(max_gap >= size)

        return results[::-1]


                




        

