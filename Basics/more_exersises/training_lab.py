w = float(input())
h = float(input())
#work_space = 1
#door = work_space
#front_desk = work_space * 2
#path_way = 100 * w
if 3 <= h <= w <= 100:
    count_per_rol = ((h * 100) - 100) // 70
    count_of_rols = (w * 100) // 120
    total_work_spaces = count_of_rols * count_per_rol - 3

    #area = ((w * 100) * (h * 100)) - path_way - door - front_desk
    #total_work_spaces = area // work_space
    print(total_work_spaces)
    #print(count_per_rol)
    #print(count_of_rols)
