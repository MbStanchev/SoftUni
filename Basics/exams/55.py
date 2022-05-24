base_camp = 5364
everest = 8848

days = 1

while True:
    night = input()
    if night == "Yes":
        days += 1
    if days > 5 or night == "END":
        break
    meters = int(input())
    base_camp += meters
    if base_camp >= everest:
        break

if base_camp >= everest:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!\n"
          f"{base_camp}")