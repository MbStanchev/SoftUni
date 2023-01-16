n = int(input())
username = set()
for _ in range(n):
    name = input()
    username.add(name)
for name in username:
    print(f'{name}')