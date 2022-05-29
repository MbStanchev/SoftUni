year = int(input())

happy_year = False
while not happy_year:
    result = set()
    year += 1
    happy = str(year)
    for i in happy:
        result.add(i)

    happy_year = len(str(year)) == len(result)
print(year)

# year = int(input())
# for i in range(len(str(year))):
#     print(str(year)[i])