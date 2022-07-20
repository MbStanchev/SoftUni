entry = input().split('\\')
extention = entry[-1].split('.')
print(f'File name: {extention[0]}')
print(f'File extension: {extention[1]}')