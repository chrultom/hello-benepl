def array123(nums):
    length = len(nums)
    count = False

    for x in range(length - 1):
        print x
        if nums[x] == 1 and nums[x + 1] == 2 and nums[x + 2] == 3:
            print nums[x], nums[x + 1], nums[x + 2]
            count = True
    if count:
        return True
    else:
        return False

ta = array123([1, 1, 2, 3, 1])
print ta
