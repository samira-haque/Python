# search for a number x in this tupple using loop : (1,4,9,16,25,36,49,64,81,100)

nums = [1,4,9,16,25,36,49,64,81,100]

x = 36
i = 0
while i < len(nums) :
    # print(nums[i])
    if(nums[i] == x):
        print("found at index",i)
    else:
        print("finding..")
    i += 1