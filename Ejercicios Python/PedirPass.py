if __name__=="__main__":
    contraseña=input("Introduce una contraseña\n")
    user=True
    while user:
        usrpass=input("Te sabes tu contraseña?\n")
        if usrpass==contraseña:
            print("Yey te la sabes")
            user=False
        else:
            print("ERROOOOOOOR")