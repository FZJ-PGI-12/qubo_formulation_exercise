def X(city, stop):
    return "x_{city}_{stop}".format(city=city, stop=stop)

for i in range(instance.num_cities):
    constraint_dict = {}
    for a in range(instance.num_cities):
        constraint_dict[X(i, a)] = 1
    mod.linear_constraint(linear=constraint_dict, sense="==", rhs=1, name="city_{}_once".format(i))


for a in range(instance.num_cities):
    constraint_dict = {}
    for i in range(instance.num_cities):
        constraint_dict[X(i, a)] = 1
    mod.linear_constraint(linear=constraint_dict, sense="==", rhs=1, name="one_city_at_stop_{}".format(a))
