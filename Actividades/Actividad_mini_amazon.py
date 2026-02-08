
# =============================
# DATOS INICIALES (enunciado)
# =============================
CATALOGO = {
    "A001": {"nombre": "Teclado Mecánico", "precio": 49.99, "stock": 10, "peso_kg": 0.9},
    "A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
    "A003": {"nombre": "Monitor 24\"", "precio": 149.00, "stock": 3, "peso_kg": 3.5},
    "A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
    "A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
    "ENVIOFREE": {"tipo": "envio", "descuento": 1.0},
    "DESC10": {"tipo": "total", "descuento": 0.10},
}

PEDIDOS = [] # Lista para guardar pedidos confirmados o cancelados

# =============================
# PARTE 2: FUNCIONES OBLIGATORIAS
# (definidas aquí para ser usadas en el menú)
# =============================

# 1. mostrar_catalogo(catalogo)
def mostrar_catalogo(catalogo):
    print("\n--- CATÁLOGO ---")
    for codigo, info in catalogo.items():
        print(f"[{codigo}] {info['nombre']} - {info['precio']}€ (Stock: {info['stock']})")

# 2. validar_codigo_producto(catalogo, codigo) -> bool (usar for-else)
def validar_codigo_producto(catalogo, codigo):
    # REQUISITO: Usar for-else para buscar
    for key in catalogo:
        if key == codigo:
            return True
            break
    else:
        # Se ejecuta si el for termina sin encontrar nada
        return False

# 3. agregar_al_carrito(...)
def agregar_al_carrito(carrito, catalogo, codigo, cantidad):
    stock_disponible = catalogo[codigo]["stock"]
    
    # Validamos si ya tenemos algunos en el carrito para no pasarnos
    en_carrito = carrito.get(codigo, 0)
    
    if (en_carrito + cantidad) <= stock_disponible:
        carrito[codigo] = en_carrito + cantidad
        print(f"-> Añadido: {cantidad} unidades de {catalogo[codigo]['nombre']}")
    else:
        print(f"ERROR: No hay suficiente stock. Disponibles: {stock_disponible}")

# 5. calcular_envio(peso_total, zona="PENINSULA")
def calcular_envio(peso_total, zona="PENINSULA"):
    precio_base = 5.0
    return precio_base + (peso_total * 2)

# 6. aplicar_promos(total, envio, *codigos)
def aplicar_promos(total, envio, *codigos):
    # REQUISITO: *codigos permite recibir múltiples argumentos
    descuento_total = 0
    nuevo_envio = envio
    
    print(f"Procesando {len(codigos)} cupón(es)...")
    
    for codigo in codigos:
        if codigo in CODIGOS_PROMO:
            info = CODIGOS_PROMO[codigo]
            if info["tipo"] == "envio":
                nuevo_envio = 0 # Gratis
                print(f"Cupón {codigo} aplicado: Envío GRATIS")
            elif info["tipo"] == "total":
                descuento_total += total * info["descuento"]
                print(f"Cupón {codigo} aplicado: -{info['descuento']*100}%")
    
    return total - descuento_total, nuevo_envio

# 4. calcular_totales(carrito, catalogo, iva=0.21) -> dict
def calcular_totales(carrito, catalogo, iva=0.21):
    subtotal = 0
    peso_total = 0
    
    for codigo, cantidad in carrito.items():
        item_data = catalogo[codigo]
        subtotal += item_data["precio"] * cantidad
        peso_total += item_data["peso_kg"] * cantidad
        
    impuestos = subtotal * iva
    total = subtotal + impuestos
    
    return {
        "subtotal": subtotal,
        "iva": impuestos,
        "total": total,
        "peso": peso_total
    }

# ==========================================
# PARTE 1: MAIN Y MENÚ INTERACTIVO
# ==========================================
def main():
    carrito = {} # Diccionario vacío para el carrito
    program_active = True # Variable de control para el while
    
    # REQUISITO: Bucle while principal
    while program_active:
        print("\n" + "="*30)
        print(" AMAZON LITE - MENÚ")
        print("="*30)
        print("1. Ver catálogo")
        print("2. Añadir producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Ver carrito")
        print("5. Confirmar pedido (PARTE 3)")
        print("0. Salir")
        
        opcion = input("\nElige opción: ")
        
        if opcion == "1":
            mostrar_catalogo(CATALOGO)
            
        elif opcion == "2":
            mostrar_catalogo(CATALOGO)
            codigo = input("Código producto: ").upper()
            if validar_codigo_producto(CATALOGO, codigo):
                try:
                    cant = int(input("Cantidad: "))
                    agregar_al_carrito(carrito, CATALOGO, codigo, cant)
                except ValueError:
                    print("Error: Introduce un número.")
            else:
                print("Producto no encontrado.")
                
        elif opcion == "3":
            codigo = input("Código a borrar: ").upper()
            if codigo in carrito:
                del carrito[codigo]
                print("Eliminado.")
            else:
                print("No está en el carrito.")

        elif opcion == "4":
            if not carrito:
                print("Carrito vacío.")
            else:
                totales = calcular_totales(carrito, CATALOGO)
                print(f"Productos en cesta: {carrito}")
                print(f"Subtotal+IVA: {totales['total']:.2f}€")

        # ==========================================
        # PARTE 3: CONFIRMACIÓN DEL PEDIDO
        # ==========================================
        elif opcion == "5":
            if not carrito:
                print("No puedes confirmar un carrito vacío.")
                continue # REQUISITO: Uso de continue
            
            # Cálculos previos
            datos = calcular_totales(carrito, CATALOGO)
            coste_envio = calcular_envio(datos["peso"])
            total_pedido = datos["total"]
            
            print(f"\nResumen: Productos ({total_pedido:.2f}€) + Envío ({coste_envio:.2f}€)")
            
            # Preguntar cupones
            tiene_promo = input("¿Tienes código promo? (s/n): ").lower()
            if tiene_promo == 's':
                cods = input("Introduce códigos separados por espacio: ").upper().split()
                # REQUISITO: Uso de * para pasar argumentos variables a la función
                total_pedido, coste_envio = aplicar_promos(total_pedido, coste_envio, *cods)
                
            total_final = total_pedido + coste_envio
            print(f"TOTAL FINAL A PAGAR: {total_final:.2f}€")
            
            accion = input("¿Confirmar compra? (CONFIRMAR/CANCELAR): ").upper()
            
            if accion == "CONFIRMAR":
                # Restar stock real
                for cd, qty in carrito.items():
                    CATALOGO[cd]["stock"] -= qty
                
                PEDIDOS.append({"estado": "CONFIRMADO", "total": total_final})
                print("¡Compra completada!")
                carrito = {} # Limpiar carrito
                
            else:
                PEDIDOS.append({"estado": "CANCELADO", "total": total_final})
                print("Compra CANCELADA.")

        elif opcion == "0":
            # REQUISITO: Cambiamos flag a False para terminar el while ordenadamente
            # y que así se ejecute la PARTE 4 (que está en el 'else' del while)
            program_active = False 
            
        else:
            print("Opción incorrecta.")

    # ==========================================
    # PARTE 4: INFORME FINAL (Usando while-else)
    # ==========================================
    else:
        # Este código se ejecuta SOLO cuando el while termina sus vueltas (program_active = False)
        # y NO se ha usado 'break'.
        print("\n" + "*"*30)
        print(" INFORME DE CIERRE DE SESIÓN")
        print("*"*30)
        
        confirmados = [p for p in PEDIDOS if p["estado"] == "CONFIRMADO"]
        cancelados = [p for p in PEDIDOS if p["estado"] == "CANCELADO"]
        
        print(f"Pedidos Confirmados: {len(confirmados)}")
        print(f"Pedidos Cancelados: {len(cancelados)}")
        
        # REQUISITO: mensaje usando for-else si no hubo ventas
        print("\nBuscando ventas destacadas...")
        for pedido in confirmados:
            if pedido["total"] > 1000:
                print(f"¡Venta grande!: {pedido['total']}€")
                break
        else:
            # Se ejecuta si terminamos de revisar todos los pedidos y ninguno cumplió la condición
            print("No hubo ventas superiores a 1000€ en esta sesión.")

if __name__ == "__main__":
    main()
