from LAB50 import Country
from LAB50 import Continent



canada = Country('Canada',34482779,9984670)
usa = Country('United States of America', 313914040, 9826675)

print("Name:" + canada.name + "\nPopulation: "  +  str(canada.population) +  "\nArea: " + str(canada.area))
print(canada.is_larger(usa))
print("______________")
print( usa.is_larger(canada))
print("______________")
print(canada.population_density())
print("______________")
print(usa)
print("______________")
print(canada)
print("______________")
print([canada])
print("______________")
