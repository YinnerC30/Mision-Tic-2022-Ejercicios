def AutoPartes(ventas: list): 
    nuevodiccionario = {}
    for idProducto, dProducto, pnProducto, cvProducto,sProducto,nComprador, cComprador, fVenta in ventas:
        if nuevodiccionario.get(idProducto) == None:
            nuevodiccionario[idProducto] = []
        nuevodiccionario[idProducto].append((dProducto,pnProducto,cvProducto,sProducto,nComprador,cComprador,fVenta))
    return nuevodiccionario

def consultaRegistro(ventas, idProducto):
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto,sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print("Producto consultado :",idProducto," Descripción ",dProducto," #Parte ", pnProducto, " Cantidad vendida ", cvProducto, " Stock ", sProducto, " Comprador",nComprador, " Documento ", cComprador, " Fecha Venta ", fVenta)
    else:
        print("No hay registro de venta de ese producto")
        