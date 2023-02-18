def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    bucket = set()
    bought = []
    for k, v in kwargs.items():
        if len(bucket) == 5:
            break
        product = k
        price, quant = v
        total_price = price * quant
        if budget >= total_price:
            bucket.add(product)
            bought.append(f"You bought {product} for {total_price:.2f} leva.")
            budget -= total_price

    return "\n".join(bought)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
