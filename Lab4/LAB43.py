def mating_pairs(males, females):
    try:
        pairs = set()
        num_gerbils = len(males)
        for i in range(num_gerbils):
            male = males.pop()
            female = females.pop()
            pairs.add((male, female),)
        return pairs
    except:
        return print("Số lượng Males và Females phải bằng nhau")
males = {'Nam1', 'Nam2', 'Nam3'}
females = {'Nu1', 'Nu2', 'Nu3'}
print(mating_pairs(males, females))