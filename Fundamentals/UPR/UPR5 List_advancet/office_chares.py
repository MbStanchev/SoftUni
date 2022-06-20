def is_it_enought(some_number):
    count_all_chairs = 0
    count_all_visitors = 0

    for i in range(number_of_rooms):
        entry = input().split()
        num_of_chairs = len(entry[0])
        num_of_visitors = int(entry[1])
        diff = num_of_visitors - num_of_chairs
        if num_of_chairs < num_of_visitors:
            print(f"{diff} more chairs needed in room {i + 1}")
        count_all_chairs += num_of_chairs
        count_all_visitors += num_of_visitors
    differemce = count_all_chairs - count_all_visitors

    return count_all_chairs, count_all_visitors


number_of_rooms = int(input())

count_all_chairs, count_all_visitors = is_it_enought(number_of_rooms)
if count_all_visitors <= count_all_chairs:
    differemce = count_all_chairs - count_all_visitors
    print(f"Game On, {differemce} free chairs left")