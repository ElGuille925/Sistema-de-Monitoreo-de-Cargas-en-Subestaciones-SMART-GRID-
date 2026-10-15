from Clase_base_MonitoreoDeCargas import MonitoreoDeCargas

class ConsumoEnergetico(MonitoreoDeCargas):                     
    def Lecturas_de_Consumo_de_Cargas(self):       
        while True:
            try:
                Cantidad_Consumo = int(input("Ingrese la cantidad de consumo de diferentes zonas: "))    
                break
            except ValueError:
                print("Error intente con un número válido")
                
        Consumo_energetico = []
        for i in range(Cantidad_Consumo):
            while True:
                try:
                    energia = int(input(f"Consumo de energía de la zona [{i + 1}]: "))    
                    Consumo_energetico.append(energia)
                    break
                except ValueError:
                    print("Error vuelva intentarlo con un número válido.")
        return Consumo_energetico
                
    def Organizador_de_RCE(self, cargas):
        n = len(cargas)
        cargas_copia = list(cargas) 
        for i in range(n):
            intercambiado = False
            for j in range(0, n - i - 1):
                if cargas_copia[j] < cargas_copia[j + 1]:
                    cargas_copia[j], cargas_copia[j + 1] = cargas_copia[j + 1], cargas_copia[j]
                    intercambiado = True
            if not intercambiado:
                break         
        return cargas_copia

    def buscar_picos_sobrecarga(self, cargas, limite):
        print(f"\n--- Búsqueda lineal de picos de sobrecarga sobre el límite > {limite}) ---")
        picos_criticos = []
        for i in range(len(cargas)):
            if cargas[i] > limite:
                picos_criticos.append((i + 1, cargas[i]))
        
        if picos_criticos:
            for zona, valor in picos_criticos:
                print(f"¡Advertencia! pico de sobrecarga crítico detectado en la Zona {zona} con {valor} Amp.")
        else:
            print("No se registraron picos de sobrecarga críticos que superen el límite")
        return picos_criticos
