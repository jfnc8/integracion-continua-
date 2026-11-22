# Operación de ejemplo: 8 + 5 debe dar 13
def operacion():
    resultado = 8 + 5
    print(f"Operación: 8 + 5 = {resultado}")
    if resultado == 13:
        print("OK - Resultado correcto")
        return True
    else:
        print("ERROR - Resultado incorrecto")
        return False

if __name__ == "__main__":
    exito = operacion()
    if not exito:
        exit(1)
