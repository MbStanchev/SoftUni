def concatenate(*args, **kwargs):
    expresion = ''.join(args)
    for key, val in kwargs.items():
        if key in expresion:
            expresion = expresion.replace(key, val)
    return expresion


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))