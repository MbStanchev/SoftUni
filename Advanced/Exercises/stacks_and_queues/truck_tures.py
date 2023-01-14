from collections import deque
num_petrol_pumps = int(input())
gas_tank = 0
list_of_gas_stations = deque()
station_num = 0
ok = False
for _ in range(num_petrol_pumps):
    info = [int(x) for x in input().split()]
    list_of_gas_stations.append(info)

for attempt in range(num_petrol_pumps):
    current_pump = list_of_gas_stations[0]
    for litters, distanse in list_of_gas_stations:
        gas_tank += litters

        if gas_tank < distanse:
            station_num += 1
            list_of_gas_stations.append(list_of_gas_stations.popleft())
            ok = False
            gas_tank = 0
            break
        else:
            gas_tank -= distanse
            ok = True

print(station_num)
# #
# for attempt in range(num_petrol_pumps):
#     gas_tank = 0
#     filed = False
#     for fuel, distanse in list_of_gas_stations:
#         gas_tank += fuel
#
#         if distanse > gas_tank:
#             filed = True
#             break
#         else:
#             gas_tank -= distanse
#     if filed:
#         list_of_gas_stations.append(list_of_gas_stations.popleft())
#     else:
#         print(attempt)
#         break