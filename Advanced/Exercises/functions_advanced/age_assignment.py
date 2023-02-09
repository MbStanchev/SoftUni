def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for letter in kwargs:
            if name.startswith(letter):
                result[name] = kwargs[letter]
    sorted_res = dict(sorted(result.items(), key=lambda x: x[0]))
    ss = ''
    for names, age in sorted_res.items():
        ss += f'{names} is {age} years old.' + '\n'
    return ss




print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))