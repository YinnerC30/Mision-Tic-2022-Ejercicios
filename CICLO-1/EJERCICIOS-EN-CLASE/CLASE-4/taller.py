def ejercicio_1(nombre: str):
    return f"¡hola {nombre}!"

def ejercicio_2(numero: int):
    import math
    return f"El factorial del numero {numero} es {math.factorial(numero)}"

def ejercicio_3(cantidad: int, iva = 19.0):
    iva2 = iva / 100
    return f"El total de la factura es de {cantidad + (cantidad * iva2)} incluido un iva del {iva} porciento"

def ejercicio_4(radio: float):
    import math
    area = math.pi * radio ** 2
    return round(area,2)

def ejercicio_4_1(funcion: float, altura: float):
    volumen = funcion * altura
    return f"El volumen del cilindro seria de {round(volumen,2)}"

def ejercicio_5(numero: int):
    suma = (numero * ( numero + 1 )) / 2
    return f"La suma del numero entero {numero} es de {round(suma)}"

def ejercicio_6(peso: float, estatura: float):
    imc = peso / (estatura ** 2)
    return f"El indice de masa corporal IMC de la persona es de {round(imc,2)}"

def ejercicio_7(numero_payasos: int,numero_muñecas: int):
    peso_payaso, peso_muñeca = 112,75
    peso_paquete = (peso_payaso * numero_payasos) + (peso_muñeca * numero_muñecas)
    peso_kilos = peso_paquete / 1000
    return f"El peso del paquete seria de {peso_paquete} gramos o {round(peso_kilos,2)} kilogramos"
    
def ejercicio_8(numero_barras_viejas: int):
    precio_pan_regular = 3.49
    descuento = 0.6
    valor_pan_regular = precio_pan_regular * numero_barras_viejas
    pan_descuento = (descuento * valor_pan_regular)
    valor_pan_descuento = valor_pan_regular - pan_descuento
    return f"El pan regularmente tendria un precio de {round(valor_pan_regular,2)} \nEl pan tuvo un descuento de {round(pan_descuento,2)} \nfinalmente el pan se vendio por {round(valor_pan_descuento,2)}"
    

def ejercicio_9(cantidad: int):
    interes = 0.04
    primer_año = cantidad + (cantidad * interes)
    segundo_año = primer_año + (primer_año * interes)
    tercer_año = segundo_año + (segundo_año * interes)
    return f"El usuario tiene en total en su primer año una cantidad de {round(primer_año,1)} con intereses\nEl usuario tiene en total en su segundo año una cantidad de {round(segundo_año,1)} con intereses \nEl usuario tiene en total en su tercer año una cantidad de {round(tercer_año,1)} con intereses"
    
def ejercicio_10(cantidad: int):
    dias = cantidad // 84600
    restante = cantidad % 84600
    horas = restante // 3600
    restante =  restante % 3600
    minutos = restante // 60
    segundos = restante % 60
    return f"{cantidad} segundos serian {dias} dias, {horas} horas , {minutos} minutos y {segundos} segundos"

    
