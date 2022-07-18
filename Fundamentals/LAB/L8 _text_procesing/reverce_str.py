command = input()
revercer = ''
while command != 'end':
    # for i in range(len(command)-1, -1, -1):
    #     revercer += command[i]
    #
    # print(f'{command} = {revercer}')
    # revercer = ''
    # command = input()
    revercer = command[::-1]
    print(revercer)
    command=input()