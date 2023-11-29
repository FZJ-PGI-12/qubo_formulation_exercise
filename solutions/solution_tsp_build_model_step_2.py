def X(city, stop):
    return "x_{city}_{stop}".format(city=city, stop=stop)


quadratic_dict = {}
for i, j in it.combinations(range(instance.num_cities), 2):
    for a in range(instance.num_cities):
        quadratic_dict[(X(i, a), X(j, ((a + 1) % instance.num_cities)))] = instance.distances[(i, j)]
mod.minimize(quadratic=quadratic_dict)
