class Party():

    def __init__(self):
        self.people = []
party = Party()
counter = 0
while True:
    line = input()
    if line == 'End':
        break
    party.people.append(line)
    counter += 1
print(f"Going: {', '.join(party.people)}")
print(f"Total: {counter}")