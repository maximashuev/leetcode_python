# return masked string
def maskify(cc):
    li=[]
    for i in range(0,len(cc)):
        if i<len(cc[:-4]):
            li.append("#")
        else:
            li.append(cc[i])
    print(''.join(li))
    return ''.join(li)

maskify("4556364607935616")