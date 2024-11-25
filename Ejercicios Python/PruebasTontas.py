if __name__ == "__main__":
    Digis = ["Omni","Shine","Beelze","Gallant"]
    Pierde=""
    for Prota in Digis:      
        if Pierde=="": 
            print(f"{Prota} gana ")
            Pierde=Prota
        else:
            print(f"{Prota} le gana a {Pierde}")
            Pierde=Prota
        if Pierde =="Beelze":
            break
    b = 8
    if b == 2:
        print("Omni gana")
    elif b==3:
        print("beelze gana")
    elif b==4:
        print("Cross gana")
    elif b==5:
        print("Galant gana")
    else:
        print("Shine gana")
    a=1
    for a in range(10):
        d=a**a
        print(d)
            
        
        