from typing import Dict


def count_values(inDict: Dict) -> int:
    finalList = []

    for i in inDict.values():
        if i not in finalList:
            finalList.append(i)

    return len(finalList)


color = {'red': 1, 'green': 1, 'blue': 2}

print(count_values(color))