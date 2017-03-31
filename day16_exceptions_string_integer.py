S = raw_input()

# Use a try-error clause to catch strings that cannot be converted to integers
try:
    print(int(S))
except ValueError:
    print('Bad String')
