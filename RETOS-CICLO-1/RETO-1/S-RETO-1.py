def CDT (usuario : str , capital : int , tiempo : int):
    """
    CDT
    Calculador del valor de los intereses ganados o perdidos y el total final de dinero para diferentes clientes.
    
    Parametros:
    - usuario : identifica el nombre del usuario.
    - capital : identifica la cantidad de dinero a consultar.
    - tiempo: identifica la cantidad de tiempo de duración del CDT.
    
    Retorna:
    El nombre del usuario, la cantidad de dinero a recibir segun el monto inicial, acompañado de la cantidad de tiempo de duración que tuvo el CDT.
    """
    porcentaje_interes = 0.03
    porcentaje_perdida = 0.02
    if tiempo > 2:
        valor_intereses = (capital * porcentaje_interes * tiempo)/12
        valor_total = capital + valor_intereses
    else:
        valor_perder = capital * porcentaje_perdida
        valor_total = capital - valor_perder 
    return (f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}")
