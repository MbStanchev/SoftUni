tail= input()
body = input()
head = input()

list = [tail, body, head]
list[0], list[-1] = list[-1], list[0]
print(list)
