def countNegatives(grid):
    # combined_list = [item for sublist in grid for item in sublist]
    output = 0
    for i in grid:
        for a in i:
            if a<0:
                output += 1
    print(output)
    return output

countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
