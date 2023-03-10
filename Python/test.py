def sortSentence(num):
    s = num.split(" ")
    result = []
    for i in s:
        # print (i[-1])
        result.insert((int((i[-1]))-1),i[:-1])




    # print(s)
    print(" ".join(result))

sortSentence("is2 sentence4 This1 a3")
sortSentence("Myself2 Me1 I4 and3")