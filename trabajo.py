'''elabore un algoritmo que muestre la factura de las siguiente compra el señor pedro ramirez compro en fallabela dos jeans 
de 125.000 pesos cada uno, 2 camisas de 45.000 pesos cada una, una camisa tipo polo por 30.000 pesos. 
tener en cuenta lo siguiente: 
si la compra lleva camisa tipo polo tiene un descuento del 5% 
si la compra es superior a 200.000 pesos se realiza un descuento del 30%.
mostrar el total a pagar y el total de ahorro en pesos '''


jeans= 250.000 
jean= 125.000 
camisas= 90.000
camisa=45.000
camisa_polo= 30.000
total= 370.000

descuento = int (input("tiene camisa tipo polo? 1 para si // 2 para no"))

if descuento == 1:
    total1 = total - 0.5 
    
    if total1 >= 200.000:
        total2 = total1 - 0.30
        print("precio inicial", total)
        print("precio a con descuento:", total2)
else:
    if total >= 200.000:
        total3 = total - 0.30
        print("precio inicial", total)
        print("precio con descuento ", total3)
        
    else:
        print("no tiene descuento valor a pagar:" , total )
