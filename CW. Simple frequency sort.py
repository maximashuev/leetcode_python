def solve(arr):
    sorted_list = sorted(arr)
    print(sorted_list)
    dict = {}
    result = []
    for i in sorted_list:

        if i in dict:

            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    sort = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    print(sort)
    for key in sort:
        result += ([key] * dict[key])
    print(result)
    return result


solve([2, 3, 5, 3, 7, 9, 5, 3, 7])
