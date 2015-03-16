# What I did was take all the numbers in the result of 2**1000 as characters
# Convert them back to an int and add them to a list.
# I know it's wasteful to do two conversions but this seemed the easiest.

sum([int(x) for x in str(2**1000)])
