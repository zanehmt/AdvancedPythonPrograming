def is_balanced(inDict: [str, float]) -> bool:
    sumVar = 0.0

    for i in inDict.values():
        sumVar = sumVar + i

    return sumVar == 1


RGB = {'R': 0.2, 'G': 0.2, 'B': 0.6}

print(is_balanced(RGB))