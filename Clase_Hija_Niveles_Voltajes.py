from Clase_base_MonitoreoDeCargas import MonitoreoDeCargas

class NivelesVoltaje(MonitoreoDeCargas):
    # Clase hija encargada exclusivamente del registro de voltajes
    def registrar_niveles(self):
        niveles_voltaje = []
        print("\n--- Registro de niveles de voltajes ---")
        for i in range(2):
            filas = []
            for j in range(2):
                while True:
                    try:
                        valor = int(input(f"Ingrese voltaje para fase y posición [{i + 1}, {j + 1}]: "))
                        filas.append(valor)
                        break
                    except ValueError:
                        print("Error intenete con un número entero válido")
            niveles_voltaje.append(filas)
        
        print("\nMatriz de niveles de voltaje:")
        for fila in niveles_voltaje:
            print(fila)
        
        return niveles_voltaje

