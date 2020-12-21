def solve(s):
    open=0
    clese=0
    stock=[]
    for i in s:
        if len(stock) == 0:
            stock.append(i)

        else:
            last = stock.pop()
            if last == "(" and i == ")":
                continue
            else:

                stock.append(last)
                stock.append(i)
    for i in stock:
        if i =="(":
            open+=1
        else:clese+=1
    print(stock)
    if (open+clese)%2!=0:
        print("----")
        return -1
    print(open,clese)
    print(int((open//2+open%2)+(clese//2+clese%2)))
    return (int((open//2+open%2)+(clese//2+clese%2)))

solve(")()(")#2
solve("((()")#1
solve("(((")#-1
solve("())(((")#3
solve("())()))))()()(")#4