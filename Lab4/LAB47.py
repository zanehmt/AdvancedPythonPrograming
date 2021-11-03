def count_duplicates(inDict) -> int:
    lstAllValues = []
    lstAdditional = []
    lstFinal = []

    for i in inDict.values():
        lstAllValues.append(i)
        lstAdditional.append(i)

    lstFinal = set(lstAllValues).intersection(lstAdditional)

    return (len(lstAllValues) - len(lstFinal))


number = {'one': 1, 'two': 2, 'two1': 2, 'three1': 3, 'three': 3}

print(count_duplicates(number))