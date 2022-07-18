num_of_vehicles = int(input())
parking = {}

for vehicles in range(num_of_vehicles):
    entry = input().split()
    status = entry[0]
    name = entry[1]


    if name not in parking and status == 'register':
        l_plate = entry[2]
        parking[name] = [status,l_plate]
        print(f"{name} registered {l_plate} successfully")

    elif name in parking and status == 'register':
        l_plate = entry[2]
        print(f"ERROR: already registered with plate number {l_plate}")

    elif name not in parking and status == 'unregister':
        print(f"ERROR: user {name} not found")

    elif name in parking and status == 'unregister':
        print(f"{name} unregistered successfully")
        del parking[name]
for k, v in parking.items():
    print(f"{k} => {''.join(v[1])}")


