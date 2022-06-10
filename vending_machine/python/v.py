lista_prod	  = [ 
#		  prod	  prec stock
		["coca"  ,100,	 4] ,
		["seven" ,232,	 1] ,
		["fanta" ,300,	 2] ,
		["pepsi" ,200,	 3] ,
		]

def main():
		producto_deseado = input("ingrese el producto deseado: ")
		cantidad_deseada = int ( input("ingrese la cantidad deseado: "))

		for producto_stock in lista_prod:
			if(producto_deseado == producto_stock[ 0 ]):
				print("la",producto_stock[ 0 ],"vale", producto_stock [ 1 ], "total",cantidad_deseada*producto_stock[ 1 ])
				pago   = int(input("ingrese el pago: "))
				vuelto = pago - producto_stock[1]*cantidad_deseada
				print("su vuelto es: ",vuelto , ". Muchas gracias por su compra" )
				return
		print("producto no encontrado")

		return


if __name__=='__main__':
   while True:
		main()

