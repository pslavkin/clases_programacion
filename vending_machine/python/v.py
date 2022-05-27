lista_prod    = ["coca" ,"pepsi" ,"fanta", "dksj"]
lista_precios = [100    ,200     ,300    , 232]

def main():

        print("ingrese el producto deseado: ")
        producto_deseado = input()
        print("ingrese la cantidad deseado: ")
        cantidad_deseada = int(input())

        apuntador=0

        for producto_stock in lista_prod:
            if(producto_deseado==producto_stock):
                print("la",producto_stock,"vale", lista_precios[apuntador], "total",cantidad_deseada*lista_precios[apuntador])
                print("ingrese el pago")
                pago   = int(input())
                vuelto = pago-lista_precios[apuntador]
                print("su vuelto es: ",vuelto)
                print("muchas gracias por su compra")
                return
            else:
                apuntador+=1

        return


if __name__=='__main__':
    while(1):
        main()



