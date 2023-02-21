def createTargetArray(nums, index):
    target = []
    for i, z in zip(nums, index):
        target.insert(z, i)
    print(target)
    return target


createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0])
