a = int(input())
b = int(input())
c = int(input())

# a and c even, b prime

for i in range(2, a + 1, 2):

    for j in range(2, b + 1):

        is_prime = True
        # prime test for j
        if j > 3:
            for p in range(2, j):
                if j % p == 0:
                    # j is not prime
                    is_prime = False
                    break

        if not is_prime:
            continue

        for k in range(2, c + 1, 2):
            print(i, j, k)