nub_of_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all_turist = 0
members_in_group = 0
for i in range (nub_of_groups):
    nub_of_members_in_group = int(input())

    all_turist += nub_of_members_in_group

    if nub_of_members_in_group <= 5:
        musala += nub_of_members_in_group
    elif nub_of_members_in_group <= 12:
        monblan += nub_of_members_in_group
    elif nub_of_members_in_group <= 25:
        kilimandjaro += nub_of_members_in_group
    elif nub_of_members_in_group <= 40:
        k2 += nub_of_members_in_group
    else:
        everest += nub_of_members_in_group
for_peak_musala = musala / all_turist * 100
for_peak_monblan = monblan / all_turist * 100
for_peak_kilimanjaro = kilimandjaro / all_turist * 100
for_peak_k2 = k2 / all_turist * 100
for_peak_everest = everest / all_turist * 100

#print(all_turist)
print(f"{for_peak_musala:.2f}%")
print(f"{for_peak_monblan:.2f}%")
print(f"{for_peak_kilimanjaro:.2f}%")
print(f"{for_peak_k2:.2f}%")
print(f"{for_peak_everest:.2f}%")
