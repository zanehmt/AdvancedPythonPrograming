def mating_pairs(males, females):

    pairs = set()
    num_gerbils = len(males)
    for i in range(num_gerbils):
        male = males.pop()
        female = females.pop()
        pairs.add((male, female), )
    return pairs

print(mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob',
'Chen'}))