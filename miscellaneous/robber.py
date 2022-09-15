def robber(nums):
    maxmoneycollected = 0
    if len(nums) == 3:
        return max(nums)
    for housenumber in range(len(nums)):
        nexthouse = housenumber + 2
        totalhoues = len(nums)
        if housenumber == 0:
            # if len(nums) % 2 == 0:
            #     totalhoues -= 2
            # else:
            #     totalhoues -= 3
            while nexthouse < totalhoues - 1:
                moneycollection = nums[housenumber]
                print(housenumber, nexthouse)
                moneycollection += nums[nexthouse]
                print("money: {}".format(moneycollection))
                nexthouse = nexthouse + 1
                if moneycollection > maxmoneycollected:
                    maxmoneycollected = moneycollection
            
        else:
            while nexthouse < totalhoues:
                moneycollection = nums[housenumber]
                print(housenumber, nexthouse)
                moneycollection += nums[nexthouse]
                nexthouse = nexthouse + 1
            if moneycollection > maxmoneycollected:
                maxmoneycollected = moneycollection
    return maxmoneycollected


#nums = [1,2,3,1]
# nums = [2,7,9,3,1]
nums = [200,3,140,20,10]
#nums = [1,2,3,1]
nums = [1,3,1,3,100]

print(robber(nums))