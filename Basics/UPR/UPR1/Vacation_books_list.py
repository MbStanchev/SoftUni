count_of_pages_in_book = int(input())
number_of_pages_per_hour = int(input())
count_of_days = int(input())
total_hours = count_of_pages_in_book // number_of_pages_per_hour / count_of_days
print(total_hours)