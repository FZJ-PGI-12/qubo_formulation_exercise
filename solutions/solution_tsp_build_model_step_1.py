mod = QuadraticProgram("TSP")
for city in range(instance.num_cities):
    for stop in range(instance.num_cities):
        variable_name = "x_{city}_{stop}".format(city=city, stop=stop)
        mod.binary_var(variable_name)
