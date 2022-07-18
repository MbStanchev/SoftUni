entry = input()
dig = ''
let = ''
syn = ''

for i in entry:
    if i.isdigit():
        dig += i
    elif i.isalnum():
        let += i
    else:
        syn += i

print(dig)
print(let)
print(syn)