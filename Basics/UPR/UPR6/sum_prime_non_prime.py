numbers = input()

sum_of_prime = 0
sum_of_nonprime = 0

while numbers != "stop":
    curent_numbber = int(numbers)
    if curent_numbber < 0:
        print(f"Number is negative.")

    else:
        num_is_prime = True
        for number in range (2, curent_numbber):
            if curent_numbber % number == 0:
                num_is_prime = False
                break
        if num_is_prime:
            sum_of_prime += curent_numbber
        else:
            sum_of_nonprime += curent_numbber

    numbers = input()
print(f"Sum of all prime numbers is: {sum_of_prime}")
print(f"Sum of all non prime numbers is: {sum_of_nonprime}")