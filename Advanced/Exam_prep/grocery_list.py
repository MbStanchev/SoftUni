def shop_from_grocery_list(budget, *args):
    shopping_list = list(args[0])
    item_prices = args[1:]
    bought_items = []
    while True:
        for key_val in item_prices:
            if key_val[0] in shopping_list:
                if key_val[0] in bought_items:
                    continue
                if budget >= key_val[1]:
                    budget -= key_val[1]
                    shopping_list.remove(key_val[0])
                    bought_items.append(key_val[0])
                else:
                    break
        if len(shopping_list) == 0:
            result = f"Shopping is successful. Remaining budget: {budget:.2f}."
        else:
            result = f"You did not buy all the products. Missing products: {', '.join(shopping_list)}."
        return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))



