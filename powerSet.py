def powerSet(items):
    power_set = [[]]
    for item in items:
        power_set.extend([subset+[item] for subset in power_set])  # Append item to all subsets generated so far
    return power_set

