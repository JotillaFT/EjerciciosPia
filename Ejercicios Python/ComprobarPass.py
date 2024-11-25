if __name__=="__main__":
    psw="omnimon"
    userpsw=input("Introduce la contraseña\n").lower()
    success=0
    while(success==0):
        if(psw==userpsw):
            print("Contraseña correcta")
            success=1
        else:
            userpsw=input("Contraseña incorrecta, intentelo de nuevo\n").lower()