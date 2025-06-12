#Using built in functions with Lists

#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
print(sum(points))


# Print average points per game
print(sum(points)/sum(games_played))


# Using points data, print best scoring years (Ex: 2004/2005)
max = 2003 + points.index(max(points))
print(f"{max}: {max+1}")


# Using points data, print worst scoring years (Ex: 2004/2005)
min = 2003 + points.index(min(points))
print(f"{min}: {max+1}")

