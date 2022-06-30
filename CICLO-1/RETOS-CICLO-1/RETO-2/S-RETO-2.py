def cliente (informacion: dict):
        
    if informacion['edad'] > 18:
        apto = True
        atraccion = 'X-Treme'        
        if informacion['primer_ingreso'] == True:
            descuento = 20000 * 0.05
            total_boleta = 20000 - descuento
        else:
            total_boleta = 20000
        
    elif informacion['edad'] >= 15 and informacion['edad'] <=18:
        apto = True
        atraccion = 'Carros chocones'        
        if informacion['primer_ingreso'] == True:
            descuento = 5000 * 0.07
            total_boleta = 5000 - descuento
        else:
            total_boleta = 5000
    
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        apto = True
        atraccion = 'Sillas voladoras'        
        if informacion['primer_ingreso'] == True:
            descuento = 10000 * 0.05
            total_boleta = 10000 - descuento
        else:
            total_boleta = 10000
    else:
        apto = False
        atraccion = 'N/A'
        total_boleta = 'N/A'
        
    mensaje = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion' : atraccion,
        'apto' : apto,
        'primer_ingreso' : informacion['primer_ingreso'],
        'total_boleta' : total_boleta
        }
        
    return mensaje
