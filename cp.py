def twoSum(nums, target):
    for i in range(len(nums)):
        print(i)
        for k in range(i+1, len(nums)):
            # solution = []
            if nums[i]+nums[k]==target:
                # solution = [nums[i],nums[k]]
                # return solution
                print(nums[i],nums[k])
                # return solution


twoSum([2,7,11,15],9)