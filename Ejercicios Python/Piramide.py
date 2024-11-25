if __name__=="__main__":
    n = input("Como de grandes quiere las piramides\n")
    n = int(n)
    piramide=''
    piso=''
    for a in range(n+1):
        for b in range(a):
            piso+='*'
        piramide+=piso+'\n'
        piso=''
    print(piramide)