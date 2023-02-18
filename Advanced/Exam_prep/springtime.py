def start_spring(**kwargs):
    dict_of_stuff = {}
    list_of_stuff = []
    for v, k in kwargs.items():
        if k not in dict_of_stuff:
            dict_of_stuff[k] = []
        dict_of_stuff[k].append(v)
    dict_of_stuff = sorted(dict_of_stuff.items(), key=lambda x: (-len(x[1]), x[0]))
    for k, v in dict_of_stuff:
        list_of_stuff.append(f"{k}:")
        v = sorted(v)
        for stuff in v:
            list_of_stuff.append(f'-{stuff}')
    return '\n'.join(list_of_stuff)


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",
                   }
print(start_spring(**example_objects))
