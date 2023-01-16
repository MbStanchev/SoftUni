# def append_in_line(num, lin_n):
#     lin_n.
first_set = set()
second_set = set()
first_n, second_n = input().split()


for num in range(int(first_n)):
    first_set.add(int(input()))
for num in range(int(second_n)):
    second_set.add(int(input()))

result = first_set.intersection(second_set)
for i in result:
    print(i)