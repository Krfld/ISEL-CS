# 16 -> 4 bit
s = 16
n = 4
l = s - n


def hash_MD_funcaof(m: str, H0: str):
    H = H0
    blocks = len(m) // l

    # Split 'm' into blocks
    mi = [m[i*l:i*l+l] for i in range(blocks+1)]

    # Add OneZerosPadding
    mi[blocks] += '1'
    mi[blocks] = mi[blocks].ljust(l, '0')

    # Add bloco de comprimento
    mi += [bin(l).removeprefix('0b').rjust(l, '0')]

    # Apply 'f'
    for m in mi:
        # Split each 'm' into blocks of 4 bits
        B = [(H + m)[i*4:i*4+4] for i in range(4)]

        # Sum each block
        for i in range(3):
            B[i+1] = bin(int(B[i], 2)+int(B[i+1], 2)).removeprefix('0b')[-4:]

        # Update next H
        H = B[3]

    return H0.rjust(4, '0')


m = '010101010101010000'
H0 = '1000'

hash_MD_funcaof(m, H0)
