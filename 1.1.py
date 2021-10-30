import math

#   i   AENDBROAASDSTAETASSELTFRHEIMARLOCAAPOLDIMUELOGIASARSPRO
#   ii  AMEDRPBOREOIASASDLTPLFAAAEUISSLRGLTHSAAEAARDRCSNEMOTOIO

TEXTO_CLARO = 'abatalhacomospersasteralugarnodesfiladeirodastermopilas'
ESPESSURA = 6


def citala_espartana(texto_claro: str, n: int):
    # * Verificar espessura da cítala
    if n < 2:
        return 'Espessura da cítala incorreta'

    # * Remover espaços e converter para maiúsculas
    texto_claro = texto_claro.replace(' ', '').upper()

    texto_claro_size = len(texto_claro)
    citala_size = math.ceil(texto_claro_size/n)

    texto_cifrado = ''
    for i in range(citala_size):
        for j in range(n):
            k = i + j * citala_size
            if k < texto_claro_size:
                texto_cifrado += texto_claro[k]

    return texto_cifrado


print(citala_espartana(TEXTO_CLARO, ESPESSURA))
