class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        You can either take a job or not take a job which are the two options

        I am thinking of keeping track of a dp array 

        I think we can iterate through the endTime and build it bottom up
        dp[i] = represents max profit at time[i]

        if index is at endtime:
            we have to check 0-start:
                dp[i] = max(dp[j]+profit[i],dp[i])

        [100. ][50]
        [90][90]

        """
        time_sort = []
        for i in range(len(startTime)):
            time_sort.append((startTime[i],endTime[i],profit[i]))
        
        time_sort.sort(key = lambda x: x[1])

        end_sort = [end for start,end,prof in time_sort]

        dp = [0]*(len(end_sort)+1)

        for i in range(len(end_sort)):
                start,end,prof = time_sort[i]

                j = bisect_right(end_sort,start)
                dp[i+1] = max(dp[i],dp[j]+prof)

        return dp[-1]
        