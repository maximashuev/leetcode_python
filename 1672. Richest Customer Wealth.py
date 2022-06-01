def maximumWealth(accounts):
    summ = 0
    for i in accounts:
        if sum(i) > summ:
            summ = sum(i)
    print(map(sum, accounts))
    print(max(map(sum, accounts)))
    return summ


maximumWealth([[1, 5], [7, 3], [3, 5]])
