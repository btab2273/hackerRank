if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# Create a list comprehension
# Remmber [output expression for iterator variable in iterable if predicate expression]
# The output should resemble the combinations from a round-robin parlay

print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if sum([i,j,k]) != n])

# Excellent! The tip about writing my code out on pen and paper first seems to be working well.
# It's easier to catch my mistakes this way
