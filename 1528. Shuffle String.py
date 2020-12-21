def restoreString(s, indices):
    # dic = {}
    # for i in range(len(indices)):
    #     dic[indices[i]] = s[i]
    # print(dic)
    # sort_dic = dict(sorted(dic.items()))
    # print(sort_dic)
    # print(sort_dic.items())
    # sort_list = ""
    # for k, v in sort_dic.items():
    #     sort_list += v
    # print(sort_list)
    # return sort_list
    print("".join(dict(sorted(zip(indices,s))).values()))
    return "".join(dict(sorted(zip(indices,s))).values())


restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
