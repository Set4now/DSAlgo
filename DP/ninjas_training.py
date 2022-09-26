
# Total task are 3 , [0, 1, 2]
# days are (len(points) - 1), in 0 based indexed points
# points, 2 day aray, where  points[i][j] means jth merit point in day i,


# Simple recursive code
def max_merit_points(day, lasttask, points):
    if day == 0:
        maxmerit = 0
        for i in range(3):
            if i != lasttask:
                maxmerit = max(maxmerit, points[0][i])
        return maxmerit
    
    maxpoint_earned = 0
    for task in range(3):
        if task != lasttask:
            maxpoint = points[day][task] + max_merit_points(day - 1, task, points)
            maxpoint_earned = max(maxpoint, maxpoint_earned)
    return maxpoint_earned

# points = [[10,50,1],[5,100,1]]
# day = len(points) - 1
# print(max_merit_points(day, 3, points))


# Dp with Memoization
"""
we need a 2D dp here, since there are two 
args in our recusrive function and 

All possible ways
we select a task each day, there must be an optimal ans for each pair ( task per day)

2D DP array 
[day][task] =  ( days * tasks )
"""

def memoization(points):

    dp = [[-1] * 4] * len(points)
    def max_merit_points(day, lasttask, points):
        if day == 0:
            maxmerit = 0
            for i in range(3):
                if i != lasttask:
                    maxmerit = max(maxmerit, points[0][i])
            return maxmerit
        
        if dp[day][lasttask] != -1:
            return dp[day][lasttask]
        
        maxpoint_earned = 0
        for task in range(3):
            if task != lasttask:
                maxpoint = points[day][task] + max_merit_points(day - 1, task, points)
                maxpoint_earned = max(maxpoint, maxpoint_earned)
        dp[day][lasttask] = maxpoint_earned
        return dp[day][lasttask]

    lastday = len(points) - 1
    return max_merit_points(lastday, 3, points)

points = [[10,50,1],[5,100,1]]
day = len(points) - 1
print(memoization(points))







