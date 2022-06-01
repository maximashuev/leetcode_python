def find_short(s):
    listik = s.split(" ")
    l = len(s)
    for i in listik:
        if len(i) < l:
            l = len(i)

    print(l)

    return l  # l: shortest word length


find_short("bitcoin take over the world maybe who knows perhaps")
