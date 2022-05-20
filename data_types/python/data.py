def coca():
    costo=150
    print("la coca vale: ",costo)
    print("ingrese el pago")
    pago=int(input())
    vuelto=pago-costo
    print("su vuelto es: ",vuelto)
    print("muchas gracias por su compra")

def pepsi():
    costo=130
    print("la pepsi vale: ",costo)
    print("ingrese el pago")
    pago=int(input())
    vuelto=pago-costo
    print("su vuelto es: ",vuelto)
    print("muchas gracias por su compra")


def main():
    while True:
#    for i in range(3):
        print("ingrese el producto deseado: ")
        producto = input()

        if(producto == "coca"):
            coca()
        else:
            if(producto == "pepsi"):
                pepsi()
            else:
                print("no lo tengo")

    return

























if __name__=='__main__':
    main()


