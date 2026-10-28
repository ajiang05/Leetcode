class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        """
        We create an dictionary of all the different times
        We go through and add to the array and we iterate throught to fill it our
        If it is not in the dict then we just use the curr result at end
        If people> start then that is when we can keep track of it
        """

        max_people = max(people)
        flowers_freq = {}

        for s,e in flowers:
            if s<=max_people:
                flowers_freq[s] = flowers_freq.get(s,0)+1
            if e<=max_people:
                flowers_freq[e+1] = flowers_freq.get(e+1,0)-1
        
        flower_sort = sorted(list(flowers_freq.keys()))

        sort_p = sorted(
            enumerate(people),
            key=lambda x: x[1]
        )
        result = [0]*len(people)
        f = 0
        curr_flower = 0
        
        for i,p in sort_p:
            while f<len(flower_sort) and flower_sort[f]<=p:
                curr_f = flower_sort[f]
                curr_flower+=flowers_freq[curr_f]
                f+=1
            
            result[i] = curr_flower
        
        return result


            


            


        

