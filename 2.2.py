#   i       00101011
#   ii      10000011
#   iii     11000011
#   iv      11010011

m = 0b11111110
k = 0b11010101
n = 8


def cifras_sustituicao_bytes(byte: int, key: int, n: int):
    mask = int('1'*n, 2)

    cifra_byte = 0
    for i in range(8//n):
        # * Shift right to apply mask
        masked_byte = byte >> i*n
        masked_key = key >> i*n

        masked_result = (masked_byte + masked_key) & mask

        # * Shift left to build cifra_byte
        cifra_byte += masked_result << i*n

    # * Convert to binary, remove '0b' and add 0's until 8 bits
    return bin(cifra_byte).removeprefix('0b').rjust(8, '0')


print(cifras_sustituicao_bytes(m, k, n))
