print("""
# Nombre del grupo(alumnos): Ricardo Avila - Anqi Yang

# Nombre de la empresa: Fashion Style

# Tipo de tienda: Tienda de ropa
""")



# ==================== PARTE 1: INFORMACIÓN DE LA EMPRESA ====================


# Mensaje de bienvenida
print(" ¡Bienvenido a nuestra tienda de Fashion Style !")
print("=" * 50)


# Variables de la empresa
nombre_empresa = "Fashion Style "
anio_fundacion = 2010
ingresos_mensuales = 35000.00 #en euros
es_internacional = True

# Mostrar informacion de la empresa
print(f"Empresa: {nombre_empresa}")
print (f"Año de fundación: {anio_fundacion}")
print (f"Ingresos mensuales promedio: ${ingresos_mensuales: .2f}")
print (f"Tienda Internacional: {'Si' if es_internacional else 'No'}")
print("=" * 50)




# ==================== PARTE 2: DATOS DEL CLIENTE ====================


# Pedir datos al usuario
print("\nPor favor, ingresa tus datos:")
nombre_cliente = input("Nombre: ")
edad_str = input("Edad: ")
producto_deseado = input("Producto que deseas comprar: ")


# Convertir edad a entero
edad = int(edad_str)


# ==================== PARTE 3: OPERADORES ARITMÉTICOS ====================
print("\n" + "=" * 50)
print("CALCULOS Y OPERACIONES")
print("=" * 50)


# Precios de productos
precios_ropa = {
    "camisa": 25,
    "pantalon": 40,
    "vestido": 60,
    "chaqueta": 80,
    "zapatos": 50,
    "sueter": 35,
    "falda": 30,
    "jeans": 45,
    "abrigo": 120,
    "short": 20,
}


# Establecer precio del producto deseado (si no está en la lista, usar un precio base)
if producto_deseado.lower() in precios_ropa:
    precio_base = precios_ropa[producto_deseado.lower()] # Precios de productos

else:
    precio_base = 30 # precio por defecto para productos no listados
    print(f"Producto no en lista, usando precio base de ${precio_base:.2f}")

print(f"\nPrecio base del {producto_deseado}: ${precio_base:.2f}")

# Operadores aritmeticos
cantidad = int(input(f"¿Cuántos {producto_deseado.lower()}s deseas comprar? "))  # Preguntar cantidad
subtotal = precio_base * cantidad  # Multiplicación


# Descuentos por cantidad (usando división entera)
descuento_por_cantidad = (cantidad // 3) * 5  # 5% por cada 3 productos
# O usando módulo para otra promoción
if cantidad % 2 == 0:  # Si la cantidad es par
    print("  ¡Promoción especial! Cantidad par - posible descuento adicional")

iva = subtotal * 0.16  # Multiplicación (16% de IVA)

# Descuentos por edad/estudiante
descuento_estudiante = subtotal * 0.15  # 15% de descuento para estudiantes
descuento_joven = subtotal * 0.10  # 10% de descuento para jóvenes
descuento_adulto_mayor = subtotal * 0.20  # 20% de descuento para adultos mayores


print("\nOperaciones aritméticas: ")
print(f"  Subtotal ({cantidad} unidades): ${subtotal:.2f} (+)")
print(f"  Descuento por cantidad: ${descuento_por_cantidad:.2f} (-)")
print(f"  IVA (16%): ${iva:.2f} (+)")


# ==================== PARTE 4 OPERADORES DE COMPARACIÓN ====================
print(f"\nComparaciones con la edad ({edad} años): ")


# Operadores de comparacion
es_menor = edad < 18
es_joven = edad >= 18 and edad < 25
es_adulto = edad >= 25 and edad < 60
es_adulto_mayor = edad >= 60


print(f"\t¿Es menor de edad? {es_menor}")
print(f"\t¿Es joven (18-24)? {es_joven}")
print(f"\t¿Es adulto (25-59)? {es_adulto}")
print(f"\t¿Es adulto mayor (60+)? {es_adulto_mayor}")


# Comparar precios
precio_alto = precio_base > 70
precio_medio = precio_base >= 30 and precio_base <= 70
precio_bajo = precio_base < 30


print(f"\nComparaciones con el precio (${precio_base:.2f}): ")
print(f"\t¿Precio alto (>$70)? {precio_alto}")
print(f"\t¿Precio medio ($30-$70)? {precio_medio}")
print(f"\t¿Precio bajo (<$30)? {precio_bajo}")




# ==================== PARTE 5: OPERADORES LÓGICOS ====================
print("\nAplicacion de descuentos (operadores logicos): ")


#Operadores logicos para determinar descuentos
descuento_total = descuento_por_cantidad


# preguntar si es estudiante
es_estudiante_input = input("Eres estudiante? (si/no): ").lower()
es_estudiante = es_estudiante_input == "sí" or es_estudiante_input == "si"


# Preguntar si tiene membresía (nuevo para tienda de ropa)
tiene_membresia_input = input("¿Tienes membresía de la tinda? (sí/no): ").lower()
tiene_membresia = tiene_membresia_input == "sí" or tiene_membresia_input == "si"


#Descuento 1: Jovenes o estudiantes
if es_estudiante or es_joven:
  descuento_total += descuento_estudiante
  print("\tDescuento joven/estudiante aplicado: 15%")


#Descuento 2: Adultos Mayores
if es_adulto_mayor:
    descuento_total = descuento_adulto_mayor
    print("\tDescuento adulto mayor aplicado: 20%")


# Descuento por membresía (nuevo)
if tiene_membresia:
    descuento_membresia = subtotal * 0.05  # 5% extra por membresía
    descuento_total += descuento_membresia
    print("\tDescuento por membresía aplicado: 5%")


# Descuento adicional si compra productos caros Y es adulto
if precio_alto and es_adulto and not es_estudiante:
    descuento_extra = subtotal * 0.08  # 8% extra
    descuento_total += descuento_extra
    print("\tDescuento extra por producto premium: 8%")


# ==================== CÁLCULO FINAL ====================


print("\n" + "=" * 50)
print("RESUMEN DE COMPRA")
print("=" * 50)


# Calculo final
subtotal_con_descuento = subtotal - descuento_total
total = subtotal_con_descuento + iva


# Envío gratis para compras mayores a $100 o miembros
envio_gratis = total > 100 or tiene_membresia


# Puntos de fidelidad (usando exponente y división entera)
puntos_base = int(total ** 0.5)  # Raíz cuadrada del total
if tiene_membresia:
    puntos_fidelidad = puntos_base * 2  # Doble puntos para miembros
else:
    puntos_fidelidad = puntos_base


# Usamos módulo para determinar si aplica regalo sorpresa
regalo_sorpresa = total % 50 == 0  # Regalo si total es múltiplo de 50


print(f"Cliente: {nombre_cliente}")
print(f"Edad: {edad} años")
print(f"Producto: {producto_deseado}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: ${descuento_total:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"TOTAL A PAGAR: ${total:.2f}")


print("\nBeneficios adicionales:")
print(f"\t¿Envío gratis? {'Sí' if envio_gratis else 'No'} (costo: $10)")
print(f"\tPuntos de fidelidad obtenidos: {puntos_fidelidad}")
print(f"\t¿Regalo sorpresa? {'¡Sí!' if regalo_sorpresa else 'No'}")
if es_estudiante:
    print("\tDescuento estudiante activo: 15%")
if tiene_membresia:
    print("\tBeneficios de membresía activos")


print(f"\n¡Gracias por tu compra, {nombre_cliente}!")
print(f"Vuelve pronto a, {nombre_empresa} - Tu estilo, nuestra pasion")




# ==================== Parte 6:  ====================


print("\n" + "=" *50)
print("Analisis de cadenas(STRING)")
print("="*50)


frase = input("Escribir un frase para analizar: ")


print("Logitud de la frase: ",len(frase))
print("Primeros 5 caracteres: ",frase[:5])
print("Ultimos 3 caracteres: ",frase[-3:])
print("Cantidad de 'a':",frase.count("a"))
print("Es numero ? ",frase.isnumeric())
print("Esta en MAYUSCULA ?",frase.isupper())
print("En MAYUSCULA: ",frase.upper())
print("En minuscula: ",frase.lower())
print("Capitalizada: ",frase.capitalize())
print("Empieza con 'hola' ? ",frase.lower().startswith("hola"))




# ==================== Parte 7:  ====================


print("\n" + "=" *50)
print("LISTAS DE PRODUCTOS")
print("=" * 50)


productos = ["camisa", "pantalón", "vestido", "chaqueta"]
precio = [25,40,60,80]


print("Lista orriginal de productos : ",productos)
print("Lista original de precio : ",precio)


#Metodos de listos
productos.append("zapatos")
precio.append(50)


productos.insert(1,"falda")
precio.insert(1,30)


productos.remove("vestido")
precio_removed = precio.pop(2)


productos_copia = productos.copy()


productos.reverse()
productos.sort()


print("Productos modificado: ",productos)
print("precio ordenados: ",precio)
print("Copia de productos: ",productos_copia)




# ==================== Parte 8:  ====================


print("\n" + "=" *50)
print("TUPLAS EN LA EMPRESA")
print("=" * 50)


marcas = ("Chanel","Dior","YSL","Chanel")


print("Tupla original: ",marcas)
print("Cantidad de 'Chanel' : ",marcas.count("Chanel"))
print("Indice de 'YSL': ",marcas.index("YSL"))


mercas_extra = marcas + ("Balenciaga", "Gucci")
print("Tupla concatenada: ",mercas_extra)


listas_marcas = list(marcas)
listas_marcas.append("Guess")


tupla_marcas = tuple(listas_marcas)
print("Tupla convertida desde lista:", tupla_marcas)




# ==================== Parte 9:  ====================


print("\n" + "=" * 50)
print("SETS DE CLIENTES")
print("=" * 50)


clientes = {"Anqi", "Cristina", "Ricardo", "Celeste"}


print("Clietes registrados: ",clientes)


clientes.add("Vernon")
clientes.remove("Anqi")


clientes_vip = {"Nana", "Carla"}


print("Union: ", clientes.union(clientes_vip))
print("Deferencia: ",clientes.difference(clientes_vip))
print("¿Ana esta en clientes? ","Ana" in clientes)


clientes.clear()
print("Clientes despues de clear()",clientes)
