entry = input().split("|")

sub_entry = []
for el in entry[::-1]:
    sub_entry.extend(el.split())

print(*sub_entry)