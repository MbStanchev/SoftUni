name_of_searched_book = input()
name_of_found_book = input()
out_of_books = False
counter = 0
while name_of_searched_book != name_of_found_book:
    if name_of_found_book == "No More Books":
        out_of_books = True
        break

    counter += 1
    name_of_found_book = input()

if out_of_books == True:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter} books and found it.")
