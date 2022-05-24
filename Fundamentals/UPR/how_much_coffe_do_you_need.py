entry = input()
num_coffies = 0
while entry != "END":
    ok_list = ["coding","dog", "cat", "movie"]
    if entry.lower() in ok_list:
        if entry == entry.lower():
            num_coffies += 1
        elif entry == entry.upper():
            num_coffies += 2
    else:
        pass
    entry = input()
if num_coffies > 5:
    print("You need extra sleep")
else:
    print(num_coffies)