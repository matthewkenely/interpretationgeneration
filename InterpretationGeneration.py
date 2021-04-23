from numpy import array, transpose

def generate_interpretations(n, t, b0, b1):
    """
    n: number of elementary propositions
    t: set to 0 for digital logic, 1 for propositional logic (inverts order)
    b0 = !(b1)
    c: number of interpretations
    a: groupings of 0, 1
    b: repetition of groupings
    """
    c = 2**n

    arr = []

    for i in range(n):
        current = []

        a = c // 2**i
        b = 2**i

        for i in range(b):
            for j in range(a):
                if t == 0:
                    current.append(b0) if j < a/2 else current.append(b1)
                else:
                    current.append(b1) if j < a/2 else current.append(b0)

        arr.append(current)

    return transpose(array(arr))

digital = generate_interpretations(4, 0, 0, 1)
propositional = generate_interpretations(4, 1, 'F', 'T')

print('Interpretations:\n', digital, end='\n\n')
print('Line 2:\n', digital[1, :], end='\n\n')
print('Column 1:\n', digital[:, 0])