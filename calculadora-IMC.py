def validar_entrada_numerica(mensaje):
    while True:
        try:
            valor_str = input(mensaje).strip()
            # Validación de no estar vacío (ya incluida en el try/except si es solo espacio)
            if not valor_str:
                print(" Error: El dato no puede estar vacío. Inténtalo de nuevo.")
                continue
            
            # Validación de que sea una cifra
            valor = float(valor_str)
            
            # Validación de que sea positivo (edad, peso y estatura deben ser positivos)
            if valor <= 0:
                print(" Error: El valor debe ser una cifra positiva. Inténtalo de nuevo.")
                continue
            
            return valor
        except ValueError:
            print(" Error: Por favor, introduce una cifra válida (número). Inténtalo de nuevo.")

def validar_entrada_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print(" Error: El dato no puede estar vacío. Inténtalo de nuevo.")

def calcular_imc(peso, estatura):

    return round(peso / (estatura ** 2), 2) # redondear a 2 decimales

def main():
    print("Calculadora de Índice de Masa Corporal (IMC)\n")

    # Captura de datos del usuario y Validación
    print("Captura de Datos Personales")
    nombre = validar_entrada_texto("Nombre: ")
    apellido_paterno = validar_entrada_texto("Apellido Paterno: ")
    apellido_materno = validar_entrada_texto("Apellido Materno: ")
    
    # Validaciones específicas para datos numéricos
    edad = int(validar_entrada_numerica("Edad (años): "))
    peso = validar_entrada_numerica("Peso (kg): ")
    estatura = validar_entrada_numerica("Estatura (metros): ")

    # Cálculo del IMC 
    imc = calcular_imc(peso, estatura)

    # Salida de datos 
    print("\n--- Resultados ---")
    print(f" Nombre Completo: {nombre} {apellido_paterno} {apellido_materno}")
    print(f" Edad: {edad} años")
    print(f" Peso: {peso} kg")
    print(f" Estatura: {estatura} m")
    print(f"\n Su Índice de Masa Corporal (IMC) es: {imc}")

if __name__ == "__main__":
    main()