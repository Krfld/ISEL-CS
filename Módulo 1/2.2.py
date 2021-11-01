def cifras_sustituicao_bytes(byte: int, key: int, n: int):
    # Create mask with sum block size
    mask = int('1'*n, 2)

    # Loop each sum block
    cifra_byte = 0
    for i in range(8//n):
        # Shift right to sum and apply mask
        masked_byte = byte >> i*n
        masked_key = key >> i*n

        # Apply mask on each sum block
        masked_result = (masked_byte + masked_key) & mask

        # Shift left to build cifra_byte
        cifra_byte += masked_result << i*n

    # Convert to binary, remove '0b' and add 0's until 8 bits
    return bin(cifra_byte).removeprefix('0b').rjust(8, '0')

#
# Testes
#


M = 0b11111110
K = 0b11010101

# i     00101011
print(cifras_sustituicao_bytes(M, K, 1))
assert cifras_sustituicao_bytes(M, K, 1) == '00101011'

# ii    10000011
print(cifras_sustituicao_bytes(M, K, 2))
assert cifras_sustituicao_bytes(M, K, 2) == '10000011'

# iii   11000011
print(cifras_sustituicao_bytes(M, K, 4))
assert cifras_sustituicao_bytes(M, K, 4) == '11000011'

# iv    11010011
print(cifras_sustituicao_bytes(M, K, 8))
assert cifras_sustituicao_bytes(M, K, 8) == '11010011'


# EX 1  00010011
print(cifras_sustituicao_bytes(0b10101110, 0b01110101, 4))
assert cifras_sustituicao_bytes(0b10101110, 0b01110101, 4) == '00010011'

# EX 2  00100011
print(cifras_sustituicao_bytes(0b10101110, 0b01110101, 8))
assert cifras_sustituicao_bytes(0b10101110, 0b01110101, 8) == '00100011'
