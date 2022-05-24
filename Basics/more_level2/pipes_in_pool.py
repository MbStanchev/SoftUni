v = int(input())
p1 = int(input())
p2 = int(input())
n = float(input())

fill_p1 = p1 * n
fill_p2 = p2 * n

fill_volium = fill_p2 + fill_p1

pool_filed_total = fill_volium / v * 100

pool_fild_by_p1 = fill_p1 / fill_volium * 100
pool_fild_by_p2 = fill_p2 / fill_volium * 100

difference = fill_volium - v

if v >= fill_volium:
    print(f"The pool is {pool_filed_total}% full. Pipe 1: {pool_fild_by_p1}%. Pipe 2: {pool_fild_by_p2}%.")

else:
    print(f"For {n} hours the pool overflows with {difference} liters.")