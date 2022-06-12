def calcular_dia_semana(fechan: str):
    """

    Args:
        fecha (str): Escriba la fecha de nacimiento de la siguiente forma:
        
        AAAA-MM-DD
    """
    
    siglo = int(fechan[0:2])
    año = int(fechan[2:4])
    mes = int(fechan[5:7])
    dia = int(fechan[8:])
    
    print(fechan)
    print("Siglo",siglo)
    print("año",año)
    print("mes",mes)
    print("dia",dia)
    
    # Hallo A
    if siglo == 20:
        pocision = 0
        formula = 0
    elif siglo < 20:
        pocision = 20 - siglo
        formula = (2*pocision) - 1
    elif siglo > 20:
        pocision = siglo - 20
        formula = (-2*pocision)
    
    A = formula
    print("Esta es a",A)
    
    # Hallo B
    B = int((año * 0.25) + año)
    print("Esta es",B)
    
    # Hallo C
    modulo = año % 4
    if modulo == 0 :
        if mes == 2 or mes == 1:
            C = -1
    else:
        C = 0

    print("Esta es c",C)
    
    # print("esta es c",C)
    # Hallo D
    if mes == 1 or mes == 10:
        D = 6
    if mes == 2 or mes == 3 or mes == 11:
        D = 2
    if mes == 4 or mes == 7:
        D = 5
    if mes == 5:
        D = 0
    if mes == 6:
        D = 3
    if mes == 8:
        D = 1
    if mes == 9 or mes == 12:
        D = 4
    print("Esta es d",D)
    
    # Hallo E
    E = dia
    print("Esta es E",E)
    
    # Hallo R
    R = int((A + B + C + D + E) % 7)
    
    print("Esta es R",R)
    # print(type(R))
    
    if R == 0:
        dian = "Domingo"
    if R == 1:
        dian = "Lunes"
    if R == 2:
        dian = "Martes"
    if R == 3:
        dian = "Miercoles"
    if R == 4:
        dian = "Jueves"
    if R == 5:
        dian = "Viernes"
    if R == 6:
        dian = "Sabado"
    
    mensaje = f"Ese día fue {dian}"
    return mensaje
    
print(calcular_dia_semana("2021-02-22"))
