c0 = int(input('Digite um número: '))

steps = 0

print(c0)
while c0 != 1:
    if c0 % 2 == 0: 
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1
print(f"steps = {steps}")
