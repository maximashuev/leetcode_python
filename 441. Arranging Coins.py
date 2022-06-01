def arrangeCoins(n: int):
    a = 0
    while n > 0 and n > a:
        n -= a + 1
        a += 1
    print(a)


arrangeCoins(5)
arrangeCoins(11)
