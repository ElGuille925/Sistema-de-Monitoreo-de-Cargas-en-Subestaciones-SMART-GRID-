from Clase_base_MonitoreoDeCargas import MonitoreoDeCargas

class HistorialCorriente(MonitoreoDeCargas):
    # Clase hija encargada del registro del historial de corriente
    def registrar_historial(self):
        print("\n--- Registro de historial de corriente ---") 
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de registros de corriente que desee evaluar: "))
                break
            except ValueError:
                print("Error intente con un número válido")
        
        historial = []
        for i in range(cantidad):
            while True:
                try:
                    valor = int(input(f"Historial de corriente {i + 1}: "))
                    historial.append(valor)
                    break
                except ValueError:
                    print("Error intente con un número válido.")
            
        print("\nHistorial de corriente:")
        print(historial)
        
        return historial
