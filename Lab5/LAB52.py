from LAB50 import Continent
from LAB50 import Country as country

canada = country('Canada', 34482779, 9984670)
usa = country('United States of America', 313914040, 9826675)
mexico = country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
print(north_america.name)
for country in north_america.countries:
    print(country)

print("______________")
print(north_america.total_population())

print("______________")
print(north_america)