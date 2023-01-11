original_versoin = input().split(".")
original_versoin_dig = [int(num) for num in original_versoin]

original_versoin_dig[-1] += 1
for i in range(len(original_versoin_dig) - 1, -1, -1):
    if original_versoin_dig[i] == 10:
        original_versoin_dig[i] = 0
        if i - 1 >=0:
            original_versoin_dig[i - 1] += 1

    # if original_versoin_dig[-1] == 10:
    #     original_versoin_dig[-1] = 0
    #     original_versoin_dig[-2] += 1
    # if original_versoin_dig[-2] == 10:
    #     original_versoin_dig[-2] = 0
    #     original_versoin_dig[-3] += 1

original_versoin_str = [str(num) for num in original_versoin_dig]
print(".".join(original_versoin_str))

# entry = input().split('.')
# entry_int = [int(i) for i in entry]
# entry_int[2] += 1
# if entry_int[2] == 10:
#     entry_int[2] = 0
#     entry_int[1] += 1
# if entry_int[1] == 10:
#     entry_int[1] = 0
#     entry_int[0] += 1
# print('.'.join(str(i) for i in entry_int))