def calcular_dia_nacimiento(fechan: str):
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
    print(A)
    
    # Hallo B
    B = (año * 0.25) + año
    print(B)
    
    # Hallo C
    C = 0
    if año % 4 == 0 or año == 0:
        C = 0
    if mes == 2 or mes == 1:
        C = -1
        
    print(C)
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
    print(D)
    # Hallo E
    E = dia
    print(E)
    # Hallo R
    
    R = (A + B + C + D + E) % 7
    
    print(R)
    print(type(R))
    
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
    
print(calcular_dia_nacimiento("2005-02-28"))


