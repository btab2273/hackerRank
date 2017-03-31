# h/t to Runcy Oommen roommen https://github.com/roommen
# I wouldn't have understood this without your code
n = int(input())

name_numbers = [input().split() for _ in range(n)]

#Create a dictionary: phone_book
phone_book = {k: v for k, v in name_numbers}

while True:
    name = input()
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')
