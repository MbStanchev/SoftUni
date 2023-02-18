from collections import deque

sequence_textile = deque([int(x) for x in input().split()])
sequence_medicaments = [int(x) for x in input().split()]

aptechka = {}

while sequence_textile and sequence_medicaments:
    current_textil = sequence_textile.popleft()
    current_medicament = sequence_medicaments.pop()
    result = current_medicament + current_textil

    if result == 30:
        if "Patch" not in aptechka.keys():
            aptechka["Patch"] = 0
        aptechka["Patch"] += 1

    elif result == 40:
        if "Bandage" not in aptechka.keys():
            aptechka["Bandage"] = 0
        aptechka["Bandage"] += 1

    elif result >= 100:
        if "MedKit" not in aptechka.keys():
            aptechka["MedKit"] = 0
        aptechka["MedKit"] += 1

        if result > 100:
            if sequence_medicaments:
                leftover = result - 100
                el = sequence_medicaments.pop()
                el = el + leftover
                sequence_medicaments.append(el)
                # sequence_medicaments[-1] += leftover
    else:
        sequence_medicaments.append(current_medicament + 10)

aptechka = sorted(aptechka.items(), key=lambda x: (-x[1], x[0]))
sequence_medicaments = sorted(sequence_medicaments, reverse=True)
# sequence_textile = sorted(sequence_textile, reverse=True)


if not sequence_textile and sequence_medicaments:
    print("Textiles are empty.")


elif not sequence_medicaments and sequence_textile:
    print("Medicaments are empty.")

if not sequence_textile and not sequence_medicaments:
    print("Textiles and medicaments are both empty.")

if aptechka:
    for item, value in aptechka:
        print(f'{item} - {value}')

if sequence_textile:
    print(f"Textiles left: {', '.join(str(x) for x in sequence_textile)}")

if sequence_medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in sequence_medicaments)}")