penalty_factor = 30

lineq2penalty = LinearEqualityToPenalty(penalty_factor)
qubo = lineq2penalty.convert(mod)
