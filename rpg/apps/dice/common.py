from dice import roll


# TODO: add possible variations: reroll lowest stat, reroll ones, etc
def roll_stats():
    return sorted([roll('4d6^3t') for _ in range(6)])

# rN rerolls <= n
# ^n keeps highest n
# t total
# s sort
# .+ element-wise addition
