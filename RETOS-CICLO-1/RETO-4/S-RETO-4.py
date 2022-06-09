def ordenes(rutinaContable):
    from functools import reduce
    
    orden_minima = 600000
    total_cada_tu_li = list(map(lambda z: [z[0]] + list(map(lambda t: t[1]*t[2],z[1:])), rutinaContable))
    
    total_cada_tu_li = list(map(lambda z:[z[0]] + [reduce(lambda a,b: round(a+b,2), z[1:])], total_cada_tu_li))
    
    total_cada_tu_li = list(map(lambda z : z if z [1] >= orden_minima else (z[0] , z[1]+25000), total_cada_tu_li))
    
    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in range(len(total_cada_tu_li)):
        print(f"La factura {total_cada_tu_li[i][0]} tiene un total en pesos de {total_cada_tu_li[i][1]:,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')