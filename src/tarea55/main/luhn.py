def luhn(numero):
    numero = numero.replace(" ", "")
    if len(numero) > 2:
        sumatorioMultiplos = 0
        invNumero = numero[::-1]
        numMult = invNumero[1::2]
        numSum = invNumero[0::2]
        numerosSumar = [int(numero) for numero in numSum]
        sumatorio = sum(numerosSumar)
        multiplos = [int(numero) for numero in numMult]
        for num in multiplos:
            num = num * 2
            if num > 9:
                num = num - 9
            sumatorioMultiplos += num
        total = sumatorio + sumatorioMultiplos
        return total % 10 == 0
    else:
        return False